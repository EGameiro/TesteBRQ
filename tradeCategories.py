class tradeCategories:

    def __init__(self, value, ClienteSector, categorie=None):
        self.value = value
        self.ClienteSector = ClienteSector
        self.categorie = categorie

        if (self.ClienteSector == 'Private' and self.value > 1000000):
            self.categorie = 'HIGHRISK'
            return
        elif (self.ClienteSector == 'Public' and self.value > 1000000):
            self.categorie = 'MEDIUNRISK'
            return 
        elif (self.ClienteSector == 'Public' and self.value < 1000000):
            self.categorie = 'LOWRISK'
            return 
        
    
        
        
        


    