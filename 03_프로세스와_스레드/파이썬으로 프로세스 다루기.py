from multiprocessing import Process
import os

def foo():
    print('foo: child process: ', os.getpid())
    print('foo: parent process: ', os.getppid())

if __name__ == '__main__':
    print('parent process: ', os.getpid())

    child1 = Process(target=foo)
    child2 = Process(target=foo)
    child3 = Process(target=foo)

    child1.start()
    child2.start()
    child3.start()

    child1.join()
    child2.join()
    child3.join()