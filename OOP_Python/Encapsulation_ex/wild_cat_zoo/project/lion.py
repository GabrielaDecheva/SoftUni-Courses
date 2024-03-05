from project.animal import Animal


class Lion(Animal):
    EXACT_MONEY_FOR_CARE = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=Lion.EXACT_MONEY_FOR_CARE)