from fastapi import APIRouter

router = APIRouter(
    prefix="/tp1_b"
)

@router.get("/user/{username}")
def hello_user(username: str):
    return {'username': username, 'message': f"Welcome, {username}!"}
