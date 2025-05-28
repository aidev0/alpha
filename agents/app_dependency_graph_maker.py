output_schema = {
    "nodes": [{"app_id", "name"}],
    "edges": [["app_id of app_i", "app_id of app_j"]]
}

ALPHA_INPUT_APP_LIST = alpha_input_apps = [
    {
        "_id": "6836492196cb52105c3b5f79",
        "name": "agents",
        "label": "AI Agents",
        "description": "Contains reusable, pluggable agents that execute tasks and support workflows across Alpha.",
        "parent_id": "6836492196cb52105c3b5f78"
    },
    {
        "_id": "6836492196cb52105c3b5f7a",
        "name": "flows",
        "label": "Workflows",
        "description": "Orchestrated pipelines of agents that carry out complex tasks step-by-step in sequence or parallel.",
        "parent_id": "6836492196cb52105c3b5f78"
    },
    {
        "_id": "6836492196cb52105c3b5f7b",
        "name": "ios",
        "label": "iOS App",
        "description": "Mobile iOS interface for users to interact with Alpha apps and services.",
        "parent_id": "6836492196cb52105c3b5f78"
    },
    {
        "_id": "6836492196cb52105c3b5f7c",
        "name": "web",
        "label": "Web UI",
        "description": "Web-based interface for user interaction with Alpha, including dashboards, builders, and messaging.",
        "parent_id": "6836492196cb52105c3b5f78"
    },
    {
        "_id": "6836492196cb52105c3b5f7d",
        "name": "android",
        "label": "Android App",
        "description": "Android mobile interface for interacting with Alpha systems and apps.",
        "parent_id": "6836492196cb52105c3b5f78"
    },
    {
        "_id": "6836492196cb52105c3b5f7e",
        "name": "api",
        "label": "Alpha API",
        "description": "Exposes Alpha functionality through REST/GraphQL endpoints to integrate with other systems.",
        "parent_id": "6836492196cb52105c3b5f78"
    },
    {
        "_id": "6836492196cb52105c3b5f7f",
        "name": "integrations",
        "label": "Integrations",
        "description": "Handles third-party integrations like Stripe, Discord, Gmail, etc. Used by agents and workflows.",
        "parent_id": "6836492196cb52105c3b5f78"
    },
    {
        "_id": "6836492196cb52105c3b5f80",
        "name": "db",
        "label": "Database Layer",
        "description": "Stores user data, projects, agents, workflows, and system logs.",
        "parent_id": "6836492196cb52105c3b5f78"
    }
]

ALPHA_APP_DEPENDENCY_GRAPH = {
  "_id": {
    "$oid": "6836a8cb2092d6367c04f4ea"
  },
  "node_type": "app",
  "nodes": [
    {
      "app_id": "6836492196cb52105c3b5f79",
      "name": "agents",
      "label": "AI Agents",
      "description": "Contains reusable, pluggable agents that execute tasks and support workflows across Alpha.",
      "parent_id": "6836492196cb52105c3b5f78"
    },
    {
      "app_id": "6836492196cb52105c3b5f7a",
      "name": "flows",
      "label": "Workflows",
      "description": "Orchestrated pipelines of agents that carry out complex tasks step-by-step in sequence or parallel.",
      "parent_id": "6836492196cb52105c3b5f78"
    },
    {
      "app_id": "6836492196cb52105c3b5f7b",
      "name": "ios",
      "label": "iOS App",
      "description": "Mobile iOS interface for users to interact with Alpha apps and services.",
      "parent_id": "6836492196cb52105c3b5f78"
    },
    {
      "app_id": "6836492196cb52105c3b5f7c",
      "name": "web",
      "label": "Web UI",
      "description": "Web-based interface for user interaction with Alpha, including dashboards, builders, and messaging.",
      "parent_id": "6836492196cb52105c3b5f78"
    },
    {
      "app_id": "6836492196cb52105c3b5f7d",
      "name": "android",
      "label": "Android App",
      "description": "Android mobile interface for interacting with Alpha systems and apps.",
      "parent_id": "6836492196cb52105c3b5f78"
    },
    {
      "app_id": "6836492196cb52105c3b5f7e",
      "name": "api",
      "label": "Alpha API",
      "description": "Exposes Alpha functionality through REST/GraphQL endpoints to integrate with other systems.",
      "parent_id": "6836492196cb52105c3b5f78"
    },
    {
      "app_id": "6836492196cb52105c3b5f7f",
      "name": "integrations",
      "label": "Integrations",
      "description": "Handles third-party integrations like Stripe, Discord, Gmail, etc. Used by agents and workflows.",
      "parent_id": "6836492196cb52105c3b5f78"
    },
    {
      "app_id": "6836492196cb52105c3b5f80",
      "name": "db",
      "label": "Database Layer",
      "description": "Stores user data, projects, agents, workflows, and system logs.",
      "parent_id": "6836492196cb52105c3b5f78"
    }
  ],
  "edges": [
    [7, 5],
    [5, 3],
    [5, 2],
    [5, 4],
    [5, 0],
    [5, 1],
    [5, 6],
    [6, 3]
  ]
}


SYSTEM_MESSAGE = f"""
You will recieve a list of apps and your task is to create a graph of the apps and their relationships.

The graph could be a tree, a fully connected graph.

Output should be in the following format: {output_schema}.

nodes are just list of the app_id.
edge [app_i_id, app_j_id] means app_j_id is dependent on app_i_id.

for example if you receive {ALPHA_INPUT_APP_LIST}, your output should be like
{ALPHA_APP_DEPENDENCY_GRAPH}
"""
