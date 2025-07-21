def main():
    try:
        a=float(input("Enter number:"))

    except:
        print("Invalid number input.")

    try:
        b=int(input("Enter exponent"))

    except:
        print("Invalid exponent input.")

    Result=1

    for i in range(b):
        Result *= a
    print("Result:", Result)
if __name__=="__main__":
    main()