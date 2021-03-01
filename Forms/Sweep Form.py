import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application 
 
t = Transaction(doc, 'Create a Sweep Form')
 
t.Start()
 
path = CurveArray()

#path.Append(Line.CreateBound(XYZ.Zero, XYZ( 0, 50, 0 )))

refptarr = ReferencePointArray()
 
#use for loop to create a series of points
for i in range(0,20):
    x = i*20
    y = i*20
    #z is controlled using sine
    z = math.sin(i)*50
 
    myXYZ = XYZ(x,y,z)
    refPt = doc.FamilyCreate.NewReferencePoint(myXYZ)
    refptarr.Append(refPt)
 
crv = doc.FamilyCreate.NewCurveByPoints(refptarr)
path.Append(crv.GeometryCurve)

p1 = XYZ( 0, 0, 0 );
p2 = XYZ( 10, 0, 0 );
p3 = XYZ( 10, 15, 0 );
p4 = XYZ( 0, 15, 0 );
a1 = XYZ( 1, 5, 0 );
a2 = XYZ( 3, 5, 0 );
a3 = XYZ( 3, 10, 0 );
a4 = XYZ( 1, 10, 0 );
b1 = XYZ( 5, 5, 0 );
b2 = XYZ( 7, 5, 0 );
b3 = XYZ( 7, 10, 0 );
b4 = XYZ( 5, 10, 0 );
p1 = XYZ( 0, 0, 0 );
p2 = XYZ( 10, 0, 0 );
p3 = XYZ( 10, 15, 0 );
p4 = XYZ( 0, 15, 0 );
a1 = XYZ( 1, 5, 0 );
a2 = XYZ( 3, 5, 0 );
a3 = XYZ( 3, 10, 0 );
a4 = XYZ( 1, 10, 0 );
b1 = XYZ( 5, 5, 0 );
b2 = XYZ( 7, 5, 0 );
b3 = XYZ( 7, 10, 0 );
b4 = XYZ( 5, 10, 0 );

arrcurve = CurveArrArray()
curve = CurveArray()
curve.Append( Line.CreateBound( p1, p2 ) )
curve.Append( Line.CreateBound( p2, p3 ) )
curve.Append( Line.CreateBound( p3, p4 ) )
curve.Append( Line.CreateBound( p4, p1 ) )
arrcurve.Append( curve )
curve = CurveArray()
curve.Append( Line.CreateBound( a1, a4 ) )
curve.Append( Line.CreateBound( a4, a3 ) )
curve.Append( Line.CreateBound( a3, a2 ) )
curve.Append( Line.CreateBound( a2, a1 ) )
arrcurve.Append( curve )
curve = CurveArray()
curve.Append( Line.CreateBound( b1, b4 ) )
curve.Append( Line.CreateBound( b4, b3 ) )
curve.Append( Line.CreateBound( b3, b2 ) )
curve.Append( Line.CreateBound( b2, b1 ) )
arrcurve.Append( curve )

profile = app.Create.NewCurveLoopsProfile(arrcurve)

plane = Plane.CreateByNormalAndOrigin( XYZ.BasisZ, XYZ.Zero)

sketchPlane = SketchPlane.Create(doc, plane)

sweep = doc.FamilyCreate.NewSweep(True, path, sketchPlane, profile, 0, ProfilePlaneLocation.Start)


 
t.Commit()
 
__window__.Close()