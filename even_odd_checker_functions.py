# ESPINO NICHAELA
# ITELECT2
# Laboratory #20 - Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python 

def main():
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            result = f"{number} is an Even number."
        else:
            result = f"{number} is an Odd number."
        print(result)
    except ValueError:
        print("Please Enter a Valid Integer.")
if __name__=="__main__":
    main()
