from queue import Queue
import time
import random


def generate_request(id, queue):
    request = {
        'id': id,
        'name': f'Name {id}',
    }

    queue.put(request)
    print(f'Request {id} added to queue')


def process_request(queue):
    if queue.empty():
        print('Queue is empty')
        return

    request = queue.get()
    time.sleep(random.uniform(0.2, 2))
    print(f'Request {request["id"]} processed')


def main():
    queue = Queue()
    try:
        while True:
            time.sleep(random.uniform(0.5, 1))

            if random.choice([True, False]):
                generate_request(random.randint(1, 100), queue)

            if random.choice([True, False]):
                process_request(queue)

    except KeyboardInterrupt:
        print('Exiting...')


if __name__ == '__main__':
    main()
