class Queue:
    def __init__(self) -> None:
        self.l = []

    def __repr__(self) -> str:
        return str(self.l)

    def enqueue(self, data) -> None:
        self.l.append(data)

    def dequeue(self) -> int:
        try:
            dequeue_data = self.l[0] 
            del self.l[0]
            return dequeue_data
        except IndexError:
            raise IndexError("the queue is empty")
