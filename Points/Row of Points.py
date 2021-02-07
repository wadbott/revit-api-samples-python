import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'create a row of reference points')
 
t.Start()
 
#use for loop variable i to increment x and y
for i in range(0,10):
    x = i * 10
    y = i * 10
    z = 0 
 
    myXYZ = XYZ(x,y,z)
    refPoint = doc.FamilyCreate.NewReferencePoint(myXYZ)
 
t.Commit()
 
__window__.Close()