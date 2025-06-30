#!/bin/bash

DATE=$(date +%Y-%m-%d_%H-%M-%S)
URL="http://localhost:8000"
WEBHOOK_URL="https://hooks.slack.com/services/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" # 실제 슬랙 Webhook URL 필요

echo "🌐 서버 상태 확인 중: $URL"

if curl -s --head "$URL" | grep "200 OK" > /dev/null; then
    echo "✅ 서버 정상 작동 중"

        curl -X POST -H 'Content-type: application/json' \
      --data "{\"text\":\"✅ 서버 정상 구동 중: $URL, $DATE\"}" \
      "$WEBHOOK_URL"
else
    echo "🚨 서버 응답 없음 - 슬랙에 알림 전송"

    curl -X POST -H 'Content-type: application/json' \
      --data "{\"text\":\"🚨 서버 다운: $URL, $DATE\"}" \
      "$WEBHOOK_URL"
fi
