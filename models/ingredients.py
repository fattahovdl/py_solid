from abc import abstractmethod


class Ingredient():
    @abstractmethod
    def show(self):
        pass


class Bun_ingredient(Ingredient):
    def __init__(self):
        self.name = "Булочка"
        self.fee = 10
        self.count = 1

    def show(self):
        return f"{self.name} - {self.fee * self.count} - {self.count} шт."

    def add(self):
        self.count += 1


class Sausage_ingredient(Ingredient):
    def __init__(self):
        self.name = "Сосиска"
        self.fee = 20
        self.count = 1

    def show(self):
        return f"{self.name} - {self.fee * self.count} - {self.count} шт."

    def add(self):
        self.count += 1


class Ketchup_ingredient(Ingredient):
    def __init__(self):
        self.name = "Кетчуп"
        self.fee = 5
        self.count = 1

    def show(self):
        return f"{self.name} - {self.fee * self.count} - {self.count} шт."

    def add(self):
        self.count += 1

class Mustard_ingredient(Ingredient):
    def __init__(self):
        self.name = "Горчица"
        self.fee = 5
        self.count = 1

    def show(self):
        return f"{self.name} - {self.fee * self.count} - {self.count} шт."

    def add(self):
        self.count += 1


class Pickle_ingredient(Ingredient):
    def __init__(self):
        self.name = "Огурец маринованный"
        self.fee = 5
        self.count = 1

    def show(self):
        return f"{self.name} - {self.fee * self.count} - {self.count} шт."

    def add(self):
        self.count += 1


class Onion_ingredient(Ingredient):
    def __init__(self):
        self.name = "Лук"
        self.fee = 5
        self.count = 1

    def show(self):
        return f"{self.name} - {self.fee * self.count} - {self.count} шт."

    def add(self):
        self.count += 1


