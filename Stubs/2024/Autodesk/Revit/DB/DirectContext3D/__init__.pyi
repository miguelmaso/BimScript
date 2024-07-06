import typing, clr, abc
from System import IDisposable
from Autodesk.Revit.DB import XYZ, Transform, ElementId, Document, Rectangle, Color, View, Outline, DisplayStyle, ColorWithTransparency
from System.Collections.Generic import ISet_1, IList_1
from Autodesk.Revit.DB.ExternalService import IExternalServer

class Camera(IDisposable):
    def __init__(self, other: Camera) -> None: ...
    @property
    def EyePosition(self) -> XYZ: ...
    @EyePosition.setter
    def EyePosition(self, value: XYZ) -> XYZ: ...
    @property
    def FarDistance(self) -> float: ...
    @FarDistance.setter
    def FarDistance(self, value: float) -> float: ...
    @property
    def HorizontalExtent(self) -> float: ...
    @HorizontalExtent.setter
    def HorizontalExtent(self, value: float) -> float: ...
    @property
    def HorizontalOffset(self) -> float: ...
    @HorizontalOffset.setter
    def HorizontalOffset(self, value: float) -> float: ...
    @property
    def IsValidObject(self) -> bool: ...
    @property
    def NearDistance(self) -> float: ...
    @NearDistance.setter
    def NearDistance(self, value: float) -> float: ...
    @property
    def ProjectionMethod(self) -> ProjectionMethod: ...
    @ProjectionMethod.setter
    def ProjectionMethod(self, value: ProjectionMethod) -> ProjectionMethod: ...
    @property
    def TargetDistance(self) -> float: ...
    @TargetDistance.setter
    def TargetDistance(self, value: float) -> float: ...
    @property
    def UpDirection(self) -> XYZ: ...
    @UpDirection.setter
    def UpDirection(self, value: XYZ) -> XYZ: ...
    @property
    def VerticalExtent(self) -> float: ...
    @VerticalExtent.setter
    def VerticalExtent(self, value: float) -> float: ...
    @property
    def VerticalOffset(self) -> float: ...
    @VerticalOffset.setter
    def VerticalOffset(self, value: float) -> float: ...
    @property
    def ViewDirection(self) -> XYZ: ...
    @ViewDirection.setter
    def ViewDirection(self, value: XYZ) -> XYZ: ...
    def Dispose(self) -> None: ...
    def Transform(self, trf: Transform) -> None: ...


class ClipPlane(IDisposable):
    def __init__(self, other: ClipPlane) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    @property
    def Normal(self) -> XYZ: ...
    @Normal.setter
    def Normal(self, value: XYZ) -> XYZ: ...
    @property
    def Origin(self) -> XYZ: ...
    @Origin.setter
    def Origin(self, value: XYZ) -> XYZ: ...
    def Dispose(self) -> None: ...


class DirectContext3DDocumentUtils(abc.ABC):
    @staticmethod
    def GetDirectContext3DHandleInstances(aDocument: Document, handleCategory: ElementId) -> ISet_1[ElementId]: ...
    @staticmethod
    def GetDirectContext3DHandleTypes(aDocument: Document, handleCategory: ElementId) -> ISet_1[ElementId]: ...
    @staticmethod
    def IsADirectContext3DHandleCategory(categoryId: ElementId) -> bool: ...
    @staticmethod
    def IsADirectContext3DHandleInstance(aDocument: Document, elementId: ElementId) -> bool: ...
    @staticmethod
    def IsADirectContext3DHandleType(aDocument: Document, elementId: ElementId) -> bool: ...


class DirectContext3DHandleOverrides(IDisposable):
    @property
    def IsValidObject(self) -> bool: ...
    def Assign(self, other: DirectContext3DHandleOverrides) -> None: ...
    def Dispose(self) -> None: ...
    def GetDirectContext3DHandleSettings(self, aDoc: Document, elementId: ElementId) -> DirectContext3DHandleSettings: ...
    def IsEqual(self, other: DirectContext3DHandleOverrides) -> bool: ...
    def SetDirectContext3DHandleSettings(self, aDoc: Document, elementId: ElementId, newSettings: DirectContext3DHandleSettings) -> None: ...


class DirectContext3DHandleSettings(IDisposable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: DirectContext3DHandleSettings) -> None: ...
    @typing.overload
    def __init__(self, visibility: bool, transparency: int) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    @property
    def Visibility(self) -> bool: ...
    @Visibility.setter
    def Visibility(self, value: bool) -> bool: ...
    def Assign(self, other: DirectContext3DHandleSettings) -> None: ...
    def Dispose(self) -> None: ...
    def GetTransparency(self) -> int: ...
    def IsEqual(self, other: DirectContext3DHandleSettings) -> bool: ...
    def SetTransparency(self, transparency: int) -> None: ...


