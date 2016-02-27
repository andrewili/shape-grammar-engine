# from package.scripts import grammar as g

class CMain(object):
    def __init__(self):
        pass

    @classmethod                                ##  2016-02-22 08:29
    def find_and_display_next_shapes_all_rules(cls):
        """Required state:
            One current shape (or a subshape of one current shape) must be 
            selected. 
        Applies all rules to the selected shape (or subshape) and draws the 
        resulting next shapes, if any. Does not retain information about the 
        rules. Returns:
            None
        """
        c       = g.Grammar.get_current_shape()
        rs      = g.Grammar.get_rules()
        ds_rs   = next_shapes_all_rules = []

        ds_rs = m.Engine.find_next_shapes_multiple_rules(c, rs)
        v.VMain.display_shapes(ds_rs)


