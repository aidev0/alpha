#!/usr/bin/env python3
"""
Alpha Database API
==================
FastAPI + MongoDB service for Alpha framework.

This API provides endpoints for managing:
- Users and Sessions
- Chats and Messages
- Apps, Plans, and Agents
- Flows and Integrations
- Runs and States

Environment Variables:
- MONGODB_URI: MongoDB connection string (default: mongodb://localhost:27017)
- MONGODB_DATABASE: Database name (default: alpha)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict, Any
from datetime import datetime
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
import os
import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.append(str(Path(__file__).parent))

from model import (
    User, Session, Chat, Message, State, App, Plan, Agent, Flow, Integration, Run,
    MessageRole, StateType, AppStatus, PlanStatus, AgentType, RunStatus, PyObjectId
)

# Database connection
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "alpha")

app = FastAPI(title="Alpha Database API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB client
client = AsyncIOMotorClient(MONGODB_URI)
db = client[MONGODB_DATABASE]

# Collections
users_collection = db.users
sessions_collection = db.sessions
chats_collection = db.chats
messages_collection = db.messages
states_collection = db.states
apps_collection = db.apps
plans_collection = db.plans
agents_collection = db.agents
flows_collection = db.flows
integrations_collection = db.integrations
runs_collection = db.runs

# Helper function to parse ObjectId
def parse_object_id(id_str: str) -> ObjectId:
    try:
        return ObjectId(id_str)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid ID format: {str(e)}")

# User endpoints
@app.post("/users")
async def create_user(user: User):
    user_dict = user.model_dump(by_alias=True)
    result = await users_collection.insert_one(user_dict)
    user_dict["_id"] = result.inserted_id
    return user_dict

@app.get("/users")
async def list_users():
    users = await users_collection.find().to_list(length=100)
    return users

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await users_collection.find_one({"_id": parse_object_id(user_id)})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
async def update_user(user_id: str, user_update: Dict[str, Any]):
    result = await users_collection.update_one(
        {"_id": parse_object_id(user_id)},
        {"$set": user_update}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    result = await users_collection.delete_one({"_id": parse_object_id(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Session endpoints
@app.post("/sessions")
async def create_session(session: Session):
    session_dict = session.model_dump(by_alias=True)
    result = await sessions_collection.insert_one(session_dict)
    session_dict["_id"] = result.inserted_id
    return session_dict

@app.get("/sessions")
async def list_sessions(user_id: Optional[str] = None, is_active: Optional[bool] = None):
    query = {}
    if user_id:
        query["user_id"] = parse_object_id(user_id)
    if is_active is not None:
        query["is_active"] = is_active
    sessions = await sessions_collection.find(query).to_list(length=100)
    return sessions

@app.get("/sessions/{session_id}")
async def get_session(session_id: str):
    session = await sessions_collection.find_one({"_id": parse_object_id(session_id)})
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@app.put("/sessions/{session_id}")
async def update_session(session_id: str, session_update: Dict[str, Any]):
    result = await sessions_collection.update_one(
        {"_id": parse_object_id(session_id)},
        {"$set": session_update}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"message": "Session updated successfully"}

@app.delete("/sessions/{session_id}")
async def delete_session(session_id: str):
    result = await sessions_collection.delete_one({"_id": parse_object_id(session_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"message": "Session deleted successfully"}

# Chat endpoints
@app.post("/chats")
async def create_chat(chat: Chat):
    chat_dict = chat.model_dump(by_alias=True)
    result = await chats_collection.insert_one(chat_dict)
    chat_dict["_id"] = result.inserted_id
    return chat_dict

@app.get("/chats")
async def list_chats(user_id: Optional[str] = None, session_id: Optional[str] = None, app_id: Optional[str] = None, agent_id: Optional[str] = None, flow_id: Optional[str] = None):
    query = {}
    if user_id:
        query["user_id"] = parse_object_id(user_id)
    if session_id:
        query["session_id"] = parse_object_id(session_id)
    if app_id:
        query["app_id"] = parse_object_id(app_id)
    if agent_id:
        query["agent_id"] = parse_object_id(agent_id)
    if flow_id:
        query["flow_id"] = parse_object_id(flow_id)
    chats = await chats_collection.find(query).to_list(length=100)
    return chats

@app.get("/chats/{chat_id}")
async def get_chat(chat_id: str):
    chat = await chats_collection.find_one({"_id": parse_object_id(chat_id)})
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

# Message endpoints
@app.post("/messages")
async def create_message(message: Message):
    message_dict = message.model_dump(by_alias=True)
    result = await messages_collection.insert_one(message_dict)
    message_dict["_id"] = result.inserted_id
    return message_dict

@app.get("/messages")
async def list_messages(chat_id: str):
    messages = await messages_collection.find({"chat_id": parse_object_id(chat_id)}).to_list(length=100)
    return messages

# State endpoints
@app.post("/states")
async def create_state(state: State):
    state_dict = state.model_dump(by_alias=True)
    result = await states_collection.insert_one(state_dict)
    state_dict["_id"] = result.inserted_id
    return state_dict

@app.get("/states/{reference_id}")
async def get_state(reference_id: str, state_type: StateType):
    state = await states_collection.find_one({
        "reference_id": parse_object_id(reference_id),
        "type": state_type
    })
    if state is None:
        raise HTTPException(status_code=404, detail="State not found")
    return state

@app.put("/states/{state_id}")
async def update_state(state_id: str, state_update: Dict[str, Any]):
    result = await states_collection.update_one(
        {"_id": parse_object_id(state_id)},
        {"$set": state_update}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="State not found")
    return {"message": "State updated successfully"}

# App endpoints
@app.post("/apps")
async def create_app(app: App):
    app_dict = app.model_dump(by_alias=True)
    result = await apps_collection.insert_one(app_dict)
    app_dict["_id"] = result.inserted_id
    return app_dict

@app.get("/apps")
async def list_apps(app_parent_id: Optional[str] = None):
    query = {}
    if app_parent_id:
        query["app_parent_id"] = parse_object_id(app_parent_id)
    apps = await apps_collection.find(query).to_list(length=100)
    return apps

@app.get("/apps/{app_id}")
async def get_app(app_id: str):
    app = await apps_collection.find_one({"_id": parse_object_id(app_id)})
    if app is None:
        raise HTTPException(status_code=404, detail="App not found")
    return app

@app.put("/apps/{app_id}")
async def update_app(app_id: str, app_update: Dict[str, Any]):
    result = await apps_collection.update_one(
        {"_id": parse_object_id(app_id)},
        {"$set": app_update}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="App not found")
    return {"message": "App updated successfully"}

# Plan endpoints
@app.post("/plans")
async def create_plan(plan: Plan):
    plan_dict = plan.model_dump(by_alias=True)
    result = await plans_collection.insert_one(plan_dict)
    plan_dict["_id"] = result.inserted_id
    return plan_dict

@app.get("/plans")
async def list_plans(app_id: Optional[str] = None):
    query = {}
    if app_id:
        query["app_id"] = parse_object_id(app_id)
    plans = await plans_collection.find(query).to_list(length=100)
    return plans

@app.get("/plans/{plan_id}")
async def get_plan(plan_id: str):
    plan = await plans_collection.find_one({"_id": parse_object_id(plan_id)})
    if plan is None:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

# Agent endpoints
@app.post("/agents")
async def create_agent(agent: Agent):
    agent_dict = agent.model_dump(by_alias=True)
    result = await agents_collection.insert_one(agent_dict)
    agent_dict["_id"] = result.inserted_id
    return agent_dict

@app.get("/agents")
async def list_agents(app_id: Optional[str] = None, agent_type: Optional[AgentType] = None):
    query = {}
    if app_id:
        query["app_id"] = parse_object_id(app_id)
    if agent_type:
        query["type"] = agent_type
    agents = await agents_collection.find(query).to_list(length=100)
    return agents

@app.get("/agents/{agent_id}")
async def get_agent(agent_id: str):
    agent = await agents_collection.find_one({"_id": parse_object_id(agent_id)})
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

# Flow endpoints
@app.post("/flows")
async def create_flow(flow: Flow):
    flow_dict = flow.model_dump(by_alias=True)
    result = await flows_collection.insert_one(flow_dict)
    flow_dict["_id"] = result.inserted_id
    return flow_dict

@app.get("/flows")
async def list_flows(app_id: Optional[str] = None):
    query = {}
    if app_id:
        query["app_id"] = parse_object_id(app_id)
    flows = await flows_collection.find(query).to_list(length=100)
    return flows

@app.get("/flows/{flow_id}")
async def get_flow(flow_id: str):
    flow = await flows_collection.find_one({"_id": parse_object_id(flow_id)})
    if flow is None:
        raise HTTPException(status_code=404, detail="Flow not found")
    return flow

# Integration endpoints
@app.post("/integrations")
async def create_integration(integration: Integration):
    integration_dict = integration.model_dump(by_alias=True)
    result = await integrations_collection.insert_one(integration_dict)
    integration_dict["_id"] = result.inserted_id
    return integration_dict

@app.get("/integrations")
async def list_integrations():
    integrations = await integrations_collection.find().to_list(length=100)
    return integrations

@app.get("/integrations/{integration_id}")
async def get_integration(integration_id: str):
    integration = await integrations_collection.find_one({"_id": parse_object_id(integration_id)})
    if integration is None:
        raise HTTPException(status_code=404, detail="Integration not found")
    return integration

# Run endpoints
@app.post("/runs")
async def create_run(run: Run):
    run_dict = run.model_dump(by_alias=True)
    result = await runs_collection.insert_one(run_dict)
    run_dict["_id"] = result.inserted_id
    return run_dict

@app.get("/runs")
async def list_runs(plan_id: Optional[str] = None):
    query = {}
    if plan_id:
        query["plan_id"] = parse_object_id(plan_id)
    runs = await runs_collection.find(query).to_list(length=100)
    return runs

@app.get("/runs/{run_id}")
async def get_run(run_id: str):
    run = await runs_collection.find_one({"_id": parse_object_id(run_id)})
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")
    return run

@app.put("/runs/{run_id}")
async def update_run(run_id: str, run_update: Dict[str, Any]):
    result = await runs_collection.update_one(
        {"_id": parse_object_id(run_id)},
        {"$set": run_update}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Run not found")
    return {"message": "Run updated successfully"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint that returns API information and available endpoints.
    """
    return {
        "name": "Alpha Database API",
        "version": "1.0.0",
        "description": "FastAPI + MongoDB service for Alpha framework",
        "endpoints": {
            "users": "/users",
            "sessions": "/sessions",
            "chats": "/chats",
            "messages": "/messages",
            "states": "/states",
            "apps": "/apps",
            "plans": "/plans",
            "agents": "/agents",
            "flows": "/flows",
            "integrations": "/integrations",
            "runs": "/runs",
            "health": "/health",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)