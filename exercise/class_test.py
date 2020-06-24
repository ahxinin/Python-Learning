# 定义一个类

class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score(self):
        print("name is %s score is %s" % (self.name, self.score))


user = Player("jack", 80)
user.get_score()