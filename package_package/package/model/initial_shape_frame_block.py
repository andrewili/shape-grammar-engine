from package.model import block as b

class InitialShapeFrameBlock(b.Block):          ##  child class of Block
    def __init__(self):
        pass

    @classmethod
    def new(cls):                               ##  i.e., new block definition
        """Makes the block definition
        """
        pass

    @classmethod
    def insert(cls, position, user_assigned_name):
        """Receives:
            position        [num, num, num]
            user_assigned_name
                            str
        Creates a new layer. Inserts an initial shape frame block on that 
        layer. Adds the name to the rule name list. Returns:
            str             user_assigned rule name, if successful
            None            otherwise
        """
        pass