class PositionDistance(object):
    def __init__(self, args):
        if isinstance(args, int):
            self.top = args
            self.right = args
            self.bottom = args
            self.left = args
        elif len(args) == 1:
            self.top = args[0]
            self.right = args[0]
            self.bottom = args[0]
            self.left = args[0]
        elif len(args) == 2:
            self.top = args[0]
            self.right = args[1]
            self.bottom = args[0]
            self.left = args[1]
        elif len(args) == 4:
            self.top = args[0]
            self.right = args[1]
            self.bottom = args[2]
            self.left = args[3]
        else:
            raise Exception('The tuple is not of the correct length to represent a position distance')

    def hor(self):
        return self.left + self.right

    def ver(self):
        return self.top + self.bottom
