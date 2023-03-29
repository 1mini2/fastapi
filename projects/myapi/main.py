from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# 모든 동작인 이 객체로 부터 비롯된다. 핵심
app = FastAPI()

# CORS 설정
origins = [
    "http://127.0.0.1:5173",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app 어노테이션은 /hello라는 URL요청이 발생하면 해당 함수를 실행하여 결과를 리턴하라는 의미이다.
# /hello 라는 URL이 요청되면 FastAPI는 {"message": "안녕하세요 파이보"} 딕셔너리를 리턴한다.
@app.get("/hello")
def hello():
    return {"message": "안녕하세요 파이보"}