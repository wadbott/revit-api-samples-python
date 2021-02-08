import clr
import System
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'Change parameters with random values.')
 
t.Start()
 
#declare randomization parameters
#random seed
seed = 4
 
#random range
r1 = 20
r2 = 150
 
#random
rand = System.Random(seed)
 
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
        #set height parameter using random variable
        for p in param:
        	p.Set(rand.Next(r1,r2))
       
 
t.Commit()
 
__window__.Close()