times = 7
names = ["Ofek", "Idan", "Eden", "Aviran", "Avidan", "Daniel"]
for name in names:
    if name.find("dan") > -1 or name.find("Dan") > -1:
        print(name)
result = [name for name in names if (name.find("dan") > -1 or name.find("Dan") > -1)]
print(result)

age = int(input("Enter your age"))
while age < 50:
    print("You are still ok")
    age = int(input("Enter your age"))

