def input_str(prompt):
    return input(prompt)


def input_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("You need to enter an integer.")


def input_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("You need to enter a decimal number.")


def input_bool(prompt, options=("yes", "no")):
    if len(options) != 2:
        raise ValueError("You can only have two options.")
    while True:
        answer = input(f"{prompt}{('/'.join(options))}: ")
        if answer not in options:
            print(f"---You need to one of following commands: {'/'.join(options)}")
            continue
        if answer == options[1]:
            return True 
        else:
            return False

def input_int_choice(prompt, choices):
    if type(choices) not in [list, tuple]:
        raise ValueError("choices needs to be a list or tuple")
    while True:
        answer = int(input(f"{prompt}"))
        if answer not in choices:
            print("Answer is not in any of the choices.")
            continue
        return answer