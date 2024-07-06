import typing
import Autodesk.Revit.Creation
from System import IDisposable, Guid
from Autodesk.Revit.DB import AddInId, Color, CitySet, ViewDiscipline, DocumentSet, ModelPath, FailureDefinitionRegistry, ServerPath, Document, DefinitionFile, IFailuresProcessor, UnitSystem, OpenOptions, IOpenFromCloudCallback
from System.Collections.Generic import IList_1, IDictionary_2
from Autodesk.Revit.DB.Visual import Asset, AssetType
from Autodesk.Revit.DB.IFC import IFCImportOptions

class Application(IDisposable):
    @property
    def ActiveAddInId(self) -> AddInId: ...
    @property
    def AllowNavigationDuringRedraw(self) -> bool: ...
    @AllowNavigationDuringRedraw.setter
    def AllowNavigationDuringRedraw(self, value: bool) -> bool: ...
    @property
    def AllUsersAddinsLocation(self) -> str: ...
    @property
    def AngleTolerance(self) -> float: ...
    @property
    def BackgroundColor(self) -> Color: ...
    @BackgroundColor.setter
    def BackgroundColor(self, value: Color) -> Color: ...
    @property
    def Cities(self) -> CitySet: ...
    @property
    def Create(self) -> Autodesk.Revit.Creation.Application: ...
    @property
    def CurrentRevitServerAccelerator(self) -> str: ...
    @CurrentRevitServerAccelerator.setter
    def CurrentRevitServerAccelerator(self, value: str) -> str: ...
    @property
    def CurrentUserAddinsLocation(self) -> str: ...
    @property
    def CurrentUsersAddinsDataFolderPath(self) -> str: ...
    @property
    def CurrentUsersDataFolderPath(self) -> str: ...
    @property
    def DefaultIFCProjectTemplate(self) -> str: ...
    @property
    def DefaultProjectTemplate(self) -> str: ...
    @property
    def DefaultViewDiscipline(self) -> ViewDiscipline: ...
    @DefaultViewDiscipline.setter
    def DefaultViewDiscipline(self, value: ViewDiscipline) -> ViewDiscipline: ...
    @property
    def Documents(self) -> DocumentSet: ...
    @property
    def ExportIFCCategoryTable(self) -> str: ...
    @property
    def FamilyTemplatePath(self) -> str: ...
    @property
    def ImportIFCCategoryTable(self) -> str: ...
    @property
    def IsArchitectureEnabled(self) -> bool: ...
    @IsArchitectureEnabled.setter
    def IsArchitectureEnabled(self, value: bool) -> bool: ...
    @property
    def IsElectricalAnalysisEnabled(self) -> bool: ...
    @IsElectricalAnalysisEnabled.setter
    def IsElectricalAnalysisEnabled(self, value: bool) -> bool: ...
    @property
    def IsElectricalEnabled(self) -> bool: ...
    @IsElectricalEnabled.setter
    def IsElectricalEnabled(self, value: bool) -> bool: ...
    @property
    def IsEnergyAnalysisEnabled(self) -> bool: ...
    @IsEnergyAnalysisEnabled.setter
    def IsEnergyAnalysisEnabled(self, value: bool) -> bool: ...
    @property
    def IsInfrastructureEnabled(self) -> bool: ...
    @IsInfrastructureEnabled.setter
    def IsInfrastructureEnabled(self, value: bool) -> bool: ...
    @classmethod
    @property
    def IsLoggedIn(cls) -> bool: ...
    @property
    def IsMassingEnabled(self) -> bool: ...
    @IsMassingEnabled.setter
    def IsMassingEnabled(self, value: bool) -> bool: ...
    @property
    def IsMechanicalAnalysisEnabled(self) -> bool: ...
    @IsMechanicalAnalysisEnabled.setter
    def IsMechanicalAnalysisEnabled(self, value: bool) -> bool: ...
    @property
    def IsMechanicalEnabled(self) -> bool: ...
    @IsMechanicalEnabled.setter
    def IsMechanicalEnabled(self, value: bool) -> bool: ...
    @property
    def IsPipingAnalysisEnabled(self) -> bool: ...
    @IsPipingAnalysisEnabled.setter
    def IsPipingAnalysisEnabled(self, value: bool) -> bool: ...
    @property
    def IsPipingEnabled(self) -> bool: ...
    @IsPipingEnabled.setter
    def IsPipingEnabled(self, value: bool) -> bool: ...
    @property
    def IsRouteAnalysisEnabled(self) -> bool: ...
    @IsRouteAnalysisEnabled.setter
    def IsRouteAnalysisEnabled(self, value: bool) -> bool: ...
    @property
    def IsStructuralAnalysisEnabled(self) -> bool: ...
    @IsStructuralAnalysisEnabled.setter
    def IsStructuralAnalysisEnabled(self, value: bool) -> bool: ...
    @property
    def IsStructureEnabled(self) -> bool: ...
    @IsStructureEnabled.setter
    def IsStructureEnabled(self, value: bool) -> bool: ...
    @property
    def IsSystemsEnabled(self) -> bool: ...
    @property
    def IsValidObject(self) -> bool: ...
    @property
    def Language(self) -> LanguageType: ...
    @property
    def LoginUserId(self) -> str: ...
    @classmethod
    @property
    def MinimumThickness(cls) -> float: ...
    @property
    def PointCloudsRootPath(self) -> str: ...
    @property
    def Product(self) -> ProductType: ...
    @property
    def RecordingJournalFilename(self) -> str: ...
    @property
    def SharedParametersFilename(self) -> str: ...
    @SharedParametersFilename.setter
    def SharedParametersFilename(self, value: str) -> str: ...
    @property
    def ShortCurveTolerance(self) -> float: ...
    @property
    def ShowGraphicalOpenEndsAreaBasedLoadBoundaryDisconnects(self) -> bool: ...
    @ShowGraphicalOpenEndsAreaBasedLoadBoundaryDisconnects.setter
    def ShowGraphicalOpenEndsAreaBasedLoadBoundaryDisconnects(self, value: bool) -> bool: ...
    @property
    def ShowGraphicalWarningCableTrayConduitDisconnects(self) -> bool: ...
    @ShowGraphicalWarningCableTrayConduitDisconnects.setter
    def ShowGraphicalWarningCableTrayConduitDisconnects(self, value: bool) -> bool: ...
    @property
    def ShowGraphicalWarningDuctDisconnects(self) -> bool: ...
    @ShowGraphicalWarningDuctDisconnects.setter
    def ShowGraphicalWarningDuctDisconnects(self, value: bool) -> bool: ...
    @property
    def ShowGraphicalWarningElectricalDisconnects(self) -> bool: ...
    @ShowGraphicalWarningElectricalDisconnects.setter
    def ShowGraphicalWarningElectricalDisconnects(self, value: bool) -> bool: ...
    @property
    def ShowGraphicalWarningHangerDisconnects(self) -> bool: ...
    @ShowGraphicalWarningHangerDisconnects.setter
    def ShowGraphicalWarningHangerDisconnects(self, value: bool) -> bool: ...
    @property
    def ShowGraphicalWarningPipeDisconnects(self) -> bool: ...
    @ShowGraphicalWarningPipeDisconnects.setter
    def ShowGraphicalWarningPipeDisconnects(self, value: bool) -> bool: ...
    @property
    def SubVersionNumber(self) -> str: ...
    @property
    def SystemsAnalysisWorkfilesRootPath(self) -> str: ...
    @property
    def Username(self) -> str: ...
    @property
    def VersionBuild(self) -> str: ...
    @property
    def VersionName(self) -> str: ...
    @property
    def VersionNumber(self) -> str: ...
    @property
    def VertexTolerance(self) -> float: ...
    def CopyModel(self, sourceModelPath: ModelPath, destFilePath: str, overwrite: bool) -> None: ...
    def Dispose(self) -> None: ...
    def ExtractPartAtomFromFamilyFile(self, familyFilePath: str, xmlFilePath: str) -> None: ...
    def GetAssets(self, assetType: AssetType) -> IList_1[Asset]: ...
    @staticmethod
    def GetFailureDefinitionRegistry() -> FailureDefinitionRegistry: ...
    def GetLibraryPaths(self) -> IDictionary_2[str, str]: ...
    def GetRevitServerNetworkHosts(self) -> IList_1[str]: ...
    def GetSystemsAnalysisWorkflowNames(self) -> IList_1[str]: ...
    def GetSystemsAnalysisWorkflows(self) -> IDictionary_2[str, str]: ...
    def GetWorksharingCentralGUID(self, serverModelPath: ServerPath) -> Guid: ...
    def IsJournalPlaying(self) -> bool: ...
    @staticmethod
    def IsValidThickness(thickness: float) -> bool: ...
    def NewFamilyDocument(self, templateFileName: str) -> Document: ...
    def NewProjectTemplateDocument(self, templateFilename: str) -> Document: ...
    def OpenBuildingComponentDocument(self, fileName: str) -> Document: ...
    def OpenSharedParameterFile(self) -> DefinitionFile: ...
    def PurgeReleasedAPIObjects(self) -> None: ...
    @staticmethod
    def RegisterFailuresProcessor(processor: IFailuresProcessor) -> None: ...
    def SetLibraryPaths(self, paths: IDictionary_2[str, str]) -> None: ...
    def SetSystemsAnalysisWorkflows(self, paths: IDictionary_2[str, str]) -> None: ...
    def UpdateRenderAppearanceLibrary(self) -> None: ...
    def WriteJournalComment(self, comment: str, timeStamp: bool) -> None: ...
    # Skipped NewProjectDocument due to it being static, abstract and generic.

    NewProjectDocument : NewProjectDocument_MethodGroup
    class NewProjectDocument_MethodGroup:
        @typing.overload
        def __call__(self, unitSystem: UnitSystem) -> Document:...
        @typing.overload
        def __call__(self, templateFileName: str) -> Document:...

    # Skipped OpenDocumentFile due to it being static, abstract and generic.

    OpenDocumentFile : OpenDocumentFile_MethodGroup
    class OpenDocumentFile_MethodGroup:
        @typing.overload
        def __call__(self, fileName: str) -> Document:...
        @typing.overload
        def __call__(self, modelPath: ModelPath, openOptions: OpenOptions) -> Document:...
        @typing.overload
        def __call__(self, modelPath: ModelPath, openOptions: OpenOptions, openFromCloudCallback: IOpenFromCloudCallback) -> Document:...

    # Skipped OpenIFCDocument due to it being static, abstract and generic.

    OpenIFCDocument : OpenIFCDocument_MethodGroup
    class OpenIFCDocument_MethodGroup:
        @typing.overload
        def __call__(self, fileName: str) -> Document:...
        @typing.overload
        def __call__(self, fileName: str, importOptions: IFCImportOptions) -> Document:...



