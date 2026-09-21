from contextlib import asynccontextmanager
from typing import List

from bson import ObjectId
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field


MONGODB_URI = "mongodb://localhost:27017"
DB_NAME = "bdunab2"
COLL_NAME = "items"

client = None
db = None
coll = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global client, db, coll

    client = AsyncIOMotorClient(MONGODB_URI)
    db = client[DB_NAME]
    coll = db[COLL_NAME]

    yield

    client.close()


app = FastAPI(lifespan=lifespan)


class Item(BaseModel):
    nombre: str = Field(min_length=1)
    precio: float = Field(gt=0)
    tags: List[str] = Field(default_factory=list)
    activo: bool = True


class ItemIn(Item):
    pass


class ItemOut(Item):
    id: str


def doc_to_itemout(doc) -> ItemOut:
    return ItemOut(
        id=str(doc["_id"]),
        nombre=doc["nombre"],
        precio=doc["precio"],
        tags=doc.get("tags", []),
        activo=doc.get("activo", True),
    )


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/mongo-test")
async def mongo_test():
    total = await coll.count_documents({})
    return {
        "status": "ok",
        "items": total
    }