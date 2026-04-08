from pathlib import Path
from sentence_transformers import SentenceTransformer
from connect_db import *
from transformers import logging as transformers_logging
from transformers import AutoTokenizer
import numpy as np


class ProfileSimilarityFinder:
    def __init__(self) -> None:

        transformers_logging.disable_progress_bar()
        transformers_logging.set_verbosity_error()

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2")
        self.tokenizer = AutoTokenizer.from_pretrained(
            "sentence-transformers/all-MiniLM-L6-v2")
        self.max_tokens = self.model.max_seq_length

    def chunk_and_encode(self, text):

        chunk_size = self.max_tokens
        tokens = self.tokenizer.tokenize(text)

        with open('tokens.txt', 'a') as a:
            print(tokens, file=a)
        # Split tokens into chunks
        token_chunks = [tokens[i:i + chunk_size]
                        for i in range(0, len(tokens), chunk_size) if (len(tokens)-(chunk_size+i)) >= (chunk_size*.80)]
        # Detokenize to get text
        text_chunks = [self.tokenizer.convert_tokens_to_string(
            chunk) for chunk in token_chunks]
        # Generate embeddings
        embeddings = self.model.encode(text_chunks)
        embeddings = np.mean(embeddings, axis=0)
        return embeddings

    def classify(self, directory: Path = Path("./testProfiles")):

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
                embedding = self.chunk_and_encode(line)
                # calculate the averae embedding for the

                db_insert_lead(
                    name=name,
                    business=profile_meta[name]["business"],
                    role=profile_meta[name]["role"],
                    embedding=embedding
                )
        print("Hello World")
        with open('results.txt', 'a') as f:
            print(db_get_cosine_similarity("jake"), file=f)
        db_delete_leads()


if __name__ == "__main__":
    # classify("lead_derek_castillo.txt")
    app = ProfileSimilarityFinder()
    app.classify()
