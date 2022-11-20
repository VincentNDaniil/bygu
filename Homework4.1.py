
def cheker(function):
    def cheker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f'Houston we have a problem - {exc}.')
        else:
            print(f'There are no problems, everything is fine.. Result - {result}')
    return cheker



def calculate(exprssion):
    return eval(exprssion)

print("In this calculator you can plus all numbers, that you want")
number_1 = input("Input number one - ")
number_2 = input("Input number two - ")

print("Calculating...")

calculate = cheker(calculate)
calculate(f"{number_1}+{number_2}")









