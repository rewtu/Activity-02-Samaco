level = 90
A = 205
D = 188
Power = 110
Targets = 1
Weather = 1
Badge = 1
Critical = 1

STAB = 1.5
Type = 0.5
Burn = 1
other = 1

Modifier = Targets * Weather * Badge * Critical * STAB * Type * Burn * other
Modifier
Damage = ((level * 2 / 5 + 2  * Power * A / D)/ 50 + 2 ) * Modifier

Damage