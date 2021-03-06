def upperlimit():
    while True:
        try:
            upper_limit = input("Please select the upper limit: ")
            upper_limit = int(upper_limit)
        except:
            print("This was not a number! Try again!")
        else:
            break
    return upper_limit