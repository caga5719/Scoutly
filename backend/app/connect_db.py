import psycopg
from pydantic import BaseModel, field_validator
from typing import List

# pydantic lead data model for sql record insert into lead and sales data


class Lead(BaseModel):
    name: str
    business: str
    role: str
    embedding: List[float]

    @field_validator("embedding")
    @classmethod
    def validate_embedding(cls, v):
        if len(v) != 384:
            raise ValueError(f"Embedding must be 384 dimensions, got {len(v)}")
        return v

# Connect to the Scoutly_DB
# TODO encryp username and password credentials


def get_connection():
    return psycopg.connect("host=localhost dbname=Scoutly_DB user=postgres password=Ebethlove22!!")


def db_insert_lead(name: str, business: str, role: str, embedding: List[float]):
    lead = Lead(name=name, business=business,
                role=role, embedding=embedding)

    conn = get_connection()
    with conn:
        conn.execute(
            "INSERT INTO leads (name, business, role, embedding) VALUES(%s, %s, %s, %s::vector)",
            (lead.name, lead.business, lead.role, lead.embedding)
        )
        conn.commit()


def db_delete_leads():

    conn = get_connection()
    with conn:
        conn.execute(
            "DELETE FROM leads"
        )
        conn.commit()


def db_get_cosine_similarity(sales_lead: str):
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT name, embedding <=> (SELECT embedding FROM leads WHERE name = %s) AS distance
        FROM leads
        WHERE name != %s
        ORDER BY distance
        LIMIT 3;
    """, (sales_lead, sales_lead))
        results = cursor.fetchall()
    return results


if __name__ == "__main__":
    get_connection()
