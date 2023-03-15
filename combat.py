import time

def Fight(mon1, mon2):
    turncount=0
    sleepTimer=0.2
    while(True):
        turncount+=1
        mon1.charge()
        mon2.charge()
        if(mon1.cha>100 and mon1.cha>mon2.cha):
            dmg=mon2.hit(mon1.atk)
            mon1.cha-=100
            if(dmg>0):
                print(mon1.name,'swung at',mon2.name,'dealing',dmg,'Damage!')
                time.sleep(sleepTimer)
            else:
                print(mon1.name,'blow is repelled by',mon2.name,'Defence!')
                time.sleep(sleepTimer)
        elif(mon2.cha>100):
            dmg=mon1.hit(mon2.atk)
            mon2.cha-=100
            
            if(dmg>0):
                print(mon2.name,'swung at',mon1.name,'dealing',dmg,'Damage!')
                time.sleep(sleepTimer)
            else:
                print(mon2.name,'blow is repelled by',mon1.name,'Defence!')
                time.sleep(sleepTimer)           
        #else:
            
            #print('The combatants charged up power!')
        if(mon1.chp<1):
            print(mon1.name,'has been defeated!')
            return mon2
        elif(mon2.chp<1):
            print(mon2.name,'has been toppled! They won',mon2.victories,'times!')
            return mon1
        if(turncount>500):
            print('The spectators grow bored of the fight!',mon1.name,'is booed off stage!')
            return mon2
    
