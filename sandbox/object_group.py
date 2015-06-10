from package.view import grammar as g
import rhinoscriptsyntax as rs

def group_and_retrieve_objects():
    g.Grammar.clear_all()
    draw_hash()
    get_group_for_selection()

def draw_hash():
    rs.AddGroup('h')
    rs.AddGroup('v')
    rs.AddGroup('l')
    horizontals = [
        ((10, 20, 0), (40, 20, 0)),
        ((10, 30, 0), (40, 30, 0))]
    verticals = [
        ((20, 10, 0), (20, 40, 0)),
        ((30, 10, 0), (30, 40, 0))]
    for horizontal in horizontals:
        guid = rs.AddLine(horizontal[0], horizontal[1])
        rs.AddObjectToGroup(guid, 'h')
        rs.AddObjectToGroup(guid, 'l')
    for vertical in verticals:
        guid = rs.AddLine(vertical[0], vertical[1])
        rs.AddObjectToGroup(guid, 'v')
        rs.AddObjectToGroup(guid, 'l')

def get_group_for_selection():
    group = rs.GetString("Enter 'h' or 'v' or 'l'")
    select = True
    guids = rs.ObjectsByGroup(group, select)
    rs.SelectObjects(guids)

group_and_retrieve_objects()
