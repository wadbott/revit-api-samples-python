import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'Modify existing family instances.')
 
t.Start()
 
instName = 'BoxFamily'
 
collector = FilteredElementCollector(doc)
collector.OfCategory(BuiltInCategory.OST_Mass)
collector.OfClass(FamilyInstance)
 
famtypeitr = collector.GetElementIdIterator()
famtypeitr.Reset()
 
inc = 1
 
for item in famtypeitr:
    famtypeID = item
    faminst = doc.GetElement(famtypeID)
 
    if faminst.Name == instName:
        param = faminst.GetParameters('height')

        # change the height for each FamilyBox
        for i in param:        
        	i.Set(2*inc)
        inc = inc + 1
 
t.Commit()
 
__window__.Close()