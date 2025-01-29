#!/usr/bin/env python
# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import sys
import warnings
import json

from datetime import datetime

from latest_ai_development.crew import LatestAiDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run_crew(topic="AI LLMs"):
    """
    Run the CrewAI and return the result.
    """
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }

    try:
        result = LatestAiDevelopment().crew().kickoff(inputs=inputs)
        return {"success": True, "result": result}  # Return the result
    except Exception as e:
        return {"success": False, "error": str(e)}  # Return error message


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        LatestAiDevelopment().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LatestAiDevelopment().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        LatestAiDevelopment().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "run":
        topic = sys.argv[2] if len(sys.argv) > 2 else "AI LLMs"
        output = run_crew(topic)  # Call the new function
        print(json.dumps(output))  # Print the result as JSON