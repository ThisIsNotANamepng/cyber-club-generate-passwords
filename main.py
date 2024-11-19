letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
word_list=["Flesh", "Curtains"]

for u in letters:
    for n in numbers:
        for l in word_list:
            password=u+n+l

            print(password)
