from package.view import layer as l
import rhinoscriptsyntax as rs

class Block(object):                            ##  parent class of RuleFrameBlock
                                                ##  rename as FrameBlock later?
    layer_name = 'frames'
    color_name = 'dark gray'

    def __init__(self):
        pass

    @classmethod
    def new(cls, frame_guids, base_point, block_name, delete_input):
        """Receives:
            frame_guids     [guid, ...]
            base_point      [num, num, num]
            block_name      str
            delete_input    boolean
        Creates a new block. Returns:
            str             the block name, if successful
            None            otherwise
        """
        method_name = 'new'
        try:
            if not (
                type(frame_guids) == list and
                type(base_point) == list and
                type(block_name) == str and
                type(delete_input) == bool
            ):
                raise TypeError
        except TypeError:
            message = "%s.%s: %s" % (
                cls.__name__,
                method_name,
                "%s %s" % (
                    "The arguments must be",
                    "a list, a point, a string, and a boolean"))
            print(message)
            return_value = None
        else:
            return_value = rs.AddBlock(
                frame_guids, base_point, block_name, delete_input)
        finally:
            return return_value

    @classmethod
    def insert(cls, frame_block_name, position):
        """Receives:
            position        [num, num, 0]
            frame_block_name
                            str
        Inserts a block. Returns:
            str             name of the block, if successful
            None            otherwise

        """
        method_name = 'insert'
        try:
            if not (
                type(frame_block_name) == str and
                type(position) == list
            ):
                raise TypeError
            if not (
                rs.IsBlock(frame_block_name) and
                position[2] == 0
            ):
                raise ValueError
        except TypeError:
            message = "%s.%s: %s" % (
                cls.__name__,
                method_name,
                "The arguments must be a string and a list")
            print(message)
            return_value = None
        except ValueError:
            message = "%s.%s: %s" % (
                cls.__name__,
                method_name,
                "The arguments must be a block name and [num, num, 0]")
            print(message)
            return_value = None
        else:
            guid = rs.InsertBlock(frame_block_name, position)
            if guid:
                return_value = frame_block_name
            else:
                return_value = None
        finally:
            return return_value

    @classmethod
    def delete(cls):
        print("Calling the parent class method")