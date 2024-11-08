def formatting_string(amount):
    it_is_float = False

the_amount = str(amount).split(".")

if len(the_amount) == 2:
    it_is_float = True

return it_is_float, the_amount
