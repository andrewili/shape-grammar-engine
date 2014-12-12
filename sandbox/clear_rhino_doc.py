#   clear_rhino_doc.py

import rhinoscriptsyntax as rs

def clear_blocks():
    rs.DeleteBlock('shape frame')

def clear_layers():
    rs.CurrentLayer('Default')
    rs.PurgeLayer('left')
    rs.PurgeLayer('right')
    rs.PurgeLayer('infrastructure')

clear_blocks()
clear_layers()