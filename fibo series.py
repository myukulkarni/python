n=int(input("enter n"))
print("generate fibo series up to ",n)
for i in range(n):
    first=0
    second=1
    next=first+second
    print(next)
first=second
second=next    