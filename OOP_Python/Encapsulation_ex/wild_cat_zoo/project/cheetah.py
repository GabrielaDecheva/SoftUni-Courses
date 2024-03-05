from project.animal import Animal


class Cheetah(Animal):
    EXACT_MONEY_FOR_CARE = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=Cheetah.EXACT_MONEY_FOR_CARE)
