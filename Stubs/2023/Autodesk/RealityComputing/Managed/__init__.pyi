import typing, clr, abc
import Autodesk.RealityComputing.Foundation
import Autodesk.RealityComputing.Data
from Autodesk.Revit.DB import BoundingBoxXYZ, Transform
from Autodesk.RealityComputing.Data import IRCPointAccessor
from System import IDisposable
from System.Collections.Generic import List_1
from Autodesk.RealityComputing.Foundation import RCSharedPtr<Autodesk::RealityComputing::Data::RCScan>, RCSharedPtr<Autodesk::RealityComputing::Data::RCSpatialFilter>
from  import AcGeMatrix3d

class RCBox:
    def __init__(self, recapBox: clr.Reference[Autodesk.RealityComputing.Foundation.RCBox]) -> None: ...
    maxPoint : RCVector3d
    minPoint : RCVector3d
    def IntersectWithRay(self, rayOrigin: RCVector3d, rayDirection: RCVector3d) -> bool: ...
    def ToReCapObject(self, : clr.Reference[Autodesk.RealityComputing.Foundation.RCBox] = ...) -> clr.Reference[Autodesk.RealityComputing.Foundation.RCBox]: ...
    def ToRevitObject(self) -> BoundingBoxXYZ: ...
    def ToString(self) -> str: ...


class RCCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    rcFalse : RCCode # 0
    rcTrue : RCCode # 1
    rcOK : RCCode # 100
    rcFailed : RCCode # 101
    rcCancelled : RCCode # 102
    rcBadArgument : RCCode # 103
    rcNullPtr : RCCode # 104
    rcOutOfMemory : RCCode # 105
    rcNotEnoughDiskSpace : RCCode # 106
    rcNotImplemented : RCCode # 107
    rcFailToCreateCacheFolder : RCCode # 108
    rcNotInitialized : RCCode # 109
    rcFileNotExist : RCCode # 1001
    rcFileOpenFailed : RCCode # 1002
    rcFileCorrupt : RCCode # 1003
    rcEOF : RCCode # 1004
    rcNoValidFiles : RCCode # 1005
    rcCreateFolderFailed : RCCode # 1006
    rcFileAlreadyExist : RCCode # 1007
    rcReadOnly : RCCode # 1008
    rcFolderNotExist : RCCode # 1009
    rcInvalidFilePath : RCCode # 1010
    rcTooFewPoints : RCCode # 10000
    rcThreadRunning : RCCode # 100000
    rcUnknownFileFormat : RCCode # 100001
    rcPluginInterfaceNotImpl : RCCode # 100002
    rcLegacyFileFormat : RCCode # 100003
    rcDeprecatedFileFormat : RCCode # 100004
    rcFutureFileFormat : RCCode # 100005
    rcIndexing : RCCode # 100011
    rcIndexCancelled : RCCode # 100012
    rcIndexFailed : RCCode # 100013
    rcEmptyFile : RCCode # 100014
    rcIndexInvalidFileFormat : RCCode # 100015
    rcNotIndexed : RCCode # 100016
    rcDuplicateFiles : RCCode # 100017
    rcLegacyProject : RCCode # 100101
    rcFutureProject : RCCode # 100102
    rcInvalidProject : RCCode # 100103
    rcPhotoProject : RCCode # 100110
    rcUnknownCoordSystem : RCCode # 100201
    rcUnsupportedCoordSystem : RCCode # 100202
    rcLoadCoordSystemFailed : RCCode # 100203
    rcNotLidarData : RCCode # 100204
    rcUnknown : RCCode # -1


