#   text_test.py

import rhinoscriptsyntax as rs

class TextTest(object):
    def __init__(self):
        pass

    def get_text(self):
        prompt_for_elements = 'Select elements'
        guids = rs.GetObjects(prompt_for_elements)
        for guid in guids:
            text = rs.TextObjectText(guid, 'new')
            print(text)

    def write_text(self):
        point = rs.GetPoint('Select a point')
        prompt = 'Enter a string'
        string = rs.GetString(prompt, 'default string')
        rs.AddText(string, point)

test = TextTest()
test.write_text()
test.get_text()