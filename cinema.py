import c4d
from c4d import gui
import random
def main():
    myObject = doc.SearchObject('MoTextRPL')
    objs = doc.GetActiveObjects(1)
    if not objs:
        gui.MessageDialog('select objects')
        return
    topx = len(objs)
    
    doc.StartUndo()
    xx = random.randint(4,topx - 1)
    objs[xx][c4d.INSTANCEOBJECT_LINK] = myObject
    doc.AddUndo(c4d.UNDOTYPE_NEW,tag)
    doc.EndUndo()
    c4d.EventAdd()

if __name__ == '__main__':
    main()