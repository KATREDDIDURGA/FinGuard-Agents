from fastapi import FastAPI

app = FastAPI(
    title="FinGuard Agents",
    description="Multi-Agent Fraud Detection & Explanation System",
    version="0.1"
)

@app.get("/health")
async def health_check():
    return {"status": "FinGuard Agents API is up and running 🚀"}
