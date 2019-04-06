from random import randint

data = [randint(400,750) for _ in range(50)]

print(data)

yiben = filter(lambda x: x >= 600, data)

yiben = [x for x in data if x >= 600]


d = {x: randint(60, 100) for x in range(1, 21)}


youxiu = {k:v for k, v in d.items() if v > 90 }

print(youxiu)

s = set(data)

print({x for x in s if x%3 == 0})
