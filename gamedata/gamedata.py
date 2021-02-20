from loader import db


class GameData:
    @staticmethod
    async def get_all_char_classes():
        char_classes = []
        resp = await db.get_char_classes()
        for x in resp:
            char_classes.append(x.get('name'))
        return char_classes

    @staticmethod
    async def create_user_character(user_id: int, class_name: str):
        char_id = await db.get_char_id_by_name(class_name)
        await db.add_user(user_id=user_id, char_id=char_id)

    @staticmethod
    async def user_already_exists(user_id: int):
        if await db.select_user(user_id) > 0:
            return True
        else:
            return False
