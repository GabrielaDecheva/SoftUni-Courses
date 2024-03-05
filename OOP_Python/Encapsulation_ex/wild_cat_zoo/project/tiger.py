from project.animal import Animal


class Tiger(Animal):
    EXACT_MONEY_FOR_CARE = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=Tiger.EXACT_MONEY_FOR_CARE)