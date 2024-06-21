from data.DefaultDataBase import DefaultDataBase


class UserRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def get_user(self, user_id):
        query = "SELECT * FROM `app1_olympus_users` WHERE `user_id` = %s;"
        return self._select_one(query, (user_id,))

