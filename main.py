import sqlite3
import random
import json
import names




class star():
    def __init__(self) -> None:
        #Func
        self.genName()
        file = 'stardatabase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        create table if not exists starsystem (
            id integer primary key autoincrement,
            planetName tinytext,
            starport int,
            navelbase boolean,
            gasgiant tinytext,
            planetoid int,
            scoutbase tinytext,
            size int,
             tinytext);
        """
        self.cursor.execute(query)

        pass
    
    def starportType(self):
        
        roll = sum(self.dice(2))
        if roll == 2 or roll == 3 or roll == 4:
            self.starport = 10
        elif roll == 5 or roll == 6:
            self.starport = 11
        elif roll == 7 or roll == 8:
            self.starport = 12
        elif roll == 9:
            self.starport == 13
        elif roll == 10 or roll == 11:
            self.starport == 14
        elif roll == 12:
            self.starport == 16
        return self.starport

    def isNavelBase(self):
        roll = sum(self.dice(2))
        if roll > 7:
            self.navelbase == True
        else:
            self.navelbase == False
        return self.navelbase
    def isGasGiant(self):
        roll = sum(self.dice(2))
        if roll > 9:
            self.gasgiant = False
        else:
            self.gasgiant = True
        return self.gasgiant
    

    def isPlanetoids(self):
        roll = sum(self.dice(2))
        if roll > 6:
            self.planetoids == False
        else:
            self.planetoids == True
        return self.planetoids
    def isScoutBase(self):
        roll = sum(self.dice(2))
        if roll > 6:
             self.scout == True
        else:
            self.scout == False
        return self.scout

    def genName(self):
        #print(names.get_full_name())
        self.Planetname = names.get_full_name()
        return self.Planetname
    
    def genPlanetSize(self): #this is funny
        self.planetsize = sum(self.dice(2)) - 2
        return self.planetsize
    
    def PlanetUPP(self):
        self.starportType()
        self.genPlanetSize()
        self.genAtm()
        self.genHyd()
        self.genPopulation()
        self.genGovt()
        self.dtTechlvl()

    def dice(self,num=1):  
        randList = []  
        for i in range(num):
            die = random.randint(1,6)
            randList.append(die)
        return randList
    
    def isTravel(self):
        pass
        
        #dieroll = random.randint(2,12)
    
    def genAtm(self):
        if self.planetsize != 0:
            self.atm = ((self.dice(2)) - 7) + self.planetsize
        
        return self.atm
    
    
    def genHyd(self):
        self.hyd = ((self.dice(2)) - 7) + self.planetsize
        if self.planetsize <= 1:
            self.hyd = 0
        if self.hyd < 0:
            self.hyd == 0
        if self.hyd > 10:
            self.hyd = 10
        
    def genPopulation(self):
        self.population = ((self.dice(2)) - 2)

        
    def genGovt(self):
        self.govt = ((self.dice(2)) - 7) + self.population

    def Lawlvl(self):
        self.law = ((self.dice(2)) - 7) + self.govt
    def dtTechlvl(self):
        self.techlvl = self.dice(1)
        if self.starport == 10:
            self.techlvl += 6
        if self.starport == 11:
            self.techlvl += 4
        if self.starport == 12:
            self.techlvl += 2
        if self.starport == 16:
            self.techlvl -= 4
        if self.planetsize == 0 or self.planetsize == 1:
            self.techlvl += 2
        if self.planetsize == 2 or self.planetsize == 3 or self.planetsize == 4:
            self.techlvl += 1
        if self.atm < 4:
            self.techlvl += 1
        if self.atm > 9 and self.atm < 15:
            self.techlvl += 1
        if self.hyd == 9:
            self.techlvl += 1
        if self.hyd == 10:
            self.techlvl += 2
        if self.population > 0 and self.population < 6:
            self.techlvl +=1
        if self.population == 9:
            self.techlvl += 2
        if self.population == 10:
            self.techlvl += 4
        if self.govt == 0:
            self.techlvl +=1
        if self.govt == 5:
            self.techlvl +=1
        if self.govt == 13:
            self.techlvl -=2
        
        







#class universe():

star()





