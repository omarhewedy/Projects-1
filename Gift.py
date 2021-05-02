import random

numPeople = int(input("How many people are playing? "))
givers = []
recivers = ['']*numPeople
print("Please enter their names: ")
for i in range(numPeople):
    givers.append(input(""))
all_set=False
while not all_set:
    all_set=True
    for j in range(numPeople):
        recivers[j] = random.sample(givers,1)[0]
    for i in range(numPeople):
        if givers[i] not in recivers or givers[i]==recivers[i]:
            all_set =False
            break

print()
print("Gift Assignments...")
for k in range (numPeople):
    print(givers[k], "will buy a gift for", recivers[k])
print()
