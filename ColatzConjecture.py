number = input("What number would you like to check?")
currently = round(int(number))
while currently > 1 :
    print(currently)
    if round(currently / 2) == currently / 2 :
        currently = currently / 2
    else:
        currently = currently * 3 + 1
print(1)
