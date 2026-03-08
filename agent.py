import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

load_dotenv()

# Initialize the LLM required by the assignment
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# --- Define the 5 LangGraph Tools ---

@tool
def log_interaction_tool(hcp_name: str, notes: str) -> str:
    """Use this tool to capture and log new interaction data with an HCP."""
    # In the next step, we will connect this to the FastAPI database session
    return f"Successfully drafted interaction log for {hcp_name} based on notes: {notes}"

@tool
def edit_interaction_tool(interaction_id: int, field_to_update: str, new_value: str) -> str:
    """Use this tool to modify or edit existing logged interaction data."""
    return f"Updated interaction {interaction_id}: {field_to_update} is now {new_value}"

@tool
def fetch_hcp_history_tool(hcp_name: str) -> str:
    """Use this tool to retrieve past interactions and meetings with a specific HCP."""
    return f"Fetched historical data for {hcp_name}."

@tool
def analyze_sentiment_tool(notes: str) -> str:
    """Use this tool to analyze the notes and determine if HCP sentiment was Positive, Neutral, or Negative."""
    return "Analyzed sentiment: Positive"

@tool
def generate_follow_ups_tool(notes: str) -> str:
    """Use this tool to suggest follow-up actions based on the meeting notes."""
    return "Suggested follow-up: Send product brochure and schedule follow-up in 2 weeks."

# --- Create the LangGraph Agent ---

tools = [
    log_interaction_tool, 
    edit_interaction_tool, 
    fetch_hcp_history_tool, 
    analyze_sentiment_tool, 
    generate_follow_ups_tool
]

# Create a ReAct agent that knows how to use these tools
agent_executor = create_react_agent(llm, tools)

def process_chat_message(user_message: str):
    """Passes the user's message to the LangGraph agent and returns the response."""
    response = agent_executor.invoke({"messages": [("user", user_message)]})
    return response["messages"][-1].content