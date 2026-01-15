from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

SECRET_KEY = "mysecretkey"  # In real apps, use env vars

app = FastAPI()
auth_scheme = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/")
def public():
    return {"message": "Welcome to the Secure API!"}

@app.get("/private")
def private(payload=Depends(verify_token)):
    return {"message": f"Hello {payload['user']}, this is a private endpoint!"}

@app.post("/token")
def get_token(user: str):
    token = jwt.encode({"user": user}, SECRET_KEY, algorithm="HS256")
    return {"token": token}
