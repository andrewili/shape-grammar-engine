from package.view import grammar as g
from package.view import frame_block as fb
import rhinoscriptsyntax as rs

def try_none_selected():
	# g.Grammar.clear_all()
	fb.FrameBlock.new()

	selected_objects = rs.SelectedObjects()
	message = "len(selected_objects)"
	length = len(selected_objects)
	print("%s: %i" % (message, length))
 
try_none_selected()