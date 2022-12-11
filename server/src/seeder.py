from src.services import *


class Seeder:
    user_service = UserService()

    def run(self):
        self.seed_user()

    def seed_user(self):
        users = [
            {
                "username" : "mark",
                "password" : "aabbcc123",
            },
            {
                "username" : "eating",
                "password" : "aabbcc123",
            },
            {
                "username" : "root",
                "password" : "aabbcc123",
            },
            {
                "username" : "admin",
                "password" : "aabbcc123",
            },
            {
                "username" : "guest",
                "password" : "aabbcc123",
            },
        ]
        for user in users:
            new_user = UserModel(user["username"], user["password"])
            self.user_service.add_user(new_user)
        

