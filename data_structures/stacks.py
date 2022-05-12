class Stack:
    def __init__(self) -> None:
        self.l = []

    def __repr__(self) -> str:
        return str(self.l)

    def push(self, data) -> None:
        self.l.append(data)
        
    def pop(self) -> int:
        try:
            popped_data = self.l[-1]
            del self.l[-1]

            return popped_data
        except IndexError:
            raise IndexError("the stack is empty")
