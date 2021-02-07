import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application
 
t = Transaction(doc, 'This is my new transaction')
 
t.Start()
 
refptarr = ReferencePointArray()
 
#use for loop to create a series of points
for i in range(0,20):
    x = math.sin(i)*5
    y = math.cos(i)*5
    z = i
 
    myXYZ = XYZ(x,y,z)
    refPt = doc.FamilyCreate.NewReferencePoint(myXYZ)
    refptarr.Append(refPt)
 
crv = doc.FamilyCreate.NewCurveByPoints(refptarr)
 
t.Commit()
 
__window__.Close()