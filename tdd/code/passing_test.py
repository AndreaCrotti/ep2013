class Queue(object):
    def __init__(self):
        self.queue = []

    def empty(self):
        # return False
        return self.queue == []


def test_queue_empty():
    q = Queue()
    assert q.empty, "Queue is not empty in the beginning"


class TestQueue(unittest.TestCase):
    def test_can_add_to_empty_queue(self):
        q = Queue()
        self.assertTrue(q.empty())


if __name__ == '__main__':
    test_queue_empty()
