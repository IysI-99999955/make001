#!/bin/bash

# 가상환경 이름
ENV_NAME="python_sesac"

# Python 3.11.8이 설치되어 있는지 확인
if ! pyenv versions | grep -q "3.11.8"; then
  echo "❌ Python 3.11.8이 설치되어 있지 않음. 먼저 설치해줘."
  exit 1
fi

# 가상환경 생성 (이미 있으면 건너뜀)
if ! pyenv virtualenvs | grep -q "$ENV_NAME"; then
  echo "👉 가상환경 '$ENV_NAME' 생성 중..."
  pyenv virtualenv 3.11.8 $ENV_NAME
else
  echo "ℹ️ 가상환경 '$ENV_NAME' 이미 존재함. 생략함."
fi

# 해당 가상환경 활성화
pyenv activate $ENV_NAME

# jupyter 설치
pip install --upgrade pip
pip install jupyter

# .bashrc에 자동 활성화 설정 추가
PROFILE_FILE="$HOME/.bashrc"
if ! grep -q "pyenv activate $ENV_NAME" "$PROFILE_FILE"; then
  echo "" >> "$PROFILE_FILE"
  echo "# python_sesac 가상환경 자동 활성화" >> "$PROFILE_FILE"
  echo "export PATH=\"\$HOME/.pyenv/bin:\$PATH\"" >> "$PROFILE_FILE"
  echo "eval \"\$(pyenv init -)\"" >> "$PROFILE_FILE"
  echo "eval \"\$(pyenv virtualenv-init -)\"" >> "$PROFILE_FILE"
  echo "pyenv activate $ENV_NAME" >> "$PROFILE_FILE"
fi

echo "✅ 'python_sesac' 가상환경 생성 및 jupyter 설치 완료"
echo "📌 터미널을 다시 켜거나 'source ~/.bashrc' 실행하면 자동 활성화됨"