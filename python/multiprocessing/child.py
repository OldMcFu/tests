import template
import multiprocessing
import logger
class Msg(template.Template):
    
    def __init__(self, msg : str):
        super().__init__(msg)

    def set_up(self) -> list:
        timeline = []
        for x in range(5):
            timeline.append([self.msg, x])
        return timeline

def test_runner():

    q = multiprocessing.Queue()
    obj1 = Msg("Hallo hier ist Obj1")
    obj2 = Msg("Hallo hier ist Obj2")
    obj3 = Msg("Hallo hier ist Obj3")

    p1 = multiprocessing.Process(target=template.runner, args=(obj1.set_up(),))
    p2 = multiprocessing.Process(target=template.runner, args=(obj2.set_up(),))
    p3 = multiprocessing.Process(target=template.runner, args=(obj3.set_up(),))
    p4 = multiprocessing.Process(target=logger.logger, args=(q,))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    for i in range(q.qsize()):
        print(q.get())

if __name__ == '__main__':
    test_runner()