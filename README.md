# AI-First CRM HCP Module: Log Interaction Screen

This repository contains the solution for the AI-First CRM Healthcare Professional (HCP) Module assignment. It features a "Log Interaction Screen" designed for Life Sciences field representatives, allowing them to log meeting details via a structured React form or a conversational AI assistant. 

*Note: In accordance with the assignment requirements, 100% of the code in this repository was generated using AI (Gemini Pro and ChatGPT) with zero human-written code.*

## 🚀 Features

* **Split-Screen Interface:** A modern UI with a structured form on the left and an AI chat interface on the right, styled with the Google Inter font.
* **State Management:** React components managed globally via Redux Toolkit.
* **FastAPI Backend:** A robust, asynchronous Python backend using SQLAlchemy for ORM.
* **PostgreSQL Database:** Secure and structured data storage for HCP interactions.
* **LangGraph AI Agent:** A stateful ReAct agent powered by Groq (`llama-3.3-70b-versatile`) equipped with 5 specialized tools for sales and CRM activities.

## 🛠️ Tech Stack

**Frontend:** React.js, Redux Toolkit, Axios, CSS3
**Backend:** Python 3, FastAPI, Uvicorn, SQLAlchemy, psycopg2
**AI Framework:** LangChain, LangGraph, Groq API
**Database:** PostgreSQL

## 🤖 LangGraph Agent Tools

The conversational AI assistant utilizes the following 5 tools to process user requests:
1. **Log Interaction:** Captures interaction data from natural language chat and prepares it for database insertion.
2. **Edit Interaction:** Modifies existing logged data based on user corrections.
3. **Fetch HCP History:** Retrieves past interactions and meeting notes for a specific doctor.
4. **Analyze Sentiment:** Evaluates chat context to determine if the meeting tone was Positive, Neutral, or Negative.
5. **Generate Follow-ups:** Suggests actionable next steps (e.g., "Send brochure", "Schedule meeting") based on the discussion topics.

## 📋 Prerequisites

Ensure you have the following installed on your Windows machine:
* [Python 3.x](https://www.python.org/downloads/)
* [Node.js & npm](https://nodejs.org/)
* [PostgreSQL](https://www.postgresql.org/)

## ⚙️ Local Setup & Installation

### 1. Database Setup
1. Open pgAdmin.
2. Create a new database named `crm_db`.

### 2. Backend Setup
Navigate to the root directory and set up the Python virtual environment:

```cmd
mkdir hcp_crm_agent
cd hcp_crm_agent
python -m venv venv
venv\Scripts\activate