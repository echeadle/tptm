

lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name

gandolf = Wizard("Gandolf", 42)
print(gandolf.__dict__)

print(lookup)
print(lookup['loc'])

#lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])