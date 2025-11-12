from fastapi import FastAPI
from routes import damages
from db.database import engine, Base
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("📦 Initializing database...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database is ready (tables created if not exist).")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(damages.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)