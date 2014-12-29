# from package.model import dictionary as d
# import rhinoscriptsyntax as rs

class Block(object):
    def __init__(self):
        pass

    # @classmethod
    # def new(cls, guids, base_point, name_in):
    #     """Receives a list of guids, a base point, and a name:
    #         [guid, ...]
    #         [num, num, num]
    #         str
    #     Converts the guids to a block. Returns the name of the new block if
    #     successful:
    #         str
    #     Otherwise returns:
    #         None
    #     """
    #     block_names = cls.get_names()
    #     if name_in in block_names:
    #         message = 'The block name already exists: "%s"' % name_in
    #         new_block_name = None
    #     else:
    #         do_delete = True
    #         new_block_name = rs.AddBlock(
    #             guids, base_point, name_in, do_delete)
    #         d.Dictionary.set_value('Blocks', name_in, '')
    #         message = 'Created block: %s' % new_block_name
    #         print(message)
    #     return new_block_name

    # @classmethod
    # def delete(cls, block_name):
    #     """Receives a block name:
    #         str
    #     Deletes the block. Returns the success value:
    #         boolean
    #     """
    #     block_was_deleted = rs.DeleteBlock(block_name)
    #     d.Dictionary.delete_entry('Blocks', block_name)
    #     return block_was_deleted

    # @classmethod
    # def get_names(cls):
    #     """Returns the names of all blocks:
    #         [str, ...]
    #     """
    #     names = rs.BlockNames()
    #     return names