class ControlledApplication:
    @property
    def ActiveAddInId(self) -> AddInId: ...
    @property
    def AllUsersAddinsLocation(self) -> str: ...
    @property
    def Cities(self) -> CitySet: ...
    @property
    def Create(self) -> Autodesk.Revit.Creation.Application: ...
    @property
    def CurrentUserAddinsLocation(self) -> str: ...
    @property
    def CurrentUsersAddinsDataFolderPath(self) -> str: ...
    @property
    def CurrentUsersDataFolderPath(self) -> str: ...
    @property
    def IsLateAddinLoading(self) -> bool: ...
    @property
    def Language(self) -> LanguageType: ...
    @property
    def Product(self) -> ProductType: ...
    @property
    def RecordingJournalFilename(self) -> str: ...
    @property
    def SharedParametersFilename(self) -> str: ...
    @SharedParametersFilename.setter
    def SharedParametersFilename(self, value: str) -> str: ...
    @property
    def SubVersionNumber(self) -> str: ...
    @property
    def VersionBuild(self) -> str: ...
    @property
    def VersionName(self) -> str: ...
    @property
    def VersionNumber(self) -> str: ...
    @staticmethod
    def GetFailureDefinitionRegistry() -> FailureDefinitionRegistry: ...
    def GetLibraryPaths(self) -> IDictionary_2[str, str]: ...
    def IsJournalPlaying(self) -> bool: ...
    def OpenSharedParameterFile(self) -> DefinitionFile: ...
    @staticmethod
    def RegisterFailuresProcessor(processor: IFailuresProcessor) -> None: ...
    def SetLibraryPaths(self, paths: IDictionary_2[str, str]) -> None: ...
    def WriteJournalComment(self, comment: str, timeStamp: bool) -> None: ...


class LanguageType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    English_USA : LanguageType # 0
    German : LanguageType # 1
    Spanish : LanguageType # 2
    French : LanguageType # 3
    Italian : LanguageType # 4
    Dutch : LanguageType # 5
    Chinese_Simplified : LanguageType # 6
    Chinese_Traditional : LanguageType # 7
    Japanese : LanguageType # 8
    Korean : LanguageType # 9
    Russian : LanguageType # 10
    Czech : LanguageType # 11
    Polish : LanguageType # 12
    Hungarian : LanguageType # 13
    Brazilian_Portuguese : LanguageType # 14
    English_GB : LanguageType # 15
    Unknown : LanguageType # -1


class ProductType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Architecture : ProductType # 0
    Structure : ProductType # 1
    MEP : ProductType # 2
    Revit : ProductType # 3
    LT : ProductType # 4
    Unknown : ProductType # 5

