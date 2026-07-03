# Write a program which accept two numbers from user and display the greater number.
def chkGreater(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

def main():
    print("Enter first number");
    no1 = int(input());

    print("Enter second number");
    no2 = int(input());

    ret = chkGreater(no1,no2);
    print(ret," is greater ");


if __name__ == "__main__":
    main()