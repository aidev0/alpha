from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum
from bson import ObjectId

# Pydantic v2 compatible ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return v
        if isinstance(v, str) and ObjectId.is_valid(v):
            return ObjectId(v)
        raise ValueError("Invalid ObjectId")

    @classmethod
    def __get_pydantic_json_schema__(cls, schema, handler):
        # This tells Pydantic/OpenAPI to treat it as a string
        return {"type": "string"}
# Enums
class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class StateType(str, Enum):
    CHAT = "chat"
    APP = "app"
    PLAN = "plan"
    RUN = "run"

class AppStatus(str, Enum):
    DRAFT = "draft"
    BUILDING = "building"
    DEPLOYED = "deployed"
    FAILED = "failed"

class PlanStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"

class AgentType(str, Enum):
    PLANNER = "planner"
    ORCHESTRATOR = "orchestrator"
    WORKER = "worker"

class RunStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

# Models
class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    user_id: str
    email: Optional[str] = None
    phone_number: Optional[str] = None
    name: Optional[str] = None
    avatar_url: Optional[str] = None
    preferences: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Session(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    session_token: str
    started_at: datetime = Field(default_factory=datetime.utcnow)
    last_activity: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None
    is_active: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Chat(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    session_id: Optional[PyObjectId] = None
    app_id: Optional[PyObjectId] = None
    agent_id: Optional[PyObjectId] = None
    flow_id: Optional[PyObjectId] = None
    title: str
    description: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Message(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    chat_id: PyObjectId
    role: MessageRole
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class State(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    type: StateType
    reference_id: PyObjectId
    state_data: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class App(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str
    label: str
    description: str
    app_parent_id: Optional[PyObjectId] = None
    status: AppStatus = AppStatus.DRAFT
    config: Dict[str, Any] = Field(default_factory=dict)
    deployment_url: Optional[str] = None
    repository_url: Optional[str] = None
    code: Optional[str] = None
    language: Optional[str] = None
    entry_point: Optional[str] = None
    dependencies: List[str] = Field(default_factory=list)
    entry_command: Optional[str] = None
    code_repository_url: Optional[str] = None
    code_path: Optional[str] = None
    docker_image: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Plan(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    app_id: PyObjectId
    name: str
    description: str
    status: PlanStatus = PlanStatus.DRAFT
    tasks: List[Dict[str, Any]] = Field(default_factory=list)
    dependencies: Dict[str, List[str]] = Field(default_factory=dict)
    estimated_duration: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Agent(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    app_id: PyObjectId
    name: str
    type: AgentType
    system_message: str
    input_schema: Dict[str, Any] = Field(default_factory=dict)
    output_schema: Dict[str, Any] = Field(default_factory=dict)
    tools: List[Dict[str, Any]] = Field(default_factory=list)
    integrations: List[str] = Field(default_factory=list)
    capabilities: List[str] = Field(default_factory=list)
    code: Optional[str] = None
    language: Optional[str] = None
    entry_point: Optional[str] = None
    dependencies: List[str] = Field(default_factory=list)
    entry_command: Optional[str] = None
    code_repository_url: Optional[str] = None
    code_path: Optional[str] = None
    docker_image: Optional[str] = None
    deployment_url: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Flow(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    app_id: PyObjectId
    name: str
    description: str
    nodes: List[Dict[str, Any]] = Field(default_factory=list)
    edges: List[Dict[str, Any]] = Field(default_factory=list)
    entry_point: str
    code: Optional[str] = None
    language: Optional[str] = None
    entry_point_code: Optional[str] = None
    dependencies: List[str] = Field(default_factory=list)
    entry_command: Optional[str] = None
    code_repository_url: Optional[str] = None
    code_path: Optional[str] = None
    docker_image: Optional[str] = None
    deployment_url: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Integration(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str
    type: str
    config: Dict[str, Any] = Field(default_factory=dict)
    credentials: Dict[str, str] = Field(default_factory=dict)
    enabled: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Run(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str})
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    plan_id: PyObjectId
    flow_id: PyObjectId
    status: RunStatus = RunStatus.PENDING
    input_data: Dict[str, Any] = Field(default_factory=dict)
    output_data: Dict[str, Any] = Field(default_factory=dict)
    execution_log: List[Dict[str, Any]] = Field(default_factory=list)
    error_message: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow) 