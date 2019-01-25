class Environement:
    """
        This class is to describe all the things in our environement
    """
    world="Earth"
    def __init__(self,envName,envDesc,envDweller):
        print("Environement is initializing ...")
        self.environement=envName
        self.description=envDesc
        self.dweller=envDweller

    # instance method <self is required>
    def desc(self):
        print(self.description)

    # class method <cls is required>
    def changeWorld(cls,world):
        Environement.world=world

    # static method <nothing is required>
    def helloEnv():
        print("Hello! e'ry body")

    hello=staticmethod(helloEnv)
    cworld=classmethod(changeWorld)
    