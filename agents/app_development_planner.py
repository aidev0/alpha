from agents.llm_inference import run_inference
ALPHA_DB_APP = {
        "app_id": "6836492196cb52105c3b5f80",
        "name": "db",
        "label": "Database Layer",
        "description": "Stores user data, projects, agents, workflows, and system logs.",
        "parent_id": "6836492196cb52105c3b5f78"
    }

ALPHA_DB_APP_DEVELOPMENT_PLAN = {
  "node_type": "app_development_task",
  "app_id": "6836492196cb52105c3b5f80",
  "description": "Development plan to create MongoDB setup for Alpha",
  "nodes": [
    {
      "name": "Create mongodb.py with all functions",
      "label": "Create mongodb.py with all functions",
      "description": "Inference LLM to create get_db, get_apps_collection, and get_graphs_collection functions using MONGODB_URI and MONGODB_DATABASE environment variables",
      "spec": "spec & tech details for the task",
      "type": "file",
      "path": "mongodb.py",
      "cmd": None,
      "language": "python",
    },
    {
      "name": "Create requirements.txt",
      "label": "Create requirements.txt",
      "description": "Add all dependencies to requirements.txt.",
      "spec": "spec & tech details for the task",
      "type": "file",
      "path": "requirements.txt",
      "cmd": None,
      "language": "text",
    }
  ],
  "edges": [
    [0, 1]
  ],
  "name": "db app development plan", 
  "label": "db app development plan", 
  "description": "Development plan to create MongoDB setup for Alpha.",
  "spec": "spec & tech details for the plan"
}

SYSTEM_MESSAGE = f"""
You are a helpful assistant that helps with the development of each app in Alpha.

You will be given a task to develop an app.

You will be given the app details and the development plan.

You will be given the system message for the app.

You shall provide the planning graph for the app development.

Each node is a task to be completed.

If we input {ALPHA_DB_APP} as the app details, the output should be:

{ALPHA_DB_APP_DEVELOPMENT_PLAN}
"""

def run(app_details: str) -> dict:
    messages = [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": app_details}
    ]
    return run_inference(messages, "gpt-4o") 
