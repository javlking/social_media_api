from pydantic import BaseModel


# Валидатор публикации поста
class PublicPostModel(BaseModel):
    user_id: int
    post_text: str


# Валидатор изменения текста к посту
class EditPostModel(BaseModel):
    post_id: int
    new_text: str
    user_id: int

