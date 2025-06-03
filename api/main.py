from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .db.mongodb import (
    get_apps_collection, get_agents_collection, get_flows_collection,
    get_plans_collection, get_graphs_collection, get_chats_collection,
    get_messages_collection
)

app = FastAPI(title="Alpha API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Alpha API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Apps endpoints
@app.get("/apps")
async def get_apps():
    apps = list(get_apps_collection().find({}, {"_id": 0}))
    return {"apps": apps}

@app.get("/apps/{app_id}")
async def get_app(app_id: str):
    app = get_apps_collection().find_one({"_id": app_id}, {"_id": 0})
    if not app:
        raise HTTPException(status_code=404, detail="App not found")
    return app

@app.get("/apps/user/{user_id}")
async def get_user_apps(user_id: str):
    apps = list(get_apps_collection().find({"user_id": user_id}, {"_id": 0}))
    return {"apps": apps}

# Agents endpoints
@app.get("/agents")
async def get_agents():
    agents = list(get_agents_collection().find({}, {"_id": 0}))
    return {"agents": agents}

@app.get("/agents/{agent_id}")
async def get_agent(agent_id: str):
    agent = get_agents_collection().find_one({"_id": agent_id}, {"_id": 0})
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

# Flows endpoints
@app.get("/flows")
async def get_flows():
    flows = list(get_flows_collection().find({}, {"_id": 0}))
    return {"flows": flows}

@app.get("/flows/{flow_id}")
async def get_flow(flow_id: str):
    flow = get_flows_collection().find_one({"_id": flow_id}, {"_id": 0})
    if not flow:
        raise HTTPException(status_code=404, detail="Flow not found")
    return flow

# Plans endpoints
@app.get("/plans")
async def get_plans():
    plans = list(get_plans_collection().find({}, {"_id": 0}))
    return {"plans": plans}

@app.get("/plans/{plan_id}")
async def get_plan(plan_id: str):
    plan = get_plans_collection().find_one({"_id": plan_id}, {"_id": 0})
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

# Graphs endpoints
@app.get("/graphs")
async def get_graphs():
    graphs = list(get_graphs_collection().find({}, {"_id": 0}))
    return {"graphs": graphs}

@app.get("/graphs/{graph_id}")
async def get_graph(graph_id: str):
    graph = get_graphs_collection().find_one({"_id": graph_id}, {"_id": 0})
    if not graph:
        raise HTTPException(status_code=404, detail="Graph not found")
    return graph

# Chats endpoints
@app.get("/chats")
async def get_chats():
    chats = list(get_chats_collection().find({}, {"_id": 0}))
    return {"chats": chats}

@app.get("/chats/{chat_id}")
async def get_chat(chat_id: str):
    chat = get_chats_collection().find_one({"_id": chat_id}, {"_id": 0})
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

# Messages endpoints
@app.get("/messages")
async def get_messages():
    messages = list(get_messages_collection().find({}, {"_id": 0}))
    return {"messages": messages}

@app.get("/messages/{message_id}")
async def get_message(message_id: str):
    message = get_messages_collection().find_one({"_id": message_id}, {"_id": 0})
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message 