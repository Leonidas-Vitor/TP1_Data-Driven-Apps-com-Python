from fastapi import APIRouter
from fastapi import HTTPException 
from pydantic import BaseModel, Field
from datetime import date


router = APIRouter(
    prefix="/tp1_c"
)

class User(BaseModel):
    name: str = Field(alias='nome')
    age: int = Field(alias='idade')
    
    class Config:
        populate_by_name = True

current_users = [
    {'nome': 'Alice', 'idade': 35},
    {'nome': 'Bob', 'idade': 45},
    {'nome': 'Charlie', 'idade': 55},
]

@router.get("/user/{username}")
def hello_user(username: str):
    if username in [user['nome'] for user in current_users]:
        return f"Hello, {username}!"
    else:
        raise HTTPException(status_code=404, detail='Erro 404: Nome de usuário não encontrado')

@router.post("/create-user")
def create_user(newUser: User):
    global current_users
    if newUser.dict() in current_users:
        return 'Usuário já existe'
    current_users.append(newUser.dict())
    return 'Usuário criado com sucesso'

items = [
    {"item_id": 1, "q": "foo"},
    {"item_id": 2, "q": "bar"},
    {"item_id": 3, "q": "baz"},
]

@router.get("/item/{item_id}")
def get_item(item_id: int):
    if item_id not in [item['item_id'] for item in items]:
        raise HTTPException(status_code=400, detail="Erro 400 - Item não encontado")
    return items[item_id]

@router.delete("/item/{item_id}")
def delete_item(item_id: int):
    global items
    if item_id not in [item['item_id'] for item in items]:
        raise HTTPException(status_code=400, detail="Erro 400 - Item não encontado")
    items.pop(item_id)
    return {"message": "Item deletado com sucesso"}


class UserBirthday(BaseModel):
    name: str = Field(alias='nome')
    birthday: date = Field(alias='aniversario')
    
    class Config:
        populate_by_name = True

@router.post("/birthday")
def day_to_birthday(userBirthday: UserBirthday):
    today = date.today()
    next_birthday = userBirthday.birthday.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    days_until_birthday = (next_birthday - today).days

    return f"Faltam {days_until_birthday} dias para o aniversário de {userBirthday.name}"
