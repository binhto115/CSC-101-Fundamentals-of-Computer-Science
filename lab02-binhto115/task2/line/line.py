class Line:
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def __str__(self):
        return "Point:Coordinates: (%f, %f, %f, %f)" % (self.x1, self.y1, self.x2, self.y2)













#class Monster:
#“““Represents a powerful monster that might attack our heroes.”””
# def _ _ init_ _(self, type : str, color : str, power : int)
	#self.type = type
	#	self.color = color
	#	self.power = power

#monster = Monster(“Dragon”, “Black”, 66535)
#	-> it calls to _ _ init_ _(itself, “Dragon,” “Black”, 65535)
#*(python is gonna make this object call the init function)
#			(it’s gonna input its “self” in the first parameter)
#			(self is the object that was just created)

