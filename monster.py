class monster:
    hp=0
    chp=0
    atk=0
    defe=0
    spe=0
    cha=0
    victories=0
    name=''

    def __init__(self,iHP,iATK,iDEFE,iSPE,iNAME) -> None:
        self.hp=iHP
        self.chp=iHP
        self.atk=iATK
        self.defe=iDEFE
        self.spe=iSPE
        self.name=iNAME

    def hit(self, damage):
        totalDmg=damage-self.defe
        if(totalDmg>0):
            self.chp-=totalDmg
        return totalDmg
    
    def charge(self):
        self.cha+=self.spe
    
    def victory(self,statbuff):
        self.victories+=1
        if(statbuff=='Health'):
            self.hp+=self.hp*0.2
        elif(statbuff=='Defense'):
            self.defe+=self.defe*0.2
        elif(statbuff=='Attack'):
            self.spe+=self.spe*0.2
        self.chp=self.hp
        self.cha=0

    def printStats(self):
        print('HP: ',self.chp,'/',self.hp)
        print('Attack: ',self.atk)
        print('Defence: ',self.defe)
        print('Speed: ',self.spe)
        print('Charge: ',self.cha)