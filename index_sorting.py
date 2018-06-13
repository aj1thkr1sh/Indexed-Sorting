
max_size = 99999999

default_variable = -1

a = [default_variable]*max_size

n = int(input("Enter the Number"))

for i in range(0,n):
    t = int(input())
    if a[t] == -1 :
        a[t] = 0
    a[t] = a[t]+t

for i in range(0,max_size):
    if a[i] != -1 :
        if a[i] != i :
            tmp = a[i]
            for t in range(0,int(tmp/i)) :
                print(i)
        else:
            print(i)

