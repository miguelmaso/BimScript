import typing, clr
from System import MarshalByRefObject, IDisposable, ICloneable, Array_1
from System.Drawing import PointF, Point, RectangleF, Rectangle, FontFamily, StringFormat, Pen, Graphics

class CombineMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Replace : CombineMode # 0
    Intersect : CombineMode # 1
    Union : CombineMode # 2
    Xor : CombineMode # 3
    Exclude : CombineMode # 4
    Complement : CombineMode # 5


class CompositingMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    SourceOver : CompositingMode # 0
    SourceCopy : CompositingMode # 1


class CompositingQuality(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : CompositingQuality # 0
    HighSpeed : CompositingQuality # 1
    HighQuality : CompositingQuality # 2
    GammaCorrected : CompositingQuality # 3
    AssumeLinear : CompositingQuality # 4
    Invalid : CompositingQuality # -1


class CoordinateSpace(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    World : CoordinateSpace # 0
    Page : CoordinateSpace # 1
    Device : CoordinateSpace # 2


class CustomLineCap(MarshalByRefObject, IDisposable, ICloneable):
    @typing.overload
    def __init__(self, fillPath: GraphicsPath, strokePath: GraphicsPath) -> None: ...
    @typing.overload
    def __init__(self, fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap) -> None: ...
    @typing.overload
    def __init__(self, fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap, baseInset: float) -> None: ...
    @property
    def BaseCap(self) -> LineCap: ...
    @BaseCap.setter
    def BaseCap(self, value: LineCap) -> LineCap: ...
    @property
    def BaseInset(self) -> float: ...
    @BaseInset.setter
    def BaseInset(self, value: float) -> float: ...
    @property
    def StrokeJoin(self) -> LineJoin: ...
    @StrokeJoin.setter
    def StrokeJoin(self, value: LineJoin) -> LineJoin: ...
    @property
    def WidthScale(self) -> float: ...
    @WidthScale.setter
    def WidthScale(self, value: float) -> float: ...
    def Clone(self) -> typing.Any: ...
    def Dispose(self) -> None: ...
    def GetStrokeCaps(self, startCap: clr.Reference[LineCap], endCap: clr.Reference[LineCap]) -> None: ...
    def SetStrokeCaps(self, startCap: LineCap, endCap: LineCap) -> None: ...


class DashCap(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Flat : DashCap # 0
    Round : DashCap # 2
    Triangle : DashCap # 3


class DashStyle(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Solid : DashStyle # 0
    Dash : DashStyle # 1
    Dot : DashStyle # 2
    DashDot : DashStyle # 3
    DashDotDot : DashStyle # 4
    Custom : DashStyle # 5


class FillMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Alternate : FillMode # 0
    Winding : FillMode # 1


class FlushIntention(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Flush : FlushIntention # 0
    Sync : FlushIntention # 1


class GraphicsContainer(MarshalByRefObject):
    pass


class GraphicsPath(MarshalByRefObject, IDisposable, ICloneable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, fillMode: FillMode) -> None: ...
    @typing.overload
    def __init__(self, pts: Array_1[PointF], types: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, pts: Array_1[Point], types: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, pts: Array_1[PointF], types: Array_1[int], fillMode: FillMode) -> None: ...
    @typing.overload
    def __init__(self, pts: Array_1[Point], types: Array_1[int], fillMode: FillMode) -> None: ...
    @property
    def FillMode(self) -> FillMode: ...
    @FillMode.setter
    def FillMode(self, value: FillMode) -> FillMode: ...
    @property
    def PathData(self) -> PathData: ...
    @property
    def PathPoints(self) -> Array_1[PointF]: ...
    @property
    def PathTypes(self) -> Array_1[int]: ...
    @property
    def PointCount(self) -> int: ...
    def AddPath(self, addingPath: GraphicsPath, connect: bool) -> None: ...
    def ClearMarkers(self) -> None: ...
    def Clone(self) -> typing.Any: ...
    def CloseAllFigures(self) -> None: ...
    def CloseFigure(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetLastPoint(self) -> PointF: ...
    def Reset(self) -> None: ...
    def Reverse(self) -> None: ...
    def SetMarkers(self) -> None: ...
    def StartFigure(self) -> None: ...
    def Transform(self, matrix: Matrix) -> None: ...
    # Skipped AddArc due to it being static, abstract and generic.

    AddArc : AddArc_MethodGroup
    class AddArc_MethodGroup:
        @typing.overload
        def __call__(self, rect: RectangleF, startAngle: float, sweepAngle: float) -> None:...
        @typing.overload
        def __call__(self, rect: Rectangle, startAngle: float, sweepAngle: float) -> None:...
        @typing.overload
        def __call__(self, x: float, y: float, width: float, height: float, startAngle: float, sweepAngle: float) -> None:...
        # Method AddArc(x : Int32, y : Int32, width : Int32, height : Int32, startAngle : Single, sweepAngle : Single) was skipped since it collides with above method

    # Skipped AddBezier due to it being static, abstract and generic.

    AddBezier : AddBezier_MethodGroup
    class AddBezier_MethodGroup:
        @typing.overload
        def __call__(self, pt1: PointF, pt2: PointF, pt3: PointF, pt4: PointF) -> None:...
        @typing.overload
        def __call__(self, pt1: Point, pt2: Point, pt3: Point, pt4: Point) -> None:...
        @typing.overload
        def __call__(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None:...
        # Method AddBezier(x1 : Int32, y1 : Int32, x2 : Int32, y2 : Int32, x3 : Int32, y3 : Int32, x4 : Int32, y4 : Int32) was skipped since it collides with above method

    # Skipped AddBeziers due to it being static, abstract and generic.

    AddBeziers : AddBeziers_MethodGroup
    class AddBeziers_MethodGroup:
        @typing.overload
        def __call__(self, points: Array_1[PointF]) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[Point]) -> None:...

    # Skipped AddClosedCurve due to it being static, abstract and generic.

    AddClosedCurve : AddClosedCurve_MethodGroup
    class AddClosedCurve_MethodGroup:
        @typing.overload
        def __call__(self, points: Array_1[PointF]) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[Point]) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[PointF], tension: float) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[Point], tension: float) -> None:...

    # Skipped AddCurve due to it being static, abstract and generic.

    AddCurve : AddCurve_MethodGroup
    class AddCurve_MethodGroup:
        @typing.overload
        def __call__(self, points: Array_1[PointF]) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[Point]) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[PointF], tension: float) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[Point], tension: float) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[PointF], offset: int, numberOfSegments: int, tension: float) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[Point], offset: int, numberOfSegments: int, tension: float) -> None:...

    # Skipped AddEllipse due to it being static, abstract and generic.

    AddEllipse : AddEllipse_MethodGroup
    class AddEllipse_MethodGroup:
        @typing.overload
        def __call__(self, rect: RectangleF) -> None:...
        @typing.overload
        def __call__(self, rect: Rectangle) -> None:...
        @typing.overload
        def __call__(self, x: float, y: float, width: float, height: float) -> None:...
        # Method AddEllipse(x : Int32, y : Int32, width : Int32, height : Int32) was skipped since it collides with above method

    # Skipped AddLine due to it being static, abstract and generic.

    AddLine : AddLine_MethodGroup
    class AddLine_MethodGroup:
        @typing.overload
        def __call__(self, pt1: PointF, pt2: PointF) -> None:...
        @typing.overload
        def __call__(self, pt1: Point, pt2: Point) -> None:...
        @typing.overload
        def __call__(self, x1: float, y1: float, x2: float, y2: float) -> None:...
        # Method AddLine(x1 : Int32, y1 : Int32, x2 : Int32, y2 : Int32) was skipped since it collides with above method

    # Skipped AddLines due to it being static, abstract and generic.

    AddLines : AddLines_MethodGroup
    class AddLines_MethodGroup:
        @typing.overload
        def __call__(self, points: Array_1[PointF]) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[Point]) -> None:...

    # Skipped AddPie due to it being static, abstract and generic.

    AddPie : AddPie_MethodGroup
    class AddPie_MethodGroup:
        @typing.overload
        def __call__(self, rect: Rectangle, startAngle: float, sweepAngle: float) -> None:...
        @typing.overload
        def __call__(self, x: float, y: float, width: float, height: float, startAngle: float, sweepAngle: float) -> None:...
        # Method AddPie(x : Int32, y : Int32, width : Int32, height : Int32, startAngle : Single, sweepAngle : Single) was skipped since it collides with above method

    # Skipped AddPolygon due to it being static, abstract and generic.

    AddPolygon : AddPolygon_MethodGroup
    class AddPolygon_MethodGroup:
        @typing.overload
        def __call__(self, points: Array_1[PointF]) -> None:...
        @typing.overload
        def __call__(self, points: Array_1[Point]) -> None:...

    # Skipped AddRectangle due to it being static, abstract and generic.

    AddRectangle : AddRectangle_MethodGroup
    class AddRectangle_MethodGroup:
        @typing.overload
        def __call__(self, rect: RectangleF) -> None:...
        @typing.overload
        def __call__(self, rect: Rectangle) -> None:...

    # Skipped AddRectangles due to it being static, abstract and generic.

    AddRectangles : AddRectangles_MethodGroup
    class AddRectangles_MethodGroup:
        @typing.overload
        def __call__(self, rects: Array_1[RectangleF]) -> None:...
        @typing.overload
        def __call__(self, rects: Array_1[Rectangle]) -> None:...

    # Skipped AddString due to it being static, abstract and generic.

    AddString : AddString_MethodGroup
    class AddString_MethodGroup:
        @typing.overload
        def __call__(self, s: str, family: FontFamily, style: int, emSize: float, layoutRect: RectangleF, format: StringFormat) -> None:...
        @typing.overload
        def __call__(self, s: str, family: FontFamily, style: int, emSize: float, layoutRect: Rectangle, format: StringFormat) -> None:...
        @typing.overload
        def __call__(self, s: str, family: FontFamily, style: int, emSize: float, origin: PointF, format: StringFormat) -> None:...
        @typing.overload
        def __call__(self, s: str, family: FontFamily, style: int, emSize: float, origin: Point, format: StringFormat) -> None:...

    # Skipped Flatten due to it being static, abstract and generic.

    Flatten : Flatten_MethodGroup
    class Flatten_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, matrix: Matrix) -> None:...
        @typing.overload
        def __call__(self, matrix: Matrix, flatness: float) -> None:...

    # Skipped GetBounds due to it being static, abstract and generic.

    GetBounds : GetBounds_MethodGroup
    class GetBounds_MethodGroup:
        @typing.overload
        def __call__(self) -> RectangleF:...
        @typing.overload
        def __call__(self, matrix: Matrix) -> RectangleF:...
        @typing.overload
        def __call__(self, matrix: Matrix, pen: Pen) -> RectangleF:...

    # Skipped IsOutlineVisible due to it being static, abstract and generic.

    IsOutlineVisible : IsOutlineVisible_MethodGroup
    class IsOutlineVisible_MethodGroup:
        @typing.overload
        def __call__(self, point: PointF, pen: Pen) -> bool:...
        @typing.overload
        def __call__(self, point: Point, pen: Pen) -> bool:...
        @typing.overload
        def __call__(self, x: float, y: float, pen: Pen) -> bool:...
        # Method IsOutlineVisible(x : Int32, y : Int32, pen : Pen) was skipped since it collides with above method
        @typing.overload
        def __call__(self, pt: PointF, pen: Pen, graphics: Graphics) -> bool:...
        @typing.overload
        def __call__(self, pt: Point, pen: Pen, graphics: Graphics) -> bool:...
        @typing.overload
        def __call__(self, x: float, y: float, pen: Pen, graphics: Graphics) -> bool:...
        # Method IsOutlineVisible(x : Int32, y : Int32, pen : Pen, graphics : Graphics) was skipped since it collides with above method

    # Skipped IsVisible due to it being static, abstract and generic.

    IsVisible : IsVisible_MethodGroup
    class IsVisible_MethodGroup:
        @typing.overload
        def __call__(self, point: PointF) -> bool:...
        @typing.overload
        def __call__(self, point: Point) -> bool:...
        @typing.overload
        def __call__(self, x: float, y: float) -> bool:...
        # Method IsVisible(x : Int32, y : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, pt: PointF, graphics: Graphics) -> bool:...
        @typing.overload
        def __call__(self, pt: Point, graphics: Graphics) -> bool:...
        @typing.overload
        def __call__(self, x: float, y: float, graphics: Graphics) -> bool:...
        # Method IsVisible(x : Int32, y : Int32, graphics : Graphics) was skipped since it collides with above method

    # Skipped Warp due to it being static, abstract and generic.

    Warp : Warp_MethodGroup
    class Warp_MethodGroup:
        @typing.overload
        def __call__(self, destPoints: Array_1[PointF], srcRect: RectangleF) -> None:...
        @typing.overload
        def __call__(self, destPoints: Array_1[PointF], srcRect: RectangleF, matrix: Matrix) -> None:...
        @typing.overload
        def __call__(self, destPoints: Array_1[PointF], srcRect: RectangleF, matrix: Matrix, warpMode: WarpMode) -> None:...
        @typing.overload
        def __call__(self, destPoints: Array_1[PointF], srcRect: RectangleF, matrix: Matrix, warpMode: WarpMode, flatness: float) -> None:...

    # Skipped Widen due to it being static, abstract and generic.

    Widen : Widen_MethodGroup
    class Widen_MethodGroup:
        @typing.overload
        def __call__(self, pen: Pen) -> None:...
        @typing.overload
        def __call__(self, pen: Pen, matrix: Matrix) -> None:...
        @typing.overload
        def __call__(self, pen: Pen, matrix: Matrix, flatness: float) -> None:...



