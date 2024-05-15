from abc import abstractmethod


class Item:
    @abstractmethod
    def show(self):
        pass


class Classic_hotdog_item(Item):
    def __init__(self, data):
        self.name = data.name
        self.fee = data.fee
    def show(self):
        print( f"{self.name} - {self.fee}")


class Handmade_hotdog_item(Item):

    def __init__(self, data):
        self.name = data.name
        self.fee = data.fee
        self.ingredients = data.ingredients

    def show(self):
        st = f"{self.name} состоит из: "
        for i in self.ingredients:
            st += f"{i.name}, "
        st += f" - {self.fee}"
        print(st)

class Cash_pay_item(Item):
    def __init__(self, fee):
        self.fee = fee
    def show(self):
        print( f"Вы оплатили наличными - {self.fee}")

class Card_pay_item(Item):

    def __init__(self, fee):
        self.fee = fee
    def show(self):
        print( f"Вы оплатили картой - {self.fee}")


class Menu(Item):

    def show(self, *items):
        for item in items:
            item.show()
