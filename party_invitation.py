names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names.extend(names1)

for i in range(2):
    extra_name = input("Enter friend's name: ")
    names.append(extra_name)


for name in names:
    print(f"{name.title()}! You are invited to the party on saturday.")