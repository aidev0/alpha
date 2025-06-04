# Alpha Database Service

Independent Docker service providing the database API for Alpha framework.

## Setup

1. **Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB connection details
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Run Locally (Development)**
   ```bash
   pip install -r requirements.txt
   python api.py
   ```

## API Endpoints

- **Health**: `GET /health`
- **Users**: `GET|POST|PUT|DELETE /users`
- **Sessions**: `GET|POST|PUT|DELETE /sessions`
- **Chats**: `GET|POST /chats`
- **Messages**: `GET|POST /messages`
- **Apps**: `GET|POST|PUT /apps`
- **Agents**: `GET|POST /agents`
- **Flows**: `GET|POST /flows`
- **Plans**: `GET|POST /plans`
- **Integrations**: `GET|POST /integrations`
- **Runs**: `GET|POST|PUT /runs`
- **States**: `GET|POST|PUT /states`

## Documentation

Auto-generated API docs available at:
- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

## Database Collections

- `users` - User accounts and profiles
- `sessions` - Browser/request sessions
- `chats` - Conversation threads
- `messages` - Individual chat messages
- `apps` - Application containers
- `agents` - AI agents with code and capabilities
- `flows` - Workflow definitions
- `plans` - Task hierarchies
- `integrations` - External service connections
- `runs` - Execution instances
- `states` - Persistent state data
