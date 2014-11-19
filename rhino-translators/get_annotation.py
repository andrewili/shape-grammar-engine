#   get_annotation.py

import rhinoscriptsyntax as rs

def get_annotation():
    prompt_for_annotation = 'Select text'
    guids = rs.GetObjects(prompt_for_annotation)
    print('number of objects: %i' % len(guids))
    for guid in guids:
        if rs.IsText(guid):
            print('text: %s' % rs.TextObjectText(guid))
        elif rs.IsTextDot(guid):
            print('text dot: %s' % rs.TextDotText(guid))
        else:
            print('guid is not text')
            
if __name__ == '__main__':
    get_annotation()