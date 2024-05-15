from abc import abstractmethod
class Hotdog:

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def add_ingredients(self):
        pass


class Classic_hotdog():
    def __init__(self, bun, mustard, sausage):
        self.name = "Классический хотдог"
        self.ingredients = [bun, mustard, sausage]

    def show(self, fee):
        st = f"{self.name}. Состав: "
        for ingredient in self.ingredients:
            st += f"{ingredient.name}, "
        st = st[:-2]
        st += "."
        st += f"\nСтоимость: {fee} рублей"
        print(st)

    def add_ingredients(self):
        pass


class Handmade_hotdog():
    def __init__(self,bun, sausage):
        self.name = "Сделай сам хотдог"
        self.ingredients = [bun, sausage]

    def show(self,fee):
        st = f"{self.name}. Состав: "
        for ingredient in self.ingredients:
            st += f"{ingredient.name}, "
        st = st[:-2]
        st += "."
        st += f"\nСтоимость: {fee}"
        print(st)

    def add_ingredients(self, data):
        self.ingredients.append(data)