class DrawContext(abc.ABC):
    @staticmethod
    def FlushBuffer(vertexBuffer: VertexBuffer, vertexCount: int, indexBuffer: IndexBuffer, indexCount: int, vertexFormat: VertexFormat, effectInstance: EffectInstance, primitiveType: PrimitiveType, start: int, primitiveCount: int) -> None: ...
    @staticmethod
    def GetCamera() -> Camera: ...
    @staticmethod
    def GetClipPlanes() -> IList_1[ClipPlane]: ...
    @staticmethod
    def GetClipRectangle() -> Rectangle: ...
    @staticmethod
    def GetOverrideColor(color: clr.Reference[Color]) -> bool: ...
    @staticmethod
    def GetOverrideTransparency(transparency: clr.Reference[float]) -> bool: ...
    @staticmethod
    def GetViewRectangle() -> Rectangle: ...
    @staticmethod
    def IsAvailable() -> bool: ...
    @staticmethod
    def IsInterrupted() -> bool: ...
    @staticmethod
    def IsTransparentPass() -> bool: ...
    @staticmethod
    def SetWorldTransform(trf: Transform) -> None: ...


class EffectInstance(IDisposable):
    def __init__(self, vertexFormatBits: VertexFormatBits) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...
    def IsValid(self) -> bool: ...
    def MatchesFormat(self, vertexFormat: VertexFormat) -> bool: ...
    def SetAmbientColor(self, color: Color) -> None: ...
    def SetColor(self, color: Color) -> None: ...
    def SetDiffuseColor(self, color: Color) -> None: ...
    def SetEmissiveColor(self, color: Color) -> None: ...
    def SetGlossiness(self, glossiness: float) -> None: ...
    def SetSpecularColor(self, color: Color) -> None: ...
    def SetTransparency(self, transparency: float) -> None: ...


class IDirectContext3DServer(IExternalServer, typing.Protocol):
    @abc.abstractmethod
    def CanExecute(self, dBView: View) -> bool: ...
    @abc.abstractmethod
    def GetApplicationId(self) -> str: ...
    @abc.abstractmethod
    def GetBoundingBox(self, dBView: View) -> Outline: ...
    @abc.abstractmethod
    def GetSourceId(self) -> str: ...
    @abc.abstractmethod
    def RenderScene(self, dBView: View, displayStyle: DisplayStyle) -> None: ...
    @abc.abstractmethod
    def UseInTransparentPass(self, dBView: View) -> bool: ...
    @abc.abstractmethod
    def UsesHandles(self) -> bool: ...


class IndexBuffer(IDisposable):
    def __init__(self, sizeInShortInts: int) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...
    def GetIndexStreamLine(self) -> IndexStreamLine: ...
    def GetIndexStreamPoint(self) -> IndexStreamPoint: ...
    def GetIndexStreamTriangle(self) -> IndexStreamTriangle: ...
    def GetMappedHandle(self) -> int: ...
    def IsValid(self) -> bool: ...
    def Map(self, sizeInShortInts: int) -> None: ...
    def Unmap(self) -> None: ...


class IndexLine(IndexPrimitive):
    def __init__(self, index0: int, index1: int) -> None: ...
    @property
    def Index0(self) -> int: ...
    @Index0.setter
    def Index0(self, value: int) -> int: ...
    @property
    def Index1(self) -> int: ...
    @Index1.setter
    def Index1(self, value: int) -> int: ...
    @property
    def IsValidObject(self) -> bool: ...
    @staticmethod
    def GetSizeInShortInts() -> int: ...


class IndexPoint(IndexPrimitive):
    def __init__(self, index: int) -> None: ...
    @property
    def Index(self) -> int: ...
    @Index.setter
    def Index(self, value: int) -> int: ...
    @property
    def IsValidObject(self) -> bool: ...
    @staticmethod
    def GetSizeInShortInts() -> int: ...


class IndexPrimitive(IDisposable):
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class IndexStream(IDisposable):
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class IndexStreamLine(IndexStream):
    @property
    def IsValidObject(self) -> bool: ...
    def AddLine(self, line: IndexLine) -> None: ...
    def AddLines(self, lines: IList_1[IndexLine]) -> None: ...


class IndexStreamPoint(IndexStream):
    @property
    def IsValidObject(self) -> bool: ...
    def AddPoint(self, point: IndexPoint) -> None: ...
    def AddPoints(self, points: IList_1[IndexPoint]) -> None: ...


class IndexStreamTriangle(IndexStream):
    @property
    def IsValidObject(self) -> bool: ...
    def AddTriangle(self, triangle: IndexTriangle) -> None: ...
    def AddTriangles(self, triangles: IList_1[IndexTriangle]) -> None: ...


