# Ai chat based Database Manager

This repository contains an AI-powered Database Management System (DBMS) designed for non-technical users. It allows users to manage a PostgreSQL database entirely through a conversational AI assistant, removing the need for complex SQL queries or manual data entry forms.

## 🚀 Key Features
* **Conversational Data Entry:** Just tell the AI what happened (e.g., "I met Dr. Smith today, it was positive") and it will structure and save the data for you.
* **Natural Language Queries:** Ask questions like "Who did I meet last week?" or "Find all positive interactions" and get instant answers.
* **Live Data Preview:** A split-screen UI that shows a real-time preview of the record the AI is currently managing.
* **Automated Persistence:** The AI agent handles database commits directly, ensuring data is saved securely and instantly.
* **LangGraph AI Agent:** A stateful ReAct agent powered by Groq (`llama-3.3-70b-versatile`) that understands database operations.

## 🛠️ Tech Stack
* **Frontend:** React.js, Redux Toolkit, CSS3 (Modern, Responsive UI)
* **Backend:** Python 3, FastAPI, SQLAlchemy (ORM)
* **AI Framework:** LangChain, LangGraph, Groq API (Llama 3.3 70B)
* **Database:** PostgreSQL

## 🤖 AI Assistant Capabilities
The AI manager uses specialized tools to handle the database:
1. **Save Interaction:** Automatically structures and saves data from chat to the database.
2. **Query Database:** Searches and retrieves records using natural language keywords.
3. **Smart Editing:** Allows you to correct or update existing records just by asking.
4. **Sentiment Analysis:** Automatically tags the tone of interactions based on your notes.

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
