import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application 
 
t = Transaction(doc, 'wave curve array')
 
t.Start()
 
refarrarr = ReferenceArrayArray()
 
#use a nested loop to create rows of profile curves
for i in range(0,20):
    refptarr = ReferencePointArray()
    for j in range(0,20):
        x = i * 10
        y = j * 10
        z = (10*math.cos(i)) + (10*math.sin(j))
 
        myXYZ = XYZ(x,y,z)
        refPoint = doc.FamilyCreate.NewReferencePoint(myXYZ)
        refptarr.Append(refPoint)
 
    crv = doc.FamilyCreate.NewCurveByPoints(refptarr)
 
    #append curves to reference arrays
    refarr = ReferenceArray()
    refarr.Append(crv.GeometryCurve.Reference)
    refarrarr.Append(refarr)
 
#create loft
loft = doc.FamilyCreate.NewLoftForm(True, refarrarr)
 
t.Commit()
 
__window__.Close()