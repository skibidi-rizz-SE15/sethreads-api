from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemyseeder import ResolvingSeeder

from .database import SessionLocal, engine
from . import models
from .api import auth, api

def is_database_empty(session):
    return session.query(models.Students).first() is None

def seed_database():
    with SessionLocal() as session:
        if is_database_empty(session):
            ResolvingSeeder(session).load_entities_from_json_file("src/seed.json")
            session.commit()
            print("Database seeded successfully.")
        else:
            print("Database already contains data. Skipping seeding.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    seed_database()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(api.router)

@app.get("/")
def read_root():
    return {"Hello": "Hackers"}