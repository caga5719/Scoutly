from pathlib import Path
import re
from sentence_transformers import SparseEncoder
from pydantic import BaseModel, field_validator
from typing import List
from sentence_transformers import SentenceTransformer
import psycopg

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


# Acquire the SparceEncoder
model = SparseEncoder("sentence-transformers/all-MiniLM-L6-v2")
model_max_token = model.max_seq_length


# Embed lines the data from each profile and return a vector representation
def embedd(lines: list[str]) -> List[float]:
    # [print(line+'\n') for line in lines]
    # embedd lines in vector and check for line coutn
    line_count = len(lines)
    combined = " ".join(lines)
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embedding = model.encode(combined)
    # while line_count > 0
    return embedding.tolist()

# Connect to the Scoutly_DB
# TODO encryp username and password credentials


def get_connection():
    return psycopg.connect("host=localhost dbname=Scoutly_DB user=postgres password=Ebethlove22!!")


def classify(fillename: str | None):
    directory = Path("./testProfiles")
    test = []

    for path in directory.iterdir():
        with open(path) as f:
            line = f.readline()
            lines = re.split(r'(?<!etc)\.\ ?', line)
            test = embedd(lines)
            # print(f"\nlines count:{len(lines)} \n\n {lines[:-1]}")
    lead = Lead(name='Jack', business='ACME',
                role='manager', embedding=test)

    conn = get_connection()
    with conn:
        conn.execute(
            "INSERT INTO leads (name, business, role, embedding) VALUES(%s, %s, %s, %s::vector)",
            (lead.name, lead.business, lead.role, lead.embedding)
        )
        conn.commit()


if __name__ == "__main__":
    # classify("lead_derek_castillo.txt")
    classify(None)
