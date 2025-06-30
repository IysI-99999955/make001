#!/bin/bash
# Shebang: 스크립트를 /bin/bash에서 실행하도록 지정

if [ $1 -gt 100 ]; then
    # if 문: 첫 번째 인자가 100보다 큰지 확인
    echo "Number is greater than 100"
else
    echo "Number is 100 or less"
fi
