

def add(num1, num2):
    sum = num1+num2
    print(sum)


def sub(num1, num2):
    sum = num1-num2
    print(sum)


def multiply(num1, num2):
    sum = num1*num2
    print(sum)


def div(num1, num2):
    sum = num1/num2
    print(sum)


def sqaure(num):
    sum = num*num
    print(sum)


def cube(num):
    sum = num*num*num
    print(sum)


while (True):
    print("\n1.add\n2.sub\n3.multiply\n4.div\n5.sqaure\n6.cube\n7.exit")
    choice = int(input("Enter choice : "))
    if choice == 1:
        num1 = int(input("enter number : "))
        num2 = int(input("Enter number : "))
        add(num1, num2)
    elif choice == 2:
        num1 = int(input("enter number : "))
        num2 = int(input("Enter number : "))
        sub(num1, num2)
    elif choice == 3:
        num1 = int(input("enter number : "))
        num2 = int(input("Enter number : "))
        multiply(num1, num2)
    elif choice == 4:
        num1 = int(input("enter number : "))
        num2 = int(input("Enter number : "))
        div(num1, num2)
    elif choice == 5:
        num = int(input("enter number : "))
        sqaure(num)
    elif choice == 6:
        num = int(input("enter number : "))
        cube(num)
    elif choice == 7:
        break

    else:
        print("incorrect")
