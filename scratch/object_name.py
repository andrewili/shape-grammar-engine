from package.scripts import grammar as g
import rhinoscriptsyntax as rs

def name_and_retrieve_objects():
    g.Grammar.clear_all()
    draw_hash()
    get_name_for_retrieval()

def draw_hash():
    horizontals = [
        ((10, 20, 0), (40, 20, 0)),
        ((10, 30, 0), (40, 30, 0))]
    verticals = [
        ((20, 10, 0), (20, 40, 0)),
        ((30, 10, 0), (30, 40, 0))]
    for horizontal in horizontals:
        guid = rs.AddLine(horizontal[0], horizontal[1])
        rs.ObjectName(guid, 'h')
    for vertical in verticals:
        guid = rs.AddLine(vertical[0], vertical[1])
        rs.ObjectName(guid, 'v')

def get_name_for_retrieval():
    name = rs.GetString("Enter 'h' or 'v'")
    select = True
    guids = rs.ObjectsByName(name, select)
    rs.SelectObjects(guids)

name_and_retrieve_objects()
