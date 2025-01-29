import streamlit as st
import subprocess

# Streamlit UI
st.title("AI Development Crew Runner")

# Input form
with st.form(key="crew_form"):
    topic = st.text_input("Enter a topic for AI Development:", "AI LLMs")
    submit_button = st.form_submit_button("Run Crew")

# Handle form submission
if submit_button:
    try:
        # Execute main.py with the user-provided topic
        result = subprocess.run(
            ["python", "src/latest_ai_development/main.py", "run", topic],
            capture_output=True,
            text=True,
            check=True,
        )
        st.success("Crew executed successfully!")
        st.text_area("Output:", result.stdout, height=200)
    except subprocess.CalledProcessError as e:
        st.error("An error occurred while running the crew.")
        st.text_area("Error Details:", e.stderr, height=200)
