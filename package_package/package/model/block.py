import rhinoscriptsyntax as rs

class Block(object):
    def __init__(self):
        pass

    @classmethod
    def new(cls, guids, base_point, name):
        """Receives a list of guids, a base point, and a name:
            [guid, ...]
            [num, num, num]
            str
        Converts the guids to a block. Returns the name of the new block if
        successful:
            str
        Otherwise returns:
            None
        """
        do_delete = True
        new_block_name = rs.AddBlock(guids, base_point, name, do_delete)
        print('Created new block: %s' % new_block_name)
        return new_block_name