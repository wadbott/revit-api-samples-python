import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'Create multiple family instances.')
 
t.Start()
 
symbName = 'BoxFamily'
 
collector = FilteredElementCollector(doc)
collector.OfCategory(BuiltInCategory.OST_Mass)
collector.OfClass(FamilySymbol)
 
famtypeitr = collector.GetElementIdIterator()
famtypeitr.Reset()
 
for item in famtypeitr:
    famtypeID = item
    famsymb = doc.GetElement(famtypeID)
 
    if famsymb.Family.Name == symbName:
    
        # To Make sure the familysymbol is active
        if famsymb.IsActive == False:
			famsymb.Activate()
			doc.Regenerate()
 
        #Use nested for loop to create grid of family instances.
        for i in range(0,10):
            for j in range(0,10):
 
                loc = XYZ((i*70),(j*70),0) 
                familyInst = doc.FamilyCreate.NewFamilyInstance(loc, famsymb, Structure.StructuralType.NonStructural)
 
t.Commit()
 
__window__.Close()