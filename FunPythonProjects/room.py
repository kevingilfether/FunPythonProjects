class Room(object):
    """This class describes a room in a text-based style game"""
    
    def __init__(self, size, description, portal_n, portal_e, portal_s, portal_w):
        self.size = size
        self.description = description
        self.portal_n = portal_n
        self.portal_e = portal_e
        self.portal_s = portal_s
        self.portal_w = portal_w
