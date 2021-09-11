people_cost = input('''Please input the persons name, then give the cost of their meal! 
You may do this for as many people as there are. Ex. Jack 25.6 Stacy 25 Jon 47.2''')
people = people_cost.split()
cost = []

for i in people:
    try:
        if isinstance(int(i), int) or isinstance(int(i), float):
            people.remove(i)
            cost.append(int(i))
    except (TypeError, ValueError) as error:
        continue

total = sum(cost)
average = int(total)/(len(people))
print(cost, people, total, average)

 # We figured my original solution was the cleanest. does not tell who is above the average