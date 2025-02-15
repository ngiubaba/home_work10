from src import widget

# from src import masks
# cart_number = int(input("Введите номер карты: "))
# print(masks.get_mask_card_number(cart_number))
#
# account_number = int(input("Введите номер счета: "))
# print(masks.get_mask_account(account_number))


user_input = input("Введите тип и номер карты/счета: ")
print(widget.mask_account_card(user_input))

date_input = input("Введите дату в формате '2024-03-11T02:26:18.671407': ")
print(widget.get_date(date_input))
