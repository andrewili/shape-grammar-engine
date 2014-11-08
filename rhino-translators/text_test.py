#	text_test.py

import rhinoscriptsyntax as rs

class TextTest(object):
	def __init__(self):
		pass

	def get_text(self):
        guids = rs.GetObjects(
            prompt_for_elements,
            rs.filter.curve + rs.filter.text)

	def write_text(self):
		string = 'kilroy'
		location = [0, 0, 0]
		rs.AddText(string, location)

test = TextTest()
test.write_text()
test.get_text()