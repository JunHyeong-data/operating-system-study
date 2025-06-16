import os
import threading

def foo():
    print('foo: my thread id is: ', threading.get_native_id())
    print('foo: my pid is: ', os.getpid())

if __name__ == '__main__':
    print('my pid is: ', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()