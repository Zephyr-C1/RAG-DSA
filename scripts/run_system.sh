#!/bin/bash
set -e

cd "$(dirname "$0")/.."
export PYTHONPATH=.

echo "========================================================================="
echo " Launching Power Grid DSA System (FastAPI Backend + Streamlit UI) "
echo "========================================================================="

# 强制杀死残留的 8000 与 8501 端口占用，清空显存
echo ">>> Freeing occupied network ports (8000, 8501) and cleaning GPU VRAM..."
fuser -k 8000/tcp 8501/tcp 2>/dev/null || true
pkill -9 -f "src.server.app" 2>/dev/null || true
pkill -9 -f "streamlit" 2>/dev/null || true
sleep 2

# 1. 后台拉起 FastAPI 服务端
python -m src.server.app &
SERVER_PID=$!
echo ">>> FastAPI server starting in background (PID: $SERVER_PID)"

# 2. 动态轮询健康检查接口（等待大模型载入显存完毕）
echo ">>> Polling backend health endpoint while model loads into GPU VRAM..."
until curl -s http://localhost:8000/health | grep -q '"status":"HEALTHY"'; do
    sleep 3
    echo -n "."
done
echo ""
echo "✅ Server initialized successfully. API is live!"

# 3. 启动 Streamlit 前端调度员操作台
echo ">>> Launching Streamlit Operator Dashboard on port 8501..."
python -m streamlit run src/client/dashboard.py \
    --server.port 8501 \
    --server.headless true \
    --browser.gatherUsageStats false

# 退出时释放后台服务端
kill $SERVER_PID 2>/dev/null || true
