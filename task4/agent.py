import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from pypdf import PdfReader
import re

load_dotenv()

class StudyAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def _parse_json_response(self, response_text: str) -> list:
        """
        Parses the JSON response from the model, cleaning up any markdown formatting.
        """
        # Remove markdown code block delimiters
        cleaned_text = re.sub(r"```json\n|```", "", response_text.strip())
        try:
            return json.loads(cleaned_text)
        except json.JSONDecodeError:
            # Handle cases where the response is not valid JSON
            return []

    def read_file(self, file_path: str) -> str:
        """
        Reads the content of a PDF or text file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} was not found.")

        if file_path.endswith(".pdf"):
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        else:
            raise ValueError("Unsupported file format. Please provide a PDF or a text file.")

    def summarize_text(self, text: str) -> str:
        """
        Generates a summary of the given text.
        """
        prompt = f"Please summarize the following text:\n\n{text}"
        response = self.model.generate_content(prompt)
        return response.text

    def generate_mcqs(self, text: str, num_questions: int = 5) -> list:
        """
        Generates multiple-choice questions from the given text and returns them as a list of dicts.
        """
        prompt = f"""
        Please generate {num_questions} multiple-choice questions based on the following text.
        Return the questions as a JSON array, where each object has "question", "options", and "answer" keys.
        The "options" should be a list of strings, and the "answer" should be the correct option string.

        Example format:
        [
            {{
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "answer": "Paris"
            }}
        ]

        Text:
        {text}
        """
        response = self.model.generate_content(prompt)
        return self._parse_json_response(response.text)

    def generate_short_questions(self, text: str, num_questions: int = 5) -> str:
        """
        Generates short answer questions from the given text.
        """
        prompt = f"Please generate {num_questions} short answer questions with answers based on the following text:\n\n{text}"
        response = self.model.generate_content(prompt)
        return response.text

    def generate_true_false(self, text: str, num_questions: int = 5) -> list:
        """
        Generates true/false questions from the given text and returns them as a list of dicts.
        """
        prompt = f"""
        Please generate {num_questions} true/false questions based on the following text.
        Return the questions as a JSON array, where each object has "question" and "answer" keys.
        The "answer" should be a boolean (true or false).

        Example format:
        [
            {{
                "question": "The sky is blue.",
                "answer": true
            }}
        ]

        Text:
        {text}
        """
        response = self.model.generate_content(prompt)
        return self._parse_json_response(response.text)
