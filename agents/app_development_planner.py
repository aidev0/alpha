ALPHA_DB_APP = {
        "app_id": "6836492196cb52105c3b5f80",
        "name": "db",
        "label": "Database Layer",
        "description": "Stores user data, projects, agents, workflows, and system logs.",
        "parent_id": "6836492196cb52105c3b5f78"
    }

ALPHA_APP_DEVELOPMENT_PLAN = {
  "node_type": "app_development_plan",
  "app_id": "6836492196cb52105c3b5f80",
  "description": "Development plan to create MongoDB setup for Alpha",
  "nodes": [
    {
      "task_name": "Create db.py with all functions",
      "type": "file",
      "path": "db.py",
      "cmd": None,
      "language": "python",
      "description": "Inference LLM to create db.py. This file should contain get_db, get_apps_collection, and get_graphs_collection functions using MONGODB_URI and MONGODB_DATABASE environment variables"
    },
    {
      "task_name": "Create requirements.txt",
      "type": "file",
      "path": "requirements.txt",
      "cmd": None,
      "language": "text",
      "description": "Add all dependencies to requirements.txt."
    }
  ],
  "edges": [
    [0, 1]
  ]
}

SYSTEMS_MESSAGE = f"""
You are a helpful assistant that helps with the development of each app in Alpha.

You will be given a task to develop an app.

You will be given the app details and the development plan.

You will be given the system message for the app.

You shall provide the planning graph for the app development.

Each node is a task to be completed.

If we input {ALPHA_DB_APP} as the app details, the output should be:

{ALPHA_APP_DEVELOPMENT_PLAN}


"""
