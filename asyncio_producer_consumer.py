import random
import asyncio

warehouse = []
max_elements = 10

def is_overflow():
    return len(warehouse) >= max_elements


def is_underflow():
    return len(warehouse) == 0


async def producer():
    while True:
        x = random.randint(1, 10000)
        print('Produced: ' + str(x))

        if not is_overflow():
            warehouse.append(x)
        else:
            print("producer pass")

        await asyncio.sleep(random.random() * 2.0)


async def consumer():
    while True:
        if not is_underflow():
            x = warehouse.pop(0)
            print('Consumed: ' + str(x))
        else:
            print("consumer pass")
        await asyncio.sleep(random.random() * 2.0)



loop = asyncio.get_event_loop()

for i in range(6):
    loop.create_task(producer())

for i in range(3):
    loop.create_task(consumer())

loop.run_forever()