class RCFileAccess(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ReadOnly : RCFileAccess # 0
    ReadWrite : RCFileAccess # 1
    Overwrite : RCFileAccess # 2


class RCPoint:
    def __init__(self, recapPoint: clr.Reference[IRCPointAccessor]) -> None: ...
    @property
    def Classification(self) -> int: ...
    @Classification.setter
    def Classification(self, value: int) -> int: ...
    @property
    def Color(self) -> RCColor: ...
    @Color.setter
    def Color(self, value: RCColor) -> RCColor: ...
    @property
    def Deleted(self) -> bool: ...
    @Deleted.setter
    def Deleted(self, value: bool) -> bool: ...
    @property
    def HasClassification(self) -> bool: ...
    @HasClassification.setter
    def HasClassification(self, value: bool) -> bool: ...
    @property
    def HasItensity(self) -> bool: ...
    @HasItensity.setter
    def HasItensity(self, value: bool) -> bool: ...
    @property
    def Index(self) -> int: ...
    @Index.setter
    def Index(self, value: int) -> int: ...
    @property
    def Intensity(self) -> float: ...
    @Intensity.setter
    def Intensity(self, value: float) -> float: ...
    @property
    def Normal(self) -> RCVector3d: ...
    @Normal.setter
    def Normal(self, value: RCVector3d) -> RCVector3d: ...
    @property
    def NormalizedIntensity(self) -> int: ...
    @NormalizedIntensity.setter
    def NormalizedIntensity(self, value: int) -> int: ...
    @property
    def Position(self) -> RCVector3d: ...
    @Position.setter
    def Position(self, value: RCVector3d) -> RCVector3d: ...
    @property
    def ReadOnly(self) -> bool: ...
    @ReadOnly.setter
    def ReadOnly(self, value: bool) -> bool: ...
    @property
    def Region(self) -> int: ...
    @Region.setter
    def Region(self, value: int) -> int: ...
    def ToString(self) -> str: ...


class RCPointIteratorSettings:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, isReadOnly: bool, isVisiblePointsOnly: bool, density: float) -> None: ...
    @property
    def Density(self) -> float: ...
    @Density.setter
    def Density(self, value: float) -> float: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @IsReadOnly.setter
    def IsReadOnly(self, value: bool) -> bool: ...
    @property
    def IsVisiblePointsOnly(self) -> bool: ...
    @IsVisiblePointsOnly.setter
    def IsVisiblePointsOnly(self, value: bool) -> bool: ...


class RCProject(IDisposable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, project: clr.Reference[Autodesk.RealityComputing.Data.RCProject]) -> None: ...
    def AddClip(self, spatialFilter: RCSpatialFilter, clipInside: bool) -> str: ...
    def AddTemporarySpatialFilter(self, spatialFilter: RCSpatialFilter) -> str: ...
    def ClearUserEdits(self) -> None: ...
    def CopyScansToProjectFolder(self) -> RCCode: ...
    def Dispose(self) -> None: ...
    def GetBoundingBox(self) -> RCBox: ...
    def GetCacheFolder(self, rcpFile: str, folder: clr.Reference[str]) -> RCCode: ...
    def GetCoordinateSystem(self) -> str: ...
    def GetIndexOfScan(self, scanId: str) -> int: ...
    def GetNumberOfPoints(self) -> int: ...
    def GetNumberOfPointsEstimate(self, settings: RCPointIteratorSettings) -> int: ...
    def GetNumberOfScans(self) -> int: ...
    def GetNumberOfStructuredScans(self) -> int: ...
    def GetPoints(self, rc_settings: RCPointIteratorSettings) -> List_1[RCPoint]: ...
    def GetProjectIdentifier(self) -> str: ...
    def GetProjectLoadCode(self) -> RCCode: ...
    def GetProjectName(self) -> str: ...
    def GetProjectToSurveyPointsTransform(self, groupToSurveyTransform: clr.Reference[RCTransform]) -> bool: ...
    def GetScanAt(self, scanIndex: int) -> RCScan: ...
    def GetScanById(self, scanId: str) -> RCScan: ...
    def GetSupportFolder(self, rcpFile: str, folder: clr.Reference[str]) -> RCCode: ...
    def GetSystemMemoryLimitInMB(self) -> int: ...
    def GetTemporarySpatialFilters(self, spatialFilters: List_1[RCSpatialFilter]) -> List_1[str]: ...
    def GetUCSTransform(self, UCSTransform: clr.Reference[RCTransform]) -> bool: ...
    def GetUnitType(self) -> RCUnitType: ...
    def GetVisibleBoundingBox(self) -> RCBox: ...
    def LoadFromFile(self, filename: str, accessOption: RCFileAccess, userEdits: RCProjectUserEdits) -> RCCode: ...
    def ModifyPoint(self, point: clr.Reference[RCPoint], settings: RCPointIteratorSettings) -> bool: ...
    def PermanentlyDeletePoints(self) -> bool: ...
    def RemoveAllClips(self) -> RCCode: ...
    def RemoveAllTemporarySpatialFilters(self) -> RCCode: ...
    def RemoveClip(self, spatialFilterId: str) -> RCCode: ...
    def RemoveLastClip(self) -> RCCode: ...
    def RemoveScan(self, scanId: str) -> RCCode: ...
    def RemoveTemporarySpatialFilter(self, spatialFilterId: str) -> RCCode: ...
    def Save(self) -> RCCode: ...
    def SetCoordinateSystem(self, coordinateSystem: str) -> RCCode: ...
    def SetProjectToSurveyPointsTransform(self, groupToSurveyTransform: clr.Reference[RCTransform]) -> bool: ...
    def SetSystemMemoryLimitInMB(self, megaBytes: int) -> None: ...
    def SetUCSTransform(self, UCSTransform: clr.Reference[RCTransform]) -> bool: ...
    def SetUnitType(self, unitType: RCUnitType) -> RCCode: ...
    # Skipped GetPointsByBatchIteration due to it being static, abstract and generic.

    GetPointsByBatchIteration : GetPointsByBatchIteration_MethodGroup
    class GetPointsByBatchIteration_MethodGroup:
        @typing.overload
        def __call__(self, rc_settings: RCPointIteratorSettings) -> List_1[RCPoint]:...
        @typing.overload
        def __call__(self, rc_settings: RCPointIteratorSettings, batchSize: int) -> List_1[RCPoint]:...



