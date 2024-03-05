from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity - len(self.workers) <= 0:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: worker_name == w.name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries_to_pay = 0
        for worker in self.workers:
            current_salary = worker.salary
            total_salaries_to_pay += current_salary
        if self.__budget >= total_salaries_to_pay:
            self.__budget -= total_salaries_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_money_for_care = 0
        for animal in self.animals:
            current_money_for_care = animal.money_for_care
            total_money_for_care += current_money_for_care
        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)
        lions_print = "\n".join(animal.__repr__() for animal in lions)
        tigers_print = "\n".join(animal.__repr__() for animal in tigers)
        cheetahs_print = "\n".join(animal.__repr__() for animal in cheetahs)
        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n" \
               f"{lions_print}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{tigers_print}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{cheetahs_print}"

    def workers_status(self) -> str:
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)
        keepers_print = "\n".join(worker.__repr__() for worker in keepers)
        caretakers_print = "\n".join(worker.__repr__() for worker in caretakers)
        vets_print = "\n".join(worker.__repr__() for worker in vets)
        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{keepers_print}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{caretakers_print}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{vets_print}"





