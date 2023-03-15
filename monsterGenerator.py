import monster
import random
adjectives = ["Terrifying", "Gigantic", "Monstrous", "Fearsome", "Horrid", "Spine-chilling", "Unearthly", "Gruesome", "Horrifying", "Horrific", "Hideous", "Macabre", "Lurking", "Sinister", "Malevolent", "Malignant", "Fiendish", "Diabolical", "Demonic", "Devilish", "Beastly", "Vicious", "Savage", "Bloodthirsty", "Ferocious","Silly","Hat-Loving","Digging"," Pancake Devouring"]

# List of nouns
nouns = ["Monster", "Beast", "Demon", "Fiend", "Creature", "Abomination", "Giant", "Ogre", "Troll", "Goblin", "Gremlin", "Imp", "Specter", "Phantom", "Spirit", "Zombie", "Vampire", "Werewolf", "Mummy", "Siren", "Kraken", "Hydra", "Dragon", "Potatokin"]

def generate(tier):
    mon=''
    if(tier==1):
        mon=monster.monster(random.randint(25,50),random.randint(5,10),random.randint(3,9),random.randint(10,20),random.choice(nouns))
        return mon
    elif(tier==2):
        mon=monster.monster(random.randint(15,30),random.randint(3,7),random.randint(2,7),random.randint(20,50),'The '+random.choice(adjectives)+' '+random.choice(nouns))
        return mon
    else:
        mon=monster.monster(random.randint(10,25),random.randint(1,5),random.randint(1,5),random.randint(50,80),random.choice(nouns)+' The aspect of '+random.choice(adjectives))
        return mon
