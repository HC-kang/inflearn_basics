from fastapi import FastAPI
from dataclasses import dataclass

app = FastAPI()

@dataclass
class LoginRequest:
    id: str
    password: str


# @app.post("/login")
# def login_endpoint(req: LoginRequest):
#     user_id = req.id
#     user_password = req.password
    
#     user_repository = UserRepository()
#     user = user_repository.find_by_id(user_id)
#     if user_id == user.id and user.password == user_password:
#         token = user_id + "_verified"
#     else:
#         raise Exception("로그인 인증에 실패했습니다.")

#     return {
#         "token": token
#     }

@app.post("/login")
def login_endpoint(req: LoginRequest):
    token = login(user_id=req.id, user_password=req.password)
    return {
        "token": token
    }