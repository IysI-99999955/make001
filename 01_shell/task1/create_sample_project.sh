#!/bin/bash

# 현재 디렉토리에 프로젝트 폴더 생성
mkdir -p ./my_project

# 예시 파일 생성
echo "print('Hello, Python')" > ./my_project/main.py
echo "<!DOCTYPE html><html><body><h1>Hello HTML</h1></body></html>" > ./my_project/index.html
echo "# Project README" > ./my_project/README.md
echo "name,score\nAlice,90\nBob,85" > ./my_project/data.csv

echo "✅ 샘플 프로젝트 디렉토리(my_project) 생성 완료!"