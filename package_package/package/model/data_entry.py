import rhinoscriptsyntax as rs

class DataEntry(object):
    def __init__(self):
        pass

    @classmethod
    def add_grammar_layer_name(cls, name):
        """Receives a layer name:
            str
        Adds the name to the dictionary's layer names entry
        """
        rs.SetDocumentData('Layer names', name, '')

    @classmethod
    def get_grammar_layer_names(cls):
        """Returns the names of the layers created by the grammar:
            [str, ...]
        """
        names = rs.GetDocumentData('Layer names')
        return names

    @classmethod
    def clear_all(cls):
        """Resets all data entries to ''. Returns the number of entries
        cleared:
            int
        """
        print('Pretending to clear all data entries')
        n_entries_cleared = 0
        keys = rs.GetDocumentUserText()
        for key in keys:
            rs.SetDocumentUserText(key, '')
            n_entries_cleared += 1
        message = 'Cleared %i data entries' % n_entries_cleared
        print(message)
        return n_entries_cleared