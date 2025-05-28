from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.mongodb import get_db, get_apps_collection, get_graphs_collection

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

@app.get("/apps")
async def get_apps():
    apps = list(get_apps_collection().find({}, {"_id": 0}))
    return {"apps": apps}

@app.get("/graphs")
async def get_graphs():
    graphs = list(get_graphs_collection().find({}, {"_id": 0}))
    return {"graphs": graphs} 