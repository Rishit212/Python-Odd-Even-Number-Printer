a = int(input("Enter the number: "))
d = 1
if a%2 != 0:
    c = a
    print("ODD NUMBERS")
    while d <= c:
        print("", d)
        d = d + 2
    d = 2
    print("EVEN NUMBERS")

    while d <= c:
        print("", d)
        d = d + 2

else:
    c = a
    d = 2
    print("EVEN NUMBERS")
    while d <= c:
        print("", d)
        d = d + 2
    d = 1
    print("ODD NUMBERS")
    while d <= c:
        print("", d)
        d = d + 2
