from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import setup_database, get_db_connection
from agent import launch_agent_session
from contextlib import asynccontextmanager
from agora_token_builder import RtcTokenBuilder
import uvicorn
import os
import time
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

templates = Jinja2Templates(directory="templates")

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_database()
    yield

app = FastAPI(lifespan=lifespan)

# Endpoint to provide App ID and Dynamic Token to the frontend
@app.get("/api/get-token")
async def get_token(channel: str):
    app_id = os.environ.get("AGORA_APP_ID")
    app_cert = os.environ.get("AGORA_APP_CERTIFICATE")
    
    if not app_id or not app_cert:
        return {"error": "Missing Agora credentials in server environment"}

    uid = 1111 
    expiration_time = 86400
    current_time = int(time.time())
    
    token = RtcTokenBuilder.buildTokenWithUid(
        app_id, app_cert, channel, uid, 1, current_time + expiration_time
    )
    return {"token": token, "app_id": app_id}

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})

@app.get("/api/chart-data")
def get_chart_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, lifetime_value FROM customers")
    customers = [dict(row) for row in cursor.fetchall()]
    cursor.execute("SELECT name, reliability_score FROM suppliers")
    suppliers = [dict(row) for row in cursor.fetchall()]
    cursor.execute("SELECT sku, stock_level FROM items")
    items = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"customers": customers, "suppliers": suppliers, "items": items}

@app.post("/api/start-agent")
async def start_agent(background_tasks: BackgroundTasks):
    background_tasks.add_task(launch_agent_session, "data-mesh-sync-test")
    return {"status": "Agent launched"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)