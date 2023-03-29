# 얼렁뚱땅 따라해보기
https://wikidocs.net/177373


# 가상환경 실행
source venv/bin/activate
# frontend 실행
cd projects/myapi/frontend && npm run dev

# fastapi 서버 실행
cd projects/myapi/ && uvicorn main:app --reload