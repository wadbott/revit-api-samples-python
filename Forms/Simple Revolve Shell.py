import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application
 
t = Transaction(doc, 'Create revolve.')
 
t.Start()
 
#Create a sketch plane
origin = XYZ.Zero
normal = XYZ.BasisZ
 
plane = Plane.CreateByNormalAndOrigin(normal, origin)
skplane = SketchPlane.Create(doc,plane)
 
#create axis curve
lnStart = XYZ(0,0,0)
lnEnd = XYZ(0,50,0)
 
line = Line.CreateBound(lnStart, lnEnd)
axis = doc.FamilyCreate.NewModelCurve(line, skplane)
axisRef = axis.GeometryCurve.Reference
 
#create revolve profile
profileRefArr = ReferenceArray()
refptarr = ReferencePointArray()
 
pts = []
pts.append(XYZ(-20,0,0))
pts.append(XYZ(-30,25,0))
pts.append(XYZ(-20,50,0))
pts.append(XYZ(-30,75,0))
pts.append(XYZ(-20,100,0))
 
for i in range(0,5):
    refpt = doc.FamilyCreate.NewReferencePoint(pts[i])
    refptarr.Append(refpt)
 
profile = doc.FamilyCreate.NewCurveByPoints(refptarr)
profileRefArr.Append(profile.GeometryCurve.Reference)
 
#Revolve parameters
startAngle = 0
endAngle = 2*math.pi
 
#Create revolve
revolve = doc.FamilyCreate.NewRevolveForms(True, profileRefArr, axisRef, startAngle, endAngle)
 
t.Commit()
 
__window__.Close()