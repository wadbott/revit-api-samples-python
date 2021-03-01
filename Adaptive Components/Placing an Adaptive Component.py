import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document
 
t = Transaction(doc, 'Place an Adaptive Component.')
 
t.Start()
 
#Family symbol name to place.
symbName = 'SOFiSTiK_Hollow_double_slope'
 
#create a filtered element collector set to Category OST_Mass and Class FamilySymbol 
collector = FilteredElementCollector(doc)
collector.OfCategory(BuiltInCategory.OST_GenericModel)
collector.OfClass(FamilySymbol)
 
famtypeitr = collector.GetElementIdIterator()
famtypeitr.Reset()
 
#Search Family Symbols in document.
for item in famtypeitr:
    famtypeID = item
    famsymb = doc.GetElement(famtypeID)
 
    #If the FamilySymbol is the name we are looking for, create a new instance.
    if famsymb.Family.Name == symbName:
 
        adaptComp = AdaptiveComponentInstanceUtils.CreateAdaptiveComponentInstance(doc, famsymb)
        adptPoints = AdaptiveComponentInstanceUtils.GetInstancePlacementPointElementRefIds(adaptComp)
 
        #Starting adaptive point locations.  get_Element returns a Reference Point
        aPt1 = doc.GetElement(adptPoints[0])
        aPt2 = doc.GetElement(adptPoints[1])
        #aPt3 = doc.get_Element(adptPoints[2])
        #aPt4 = doc.get_Element(adptPoints[3])
 
        #Desired Adaptive Point Locations
        loc1 = XYZ(50,10,60)
        loc2 = XYZ(0,40,20) 
        #loc3 = XYZ(40,40,0) 
        #loc4 = XYZ(40,0,20) 
 
        #Some vector math to get the translation for MoveElement()
        trans1 = loc1.Subtract(aPt1.Position)
        trans2 = loc2.Subtract(aPt2.Position)
        #trans3 = loc3.Subtract(aPt3.Position)
        #trans4 = loc4.Subtract(aPt4.Position)
 
        #Position Adaptive Component using MoveElement()
        ElementTransformUtils.MoveElement(doc, adptPoints[0], trans1)
       	ElementTransformUtils.MoveElement(doc, adptPoints[1], trans2)
        #ElementTransformUtils.MoveElement(doc, adptPoints[2], trans3)
        #ElementTransformUtils.MoveElement(doc, adptPoints[3], trans4)
 
t.Commit()
 
__window__.Close()