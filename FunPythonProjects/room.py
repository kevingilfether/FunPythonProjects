class Room(object):
    """This class describes a room in a text-based style game"""
    
    def __init__(self, size, description, doors):
        self.size =size
        self.description = description
        self.doors = doors
