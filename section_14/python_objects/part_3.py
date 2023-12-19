# class PartyAnimal:
#     x = 0
#     def __init__(self):
#         print('I am constructed')
#     def                               party(self):
#         self.x = self.x + 1
#         print('So far',  self.x)
#
#     def __del__(self):
#         print('I am destructed', self.x)
#
# an = PartyAnimal() # Uses constructor.
# an.party()
# an.party()
# an = 42 # Uses destructor.
# print('an contains', an)


# Many instances
class PartyAnimal:
    x = 0
    name = ""
    def __init__(object, name):
        object.name = name
        print(object.name, "constructed")

    def party(object):
        object.x = object.x + 1
        print(object.name, "party count", object.x)
    def __del__(object):
        print("Del object:", object.name, object.x)


s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()