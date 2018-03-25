class Vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __repr__(self):
        print('__repr__ called')
        return "Vec2({}, {})".format(self.x, self.y)
    def __bytes__(self):
        tmp = "{:02x}{:02x}".format(self.x, self.y)
        return bytes.fromhex(tmp)
    def __eq__(self, other):
        print('__eq__ called')
        return (self.x, self.y) == (other.x, other.y)
    def __hash__(self):
        print('__hash__ called')
        return hash( (self.x, self.y) )
    def __format__(self, format_spec):
        if(format_spec == 'b'):
            return "Vec2(x={:b}, y={:b})".format(self.x, self.y)
        elif(format_spec == 'x'):
            return "Vec2(x={:x}, y={:x})".format(self.x, self.y)
        else:
            return "Vec2(x={:d}, y={:d})".format(self.x, self.y)

a = Vec2(128, 255)

repr(a)
