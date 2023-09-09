from fastapi import APIRouter


# Создать компонент
comment_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])


# запрос на публикацию комментария
@comment_router.post('/add_comment')
async def add_comment():
    pass


# запрос на изменение комментария
@comment_router.put('/edit_comment')
async def edit_comment():
    pass


# запрос на удаление комментария
@comment_router.delete('/delete_comment')
async def delete_comment():
    pass


# запрос на получение комментариев к определенной публикации
@comment_router.get('/get_comments')
async def get_comments():
    pass

