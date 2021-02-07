import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'create a single reference point')
 
t.Start()
 
#define x, y, and z variables
x = 10
y = 10
z = 0
 
#declare a XYZ variable
myXYZ = XYZ(x,y,z)
 
#use XYZ to define a reference point
refPoint = doc.FamilyCreate.NewReferencePoint(myXYZ)
 
t.Commit()
 
__window__.Close()