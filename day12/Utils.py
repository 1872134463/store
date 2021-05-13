import random

class Utils:
    def random(self):
        li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
        account = ""
        for i in range(8):
            index = random.randint(0, len(li) - 1)
            account = account + li[index]
        return account