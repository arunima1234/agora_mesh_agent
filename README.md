# MDM Intelligence Dashboard & Governance Agent

An enterprise-grade Master Data Management (MDM) Data Governance platform featuring a unified analytics interface and a real-time conversational voice agent. Powered by the high-performance **Agora RTC Network** and **Conversational AI**, this architecture serves as an interactive knowledge base and strategic tool for enterprise data architecture.

---

## 🚀 Key Capabilities & Application Features

* **Voice-Activated Strategy Engine:** Features a real-time, ultra-low latency voice assistant built on the `agora-agents` framework. It interprets incoming audio stream tracks synchronously and uses turn-detection technology optimized for human pacing.
* **Master Data Insight Frameworks:** The backend conversational LLM acts as an on-demand corporate strategy knowledge base, capable of immediately explaining Data Governance structures, Master Data Management rules, distributed data ecosystem tradeoffs, and Data Mesh design patterns.
* **Deterministic Structured Query Routing:** Equipped with multi-layered routing directives. For conceptual inquiries, the assistant leverages semantic contextual understanding to respond concisely. For data-specific lookups, it directly triggers a deterministic schema execution tool to pull ground-truth records.
* **Unified Domain Monitoring:** The front-end delivers an instantly scannable overview monitoring dynamic operational entity data across three crucial corporate data pillars:
  * 🔹 **Customer Domain:** Customer Lifetime Value (LTV) distributions and customer segmentation profiles.
  * 🌿 **Supplier Domain:** Performance metrics displaying partner reliability indicators and contract health statuses.
  * 🔮 **Items Domain:** High-fidelity operational visibility over live SKU inventory thresholds and stock levels.

---

## 🛠️ Infrastructure Prerequisites & Initial Setup

Ensure your local development environment runs **Python 3.12**.

### 1. Clone & Install Dependencies
First, set up your project workspace and install the verified core dependencies and token libraries:

```bash
# Navigate to your project directory
cd agora_mesh_agent

# Install the production-pinned requirements
pip install -r requirements.txt

```

### 2. Generate Your Agora Credentials

To secure communication pipelines, you must register a project configuration inside the Agora Developer Console:

1. Log in to the [Agora Console](https://console.agora.io/).
    
2. Navigate to **Project Management** and click **Create Project**.
    
3. Select **Secured Mode: App ID + Token** during project creation.
    
4. Once created, copy your unique **App ID** string.
    
5. In the project details screen, locate and copy the **Primary Certificate**.
    

### 3. Establish the Environment Configuration (`.env`)

Before initializing the web server layer, you **must** create an environment variables file to safely feed your access keys to the running process.

Create a file named `.env` in the root folder of the project and add your keys exactly like this:

```
# ==============================================================================
# Enterprise Gateway App Credentials
# ==============================================================================
AGORA_APP_ID=your_agora_app_id_here
AGORA_APP_CERTIFICATE=your_agora_primary_certificate_here
```


## 🏁 Running the Application

With the database initialized and environment configuration locked in, execute the main application gateway file:

```bash
python server.py
```

- The system will initialize the persistent database layer (`database.py`) and populate mock tables with baseline sample records if they do not yet exist.
    
- The web gateway will start running via Uvicorn. Open your preferred browser and navigate to: **`http://localhost:8000`**
    
- Click **Connect Voice Agent** to start a real-time dynamic channel token handshake and wake up the voice intelligence system.

## 🗺️ Engineering Roadmap & Future Enhancements

- **Seamless Dual-Query Synchronization Engine:** Upgrade the current SQLite mapping architecture to an active change-data-capture (CDC) pipeline connecting live relational or real-time distributed databases (e.g., PostgreSQL or Redis caches) to optimize deep SQL analytical tooling and vector searches.
    
- **Bidirectional Interactive Visual Controls:** Build an active state synchronization loop between the agent and UI. Asking the agent to adjust filters or calculate complex metrics will automatically render, update, and sort data charts on the client interface in real time.
    
- **Persistent Event Transcription & Auditing:** Integrate the **Agora Cloud Recording / Real-Time Speech-to-Text** REST infrastructure to generate structured, server-side `.vtt` conversational logs. This will display a scrollable text transcript directly in the UI and allow conversation logs to be exported or downloaded.
    
- **Automated Analytical Reporting Workflows:** Enable the assistant to autonomously aggregate analytical records, construct cross-domain data summary files (PDF/JSON format), and distribute them directly via cloud object stores like AWS S3 or Google Cloud Storage.
    
- **Dynamic Context Injection and Memory Refresh:** Implement a real-time data ingestion portal where adding new schemas, business definitions, or entity items allows the voice agent to instantly rebuild its vector store memory layout and understand the new data mid-session.
    

## 👤 Project Author

Developed and maintained by: **Arunima Mishra**