from fastapi import FastAPI

app = FastAPI()

class LoginRequest(BaseModel):
    id: str
    password: str

@app.get("/login")
def login_endpoint(req: LoginRequest):
    token = login(user_id=req.id, user_password=req.password)
    return {
        "token": token
    }


import requests


def test_login_endpoint():
    # given
    api_host = "localhost:8000"
    payload = {
        "id": "ford",
        "password": "1234"
    }
    
    # when
    res = requests.post(url=f"{api_host}/login", json=payload)
    
    # then
    assert res.data() == {
        "token": "ford_verified"
    }
