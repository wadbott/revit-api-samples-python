import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application
 
t = Transaction(doc, 'Create simple cap.')
 
t.Start()
#Define cap form corners XYZ to define plane corners
p1 = XYZ(0,0,0)
p2 = XYZ(20,0,0)
p3 = XYZ(20,20,10)
p4 = XYZ(0,20,10)
 
#Define edge of the cap form
line1 = Line.CreateBound(p1, p2)
line2 = Line.CreateBound(p2, p3)
line3 = Line.CreateBound(p3, p4)
line4 = Line.CreateBound(p4, p1)
 
 
#Create a plane by three points
plane = Plane.CreateByThreePoints(p1, p2, p3)

#Create a sketch plane
skplane = SketchPlane.Create(doc,plane) 
 
#create model curves
crv1 = doc.FamilyCreate.NewModelCurve(line1, skplane)
crv2 = doc.FamilyCreate.NewModelCurve(line2, skplane)
crv3 = doc.FamilyCreate.NewModelCurve(line3, skplane)
crv4 = doc.FamilyCreate.NewModelCurve(line4, skplane)
 
#create reference array for model curves
refarr = ReferenceArray()
refarr.Append(crv1.GeometryCurve.Reference)
refarr.Append(crv2.GeometryCurve.Reference)
refarr.Append(crv3.GeometryCurve.Reference)
refarr.Append(crv4.GeometryCurve.Reference)
 
#create cap form
cap = doc.FamilyCreate.NewFormByCap(True, refarr)
 
t.Commit()
 
__window__.Close()