import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

#Firt thing we need to load the family into the doc (insert -> load family)
 
t = Transaction(doc, 'Create family instance.')
 
t.Start()
 
#Family symbol name to place.
symbName = 'BoxFamily'
 
#create a filtered element collector set to Category OST_Mass and Class FamilySymbol 
collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Mass).OfClass(FamilySymbol)
 
famtypeitr = collector.GetElementIdIterator()
famtypeitr.Reset()
 
#Search Family Symbols in document.
for item in famtypeitr:
    famtypeID = item
    famsymb = doc.GetElement(famtypeID)  

    #If the FamilySymbol is the name we are looking for, create a new instance.
    if famsymb.Family.Name == symbName:        
 
        #location to place family
        loc = XYZ(0,0,0) 
        
        # To Make sure the familysymbol is active
        if famsymb.IsActive == False:
			famsymb.Activate()
			doc.Regenerate()
			
        #NewFamilyInstance()
        familyInst = doc.FamilyCreate.NewFamilyInstance(loc, famsymb, Structure.StructuralType.NonStructural)
 
t.Commit()
 
__window__.Close()