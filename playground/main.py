from sentence_transformers import SentenceTransformer
import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
conn = psycopg2.connect(
    "dbname=Scoutly_DB user=postgres password=Ebethlove22!! host=localhost")
cur = conn.cursor()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/leads/{lead_name}")
def update_item(lead_name: str, business: str, role: str, embedding: float):
    cur.execute(
        "INSERT INTO public.leads (name, business, role, test_val) VALUES (%s, %s, %s, %s)",
        (lead_name, business, role, embedding)
    )
    conn.commit()
    return {"lead_name": lead_name, "business": business, "role": role, "embedding": embedding}
