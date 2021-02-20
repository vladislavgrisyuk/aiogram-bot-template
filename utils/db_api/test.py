import asyncio

from utils.db_api.postgresql import Database



async def test():
    print('Создаем таблицу юзеров...')
    await db.create_table_users()

    await db.add_user('bob', 'bobmarley@gmail.com')
    await db.add_user('John', 'Johndick@gmail.com')

    users = await db.select_all_users()
    print(f'Пользователи: {users}')
loop = asyncio.get_event_loop()
db = Database(loop)
loop.run_until_complete(test())
