import sqlite3
from configs import Config_Read

class CausalityDumper:
    def __init__(self):
        self.config = Config_Read()
        self.db_path = self.config.get('DEFAULT', 'database_path')
        self.db = sqlite3.connect(self.db_path)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
    

    def grabCausalities(self) -> dict:
        self.cursor.execute("SELECT id, causality_type, cau_val1, cau_val2, cau_val3 FROM skill_causalities")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def formatCausalityData(self) -> dict:
        causalityDict = {}
        causalityData = self.grabCausalities()
        for row in causalityData:
            causalityDict[row['id']] = {
                'causality_type': row['causality_type'],
                'cau_val1': row['cau_val1'],
                'cau_val2': row['cau_val2'],
                'cau_val3': row['cau_val3']
            }
        return causalityData
    
    def simplifyCausalityData(self) -> dict:
        causalityDict = {}
        causalityData = self.formatCausalityData()
        for row in causalityData:
            causalityDict[row['id']] = {
                'causality_type': row['causality_type']
            }
        return causalityDict
    
    def printData(self) -> None:
        print(self.formatCausalityData())

    
    def close(self) -> None:
        self.db.close()


    def createCausalityTypeDict(self) -> dict:
        return {
            1 : 'When HP is over',
            2 : 'When HP is under',
            3 : 'Ki is over',
            4 : 'Ki is under',
            5 : 'Past Turn',
            6 : 'Deck Has Link Skill',
            7 : 'Enemy Has Link Skill',
            8 : 'Is ATK & DEF over',
            9 : 'Is ATK & DEF under',
            10 : 'Is HP over and Ki above',
            11 : 'Is HP over and Ki below',
            12 : 'Is HP below and Ki above',
            13 : 'Is HP below and Ki below',
            14 : 'Is First Slot',
            15 : 'Over # Enemies',
            16 : 'Under # Enemies',
            17 : 'Target Over HP',
            18 : 'Target Under HP',
            19 : 'Card Slot',
            20 : 'When Ki is above',
            21 : 'When Ki is below',
            22 : 'Character on team',
            23 : 'If # of links are active',
            24 : 'Hit Received',
            25 : 'Target Killed',
        }

# CausalityDumper().printData()
