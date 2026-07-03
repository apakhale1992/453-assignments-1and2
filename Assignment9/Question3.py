#Square of number using function
def Square(Number):
    return Number * Number

def main():
    print("Enter number : ");
    Value = int(input());

    Ret = Square(Value);
    print("Square of number is : ",Ret);

if __name__ == "__main__":
    main()