from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class InteractionBase(BaseModel):
    hcp_name: str
    interaction_type: str
    interaction_date: date
    interaction_time: time
    attendees: Optional[str] = None
    topics_discussed: Optional[str] = None
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None
    sentiment: str
    outcomes: Optional[str] = None
    follow_up_actions: Optional[str] = None

class InteractionCreate(InteractionBase):
    pass

class InteractionResponse(InteractionBase):
    id: int

    class Config:
        from_attributes = True