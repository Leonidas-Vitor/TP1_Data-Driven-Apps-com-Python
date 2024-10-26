from fastapi import APIRouter

router = APIRouter(
    prefix="/tp1_a"
)

@router.get("/")
def hello():
    return "Hello, FastAPI!"

@router.get("/status")
def status():
    return {"status": "ok"}

@router.get("/user/{username}")
def hello_user(username: str):
    return f"Hello, {username}!"
