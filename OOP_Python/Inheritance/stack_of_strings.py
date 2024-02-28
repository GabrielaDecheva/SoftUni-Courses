class Stack:
    def __init__(self):
        self.data = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return True if not self.data else False

    def __str__(self) -> str:
        reversed_stack = reversed(self.data)
        result = ", ".join(reversed_stack)
        return f"[{result}]"


s = Stack()
s.push("one")
s.push("two")
s.push("three")
print(s)
s.pop()
print(s)
s.top()
print(s.is_empty())
s.pop()
s.pop()
print(s.is_empty())
print(s)
