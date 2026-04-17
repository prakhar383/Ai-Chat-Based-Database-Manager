import json
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

# Import our local files
import models
import schemas
import database
import agent 

# Creates the tables in PostgreSQL automatically when the server starts
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Ai Chat based Database Manager")


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows your React app to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- Standard Database Endpoints ---

@app.post("/interactions/", response_model=schemas.InteractionResponse)
def log_interaction(interaction: schemas.InteractionCreate, db: Session = Depends(database.get_db)):
    """Standard endpoint to log an interaction via the structured form."""
    db_interaction = models.Interaction(**interaction.model_dump())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

@app.get("/interactions/", response_model=List[schemas.InteractionResponse])
def get_interactions(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """Standard endpoint to fetch all logged interactions."""
    interactions = db.query(models.Interaction).offset(skip).limit(limit).all()
    return interactions

# --- AI Conversational Agent Endpoint ---

# Schema for the incoming chat message from the frontend
class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
def chat_with_agent(request: ChatRequest):
    """Endpoint that passes the user's chat message to the LangGraph agent."""
    try:
        # Calls the function we built in agent.py
        response = agent.process_chat_message(request.message)
        
        # Default reply is the AI's conversational text
        final_reply = response["messages"][-1].content
        extracted_data = None

        # Look back through the AI's thoughts to see if it used the save_interaction tool
        for msg in reversed(response["messages"]):
            if hasattr(msg, "name") and msg.name == "save_interaction":
                try:
                    tool_result = json.loads(msg.content)
                    if "extracted_data" in tool_result:
                        extracted_data = tool_result["extracted_data"]
                        final_reply = f"✅ I've successfully saved that record to the database! You can see the details in the preview panel on the left."
                        break
                except json.JSONDecodeError:
                    continue

        # Send BOTH the reply text and the hidden form data back to React
        return {
            "reply": final_reply,
            "extracted_data": extracted_data
        }
    except Exception as e:
        # This will print the exact reason to your Uvicorn terminal!
        print(f"🚨 CRITICAL ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Agent Error: {str(e)}")