print("You can try 3 times")
trial = 0

while trial < 3:
    trial += 1
    x = int(input("Input x (0=exit): "))

    if x == 0:
        print("Bye!!!")
        break
    else:
        print("x is", x)
else:
    print("bye~!!!")
