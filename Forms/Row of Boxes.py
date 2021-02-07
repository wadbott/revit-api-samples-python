import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application
 
t = Transaction(doc, 'Create row of extrusion.')
 
t.Start()
 
#Create a sketch plane
origin = XYZ.Zero
normal = XYZ.BasisZ
 
plane = Plane.CreateByNormalAndOrigin(normal, origin)
skplane = SketchPlane.Create(doc, plane)
 
# the first loop changes the position of corner points
for i in range(0,10):
    #Create array of vertex points and append vertices
    pts = []
    pts.append(XYZ(0+(i*15),0+(i*15),0))
    pts.append(XYZ(10+(i*15),0+(i*15),0))
    pts.append(XYZ(10+(i*15),10+(i*15),0))
    pts.append(XYZ(0+(i*15),10+(i*15),0))
    pts.append(XYZ(0+(i*15),0+(i*15),0))
 
    refarr = ReferenceArray()
 
    # this nested loop creates curves to extrude
    for j in range(0,len(pts)-1):
        ptA = pts[j]
        ptB = pts[j+1]
 
        line = Line.CreateBound(ptA,ptB)
        crv = doc.FamilyCreate.NewModelCurve(line,skplane)
        refarr.Append(crv.GeometryCurve.Reference)
 
    #The z direction is controlled by the value of i
    dir = XYZ(0,0,10+(i*10))
 
    #extrude the form
    extrude = doc.FamilyCreate.NewExtrusionForm(True,refarr,dir)
 
t.Commit()
 
__window__.Close()