from pathlib import Path
import re
from sentence_transformers import SentenceTransformer
from connect_db import *
import torch
from transformers import logging as transformers_logging

# Suppress all transformers logging
transformers_logging.disable_progress_bar()
transformers_logging.set_verbosity_error()

# Acquire the SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
model_max_token = model.max_seq_length


# Embed lines the data from each profile and return a vector representation
def embedd(lines: list[str]) -> torch.Tensor:
    combined = " ".join(lines)
    embedding = model.encode(combined)
    print(type(embedding))
    return embedding


def classify(filename: str | None):
    directory = Path("./testProfiles")
    profile_meta = {
        "derek": {"business": "IT", "role": "Senior Sales Representative"},
        "marcus": {"business": "Financial", "role": "Sales Director"},
        "rachel": {"business": "Health Care", "role": "Account Manager"},
        "jake": {"business": "IT", "role": "Regional Sales Manager"}
    }

    for path in directory.iterdir():
        name = path.stem.split("_")[1]  # extract name from filename
        print(name)
        if name not in profile_meta:
            continue

        with open(path) as f:
            line = f.readline()
            lines = re.split(r'(?<!etc)\.\ ?', line)
            embedding = embedd(lines).tolist()

            db_insert_lead(
                name=name,
                business=profile_meta[name]["business"],
                role=profile_meta[name]["role"],
                embedding=embedding
            )

    print(db_get_cosine_similarity("jake"))
    db_delete_leads()


if __name__ == "__main__":
    # classify("lead_derek_castillo.txt")
    classify(None)
