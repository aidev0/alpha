from typing import List, Dict, Any
import json
from agents.llm_inference import run_inference

input_schema = {
    "messages": List[Dict[str, str]]
}

output_schema = {
    "problem_understanding": str,
    "tech_list": list,
    "clarification_questions": list,
}
# 🔧 Agent config
SYSTEM_MESSAGE = f"""
You are the Alpha User Understanding Agent.

You receive messages from Alpha users and system agents. Your job is to:
- Understand what the user wants Alpha to build
- Assess their technical level
- Identify what tech (APIs, bots, platforms) might be required
- Decide if we are ready to design or build a workflow of agents

Alpha is a multi-agent AI platform that builds and deploys apps with integrations (bots, APIs, UIs, etc).
Do not ask for unnecessary technical details unless clarification is critical.
Prioritize newer messages, but use older ones for background.

Output MUST be JSON. No markdown. No ```json``` blocks. No other text or formatting or explanation.
Use this exact schema:
{output_schema}
"""

model_name = "gpt-4o"

def run(input: dict) -> dict:
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + input["messages"]

    for attempt in range(3):
        try:
            response = run_inference(messages, model_name=model_name)
            response = response.replace("```json", "").replace("```", "")
            parsed = json.loads(response)

            # Validate output schema
            for key, expected_type in output_schema.items():
                if key not in parsed:
                    raise ValueError(f"Missing key: {key}")
                if not isinstance(parsed[key], expected_type):
                    raise TypeError(f"Key '{key}' should be {expected_type}, got {type(parsed[key])}")

            return parsed

        except Exception as e:
            if attempt < 2:
                messages.append({
                    "role": "assistant",
                    "content": f"⚠️ Retry {attempt + 1}: Your output must match the required JSON schema exactly. Error: {str(e)}"
                })
            else:
                return {
                    "error": f"Failed to produce valid JSON after 3 attempts. Final error: {str(e)}",
                    "raw_response": response if 'response' in locals() else None
                }
