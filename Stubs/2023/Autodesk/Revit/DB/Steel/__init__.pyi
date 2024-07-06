from Autodesk.Revit.DB import APIObject, ElementId, Document, Reference, Element
from System import Guid
from System.Collections.Generic import IList_1

class SteelElementProperties(APIObject):
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsValidObject(self) -> bool: ...
    @property
    def UniqueID(self) -> Guid: ...
    @UniqueID.setter
    def UniqueID(self, value: Guid) -> Guid: ...
    @staticmethod
    def AddFabricationInformationForRevitElements(aDoc: Document, elementIds: IList_1[ElementId]) -> IList_1[ElementId]: ...
    @staticmethod
    def GetFabricationUniqueID(aDoc: Document, reference: Reference) -> Guid: ...
    @staticmethod
    def GetReference(aDoc: Document, guid: Guid) -> Reference: ...
    @staticmethod
    def GetSteelElementProperties(pElement: Element) -> SteelElementProperties: ...
