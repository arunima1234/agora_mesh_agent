import os
from dotenv import load_dotenv
from agora_agent import Agora, Agent, Area, DeepgramSTT, OpenAI, MiniMaxTTS, expires_in_hours
from database import execute_sql_query

load_dotenv()

# FIX: Highly prescriptive prompt to stop hallucinations and speed up responses
DATA_GOVERNANCE_PROMPT = """
You are an elite Enterprise Master Data Management (MDM), Data Governance, and Data Mesh AI Assistant.
Your primary role is to serve as an expert informational guide. You fluently explain complex concepts, system architecture trade-offs (such as scaling distributed systems or using message brokers for data sync), advanced data pipeline management, and product strategy frameworks.

CONVERSATION RULES:
1. For general questions about MDM, Data Mesh, Governance, or concepts, rely ONLY on your internal knowledge. DO NOT trigger any tools. Speak naturally, concisely, and immediately.
2. Keep explanations professional, focusing on enterprise-grade solutions.

DATABASE QUERY RULES (SECONDARY FUNCTION):
You are connected to a mock SQLite database. 
Schema:
- customers: id, name, churn_risk, lifetime_value
- suppliers: id, name, reliability_score, active_contracts
- items: id, sku, category, stock_level

1. ONLY use the 'execute_sql_query' tool if the user explicitly asks about the internal database records (e.g., "How many customers are there?", "What is in the items table?").
2. NEVER guess the data. NEVER assume a table has 0 records.
3. You must completely wait for the tool's JSON output before speaking. 
4. If you run SELECT COUNT(*) FROM customers and the tool returns [{"COUNT(*)": 5}], you must confidently say "There are 5 records."
5. You are an expert at advanced SQL (including CTEs). If complex data is requested, write the optimal query.
"""

# Tool schema
sql_tool = {
    "type": "function",
    "function": {
        "name": "execute_sql_query",
        "description": "Execute a valid SQL query against the SQLite database to fetch data or schema info.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "A valid SQL query string"}
            },
            "required": ["query"]
        }
    }
}

async def launch_agent_session(channel_name: str):
    app_id = os.environ.get("AGORA_APP_ID")
    app_cert = os.environ.get("AGORA_APP_CERTIFICATE")
    
    client = Agora(area=Area.US, app_id=app_id, app_certificate=app_cert)

    agent = Agent(client=client, turn_detection={"language": "en-US"})

    agent = agent.with_stt(DeepgramSTT(model="nova-3", language="en"))
    
    agent = agent.with_llm(
        OpenAI(
            model="gpt-4o-mini",
            system_messages=[{"role": "system", "content": DATA_GOVERNANCE_PROMPT}],
            greeting_message="Data Governance Dashboard online. How can I assist you?"
        )
    )
    
    agent = agent.with_tts(MiniMaxTTS(model="speech_2_6_turbo", voice_id="English_captivating_female1"))

    if hasattr(agent, "add_tool"):
        agent.add_tool(sql_tool, execute_sql_query)
    
    session = agent.create_session(
        channel=channel_name,
        agent_uid="999999",
        remote_uids=["*"],
        idle_timeout=300,
        expires_in=expires_in_hours(1),
    )
    
    session.start()
    print(f"DEBUG: Agent session started for channel: {channel_name}")
    return session
