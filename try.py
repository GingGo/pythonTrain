class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __key(self):
        return (self.name, self.age, self.address)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented


robot = Robot("Terry", 25, "Taiwan")
robot1 = Robot("Terry", 25, "Taiwan")
print(robot == robot1)
