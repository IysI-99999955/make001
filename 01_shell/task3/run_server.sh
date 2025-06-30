#!/bin/bash

PORT=8000

echo "🚀 로컬 테스트 서버 구동 중... (http://localhost:$PORT)"
echo "🔁 중지하려면 Ctrl+C 를 누르세요."

# Python 내장 HTTP 서버 실행
python3 -m http.server "$PORT"