class RCProjectUserEdits(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : RCProjectUserEdits # 0
    All : RCProjectUserEdits # 1


class RCScan(IDisposable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, scanPtr: clr.Reference[RCSharedPtr<Autodesk::RealityComputing::Data::RCScan>]) -> None: ...
    def ~RCScan(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetBoundingBox(self) -> RCBox: ...
    def GetFilePath(self) -> str: ...
    def GetFullTransform(self, fullTransform: clr.Reference[RCTransform]) -> bool: ...
    def GetGroupId(self) -> int: ...
    def GetGroupName(self) -> str: ...
    def GetIntensityMaxValue(self) -> float: ...
    def GetIntensityMinValue(self) -> float: ...
    def GetName(self) -> str: ...
    def GetNumberOfPoints(self) -> int: ...
    def GetNumberOfPointsEstimate(self, settings: RCPointIteratorSettings) -> int: ...
    def GetOrigin(self) -> RCVector3d: ...
    def GetPoints(self, rc_settings: RCPointIteratorSettings) -> List_1[RCPoint]: ...
    def GetScale(self) -> RCVector3d: ...
    def GetScanId(self) -> str: ...
    def GetScanProvider(self) -> str: ...
    def GetScanToGroupTransform(self, scanToGroupTransform: clr.Reference[RCTransform]) -> bool: ...
    def GetStructuredScan(self) -> RCStructuredScan: ...
    def GetStructuredScanAzimuthEnd(self) -> float: ...
    def GetStructuredScanAzimuthStart(self) -> float: ...
    def GetStructuredScanElevationEnd(self) -> float: ...
    def GetStructuredScanElevationStart(self) -> float: ...
    def GetStructuredScanHeight(self) -> int: ...
    def GetStructuredScanWidth(self) -> int: ...
    def GetType(self) -> RCScanType: ...
    def HasColors(self) -> bool: ...
    def HasIntensities(self) -> bool: ...
    def HasNormals(self) -> bool: ...
    def HasSegmentInfo(self) -> bool: ...
    def HasTimeStamp(self) -> bool: ...
    def IsStructured(self) -> bool: ...
    def LoadFile(self, filePath: str, accessMode: RCFileAccess) -> RCCode: ...
    def ModifyPoint(self, point: clr.Reference[RCPoint], settings: RCPointIteratorSettings) -> bool: ...
    def SetFullTransform(self, fullTransform: clr.Reference[RCTransform]) -> bool: ...
    # Skipped GetPointsByBatchIteration due to it being static, abstract and generic.

    GetPointsByBatchIteration : GetPointsByBatchIteration_MethodGroup
    class GetPointsByBatchIteration_MethodGroup:
        @typing.overload
        def __call__(self, rc_settings: RCPointIteratorSettings) -> List_1[RCPoint]:...
        @typing.overload
        def __call__(self, rc_settings: RCPointIteratorSettings, batchSize: int) -> List_1[RCPoint]:...



class RCSpatialFilter(abc.ABC):
    def __init__(self) -> None: ...
    def CheckBox(self, box: RCBox) -> RCSpatialFilter.FilterResult: ...
    def CheckPoint(self, point: RCVector3d) -> RCSpatialFilter.FilterResult: ...
    def GetInverse(self) -> RCSpatialFilter: ...
    def GetType(self) -> FilterType: ...
    def ToRecapObject(self, : clr.Reference[RCSharedPtr<Autodesk::RealityComputing::Data::RCSpatialFilter>] = ...) -> clr.Reference[RCSharedPtr<Autodesk::RealityComputing::Data::RCSpatialFilter>]: ...
    def TransformBy(self, transform4x4: clr.Reference[RCTransform]) -> RCSpatialFilter: ...

    class FilterResult(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Inside : RCSpatialFilter.FilterResult # 0
        Outside : RCSpatialFilter.FilterResult # 1
        Intersection : RCSpatialFilter.FilterResult # 2



class RCTransform:
    @typing.overload
    def __init__(self, acGeMatrix: clr.Reference[AcGeMatrix3d]) -> None: ...
    @typing.overload
    def __init__(self, recapTransform: clr.Reference[Autodesk.RealityComputing.Foundation.RCTransform]) -> None: ...
    @typing.overload
    def __init__(self, revitTransform: Transform) -> None: ...
    @property
    def rotation(self) -> RCVector3d: ...
    @rotation.setter
    def rotation(self, value: RCVector3d) -> RCVector3d: ...
    @property
    def scale(self) -> RCVector3d: ...
    @scale.setter
    def scale(self, value: RCVector3d) -> RCVector3d: ...
    @property
    def translation(self) -> RCVector3d: ...
    @translation.setter
    def translation(self, value: RCVector3d) -> RCVector3d: ...
    def GetInverse(self, type: TransformType) -> RCTransform: ...
    def LookAt(self, eye: RCVector3d, center: RCVector3d, up: RCVector3d) -> None: ...
    def ToAcGeMatrix3d(self, : clr.Reference[AcGeMatrix3d] = ...) -> clr.Reference[AcGeMatrix3d]: ...
    def ToReCapTransform(self, : clr.Reference[Autodesk.RealityComputing.Foundation.RCTransform] = ...) -> clr.Reference[Autodesk.RealityComputing.Foundation.RCTransform]: ...
    def ToRevitTransform(self) -> Transform: ...
    def ToString(self) -> str: ...
    # Skipped MultiplyBy due to it being static, abstract and generic.

    MultiplyBy : MultiplyBy_MethodGroup
    class MultiplyBy_MethodGroup:
        @typing.overload
        def __call__(self, other: RCTransform) -> RCTransform:...
        @typing.overload
        def __call__(self, pt: RCVector3d) -> RCVector3d:...



class RCUnitType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Unknown : RCUnitType # 0
    Meter : RCUnitType # 1
    Foot : RCUnitType # 2
    Inch : RCUnitType # 3
    IFoot : RCUnitType # 4
    ClarkeFoot : RCUnitType # 5
    IInch : RCUnitType # 6
    Centimeter : RCUnitType # 7
    Kilometer : RCUnitType # 8
    Yard : RCUnitType # 9
    SearsYard : RCUnitType # 10
    Mile : RCUnitType # 11
    IYard : RCUnitType # 12
    IMile : RCUnitType # 13
    Knot : RCUnitType # 14
    NautM : RCUnitType # 15
    Lat66 : RCUnitType # 16
    Lat83 : RCUnitType # 17
    Decimeter : RCUnitType # 18
    Millimeter : RCUnitType # 19
    Dekameter : RCUnitType # 20
    Hectometer : RCUnitType # 21
    GermanMeter : RCUnitType # 22
    CaGrid : RCUnitType # 23
    ClarkeChain : RCUnitType # 24
    GunterChain : RCUnitType # 25
    BenoitChain : RCUnitType # 26
    SearsChain : RCUnitType # 27
    ClarkeLink : RCUnitType # 28
    GunterLink : RCUnitType # 29
    BenoitLink : RCUnitType # 30
    SearsLink : RCUnitType # 31
    Rod : RCUnitType # 32
    Perch : RCUnitType # 33
    Pole : RCUnitType # 34
    Furlong : RCUnitType # 35
    Rood : RCUnitType # 36
    CapeFoot : RCUnitType # 37
    Brealey : RCUnitType # 38
    SearsFoot : RCUnitType # 39
    GoldCoastFoot : RCUnitType # 40
    MicroInch : RCUnitType # 41
    IndianYard : RCUnitType # 42
    IndianFoot : RCUnitType # 43
    IndianFt37 : RCUnitType # 44
    IndianFt62 : RCUnitType # 45
    IndianFt75 : RCUnitType # 46
    IndianYd37 : RCUnitType # 47
    Decameter : RCUnitType # 48
    InternationalChain : RCUnitType # 49
    InternationalLink : RCUnitType # 50
    Micrometer : RCUnitType # 51
    FootAndInch : RCUnitType # 101
    IFootAndInch : RCUnitType # 102
    Degree : RCUnitType # 1001
    Grad : RCUnitType # 1002
    Grade : RCUnitType # 1003
    MapInfo : RCUnitType # 1004
    Mil : RCUnitType # 1005
    Minute : RCUnitType # 1006
    Radian : RCUnitType # 1007
    Second : RCUnitType # 1008
    Decisec : RCUnitType # 1009
    Centisec : RCUnitType # 1010
    Millisec : RCUnitType # 1011