class GraphicsState(MarshalByRefObject):
    pass


class InterpolationMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : InterpolationMode # 0
    Low : InterpolationMode # 1
    High : InterpolationMode # 2
    Bilinear : InterpolationMode # 3
    Bicubic : InterpolationMode # 4
    NearestNeighbor : InterpolationMode # 5
    HighQualityBilinear : InterpolationMode # 6
    HighQualityBicubic : InterpolationMode # 7
    Invalid : InterpolationMode # -1


class LineCap(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Flat : LineCap # 0
    Square : LineCap # 1
    Round : LineCap # 2
    Triangle : LineCap # 3
    NoAnchor : LineCap # 16
    SquareAnchor : LineCap # 17
    RoundAnchor : LineCap # 18
    DiamondAnchor : LineCap # 19
    ArrowAnchor : LineCap # 20
    AnchorMask : LineCap # 240
    Custom : LineCap # 255


class LineJoin(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Miter : LineJoin # 0
    Bevel : LineJoin # 1
    Round : LineJoin # 2
    MiterClipped : LineJoin # 3


class Matrix(MarshalByRefObject, IDisposable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, m11: float, m12: float, m21: float, m22: float, dx: float, dy: float) -> None: ...
    @typing.overload
    def __init__(self, rect: RectangleF, plgpts: Array_1[PointF]) -> None: ...
    @typing.overload
    def __init__(self, rect: Rectangle, plgpts: Array_1[Point]) -> None: ...
    @property
    def Elements(self) -> Array_1[float]: ...
    @property
    def IsIdentity(self) -> bool: ...
    @property
    def IsInvertible(self) -> bool: ...
    @property
    def OffsetX(self) -> float: ...
    @property
    def OffsetY(self) -> float: ...
    def Clone(self) -> Matrix: ...
    def Dispose(self) -> None: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def Invert(self) -> None: ...
    def Reset(self) -> None: ...
    def VectorTransformPoints(self, pts: Array_1[Point]) -> None: ...
    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        @typing.overload
        def __call__(self, matrix: Matrix) -> None:...
        @typing.overload
        def __call__(self, matrix: Matrix, order: MatrixOrder) -> None:...

    # Skipped Rotate due to it being static, abstract and generic.

    Rotate : Rotate_MethodGroup
    class Rotate_MethodGroup:
        @typing.overload
        def __call__(self, angle: float) -> None:...
        @typing.overload
        def __call__(self, angle: float, order: MatrixOrder) -> None:...

    # Skipped RotateAt due to it being static, abstract and generic.

    RotateAt : RotateAt_MethodGroup
    class RotateAt_MethodGroup:
        @typing.overload
        def __call__(self, angle: float, point: PointF) -> None:...
        @typing.overload
        def __call__(self, angle: float, point: PointF, order: MatrixOrder) -> None:...

    # Skipped Scale due to it being static, abstract and generic.

    Scale : Scale_MethodGroup
    class Scale_MethodGroup:
        @typing.overload
        def __call__(self, scaleX: float, scaleY: float) -> None:...
        @typing.overload
        def __call__(self, scaleX: float, scaleY: float, order: MatrixOrder) -> None:...

    # Skipped Shear due to it being static, abstract and generic.

    Shear : Shear_MethodGroup
    class Shear_MethodGroup:
        @typing.overload
        def __call__(self, shearX: float, shearY: float) -> None:...
        @typing.overload
        def __call__(self, shearX: float, shearY: float, order: MatrixOrder) -> None:...

    # Skipped TransformPoints due to it being static, abstract and generic.

    TransformPoints : TransformPoints_MethodGroup
    class TransformPoints_MethodGroup:
        @typing.overload
        def __call__(self, pts: Array_1[PointF]) -> None:...
        @typing.overload
        def __call__(self, pts: Array_1[Point]) -> None:...

    # Skipped TransformVectors due to it being static, abstract and generic.

    TransformVectors : TransformVectors_MethodGroup
    class TransformVectors_MethodGroup:
        @typing.overload
        def __call__(self, pts: Array_1[PointF]) -> None:...
        @typing.overload
        def __call__(self, pts: Array_1[Point]) -> None:...

    # Skipped Translate due to it being static, abstract and generic.

    Translate : Translate_MethodGroup
    class Translate_MethodGroup:
        @typing.overload
        def __call__(self, offsetX: float, offsetY: float) -> None:...
        @typing.overload
        def __call__(self, offsetX: float, offsetY: float, order: MatrixOrder) -> None:...



class MatrixOrder(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Prepend : MatrixOrder # 0
    Append : MatrixOrder # 1


class PathData:
    def __init__(self) -> None: ...
    @property
    def Points(self) -> Array_1[PointF]: ...
    @Points.setter
    def Points(self, value: Array_1[PointF]) -> Array_1[PointF]: ...
    @property
    def Types(self) -> Array_1[int]: ...
    @Types.setter
    def Types(self, value: Array_1[int]) -> Array_1[int]: ...


class PenAlignment(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Center : PenAlignment # 0
    Inset : PenAlignment # 1
    Outset : PenAlignment # 2
    Left : PenAlignment # 3
    Right : PenAlignment # 4


class PenType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    SolidColor : PenType # 0
    HatchFill : PenType # 1
    TextureFill : PenType # 2
    PathGradient : PenType # 3
    LinearGradient : PenType # 4


class PixelOffsetMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : PixelOffsetMode # 0
    HighSpeed : PixelOffsetMode # 1
    HighQuality : PixelOffsetMode # 2
    None_ : PixelOffsetMode # 3
    Half : PixelOffsetMode # 4
    Invalid : PixelOffsetMode # -1


class RegionData:
    @property
    def Data(self) -> Array_1[int]: ...
    @Data.setter
    def Data(self, value: Array_1[int]) -> Array_1[int]: ...


class SmoothingMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : SmoothingMode # 0
    HighSpeed : SmoothingMode # 1
    HighQuality : SmoothingMode # 2
    None_ : SmoothingMode # 3
    AntiAlias : SmoothingMode # 4
    Invalid : SmoothingMode # -1


class WarpMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Perspective : WarpMode # 0
    Bilinear : WarpMode # 1

