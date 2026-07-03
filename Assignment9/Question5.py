def divisibleBy3And5(no):
    if((no % 3 == 0) and (no % 5 == 0)):
        return True
    else:
        return False
    
def main():
    print("Enter number : ");
    Value = int(input());

    Ret = divisibleBy3And5(Value);
    if(Ret == True):
        print("Dvisible by 3 and 5");
    else:
        print("Not divisible by 3 and 5");

if __name__ == "__main__":
    main()