for i in range(100):
    if ((i+1) % 7 == 0) or ("7" in str(i+1)):
        print("Boom")
        continue
    print(i+1)
