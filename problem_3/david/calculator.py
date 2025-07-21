def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return print("Error:Division by zero.")
    return a/b

def main():
    try:
        num1=int(float(input("실수형 숫자 입력")))
        num2=int(float(input("실수형 숫자 입력")))
    except:
        print("invalid number.")
    
    
    operator=input("연산자를 입력하세요.")

    if operator == '+':
        result=add(num1,num2)
    elif operator=='-':
        result=subtract(num1,num2)
    elif operator=='*':
        result=multiply(num1,num2)
    elif operator=='/':
        result=divide(num1,num2)
    else:
        print("invalid operator")
    print(f'Result:{result}')

if __name__=='__main__':
    main()