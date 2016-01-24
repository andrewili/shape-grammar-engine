from package.scripts import grammar as g
import rhinoscriptsyntax as rs
from package.scripts import settings as s

def create_group(group_in):
    group = rs.AddGroup(group_in)
    print('Added %s' % group)
    return group

def draw_objects():
    text_1a, text_1b = '1a', '1b'
    point_1a, point_1b = (10, 10, 0), (10, 20, 0)
    text_dot_1a = rs.AddTextDot(text_1a, point_1a)
    text_dot_1b = rs.AddTextDot(text_1b, point_1b)
    text_dots = [text_dot_1a, text_dot_1b]
    return text_dots

def add_objects_to_group(objects, group):
    n_objects_added = rs.AddObjectsToGroup(objects, group)
    print('Added %i objects to %s' % (n_objects_added, group))

def hide_group(group):
    n_objects_hidden = rs.HideGroup(group)
    print('Hid %i objects in %s' % (n_objects_hidden, group))

def draw_more_objects():
    text_2a, text_2b = '2a', '2b'
    point_2a, point_2b = (20, 10, 0), (20, 20, 0)
    text_dot_2c = rs.AddTextDot(text_2a, point_2a)
    text_dot_2d = rs.AddTextDot(text_2b, point_2b)
    more_text_dots = [text_dot_2c, text_dot_2d]
    return more_text_dots

def show_group(group):
    n_objects_shown = rs.ShowGroup(group)
    print('Showed %i objects' % n_objects_shown)

def draw_still_more_objects():
    text_3a, text_3b = '3a', '3b'
    point_3a, point_3b = (30, 10, 0), (30, 20, 0)
    text_dot_2c = rs.AddTextDot(text_3a, point_3a)
    text_dot_2d = rs.AddTextDot(text_3b, point_3b)
    still_more_text_dots = [text_dot_2c, text_dot_2d]
    return still_more_text_dots

def take_some_action():
    add_delete_point()
    # rs.ObjectsByGroup(group, True)              ##  successful if select
    # rs.CurrentLayer(s.Settings.default_layer_name)    ##  unsuccessful

def add_delete_point():
    point = rs.AddPoint(0, 0, 0)
    value = rs.DeleteObject(point)

g.Grammar.clear_all()
group = create_group('group_x')
objects = draw_objects()
add_objects_to_group(objects, group)
hide_group(group)                               # 1a, 1b shown
                                                # Move cursor; 1a, 1b hidden
more_objects = draw_more_objects()              # 2c, 2d shown
add_objects_to_group(more_objects, group)       # 2c, 2d still shown
hide_group(group)                               # 2c, 2d still shown 
                                                  # Move cursor; 2c, 2d hidden
show_group(group)                               # 2c, 2d shown
                                                  # Move cursor; 1a, 1b shown;
take_some_action()                              # 1a, 1b, 2c, 2d shown

"""
Observations 

AddObjectsToGroup
    If group is invisible, newly added objects remain shown until some 
    additional action is taken
HideGroup
    Objects in group remain shown until some further action is taken
ShowGroup
    Objects in group remain hidden until some further action is taken
Further action 
    Drag the cursor. Change the view port. Add and delete a point
"""
