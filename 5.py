isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
is_age_above_21 = (a == 24 or strOne == "One")
is_not_aviel = not (strThree != "Aviel")
my_list = []
if isTrue and is_age_above_21 and is_not_aviel:
    print("True and two")
elif is_age_above_21 and b == 2.5:
    print("blabla2")
else:
    print("blabla")

if my_list:
    print("I have items")
else:
    print("I don't have items")
