from data.DefaultDataBase import DefaultDataBase


class UserRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()

    def get_user(self, user_id, bundle):
        query = "SELECT * FROM `users2` WHERE `user_id` = %s AND `bundle` = %s;"
        return self._select_one(query, (user_id, bundle))

