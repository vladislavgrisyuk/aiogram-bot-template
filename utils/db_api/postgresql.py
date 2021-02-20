import asyncio
import asyncpg

from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = asyncio.get_event_loop().run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                password=config.PGPASSWORD,
                host='127.0.0.1'
            )
        )

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users1 (
        id INT NOT NULL GENERATED BY DEFAULT AS IDENTITY,
        name VARCHAR (255),
        email VARCHAR(255),
        PRIMARY KEY (id) 
        )
        """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
        ])

        return sql, tuple(parameters.values())

    async def add_user(self, user_id: int, char_id: int):
        sql = "INSERT INTO userdata (id, charclassid) VALUES ($1, $2)"

        await self.pool.execute(sql, user_id, char_id)

    async def get_char_id_by_name(self, name: str):
        sql = 'SELECT id FROM charclasses WHERE name = $1'
        return await self.pool.fetchval(sql, name)

    async def select_all_users(self):
        sql = "SELECT * FROM Users1"
        return await self.pool.fetch(sql)

    async def select_user(self, id: int):
        sql = "SELECT COUNT(*) FROM userdata WHERE id = $1"
        return await self.pool.fetchval(sql, id)

    async def count_users(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM CharClasses")

    async def update_user_email(self, email, id):
        sql = "UPDATE USERS1 SET email = $1 where id = $2"
        return await self.pool.execute(sql, email, id)

    async def delete_users(self):
        await self.pool.execute("DELETE FROM Users1")

    async def get_char_classes(self):
        dict = await self.pool.fetch('SELECT id, name FROM CharClasses')
        return dict
