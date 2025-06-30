#!/bin/bash
cat <<EOL > test.log
[2025-06-21 22:00:01] INFO: Application started
[2025-06-21 22:01:12] ERROR: Failed to load config file
[2025-06-21 22:02:45] INFO: Request received
[2025-06-21 22:03:10] WARNING: Memory usage high
[2025-06-21 22:04:00] ERROR: Database connection lost
EOL

echo "✅ 로그 파일(test.log) 생성 완료"
