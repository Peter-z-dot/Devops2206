a = "Aviel Buskila"
b = 'Aviel Buskila'
c = "Aviel \"Buskila\""
d = "Devops experts"
e = b + " from " + d
print(e)
f = f"{b} {d}"
h = {"fname": "Aviel",
     "lname": "Buskila",
     "age": 33,
     "is_married": True,
     "hobbies": ["bycicle", "Guitar"]}
e = f"his name is {h['fname']} {h['lname']} and his hobbies are {h['hobbies']}"
i = ("Aviel", "Buskila", 33, True)
print(i[2])
print(e)
g = "%s %s" % (b, d)
print(g)
print(str(i[2]))
print(" ".join(h["hobbies"]))