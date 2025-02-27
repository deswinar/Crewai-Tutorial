import streamlit as st
import os
import json
from latest_ai_development.main import run_crew  # Import the new function

os.environ["MODEL"] = st.secrets["OPENAI_API_KEY"]
os.environ["GEMINI_API_KEY"] = st.secrets["GROQ_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

st.title("CrewAI Runner")

# Input field for topic
topic = st.text_input("Enter a topic:", "AI LLMs")

if st.button("Run CrewAI"):
    with st.spinner("Running CrewAI..."):
        try:
            # Call the run_crew function directly
            output = run_crew(topic)

            if output.get("success"):
                st.subheader("CrewAI Output:")
                st.text_area("Result", output["result"], height=300)
            else:
                st.error(f"Error: {output.get('error', 'Unknown error')}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
