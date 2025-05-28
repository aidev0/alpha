from agents.llm_inference import run_inference

ALPHA_APP_IDEA = """
Alpha is a self-developing AI platform that builds, deploys, and runs software automatically across 1000+ integrations. It acts like a universal developer and operator for any app idea.

At its core, Alpha is an AI-powered OS made up of modular apps, agents, and flows:

Apps are major functional units (e.g., web, api, ios, android, agents, flows, integrations, db).

Agents are autonomous functions with clear input/output. They perform tasks like understanding the user, generating code, managing state, or deploying services.

Flows are orchestrated pipelines of agents designed to fulfill specific goals like building an API, deploying a bot, or running automation.

Plans are trees of tasks (leaf nodes = shell commands, code generation, deployments) that define how to implement an app, a feature, or a response to a user request.

Alpha receives a user message (e.g., “Build a calculator app”) and intelligently:

Understands the request via agents.

Designs a development plan.

Builds the required apps and services using agents.

Deploys to all target platforms (e.g., Discord, iOS, Web, etc.)

Manages the app lifecycle with monitoring, updates, and user interaction.

Alpha’s mission is to turn natural language into real software and services, deploy them everywhere, and allow users to earn or operate apps without needing technical skills.
"""

ALPHA_APP_LIST = [
  {
    "name": "alpha",
    "label": "Alpha Core",
    "description": "The central app responsible for coordinating all other apps, agents, and workflows. It is the brain of the system.",
    "parent_id": None
  },
  {
    "name": "agents",
    "label": "AI Agents",
    "description": "Contains reusable, pluggable agents that execute tasks and support workflows across Alpha.",
    "parent_id": "alpha"
  },
  {
    "name": "flows",
    "label": "Workflows",
    "description": "Orchestrated pipelines of agents that carry out complex tasks step-by-step in sequence or parallel.",
    "parent_id": "alpha"
  },
  {
    "name": "ios",
    "label": "iOS App",
    "description": "Mobile iOS interface for users to interact with Alpha apps and services.",
    "parent_id": "alpha"
  },
  {
    "name": "web",
    "label": "Web UI",
    "description": "Web-based interface for user interaction with Alpha, including dashboards, builders, and messaging.",
    "parent_id": "alpha"
  },
  {
    "name": "android",
    "label": "Android App",
    "description": "Android mobile interface for interacting with Alpha systems and apps.",
    "parent_id": "alpha"
  },
  {
    "name": "api",
    "label": "Alpha API",
    "description": "Exposes Alpha functionality through REST/GraphQL endpoints to integrate with other systems.",
    "parent_id": "alpha"
  },
  {
    "name": "integrations",
    "label": "Integrations",
    "description": "Handles third-party integrations like Stripe, Discord, Gmail, etc. Used by agents and workflows.",
    "parent_id": "alpha"
  },
  {
    "name": "db",
    "label": "Database Layer",
    "description": "Stores user data, projects, agents, workflows, and system logs.",
    "parent_id": "alpha"
  }
]


output_schema = [{
                    "name": "App Name",
                    "label": "App Label",
                    "description": "App Description",
                    "parent_id": ""
                }]

SYSTEM_MESSAGE = f"""
You are an AI agent that analyzes app ideas and generates a structured list of required apps. 
Output should be in the following format: {output_schema}.
Only output the JSON object, no other text. No markdown. No explanation.

For example, if I give you this idea {ALPHA_APP_IDEA}, you should output this: {ALPHA_APP_LIST}
"""

input_schema = {
    "type": "object",
    "properties": {
        "app_idea": {
            "type": "string",
            "description": "The main app idea or concept to analyze"
        }
    },
    "required": ["app_idea"]
}



def run(app_idea: str) -> dict:
    messages = [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": app_idea}
    ]
    return run_inference(messages, "gpt-4o") 