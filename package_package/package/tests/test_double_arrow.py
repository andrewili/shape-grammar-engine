from package.scripts import double_arrow as da
from package.scripts import grammar as g
import rhinoscriptsyntax as rs
from package.scripts import settings as s

def test_new_instance():
    def try_yes_definition():
        try_name = 'yes_definition'
        g.Grammar.clear_all()
        double_arrow_name = s.Settings.double_arrow_name
        color_name = s.Settings.double_arrow_color_name
        rs.AddLayer(double_arrow_name, color_name)
        rs.CurrentLayer(double_arrow_name)
        position = (0, 0, 0)
        guids = da.DoubleArrow._get_guids(position)
        delete_input = True
        rs.AddBlock(guids, position, double_arrow_name, delete_input)
        da.DoubleArrow.new_instance(double_arrow_name, position)

    def try_no_definition():
        try_name = 'no_definition'
        g.Grammar.clear_all()
        double_arrow_name = s.Settings.double_arrow_name
        position = (0, 0, 0)
        da.DoubleArrow.new_instance(double_arrow_name, position)

    method_name = 'new_instance'
    try_yes_definition()
    try_no_definition()

def test__get_guids():
    def try_():
        try_name = 'try_'
        message = "Select the position of the double arrow"
        position = rs.GetPoint(message)
        actual_value = da.DoubleArrow._get_guids(position)

    method_name = '_get_guids'
    try_()

# test_new_instance()                         ##  manual / done
# test__get_guids()                           ##  manual / done
