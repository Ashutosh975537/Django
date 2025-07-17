from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import RequestLog
import uuid

app = FastAPI()

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get a DB session for each request
def get_db():
    db = SessionLocal()
    try:
        print("🔄 Opening DB session...")
        yield db
    finally:
        print("✅ Closing DB session.")
        db.close()
        
        
@app.get("/")
def root():
    return {"message": "Welcome to the Request Logger API!"}

@app.post("/log/")
async def log_user_request(request: Request, db: Session = Depends(get_db)):
    body = await request.json()
    
    user_id = body.get("user_id", "unknown")

    # Generate request/response IDs
    request_id = str(uuid.uuid4())
    response_id = str(uuid.uuid4())

    # Create log entry
    log = RequestLog(
        user_id=user_id,
        request_id=request_id,
        response_id=response_id
    )

    # Save to DB
    db.add(log)
    db.commit()
    db.refresh(log)

    return {
        "message": "Request logged successfully",
        "log": {
            "id": log.id,
            "user_id": user_id,
            "request_id": request_id,
            "response_id": response_id,
            "timestamp": log.timestamp.isoformat()
        }
    }
