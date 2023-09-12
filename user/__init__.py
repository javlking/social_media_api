from pydantic import BaseModel


# валидатор входа в аккаунт
class LoginUserModel(BaseModel):
    email: str
    password: str


# валидатор регистрации пользователя
class RegisterUserModel(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    city: str
    password: str


# валидатор изменения данных пользователя
class EditUserModel(BaseModel):
    user_id: int
    edit_data: str
    new_data: str
