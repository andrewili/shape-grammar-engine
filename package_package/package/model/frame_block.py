from package.model import frame as f
from package.model import layer as l
import rhinoscriptsyntax as rs

class FrameBlock(object):
    base_point = [0, 0, 0]
    block_name = 'frame block'
    color_name = 'dark gray'
    layer_name = 'frames'

    def __init__(self):
        pass

    @classmethod
    def new(cls):
        """Creates a frame layer, draws a shape frame there, and converts the
        shape frame to a block. Returns:
            str             the name of the block, if successful
            None            otherwise
        """
        if cls._frame_block_exists():
            return_value = None
        else:
            l.Layer.new(cls.layer_name, cls.color_name)
            rs.CurrentLayer(cls.layer_name)
            frame_guids = f.Frame.new(cls.base_point)
            # frame_guids = f.Frame.new()
            actual_block_name = rs.AddBlock(
                frame_guids, cls.base_point, cls.block_name, True)
            rs.CurrentLayer('Default')
            layer_names = rs.LayerNames()
            if (
                cls.layer_name in layer_names and
                actual_block_name == cls.block_name
            ):
                return_value = actual_block_name
            else:
                return_value = None
        return return_value

    @classmethod
    def delete(cls):                            ##  not needed?
        """Deletes the frame block and its layer. Returns:
            boolean         True if successful; False otherwise
        """
        if not (
            cls._frame_block_exists() and
            l.Layer.layer_name_is_in_use(cls.layer_name)
        ):
            return_value = False
        else:
            block_was_deleted = rs.DeleteBlock(cls.block_name)
            guids = rs.ObjectsByLayer(cls.layer_name)
            rs.DeleteObjects(guids)
            actual_value = l.Layer.delete(cls.layer_name)
            expected_value = True
            if (
                block_was_deleted and
                actual_value == expected_value
            ):
                return_value = True
            else:
                return_value = False
        return return_value

    @classmethod
    def _frame_block_exists(cls):
        block_names = rs.BlockNames()
        return_value = cls.block_name in block_names
        return return_value


    @classmethod
    def insert(cls, position):
        """Receives:
            position        point from user input (i.e., type guaranteed) or
                            list from Grammar (type not guaranteed)
        Inserts a frame block. Returns:
            guid            the guid of the new block instance, if successful
            None            otherwise
        """
        method_name = 'insert'
        try:
            if not position[2] == 0:
                raise ValueError
        except TypeError:
            message = "%s.%s: The argument must be a point" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        except ValueError:
            message = "%s.%s: The point must lie on the xy plane" % (
                cls.__name__, method_name)
            print(message)
            return_value = None
        else:
            return_value = rs.InsertBlock(cls.block_name, position)
        finally:
            return return_value

