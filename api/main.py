from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from models import Ticket
from schemas import TicketCreate, TicketOut, TicketUpdate, StatsOut, TicketStatus
from database import SessionLocal, engine, Base
from sqlalchemy import func
from fastapi.middleware.cors import CORSMiddleware


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}

# ✅ Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tickets", response_model=TicketOut)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@app.get("/tickets", response_model=List[TicketOut])
def list_tickets(status: Optional[TicketStatus] = Query(None), db: Session = Depends(get_db)):
    query = db.query(Ticket)
    if status:
        query = query.filter(Ticket.status == status)
    return query.all()

@app.put("/tickets/{ticket_id}", response_model=TicketOut)
def update_ticket(ticket_id: int, update: TicketUpdate, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db_ticket.status = update.status
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@app.get("/stats", response_model=List[StatsOut])
def get_stats(db: Session = Depends(get_db)):
    results = db.query(Ticket.status, func.count(Ticket.id)).group_by(Ticket.status).all()
    return [{"status": status, "count": count} for status, count in results]
