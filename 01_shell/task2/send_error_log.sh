#!/bin/bash

LOG_FILE="./test.log"
DATE=$(date +%Y-%m-%d_%H-%M-%S)
OUTPUT_FILE="./error_report_$DATE.txt"

echo "📑 로그 파일에서 에러 추출 중..."

# error 포함된 라인 추출 (대소문자 무시)
ERRORS=$(grep -i "error" "$LOG_FILE")

if [ ! -z "$ERRORS" ]; then
    echo "$ERRORS" > "$OUTPUT_FILE"
    echo "📝 에러 내용이 '$OUTPUT_FILE'에 저장되었습니다."
else
    echo "✅ 에러 없음"
fi
