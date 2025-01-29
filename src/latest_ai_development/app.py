import sys
print(sys.version)
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import json
from latest_ai_development.main import run_crew  # Import the new function

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