class IndexTriangle(IndexPrimitive):
    def __init__(self, index0: int, index1: int, index2: int) -> None: ...
    @property
    def Index0(self) -> int: ...
    @Index0.setter
    def Index0(self, value: int) -> int: ...
    @property
    def Index1(self) -> int: ...
    @Index1.setter
    def Index1(self, value: int) -> int: ...
    @property
    def Index2(self) -> int: ...
    @Index2.setter
    def Index2(self, value: int) -> int: ...
    @property
    def IsValidObject(self) -> bool: ...
    @staticmethod
    def GetSizeInShortInts() -> int: ...


class PrimitiveType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    TriangleList : PrimitiveType # 0
    LineList : PrimitiveType # 1
    PointList : PrimitiveType # 2


class ProjectionMethod(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Orthographic : ProjectionMethod # 0
    Perspective : ProjectionMethod # 1


class Vertex(IDisposable):
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class VertexBuffer(IDisposable):
    def __init__(self, sizeInFloats: int) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...
    def GetMappedHandle(self) -> int: ...
    def GetVertexStreamPosition(self) -> VertexStreamPosition: ...
    def GetVertexStreamPositionColored(self) -> VertexStreamPositionColored: ...
    def GetVertexStreamPositionNormal(self) -> VertexStreamPositionNormal: ...
    def GetVertexStreamPositionNormalColored(self) -> VertexStreamPositionNormalColored: ...
    def IsValid(self) -> bool: ...
    def Map(self, sizeInFloats: int) -> None: ...
    def Unmap(self) -> None: ...


class VertexFormat(IDisposable):
    def __init__(self, vertexFormatBits: VertexFormatBits) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...
    def IsValid(self) -> bool: ...


class VertexFormatBits(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Position : VertexFormatBits # 1
    PositionNormal : VertexFormatBits # 3
    PositionColored : VertexFormatBits # 5
    PositionNormalColored : VertexFormatBits # 7


class VertexPosition(Vertex):
    def __init__(self, position: XYZ) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    @property
    def Position(self) -> XYZ: ...
    @Position.setter
    def Position(self, value: XYZ) -> XYZ: ...
    @staticmethod
    def GetSizeInFloats() -> int: ...


class VertexPositionColored(Vertex):
    def __init__(self, position: XYZ, color: ColorWithTransparency) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    @property
    def Position(self) -> XYZ: ...
    @Position.setter
    def Position(self, value: XYZ) -> XYZ: ...
    def GetColor(self) -> ColorWithTransparency: ...
    @staticmethod
    def GetSizeInFloats() -> int: ...
    def SetColor(self, color: ColorWithTransparency) -> None: ...


class VertexPositionNormal(Vertex):
    def __init__(self, position: XYZ, normal: XYZ) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    @property
    def Normal(self) -> XYZ: ...
    @Normal.setter
    def Normal(self, value: XYZ) -> XYZ: ...
    @property
    def Position(self) -> XYZ: ...
    @Position.setter
    def Position(self, value: XYZ) -> XYZ: ...
    @staticmethod
    def GetSizeInFloats() -> int: ...


class VertexPositionNormalColored(Vertex):
    def __init__(self, position: XYZ, normal: XYZ, color: ColorWithTransparency) -> None: ...
    @property
    def IsValidObject(self) -> bool: ...
    @property
    def Normal(self) -> XYZ: ...
    @Normal.setter
    def Normal(self, value: XYZ) -> XYZ: ...
    @property
    def Position(self) -> XYZ: ...
    @Position.setter
    def Position(self, value: XYZ) -> XYZ: ...
    def GetColor(self) -> ColorWithTransparency: ...
    @staticmethod
    def GetSizeInFloats() -> int: ...
    def SetColor(self, color: ColorWithTransparency) -> None: ...


class VertexStream(IDisposable):
    @property
    def IsValidObject(self) -> bool: ...
    def Dispose(self) -> None: ...


class VertexStreamPosition(VertexStream):
    @property
    def IsValidObject(self) -> bool: ...
    def AddVertex(self, vertex: VertexPosition) -> None: ...
    def AddVertices(self, vertices: IList_1[VertexPosition]) -> None: ...


class VertexStreamPositionColored(VertexStream):
    @property
    def IsValidObject(self) -> bool: ...
    def AddVertex(self, vertex: VertexPositionColored) -> None: ...
    def AddVertices(self, vertices: IList_1[VertexPositionColored]) -> None: ...


class VertexStreamPositionNormal(VertexStream):
    @property
    def IsValidObject(self) -> bool: ...
    def AddVertex(self, vertex: VertexPositionNormal) -> None: ...
    def AddVertices(self, vertices: IList_1[VertexPositionNormal]) -> None: ...


class VertexStreamPositionNormalColored(VertexStream):
    @property
    def IsValidObject(self) -> bool: ...
    def AddVertex(self, vertex: VertexPositionNormalColored) -> None: ...
    def AddVertices(self, vertices: IList_1[VertexPositionNormalColored]) -> None: ...

