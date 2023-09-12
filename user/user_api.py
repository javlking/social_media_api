from fastapi import APIRouter
from user import RegisterUserModel, LoginUserModel, EditUserModel


# Создать компонент
user_router = APIRouter(prefix='/user', tags=['Управление пользователями'])


# запрос на вход в аккаунт
@user_router.post('/login')
async def login_user(data: LoginUserModel):
    pass


# запрос на регистрацию пользователя
@user_router.post('/register')
async def register_user(data: RegisterUserModel):
    pass


# запрос на изменение информации пользователя
@user_router.put('/change_info')
async def change_info(data: EditUserModel):
    pass


# запрос на получение информации о пользователе
@user_router.get('/get_user')
async def get_user(user_id: int):
    pass

