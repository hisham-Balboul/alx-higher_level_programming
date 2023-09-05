i = 0
for j in range(122, 96, -1):
    print("{}".format(chr(j - i)), end="")
    if (i == 0):
        i = 32
    else:
        i = 0
