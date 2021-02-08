import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'Set family parameters')
 
t.Start()
 
#define parameter variables
height = [a for a in doc.FamilyManager.Parameters if a.Definition.Name=='height'][0]
length = [a for a in doc.FamilyManager.Parameters if a.Definition.Name=='length'][0]
width = [a for a in doc.FamilyManager.Parameters if a.Definition.Name=='width'][0]
 
#set parameters
doc.FamilyManager.Set(height, 100)
doc.FamilyManager.Set(length, 25)
doc.FamilyManager.Set(width, 50)
 
t.Commit()
 
__window__.Close()