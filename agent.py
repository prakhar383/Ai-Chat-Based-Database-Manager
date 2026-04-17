import os
import json
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

# Add these so the AI can read and write to the database!
import database
import models

load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# --- Define the LangGraph Tools for the AI Data Assistant ---

@tool
def save_interaction(hcp_name: str, interaction_type: str, sentiment: str, topics_discussed: str = "", follow_up_actions: str = ""):
    """
    Directly SAVES an interaction to the database. 
    Use this when the user describes a meeting or interaction they want to record.
    """
    db = database.SessionLocal()
    try:
        new_entry = models.Interaction(
            hcp_name=hcp_name,
            interaction_type=interaction_type,
            sentiment=sentiment,
            topics_discussed=topics_discussed,
            follow_up_actions=follow_up_actions
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        
        # We still return the data as JSON so the Frontend can show a "Live Preview"
        return json.dumps({
            "status": "success",
            "message": f"Successfully saved interaction for {hcp_name}",
            "extracted_data": {
                "hcp_name": hcp_name,
                "interaction_type": interaction_type,
                "sentiment": sentiment,
                "topics_discussed": topics_discussed,
                "follow_up_actions": follow_up_actions
            }
        })
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})
    finally:
        db.close()

@tool
def query_database_tool(search_query: str) -> str:
    """
    Searches the entire database for records matching a keyword or name.
    Use this to answer questions about past interactions.
    """
    db = database.SessionLocal()
    try:
        results = db.query(models.Interaction).filter(
            (models.Interaction.hcp_name.ilike(f"%{search_query}%")) |
            (models.Interaction.topics_discussed.ilike(f"%{search_query}%")) |
            (models.Interaction.interaction_type.ilike(f"%{search_query}%"))
        ).all()
        
        if not results:
            return f"No records found for '{search_query}'."
        
        summary = f"I found {len(results)} matching records:\n"
        for r in results:
            summary += f"- [{r.id}] {r.hcp_name} ({r.interaction_date}): {r.topics_discussed}\n"
        return summary
    except Exception as e:
        return f"Database query error: {str(e)}"
    finally:
        db.close()

@tool
def edit_interaction_tool(interaction_id: int, field_to_update: str, new_value: str) -> str:
    """Use this tool to modify or edit existing interaction data in the database by ID."""
    db = database.SessionLocal()
    try:
        item = db.query(models.Interaction).filter(models.Interaction.id == interaction_id).first()
        if not item:
            return f"Could not find record with ID {interaction_id}"
        
        setattr(item, field_to_update, new_value)
        db.commit()
        return f"Updated record {interaction_id}: {field_to_update} is now '{new_value}'."
    except Exception as e:
        return f"Error updating record: {str(e)}"
    finally:
        db.close()

@tool
def analyze_sentiment_tool(notes: str) -> str:
    """Analyzes text to determine if sentiment is Positive, Neutral, or Negative."""
    # In a real app, this would use an LLM or specialized model. 
    # For now, we'll return a placeholder that the agent can override.
    return "The sentiment appears to be Positive based on the context."

# --- Create the LangGraph Agent ---

tools = [
    save_interaction, 
    query_database_tool, 
    edit_interaction_tool, 
    analyze_sentiment_tool
]

system_message = (
    "You are the 'Ai Chat-based Database Manager'. Your goal is to help non-technical users manage "
    "their database through simple conversation. You can save new records, search existing ones, "
    "and edit data. Always confirm when you have successfully saved or changed something in the database. "
    "If information is missing for a record, ask the user concisely."
)

# Create a ReAct agent
agent_executor = create_react_agent(llm, tools, state_modifier=system_message)

def process_chat_message(user_message: str):
    """Passes message to agent and returns FULL response."""
    return agent_executor.invoke({"messages": [("user", user_message)]})