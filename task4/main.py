import streamlit as st
from agent import StudyAgent
import os
import tempfile

def main():
    st.set_page_config(page_title="Study Notes Summarizer & Quiz Generator")
    st.title("Study Notes Summarizer & Quiz Generator Agent")

    # Initialize the agent
    if "agent" not in st.session_state:
        st.session_state.agent = StudyAgent()
    agent = st.session_state.agent

    # Initialize session state for quiz
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}
    if "score" not in st.session_state:
        st.session_state.score = 0

    uploaded_file = st.file_uploader("Upload your study notes (PDF or TXT)", type=["pdf", "txt"])

    if uploaded_file is not None:
        if "processed_text" not in st.session_state or st.session_state.get("uploaded_file_name") != uploaded_file.name:
            file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
            st.write(file_details)

            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                temp_file_path = tmp_file.name
            
            try:
                text = agent.read_file(temp_file_path)
                st.success("File read successfully!")
                st.session_state.processed_text = text
                st.session_state.uploaded_file_name = uploaded_file.name
                # Clear previous quiz data
                st.session_state.questions = []
                st.session_state.user_answers = {}
                st.session_state.score = 0
            except Exception as e:
                st.error(f"Error reading file: {e}")
            finally:
                if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
                    os.unlink(temp_file_path)
        
    if "processed_text" in st.session_state:
        st.subheader("Choose an action:")
        action = st.radio(
            "Select what you want to generate:",
            ("Summary", "Multiple-Choice Questions (MCQs)", "Short Answer Questions", "True/False Questions"),
            key="action_radio"
        )

        if st.button(f"Generate {action}"):
            with st.spinner(f"Generating {action.lower()}..."):
                if action == "Summary":
                    result = agent.summarize_text(st.session_state.processed_text)
                    st.text_area("Generated Summary:", value=result, height=300)
                elif action == "Short Answer Questions":
                    result = agent.generate_short_questions(st.session_state.processed_text)
                    st.text_area("Generated Short Answer Questions:", value=result, height=300)
                else: # MCQs or True/False
                    st.session_state.questions = [] # Clear previous questions
                    if action == "Multiple-Choice Questions (MCQs)":
                        st.session_state.questions = agent.generate_mcqs(st.session_state.processed_text)
                    elif action == "True/False Questions":
                        st.session_state.questions = agent.generate_true_false(st.session_state.processed_text)
                    
                    if not st.session_state.questions:
                        st.error("Failed to generate questions. The returned data may not be valid JSON.")

    # Display quiz if questions are available
    if st.session_state.questions:
        st.subheader("Quiz Time!")
        with st.form(key="quiz_form"):
            user_answers = {}
            for i, q in enumerate(st.session_state.questions):
                st.write(f"**Question {i+1}:** {q['question']}")
                options = q.get("options") if "options" in q else ["True", "False"]
                user_answers[i] = st.radio(
                    "Your answer:",
                    options,
                    key=f"q_{i}",
                    label_visibility="collapsed"
                )
            
            submit_button = st.form_submit_button(label="Submit Quiz")

            if submit_button:
                st.session_state.user_answers = user_answers
                score = 0
                for i, q in enumerate(st.session_state.questions):
                    correct_answer = str(q["answer"]) # Ensure consistent type
                    if st.session_state.user_answers[i] == correct_answer:
                        score += 1
                st.session_state.score = score
                
                st.subheader("Quiz Results")
                st.write(f"You scored {st.session_state.score} out of {len(st.session_state.questions)}")

                for i, q in enumerate(st.session_state.questions):
                    st.write(f"**Question {i+1}:** {q['question']}")
                    user_answer = st.session_state.user_answers[i]
                    correct_answer = str(q["answer"])
                    
                    if user_answer == correct_answer:
                        st.success(f"Your answer: {user_answer} (Correct)")
                    else:
                        st.error(f"Your answer: {user_answer} (Incorrect)")
                        st.info(f"Correct answer: {correct_answer}")
                    st.write("---")

if __name__ == "__main__":
    main()