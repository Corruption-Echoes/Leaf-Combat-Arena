def getBool():
    yes=['y','yes','true','t']
    intake= input('Y/N:').lower()
    if(intake in yes):
        return True
    return False