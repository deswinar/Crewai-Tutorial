import streamlit as st
import subprocess
import json

st.title("CrewAI Runner")

# Input field for topic
topic = st.text_input("Enter a topic:", "AI LLMs")

if st.button("Run CrewAI"):
    with st.spinner("Running CrewAI..."):
        try:
            # Run `main.py` and capture JSON output
            result = subprocess.run(
                ["python", "src/latest_ai_development/main.py", "run", topic],
                capture_output=True, text=True
            )

            # Parse JSON output
            output = json.loads(result.stdout.strip()) if result.stdout else {}

            if output.get("success"):
                st.subheader("CrewAI Output:")
                st.text_area("Result", output["result"], height=300)
            else:
                st.error(f"Error: {output.get('error', 'Unknown error')}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
