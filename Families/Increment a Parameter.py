import clr
import math
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'Increment family parameters')
 
t.Start()
 
#define parameter variables
height = [a for a in doc.FamilyManager.Parameters if a.Definition.Name=='height'][0]
length = [a for a in doc.FamilyManager.Parameters if a.Definition.Name=='length'][0]
width = [a for a in doc.FamilyManager.Parameters if a.Definition.Name=='width'][0]
 
#get current values
hvalue = doc.FamilyManager.CurrentType.AsDouble(height)
lvalue = doc.FamilyManager.CurrentType.AsDouble(length)
wvalue = doc.FamilyManager.CurrentType.AsDouble(width)
 
#set new values
doc.FamilyManager.Set(height, hvalue + 10)
doc.FamilyManager.Set(length, lvalue + 10)
doc.FamilyManager.Set(width, wvalue + 10)
 
t.Commit()
 
__window__.Close()