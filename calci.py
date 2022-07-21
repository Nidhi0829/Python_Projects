def calci(a,op,b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    else:
        print("wrong operator")

x = int(input())
y = int(input())
operat = input()

value = calci(x,operat,y)
print(value)
