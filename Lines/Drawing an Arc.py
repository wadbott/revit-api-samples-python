import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application
 
t = Transaction(doc, 'Create Line')
 
t.Start()
 
 
#Create a plane by normal and origin
origin = XYZ.Zero
normal = XYZ.BasisZ
 
plane = Plane.CreateByNormalAndOrigin(normal, origin)

#Create a sketch plane
skplane = SketchPlane.Create(doc,plane) 
 
#Define arc parameters
startAngle = 0
endAngle = 2* math.pi
radius = 100
 
#create NewArc()
arc = Arc.Create(plane, radius, startAngle, endAngle)
 
#create NewModelCurve()
arc_crv = doc.FamilyCreate.NewModelCurve(arc, skplane)
 
t.Commit()
 
__window__.Close()