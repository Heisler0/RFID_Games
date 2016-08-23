from random import Random


class Character:

    names_prefix = ['Ku', 'Or', 'Th', 'Ma', 'Li', 'Cr', 'Be']
    names_postfix = ['uh', 'an', 'lo', 'yn', 'ew', 'sa']
    names_title = ['Gladiator', 'Knight', 'Rogue', 'Marksman', 'Magician', 'Wizard']
          
    def __init__(self, seed):
        self.random = Random(seed)
        self.name = self.generateName()
        self.abilities = self.generateAbilities()    
    
    def generateName(self):
        prefix = self.random.randrange(len(self.names_prefix))
        postfix = self.random.randrange(len(self.names_postfix))
        title = self.random.randrange(len(self.names_title))
        return self.names_prefix[prefix] + self.names_postfix[postfix] + ' The ' + self.names_title[title]
  
    def generateAbilities(self):
        abilities = []
        abilities.append(self.random.randrange(5) + 1)
        abilities.append(self.random.randrange(5) + 1)
        abilities.append(self.random.randrange(5) + 1)
        return abilities
