import os
import shutil
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

INDEX_DIR = Path("data/index")
PROCESSED_CHUNKS_PATH = Path("data/processed/chunks.json")
MODEL_NAME = "BAAI/bge-small-en-v1.5"

def clean_target_directory(target_dir: Path):
    if target_dir.exists():
        logger.info(f"Purging existing index directory: {target_dir}")
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

def build_index():
    clean_target_directory(INDEX_DIR)

    if not PROCESSED_CHUNKS_PATH.exists():
        raise FileNotFoundError(f"Processed chunks not found at {PROCESSED_CHUNKS_PATH}. Run chunking_parser.py first.")

    with open(PROCESSED_CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks: List[Dict[str, Any]] = json.load(f)

    logger.info(f"Loaded {len(chunks)} chunks from {PROCESSED_CHUNKS_PATH}")
    texts = [c["content"] for c in chunks]

    logger.info(f"Loading embedding model: {MODEL_NAME}...")
    embed_model = SentenceTransformer(MODEL_NAME)

    logger.info("Generating embeddings for all regulatory chunks...")
    embeddings = embed_model.encode(texts, batch_size=32, show_progress_bar=True, normalize_embeddings=True)
    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    logger.info(f"Building FAISS IndexFlatIP with dimension {dim}...")
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    index_file = INDEX_DIR / "faiss_index.bin"
    faiss.write_index(index, str(index_file))

    meta_file = INDEX_DIR / "docstore.json"
    with open(meta_file, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    logger.info(f"Successfully saved clean FAISS index to {index_file}")
    logger.info(f"Successfully saved docstore mapping to {meta_file}")

if __name__ == "__main__":
    build_index()