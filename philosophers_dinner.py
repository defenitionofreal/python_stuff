import time
from threading import Thread, \
    BoundedSemaphore # error if release > acquire

forks = 5
semaphore = BoundedSemaphore(forks) # value = 5

class Philosopher(Thread):

    def __init__(self, index, semaphore):
        Thread.__init__(self)
        self.index = index
        self.semaphore = semaphore

    def run(self):
        if self.index % 2 == 0:
            self.run_one()
        else:
            self.run_two()


    def run_one(self):
        time.sleep(1)
        print('Philosopher {} is hungry \n'.format(self.index))
        self.semaphore.acquire()  # -1 counter
        print('Philosopher {} gets first fork \n'.format(self.index))
        print('Philosopher {} waits for the second fork \n'.format(self.index))
        self.semaphore.acquire()  # -1 counter
        print('Philosopher {} gets second fork \n'.format(self.index))
        print('Philosopher {} eats'.format(self.index))
        self.semaphore.release()  # +1 counter
        print('Philosopher {} released first fork \n'.format(self.index))
        self.semaphore.release()  # +1 counter
        print('Philosopher {} released second fork \n'.format(self.index))

    def run_two(self):
        time.sleep(1)
        print('Philosopher {} is trying to get a first fork \n'.format(self.index))
        if self.semaphore.acquire(False): # blocking=False
            print('Philosopher {} finally gets a first fork \n'.format(self.index))
            print('Philosopher {} is trying to get a second fork \n'.format(self.index))
        if self.semaphore.acquire(False): # blocking=False
            print('Philosopher {} finally gets a second fork \n'.format(self.index))
            self.semaphore.release()
            print('Philosopher {} finally released first fork \n'.format(self.index))
            self.semaphore.release()
            print('Philosopher {} finally released second fork \n'.format(self.index))
        else:
            print('Philosopher {} got unlucky and have to wait \n'.format(self.index))


philosophers = 5

for i in range(philosophers):
    th = Philosopher(i, semaphore)
    th.start()
    #th.join() # blocking other threads



