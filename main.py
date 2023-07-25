from roman_to_int import Converter

game = True

while game:

    number = input("Enter roman number to convert. Please use only roman numbers: 'I', 'V', 'X', 'L', 'C', 'D', 'M': ")
    original_number = number.upper()
    new_number = Converter(original_number)
    should_continue = new_number.check_answer()

    if should_continue:
        new_number.roman_to_int()
        print(f"Here is your answer in Arabic Numbers: {new_number.int_number}. ")
        next_round = input("Do you want to insert next number? Type 'y' or 'n': ").lower()
        if next_round == 'y':
            game = True
        elif next_round == 'n':
            game = False
        else:
            print("You provided invalid answer. ")
            game = False
    else:
        print("Please provide valid number. ")