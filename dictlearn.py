from random import randint

d = {x: randint(60,100) for x in 'xyzabc'}
print(d)

print(sorted(d))

print(d.items())