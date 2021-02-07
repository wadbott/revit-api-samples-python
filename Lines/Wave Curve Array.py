import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application 
 
t = Transaction(doc, 'wave curve array')
 
t.Start()
 
for i in range(0,20):
    #nesting Reference Points and Reference Point Array
    refptarr = ReferencePointArray()
    for j in range(0,20):
        x = i * 10
        y = j * 10
        z = (10*math.cos(i)) + (10*math.sin(j))
 
        myXYZ = XYZ(x,y,z)
        refPoint = doc.FamilyCreate.NewReferencePoint(myXYZ)
        refptarr.Append(refPoint)
 
    crv = doc.FamilyCreate.NewCurveByPoints(refptarr)
 
t.Commit()
 
__window__.Close()