from src.services import *


class Seeder:
    user_service = UserService()
    rank_service = RankService()

    def run(self):
        self.seed_user()
        self.seed_rank()

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
    
    def seed_rank(self):
        records = [
            {
                "id" : 1,
                "mode" : "single",
                "score" : 100,
            },
            {
                "id" : 2,
                "mode" : "single",
                "score" : 200,
            },
            {
                "id" : 2,
                "mode" : "connection",
                "score" : 120,
            },
            {
                "id" : 3,
                "mode" : "single",
                "score" : 40,
            },
            {
                "id" : 3,
                "mode" : "connection",
                "score" : 10,
            },
            {
                "id" : 4,
                "mode" : "single",
                "score" : 700,
            },
        ]
        for record in records:
            user = self.user_service.get_user_by_id(record["id"])
            self.rank_service.update_score(user, record["mode"], record["score"])
