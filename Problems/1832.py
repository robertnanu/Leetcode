sentence = "thequickbrownfoxjumpsoverthelazydog"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet1 = []

for i in sentence:
    if i not in alphabet1:
        alphabet1.append(i)

alphabet1 = sorted(alphabet1)

if alphabet == alphabet1:
    print(True)
else:
    print(False)