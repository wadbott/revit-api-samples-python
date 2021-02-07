import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'create a grid of reference points')
 
t.Start()
 
for i in range(0,10):
    #use a nested for loop variable j to increment x by i and y by j.
    for j in range(0,10):
        x = i * 10
        y = j * 10
        z = 0 
 
        myXYZ = XYZ(x,y,z)
        refPoint = doc.FamilyCreate.NewReferencePoint(myXYZ)
 
t.Commit()
 
__window__.Close()