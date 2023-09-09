from fastapi import APIRouter


# Создать компонент
posts_router = APIRouter(prefix='/user_post', tags=['Работа с публикациями'])


# запрос на публикацию поста
@posts_router.post('/public_post')
async def public_post():
    pass


# запрос на изменение текста
@posts_router.put('/change_post')
async def change_post():
    pass


# запрос на удаление публикации
@posts_router.delete('/delete_post')
async def delete_post():
    pass


# запрос на получение публикаций
@posts_router.get('/get_all_posts')
async def get_all_posts():
    pass


# запрос на добавление фото для публикации
@posts_router.post('/add_photo')
async def add_photo():
    pass


# запрос на удаление фотографии к публикации
@posts_router.delete('/delete_photo')
async def delete_photo():
    pass


