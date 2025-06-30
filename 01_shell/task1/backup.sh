#!/bin/bash

SOURCE_DIR="./my_project"
BACKUP_DIR="./backups"
DATE=$(date +%Y-%m-%d)
FILENAME="backup_$DATE.tar.gz"

echo "📁 백업을 시작합니다..."
echo "📂 원본 디렉토리: $SOURCE_DIR"
echo "💾 백업 파일 저장 위치: $BACKUP_DIR/$FILENAME"

mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/$FILENAME" "$SOURCE_DIR"

if [ $? -eq 0 ]; then
    echo "✅ 백업 완료: $BACKUP_DIR/$FILENAME"
else
    echo "❌ 백업 실패"
fi
