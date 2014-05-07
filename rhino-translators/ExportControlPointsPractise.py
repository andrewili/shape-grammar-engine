import rhinoscriptsyntax as rs

def ExportControlPoints():
    "Export curve's control points to a text file"
    #pick a curve object
    curve = rs.GetObject("Select curve", rs.filter.curve)

    #get the curve's control points
    points = rs.CurvePoints(curve)
    if not points: return

    #prompt the user to specify a file name
    filter = "Text file (*.txt)|*.txt|All files (*.*)|*.*||"
    filename = rs.SaveFileName("Save Control Points As", filter)
    if not filename: return

    file = open( filename, "w" )
    for point in points:
        x_str = str(point.X)
        y_str = str(point.Y)
        z_str = str(point.Z)
        coord_string = x_str + ', ' + y_str + ', ' + z_str + '\n'
        file.write(coord_string)
    file.close()



##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    ExportControlPoints()