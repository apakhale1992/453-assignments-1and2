# Write a program which contains one function named as Cube.
def Cube(no):
    return no * no * no

def main():
    print("Enter number : ");    Value = int(input());

    Ret = Cube(Value);
    print("Cube of number is : ",Ret);

if __name__ == "__main__":
    main()