from random import Random


class Character:

    names_prefix = ['Ku', 'Or', 'Th', 'Ma', 'Li', 'Cr', 'Be']
    names_postfix = ['uh', 'an', 'lo', 'yn', 'ew', 'sa']
    names_title = ['Gladiator', 'Knight', 'Rogue', 'Marksman', 'Magician', 'Wizard']
    ap_limit = 9
    ap_base = 2
    ability_count = 3
    ap_total = 10

    
    def __init__(self, seed):
        self.random = Random(seed)
        self.name = self.generateName()
        self.abilities = self.generateAbilities()    
    
    def generateName(self):
        prefix = self.random.randrange(len(self.names_prefix))
        postfix = self.random.randrange(len(self.names_postfix))
        title = self.random.randrange(len(self.names_title))
        return self.names_prefix[prefix] + self.names_postfix[postfix] + ' The ' + self.names_title[title]
  
    def generateAbilities(s):
        abilities = []
        total = 0
        ap_remaining = s.ap_total
        
        for i in range(s.ability_count):
            abilities.append(s.ap_base)
            
        while ap_remaining > 0:
            index = s.random.randrange(s.ability_count)
            if abilities[index] < s.ap_limit:
                abilities[index] += 1
                ap_remaining -= 1
          
        return abilities
