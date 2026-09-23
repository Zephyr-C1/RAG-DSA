#!/bin/bash
set -e

echo "=================================================="
echo "Starting Clean Update for Cyprus Grid Knowledge Base"
echo "=================================================="

# 1. 显式删除所有历史切分缓存、索引与临时输出残留
echo "[1/4] Purging old cache, vector indices, and temporary outputs..."
rm -rf data/processed/*
rm -rf data/index/*
rm -rf output/*
rm -f data/benchmark/eval_results.json

# 确保目标输出目录存在
mkdir -p data/processed
mkdir -p data/index
mkdir -p output

# 2. 重新进行切分与结构化解析 (Chunking)
echo "[2/4] Chunking new regulatory documents (KM Version 1.1.0 & Operating Margin Policy)..."
python3 src/ingest/chunking_parser.py

# 3. 重新构建 FAISS 稠密索引与 BM25 稀疏索引
echo "[3/4] Rebuilding FAISS vector index from clean slate..."
python3 src/index/build_faiss_index.py

# 4. 验证更新结果
echo "[4/4] Verifying generated index files..."
ls -lh data/index/

echo "=================================================="
echo "Knowledge base successfully rebuilt with ZERO residue!"
echo "=================================================="