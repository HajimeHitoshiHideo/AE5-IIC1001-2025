def BS(x, ls):
    l = 0
    r = len(ls)-1
    o = "Not Found"
    while(o == "Not Found" and r-l >= 0):
        m = int(l + ((r-l)/2))
        if(ls[m] > x):
            r = m-1
        elif(ls[m] < x):
            l = m+1
        else:
            o = m+1
    return o

L = []

print("Type integers to add them to a list, to stop type 'END'")
a = input()

I = 1

while(a != "END"):
    L.append(int(a))
    a = input()

L.sort()

print("Now type an integer to find in the list")
print("you will be given the index of an appearance of the number (starting from 1)")
print("to stop type 'END'")

a = input()

while(a != "END"):
    res = BS(int(a), L)
    if(res != "Not Found"):
        print(f"Found at index {res}!")
    else:
        print(res)
    a = input()
