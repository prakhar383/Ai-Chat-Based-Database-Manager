# AI-First CRM HCP Module: Log Interaction Screen

This repository contains the solution for the AI-First CRM Healthcare Professional (HCP) Module assignment. It features a "Log Interaction Screen" designed for Life Sciences field representatives, allowing them to log meeting details via a structured React form or a conversational AI assistant.


## 🚀 Features
* **Split-Screen Interface:** A modern UI with a structured form on the left and an AI chat interface on the right.
* **State Management:** React components managed globally via Redux Toolkit.
* **FastAPI Backend:** A robust, asynchronous Python backend using SQLAlchemy for ORM.
* **PostgreSQL Database:** Secure and structured data storage for HCP interactions.
* **LangGraph AI Agent:** A stateful ReAct agent powered by Groq (`llama-3.3-70b-versatile`) equipped with 5 specialized tools for sales and CRM activities.

## 🛠️ Tech Stack
* **Frontend:** React.js, Redux Toolkit, Axios, CSS3
* **Backend:** Python 3, FastAPI, Uvicorn, SQLAlchemy, psycopg2
* **AI Framework:** LangChain, LangGraph, Groq API
* **Database:** PostgreSQL

## 🤖 LangGraph Agent Tools
The conversational AI assistant utilizes the following 5 tools to process user requests:
1. **Log Interaction:** Captures interaction data from natural language chat and prepares it for database insertion.
2. **Edit Interaction:** Modifies existing logged data based on user corrections.
3. **Fetch HCP History:** Retrieves past interactions and meeting notes for a specific doctor.
4. **Analyze Sentiment:** Evaluates chat context to determine if the meeting tone was Positive, Neutral, or Negative.
5. **Generate Follow-ups:** Suggests actionable next steps based on the discussion topics.

## 📋 Prerequisites
Ensure you have the following installed on your Windows machine:
* Python 3.x
* Node.js & npm
* PostgreSQL

## ⚙️ Local Setup & Installation

### 1. Database Setup
1. Open **pgAdmin**.
2. Create a new database named `crm_db`.

### 2. Backend Setup
Open a terminal, navigate to your project directory, and set up the Python environment:

```cmd
python -m venv venv
venv\Scripts\activate
python -m pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic langchain langchain-groq langgraph python-dotenv
```

Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_actual_api_key_here
```

Update the database connection string in `database.py` with your PostgreSQL password:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost/crm_db"
```

Start the FastAPI server:
```cmd
python -m uvicorn main:app --reload
```
*The API will be available at http://127.0.0.1:8000*

### 3. Frontend Setup
Open a new terminal window, navigate to the frontend directory, and install the dependencies:

```cmd
cd frontend
npm install
npm start
```
*The UI will be available at http://localhost:3000*

## 📁 Repository Structure
* `/` (Root) - Contains the Python backend (FastAPI, LangGraph agent, SQLAlchemy models).
* `/frontend` - Contains the React app, Redux store, and UI components.
