from random import Random


class Pymon:

    names = ['Venusaur', 'Charizard', 'Blastoise', 'Butterfree', 'Beedrill', 'Pidgeot', 'Raichu',
             'Nidoqueen', 'Nidoking', 'Alakazam', 'Machamp', 'Victreebel', 'Golem', 'Kingdra']
    ap_limit = 9
    ap_base = 2
    ability_count = 3
    ap_total = 10

    
    def __init__(self, seed):
        self.random = Random(seed)
        self.name = self.random.choice(self.names)
        self.abilities = self.generateAbilities()    
    
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
