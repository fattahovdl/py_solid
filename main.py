from models import *

bun = Bun_ingredient()
mustard = Mustard_ingredient()
sausage = Sausage_ingredient()

hotdog = Classic_hotdog(bun, mustard, sausage)
handmade_hotdog = Handmade_hotdog(bun, sausage)


calc = Calc()
hotdog.fee = calc.calculate(hotdog.ingredients)
handmade_hotdog.fee = calc.calculate(handmade_hotdog.ingredients)

classic_hotdog_item = Classic_hotdog_item(hotdog)
handmade_hotdog_item = Handmade_hotdog_item(handmade_hotdog)

fee = hotdog.fee

cash_pay_item = Cash_pay_item(fee)
card_pay_item = Card_pay_item(fee)

menu = Menu()
menu.show(classic_hotdog_item,handmade_hotdog_item)