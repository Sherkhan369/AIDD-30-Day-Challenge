# Study Notes Summarizer & Quiz Generator Agent

This project is a Study Notes Summarizer & Quiz Generator Agent that uses the OpenAI Agents SDK to help you study more effectively. You can provide a PDF or a text file, and the agent will generate a summary and various types of quiz questions based on the content.

## Features

- **Summarize Text:** Get a concise summary of your study notes.
- **Generate MCQs:** Create multiple-choice questions to test your knowledge.
- **Generate Short Answer Questions:** Get open-ended questions to practice your understanding.
- **Generate True/False Questions:** Create true or false questions for quick review.
- **Supports PDF and Text Files:** You can use both PDF and plain text files as input.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/asmamasood/Ai-Driven-Development.git
    cd study-agent
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create a `.env` file** in the root of the project and add your Gemini API key:
    ```
    GEMINI_API_KEY=your_gemini_api_key
    ```

## How to Run the Agent

You can run the Streamlit application by executing the following command in your terminal from the `study-agent` directory:

```bash
streamlit run main.py
```

## How to Use It

Once the Streamlit application is running, open your web browser to the address provided by Streamlit (usually `http://localhost:8501`).

1.  **Upload your study notes**: Use the file uploader to select a PDF or TXT file.
2.  **Choose an action**: Select whether you want to generate a summary, multiple-choice questions, short answer questions, or true/false questions using the radio buttons.
3.  **Generate**: Click the "Generate" button to see the output. The generated content will appear in a text area below.
