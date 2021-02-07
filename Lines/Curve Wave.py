import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application 
 
t = Transaction(doc, 'Create a sine wave curve.')
 
t.Start()
 
refptarr = ReferencePointArray()
 
#use for loop to create a series of points
for i in range(0,20):
    x = i*2
    y = i*2
    #z is controlled using sine
    z = math.sin(i)*2
 
    myXYZ = XYZ(x,y,z)
    refPt = doc.FamilyCreate.NewReferencePoint(myXYZ)
    refptarr.Append(refPt)
 
crv = doc.FamilyCreate.NewCurveByPoints(refptarr)
 
t.Commit()
 
__window__.Close()