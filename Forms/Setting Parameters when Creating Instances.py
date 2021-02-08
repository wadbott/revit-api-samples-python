import clr
import math
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
 
        for i in range(0,20):
            for j in range(0,20):
 
                loc = XYZ((i*70),(j*70),0) 
                familyInst = doc.FamilyCreate.NewFamilyInstance(loc, famsymb, Structure.StructuralType.NonStructural)
 
                #modify FamilyInstance parameter using i and j values
                h = abs((60 * math.sin(i))+(60 * math.cos(j))) + 10
                print(h)
                param = familyInst.GetParameters('height')
                
                for p in param:                
                    p.Set(h)
 
t.Commit()
 
__window__.Close()