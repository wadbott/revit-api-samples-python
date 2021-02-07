import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application
 
t = Transaction(doc, 'Create extrusion.')
 
t.Start()
 
#Create a sketch plane
origin = XYZ.Zero
normal = XYZ.BasisZ
 
plane = Plane.CreateByNormalAndOrigin(normal, origin)
skplane = SketchPlane.Create(doc, plane)
 
#Create line vertices
lnPt1 = XYZ(0,0,0)
lnPt2 = XYZ(10,0,0)
lnPt3 = XYZ(10,10,0)
lnPt4 = XYZ(0,10,0)
 
#create lines
line1 = Line.CreateBound(lnPt1, lnPt2)
line2 = Line.CreateBound(lnPt2, lnPt3)
line3 = Line.CreateBound(lnPt3, lnPt4)
line4 = Line.CreateBound(lnPt4, lnPt1)
 
#create model curves from lines
crvA = doc.FamilyCreate.NewModelCurve(line1, skplane)
crvB = doc.FamilyCreate.NewModelCurve(line2, skplane)
crvC = doc.FamilyCreate.NewModelCurve(line3, skplane)
crvD = doc.FamilyCreate.NewModelCurve(line4, skplane)
 
#create reference array and append with geometry curve references
refarr = ReferenceArray()
refarr.Append(crvA.GeometryCurve.Reference)
refarr.Append(crvB.GeometryCurve.Reference)
refarr.Append(crvC.GeometryCurve.Reference)
refarr.Append(crvD.GeometryCurve.Reference)
 
#establish extrusion vector
dir = XYZ(0,0,10)
 
#extrude the form
extrude = doc.FamilyCreate.NewExtrusionForm(True,refarr,dir)
 
t.Commit()
 
__window__.Close()