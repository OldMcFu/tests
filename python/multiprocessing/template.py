import time

class Template():
    def __init__(self, msg : str):
        self.msg = msg
    
    def set_up(self) -> list:
        pass

    
def runner(timeline : list):
    for x in timeline:
        print(x[0])
        time.sleep(x[1])
