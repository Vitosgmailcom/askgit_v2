
class SQLStatements(object):

    def get_all_users(self):
        pass

    def get_user_by_id(self):
        pass

    def get_random_user(self):
        return f"SELECT * FROM users WHERE `group`='APG777' order by id desc limit 100;"

    def get_user_by_name(self, name):
        return f"SELECT * FROM users WHERE name='{name}';"