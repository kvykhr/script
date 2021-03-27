import c4d
from c4d import gui
from random import shuffle, randint 
 

 
def main():
     
    objs = doc.GetActiveObjects(1)
    doc.StartUndo()
    for obj in objs:
        tag = obj.GetTag(c4d.Tvibrate)
        if tag == None:
            tag = obj.MakeTag(c4d.Tvibrate)
            doc.AddUndo(c4d.UNDOTYPE_NEW,tag)
    doc.EndUndo()           
if __name__ == '__main__':
    main()