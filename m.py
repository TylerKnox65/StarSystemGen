
import sqlite3
def pretty():
        file = 'stardatabase.db'
        connection = sqlite3.connect(file)
        cursor = connection.cursor()
        query = f"select * from starsystem"
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)

pretty()
#print(f"\n          Planet Name: {1}\n--------------------------------------\n  Starport:  {2}         Navel Base: {3}\n  gasgiant {4}           Planetoid: 5\n  Scout Base: 6        Planet Size: 4\n  Atmosphere {4}         Hydrogeneics: 4\n  Population {4}         Government : 4\n  Law level{4}           Tech level: 4\n")
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