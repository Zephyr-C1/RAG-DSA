#!/bin/bash
set -e
cd "$(dirname "$0")/.."
export PYTHONPATH=.

echo ">>> [Step 1] Ingestion & Dynamic Chunking (ingest)"
python src/ingest/chunking_parser.py

echo ">>> [Step 2] Index Building & Persistent Vector Store (index)"
python src/index/build_faiss_index.py

echo ">>> [Step 3] Dual-Stage Retrieval Unit Test (retrieval)"
python src/retrieval/engine.py

echo ">>> [Step 4] CoD Decision Pipeline & Tool Routing (orchestration)"
python src/orchestration/pipeline.py

echo ">>> [Step 5] Quantitative RAGAS Ablation Benchmark (eval)"
python src/eval/run_ragas_eval.py

echo "========================================================================="
echo " ✅ All 5 modules completed successfully! Artifacts stored in output/."
echo "========================================================================="
