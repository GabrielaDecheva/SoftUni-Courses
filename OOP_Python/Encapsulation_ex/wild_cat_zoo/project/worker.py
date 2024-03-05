class Worker: # base class for any type of employee in the zoo

    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

