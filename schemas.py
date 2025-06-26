from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class TicketStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class TicketCreate(BaseModel):
    title: str
    description: str
    assigned_to: Optional[str] = None

class TicketUpdate(BaseModel):
    status: TicketStatus

class TicketOut(BaseModel):
    id: int
    title: str
    description: str
    status: TicketStatus
    created_at: datetime
    assigned_to: Optional[str]

    class Config:
        orm_mode = True

class StatsOut(BaseModel):
    status: TicketStatus
    count: int
