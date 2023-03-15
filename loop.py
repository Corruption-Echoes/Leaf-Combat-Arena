import IV6
import monsterGenerator
import combat
import random

run=True
winner=monsterGenerator.generate(random.randint(1,3))

while(run):
    challenger=monsterGenerator.generate(random.choice([1,2,3]))
    prize=random.choice(['Health','Attack','Defense'])
    print('The 2 monsters square off over a',prize,'crystal')
    winner=combat.Fight(challenger,winner)
    winner.victory(prize)
    print('The victor is', winner.name,'Their',prize,'grows!')
    print('Would you like to watch another fight?', winner.name,'Is raring to go!')
    run=IV6.getBool()
    