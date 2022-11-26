import multiprocessing

def logger(q : multiprocessing.Queue):
    for i in range(10):
        q.put(i)