import random
level = 90
A = 205
D = 188
Power = 110
Targets = 1
Weather = 1
Badge = 1
Critical = 1
randamage = 0
STAB = 1.5
Type = 0.5
Burn = 1
other = 1

rand = random.randint(1,2)
if rand == 1:
        randamage = 0.85
elif rand == 2:
        randamage = 1.0
Modifier = Targets * Weather * Badge * rand * Critical * STAB * Type * Burn * other
Damage = (((level * 2 / 5 + 2 ) * Power * A / D)/ 50 + 2 ) * Modifier
#dam =int(Damage)
print("Charizard's attack damage:")
print(Damage)