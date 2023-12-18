class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()
print(f"Type: {type(an)}\nDir: {dir(an)}")


# A Nerdy Way to Find Capabilities
x = list()
print(f'{type(x)}\n{dir(x)}')

# Try dir() with a String
y = 'Hello there'
print(dir(y))
