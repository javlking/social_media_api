from fastapi import APIRouter, UploadFile, Body

from post import PublicPostModel, EditPostModel

from database.postservice import get_all_posts_db, get_exact_post_db, add_post_db, add_post_photo_db, edit_post_db, delete_post_db

# Создать компонент
posts_router = APIRouter(prefix='/user_post', tags=['Работа с публикациями'])


# запрос на публикацию поста
@posts_router.post('/public_post')
async def public_post(data: PublicPostModel):
    result = add_post_db(**data.model_dump())

    return {'status': 1, 'message': result}


# запрос на изменение текста
@posts_router.put('/change_post')
async def change_post(data: EditPostModel):
    result = edit_post_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Пост не найден'}


# запрос на удаление публикации
@posts_router.delete('/delete_post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Пост не найден'}


# запрос на получение публикаций
@posts_router.get('/get_all_posts')
async def get_all_posts():
    result = get_all_posts_db()

    return {'status': 1, 'message': result}


# запрос на добавление фото для публикации
@posts_router.post('/add_photo')
async def add_photo(post_id: int = Body(),
                    user_id: int = Body(),
                    photo_file: UploadFile = None):
    photo_path = f'/media/{photo_file.filename}'

    try:
        # Сохранение фотографии в папку media
        with open(f'media/{photo_file.filename}', 'wb') as file:
            user_photo = await photo_file.read()

            file.write(user_photo)

        # Сохранение ссылки к фотографии в базу
        result = add_post_photo_db(post_id=post_id,
                                   photo=photo_path)

    except Exception as error:
        result = error

    return {'status': 1, 'message': result}


# получить определенный пост
@posts_router.get('/get-exact-post')
async def get_exact_post(post_id: int):
    result = get_exact_post_db(post_id)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Пост не найден'}
