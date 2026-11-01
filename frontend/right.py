from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.get("/api/status")
def status():
    return {
        "status": "idle",
        "participants": 1,
        "room": "Demo Room",
        "region": "India"
    }

@app.post("/api/start-session")
def start_session():
    return {
        "message": "Session Started",
        "status": "active"
    }

@app.post("/api/stop-session")
def stop_session():
    return {
        "message": "Session Stopped",
        "status": "idle"
    }