import sqlite3
import random
import json
import names
import PySimpleGUI as sg
import dataBaseCreator as db



class star():
    def __init__(self) -> None:
        #Func
        #self.genName()
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
            atm int,
            hyd int,
            population int,
            govt int,
            lawlvl int,
            techlvl int);
        """
        self.cursor.execute(query)
        self.PlanetUPP()
        query = "select * from starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        #print("Num, Name, Starport LVL, Is Navel Base?, Is gas giant?, is stciut base?, Size, Atm,Hyd,Population,govt,lawlvl,techlvl\n")
       # for i in result:
        #    print(i)
        self.look_pretty()

    def look_pretty(self):
        query = "select * from starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:
            '''
            planetName tinytext,
            starport int,
            navelbase boolean,
            gasgiant tinytext,
            planetoid int,
            scoutbase tinytext,
            size int,
            atm int,
            hyd int,
            population int,
            govt int,
            lawlvl int,
            techlvl int
            '''
            #print(f"Planet Name: {i[1]}, Starport:  {i[2]}, Navel Base:  {i[3]}, Gasgiant:  {i[4]}, Planetoid:  {i[5]}, Scout Base:  {i[6]}, Planet Size:  {i[7]}\nAtmosphere:  {i[8]}, Hydogenics:  {i[8]}, Population:  {i[10]}, Government level:  {i[11]}, Law Level:  {i[12]}, Tech Level:  {i[13]}\n")
            for i in result:
                    #print(f"\n          Planet Name: {i[1]}\n--------------------------------------\n  Starport:  {i[2]}         Navel Base: {i[3]}\n  Gasgiant: {i[4]}           Planetoid: {i[5]}\n  Scout Base: {i[6]}        Planet Size: {i[7]}\n  Atmosphere: {i[8]}         Hydrogeneics: {i[9]}\n  Population: {i[10]}         Government : {i[11]}\n  Law level: {i[12]}           Tech level: {i[13]}\n")
                txt = f"Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
                new_str = txt.center(500)
                print(new_str)
    
    
    def starportType(self):
        roll = sum(self.dice(2))
        if roll == 2 or roll == 3 or roll == 4:
            self.starport = 10
        elif roll == 5 or roll == 6:
            self.starport = 11
        elif roll == 7 or roll == 8:
            self.starport = 12
        elif roll == 9:
            self.starport = 13
        elif roll == 10 or roll == 11:
            self.starport = 14
        elif roll == 12:
            self.starport = 16
        return self.starport

    def isNavelBase(self):
        roll = sum(self.dice(2))
        if roll > 7:
            self.navelbase = True
        else:
            self.navelbase = False
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
            self.planetoids = False 
        else:
            self.planetoids = True
        return self.planetoids
        
    def isScoutBase(self):
        roll = sum(self.dice(2))
        if roll > 6:
             self.scout = True
        else:
            self.scout = False
        return self.scout

    def genName(self):
        #print(names.get_full_name())
        self.Planetname = names.get_full_name()
        return self.Planetname
    
    def genPlanetSize(self): #this is funny
        self.planetsize = sum(self.dice(2)) - 2
        return self.planetsize
    
    def PlanetUPP(self):
        
        '''
        self.genAtm()
        self.genHyd()
        self.genPopulation()
        self.genGovt()
        self.Lawlvl()
        self.dtTechlvl()
        '''
        query = f"insert into starsystem (planetname,starport,navelbase,gasgiant,planetoid,scoutbase,size,atm,hyd,population,govt,lawlvl,techlvl) values ('{self.genName()}','{self.starportType()}','{self.isNavelBase()}','{self.isGasGiant()}','{self.isPlanetoids()}','{self.isScoutBase()}','{self.genPlanetSize()}','{self.genAtm()}','{self.genHyd()}','{self.genPopulation()}','{self.genGovt()}','{self.Lawlvl()}','{self.dtTechlvl()}');"
        self.cursor.execute(query)
        self.connection.commit()
        #I'm a goofy goober
        #I agree with the comment above
        #I challenge you to a debate

    def dice(self,num=1):  
        randList = []  
        for i in range(num):
            die = random.randint(1,6)
            randList.append(die)
        return randList
    
    def isTravel(self):
        pass
        
        
    
    def genAtm(self):
        if self.planetsize != 0:
            self.atm = (sum((self.dice(2))) - 7) + self.planetsize
        
        return self.atm
    
    
    def genHyd(self):
        self.hyd = (sum((self.dice(2))) - 7) + self.planetsize
        if self.planetsize <= 1:
            self.hyd = 0
        if self.hyd < 0:
            self.hyd = 0
        if self.hyd > 10:
            self.hyd = 10
        return self.hyd
        
    def genPopulation(self):
        self.population = (sum(self.dice(2)) - 2)
        return self.population

        
    def genGovt(self):
        self.govt = (sum(self.dice(2)) - 7) + self.population
        return self.govt

    def Lawlvl(self):
        self.law = (sum(self.dice(2)) - 7) + self.govt
        return self.law
        
    def dtTechlvl(self):
        self.techlvl = sum(self.dice(1))
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
        return self.techlvl
        
        







#class universe():


class createUniverse():
    def __init__(self) -> None:
        #star()
        self.help = False
        self.current_val = 0
        self.firstPass = True
        file = 'stardatabase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        self.updated = False
        
        
        #self.window['ButtonLeft'].update(visible=False)    
        #self.window['ButtonRight'].update(visible=False)         
        self.mainRun()
    def runMainWindow(self):
        sg.theme('DarkAmber')
        temp = ['<','>','=']
        temp2 = ['planetName','starport','navelbase','gasgiant','planetoid','scoutbase','size','atm','hyd','population','govt','lawlvl','techlvl']
        self.temp3 = ['planetName','size','atm','hyd','population','govt','lawlvl','techlvl','getall']
        layout = [  [sg.Text('Star system generator and database search tool'),sg.Button("Gen New Starsystem",key="NEWStar")],
            [sg.Text('Enter what you are seaching'), sg.InputText()],
            [sg.Text("Symbol"),sg.Combo(values=temp),sg.Button('Search'), sg.Button('Help'), sg.Combo(values=self.temp3),sg.Push()],
            [sg.Button("Left"),sg.Push(),sg.Button("Right")],
            [sg.Text("",key="updateText",justification="left")],
            [sg.Text("",key="ANSON")],
            [sg.Button("EDIT",key='edit')]]
        self.window = sg.Window('Window Title', layout,element_justification="c",finalize=True)
        return self.window
    def mainRun(self):    
        window1 = self.runMainWindow()
        window2 = None
        event2 = ''
        values2 = ''
        while True:             
            #event, values = self.window.read()
            window, event, values = sg.read_all_windows()
            #print(window,event,values)

            
            if event in ('Search'):
                
                print(values[0],values[1],values[2])
                x = self.searchQuery(values[0],values[1],values[2])
                #print(type(x))
                #output = ""
                #for i in x:
                #    output += str(i) + "\n"
               
                #self.window['ButtonLeft'].update(visible=True)    
                #self.window['ButtonRight'].update(visible=True)
                self.current_val = 0
                try:
                    self.window['updateText'].update(f"Index: {x[self.current_val][0]}\nName: {x[self.current_val][1]}\n--------------------------------------------\nStarport: {x[self.current_val][2]}            NavelBase: {x[self.current_val][3]}\nGasGiant: {x[self.current_val][4]}     Planetoid: {x[self.current_val][5]}\nScoutBase: {x[self.current_val][6]}   Size: {x[self.current_val][7]}\nAtmosphere: {x[self.current_val][8]}       Hydrogenics: {x[self.current_val][9]}\nPopulation: {x[self.current_val][10]}         Govt: {x[self.current_val][11]}\nLawLVL: {x[self.current_val][12]}             TechLVL: {x[self.current_val][13]}")
                except Exception as e:
                    print(e)
            
            elif event in ('Help'):
                if self.help:
                    self.window['ANSON'].update('')
                    self.help = False
                else:
                    self.help = True
                    #print("Help ran")
                    self.window['ANSON'].update("1) select what planet you are looking for by name or by number of the starsystem option\n2) select the symbol to greater than, lesser than or equal to the number you select \n3) select the starsystem option you want")
            elif event in ('NEWStar'):
                #print("NEW start ran")
                star()

            elif event in ("Left"):
                #print("L")
                self.current_val -= 1
                if self.current_val < 0:
                    try:
                        self.current_val = len(x)-1
                    except UnboundLocalError:
                        self.current_val = 0
                try:
                    #planetname,starport,navelbase,gasgiant,planetoid,scoutbase,size,atm,                                                                                                                                                                                                                                                                                               hyd,population,govt,lawlvl,techlvl
                    #self.window['updateText'].update(f"Index: {x[self.current_val][0]}\nName: {x[self.current_val][1]}\n--------------------------------------------\nStarport: {x[self.current_val][2]}           NavelBase: {x[self.current_val][3]}\nGasGiant: {x[self.current_val][4]}      Planetoid: {x[self.current_val][5]}\nScoutBase: {x[self.current_val][6]}        Size: {x[self.current_val][7]}\nAtm: {x[self.current_val][8]}         Hyd: {x[self.current_val][9]}\nPopulation: {x[self.current_val][10]}            Govt: {x[self.current_val][11]}\nLawLVL: {x[self.current_val][12]}\nTechLVL: {x[self.current_val][13]}")
                    self.window['updateText'].update(f"Index: {x[self.current_val][0]}\nName: {x[self.current_val][1]}\n--------------------------------------------\nStarport: {x[self.current_val][2]}            NavelBase: {x[self.current_val][3]}\nGasGiant: {x[self.current_val][4]}     Planetoid: {x[self.current_val][5]}\nScoutBase: {x[self.current_val][6]}   Size: {x[self.current_val][7]}\nAtmosphere: {x[self.current_val][8]}       Hydrogenics: {x[self.current_val][9]}\nPopulation: {x[self.current_val][10]}         Govt: {x[self.current_val][11]}\nLawLVL: {x[self.current_val][12]}             TechLVL: {x[self.current_val][13]}")
                except Exception as e:
                    self.current_val += 1
                    print(e)
            elif event in ("Right"):
                #print("R")
                self.current_val += 1
                try:
                    self.window['updateText'].update(f"Index: {x[self.current_val][0]}\nName: {x[self.current_val][1]}\n--------------------------------------------\nStarport: {x[self.current_val][2]}            NavelBase: {x[self.current_val][3]}\nGasGiant: {x[self.current_val][4]}     Planetoid: {x[self.current_val][5]}\nScoutBase: {x[self.current_val][6]}   Size: {x[self.current_val][7]}\nAtmosphere: {x[self.current_val][8]}       Hydrogenics: {x[self.current_val][9]}\nPopulation: {x[self.current_val][10]}         Govt: {x[self.current_val][11]}\nLawLVL: {x[self.current_val][12]}             TechLVL: {x[self.current_val][13]}")
                except Exception as e:
                    self.current_val = 0
                    try:
                        self.window['updateText'].update(f"Index: {x[self.current_val][0]}\nName: {x[self.current_val][1]}\n--------------------------------------------\nStarport: {x[self.current_val][2]}            NavelBase: {x[self.current_val][3]}\nGasGiant: {x[self.current_val][4]}     Planetoid: {x[self.current_val][5]}\nScoutBase: {x[self.current_val][6]}   Size: {x[self.current_val][7]}\nAtmosphere: {x[self.current_val][8]}       Hydrogenics: {x[self.current_val][9]}\nPopulation: {x[self.current_val][10]}         Govt: {x[self.current_val][11]}\nLawLVL: {x[self.current_val][12]}             TechLVL: {x[self.current_val][13]}")
                    except Exception as a:
                        print(f"{a},{e}")
            elif event in ("edit"):
                self.editingWindow()
            elif event in 'Find':
                x = self.searchIndex(values[0])
                
                self.window2['found'].update(f"Index: {x[self.current_val][0]}\nName: {x[self.current_val][1]}\n--------------------------------------------\nStarport: {x[self.current_val][2]}            NavelBase: {x[self.current_val][3]}\nGasGiant: {x[self.current_val][4]}     Planetoid: {x[self.current_val][5]}\nScoutBase: {x[self.current_val][6]}   Size: {x[self.current_val][7]}\nAtmosphere: {x[self.current_val][8]}       Hydrogenics: {x[self.current_val][9]}\nPopulation: {x[self.current_val][10]}         Govt: {x[self.current_val][11]}\nLawLVL: {x[self.current_val][12]}             TechLVL: {x[self.current_val][13]}")
                if self.updated:
                    pass
                else:
                    self.window2.extend_layout(self.window2["column"], [[sg.T("What are you going to edit?"),sg.Combo(values=[i for i in self.temp3 if i != "getall"])],[sg.T("What are you changing it to?"),sg.InputText(size=4)],[sg.Button(button_text="Save!",key="save")]])
                self.updated = True
            elif event in "save":
                if values[0] == "": values[0] = 1
                values[0] = int(values[0])
                #1 is whats being changed (name etc)
                #2 if value changing to
                
                db.main().update(filename="stardatabase.db",Basename="starsystem",updatename=values[1], updateTo=values[2], params=f"id == {values[0]}")
                x = self.searchIndex(values[0])
                self.window2['found'].update(f"Index: {x[self.current_val][0]}\nName: {x[self.current_val][1]}\n--------------------------------------------\nStarport: {x[self.current_val][2]}            NavelBase: {x[self.current_val][3]}\nGasGiant: {x[self.current_val][4]}     Planetoid: {x[self.current_val][5]}\nScoutBase: {x[self.current_val][6]}   Size: {x[self.current_val][7]}\nAtmosphere: {x[self.current_val][8]}       Hydrogenics: {x[self.current_val][9]}\nPopulation: {x[self.current_val][10]}         Govt: {x[self.current_val][11]}\nLawLVL: {x[self.current_val][12]}             TechLVL: {x[self.current_val][13]}")

        self.searchQuery()
    def new_layout(self):
        return [[sg.T("Question: "), sg.InputText(key="quest"), sg.T("Answer"), sg.InputText(key=("ans"))]]

    def searchIndex(self, index="0"):
        if index == "" or index==None: index = "1"
        print(index)
       # query = f"select * from starsystem where id=?"
        self.cursor.execute(f"select * from starsystem where id={index}")
        result = self.cursor.fetchall()
        print(result)
        return(result)
    def editingWindow(self, index=None):
        sg.theme('DarkAmber')
        temp = ['<','>','=']
        temp3 = ['planetName','size','atm','hyd','population','govt','lawlvl','techlvl','getall']
        layout = [  [sg.Text('Database Editor')],
            [sg.Text('Enter index'), sg.InputText(size=10), sg.Button(button_text="Find!",key="Find")],
            [sg.Text("",key="found",justification="left")],
            [sg.Column(layout=[[sg.Text(""),sg.T("")]],key="column")]]
        self.window2 = sg.Window('Editing window', layout,element_justification="c",finalize=True)
        return self.window2
        
    def searchQuery(self,search=None,symbol='=',selection='getall'):
        #print("The options to search for are: planetName (1), size (2), atm (3), hyd (4), population (5), govt (6), lawlvl (7), techlvl (8), getall (9), run Create Star (10)")
        #try:
           # self.selection = int(input("Enter what you want to seach for: "))
        # except:
        #self.symbol = str(input("Enter the symbol you want to search with, ex: >, <, = : "))
        self.symbol = symbol
        #'planetName','size','atm','hyd','population','govt','lawlvl','techlvl','getall'
        if selection == 'planetName':
            
            return(self.searchName(search))
        elif selection == 'size':
            
            return(self.searchSize(search))
        elif selection == 'atm':
            
            return(self.searchAtm(search))
        elif selection == 'hyd':
            
            return(self.searchHyd(search))
        elif selection == 'population':
            
            return(self.searchPop(search))
        elif selection == 'govt':
            
            return(self.searchGov(search))
        elif selection == 'lawlvl':
            
            return(self.searchLaw(search))
        elif selection == 'techlvl':
            
            return(self.searchTech(search))
        elif selection == 'getall':
            return(self.getall())
        else:
            self.mainRun()
    def searchTech(self,search=None):
        #self.techselect = int(input(f"Enter the tech level that you want to find return {self.symbol} results for: "))
        self.techselect = search
        query = f"select * from starsystem where techlvl {self.symbol}={self.techselect}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return(result)
        self.searchQuery()
    def searchName(self,search=None):
        
        query = f"select * from starsystem where planetName{self.symbol}={search}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return(result)
        
        self.searchQuery()
    def getall(self,search=None):
        query = f"select * from starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return(result)
        self.searchQuery()
    
    def searchSize(self,search=None):
        name = 0
        try:
            query = f"select * from starsystem where size{self.symbol}={search}"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
        except:
            result = None
        return(result)
        self.searchQuery()
    def searchAtm(self,search=None):
        '''
        name = 0
        try:
            name = int(input("Enter the planet atmosphere you want to search for: "))
        except:
            self.searchAtm()
            '''
        query = f"select * from starsystem where atm{self.symbol}={search}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return(result)
        self.searchQuery()
    def searchHyd(self,search=None):
        '''
        name = 0
        try:
            name = int(input("Enter the planet hydrogeneics you want to search for: "))
        except:
            self.searchHyd()
        '''
        query = f"select * from starsystem where hyd{self.symbol}={search}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return(result)
        self.searchQuery()
    def searchPop(self,search=None):
        '''
        name = 0
        try:
            name = int(input("Enter the planet population you want to search for: "))
        except:
            self.searchPop()
            '''
        query = f"select * from starsystem where population{self.symbol}={search}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return(result)
        self.searchQuery()
    def searchGov(self,search=None):
        
        '''name = 0
        try:
            name = int(input("Enter the planet govt you want to search for: "))
        except:
            self.searchGov()
            '''
        query = f"select * from starsystem where govt{self.symbol}={search}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return(result)
        self.searchQuery()
    def searchLaw(self,search=None):
        '''
        name = 0
        try:
            name = int(input("Enter the planet law level you want to search for: "))
        except:
            self.searchLaw()
            '''
        query = f"select * from starsystem where lawlvl{self.symbol}={search}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return(result)
        self.searchQuery()

if __name__ == "__main__":
    createUniverse()