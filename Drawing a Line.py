import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application
 
t = Transaction(doc, 'Create Line')
 
t.Start()
 
#Create a sketch plane
origin = XYZ.Zero
normal = XYZ.BasisZ
 
plane = Plane.CreateByNormalAndOrigin(normal, origin)
skplane = SketchPlane.Create(doc,plane)
 
#Create line vertices
lnStart = XYZ(0,0,0)
lnEnd = XYZ(20,20,0)
 
#create NewLine()
line = Line.CreateBound(lnStart, lnEnd)
 
#create NewModelCurve()
crv = doc.FamilyCreate.NewModelCurve(line, skplane)
 
t.Commit()
 
__window__.Close()