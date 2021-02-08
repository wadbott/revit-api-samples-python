import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'Print family parameters')
 
t.Start()
 
#define parameter variables
height = [a for a in doc.FamilyManager.Parameters if a.Definition.Name=='height'][0]
length = [a for a in doc.FamilyManager.Parameters if a.Definition.Name=='length'][0]
width = [a for a in doc.FamilyManager.Parameters if a.Definition.Name=='width'][0]
 
#get parameter values
hvalue = doc.FamilyManager.CurrentType.AsDouble(height)
lvalue = doc.FamilyManager.CurrentType.AsDouble(length)
wvalue = doc.FamilyManager.CurrentType.AsDouble(width)
 
#print parameter values
print 'Height = ' + str(hvalue)
print 'Length = ' + str(lvalue)
print 'Width = ' + str(wvalue)
 
t.Commit()