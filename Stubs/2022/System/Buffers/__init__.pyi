import typing, clr, abc
from System import Array_1, IDisposable, Memory_1, Span_1, MulticastDelegate, IAsyncResult, ReadOnlySpan_1, AsyncCallback, IEquatable_1
from System.Runtime.InteropServices import GCHandle
from System.Reflection import MethodInfo

class ArrayPool_GenericClasses(abc.ABCMeta):
    Generic_ArrayPool_GenericClasses_ArrayPool_1_T = typing.TypeVar('Generic_ArrayPool_GenericClasses_ArrayPool_1_T')
    def __getitem__(self, types : typing.Type[Generic_ArrayPool_GenericClasses_ArrayPool_1_T]) -> typing.Type[ArrayPool_1[Generic_ArrayPool_GenericClasses_ArrayPool_1_T]]: ...

ArrayPool : ArrayPool_GenericClasses

ArrayPool_1_T = typing.TypeVar('ArrayPool_1_T')
class ArrayPool_1(typing.Generic[ArrayPool_1_T], abc.ABC):
    @classmethod
    @property
    def Shared(cls) -> ArrayPool_1[ArrayPool_1_T]: ...
    @abc.abstractmethod
    def Rent(self, minimumLength: int) -> Array_1[ArrayPool_1_T]: ...
    @abc.abstractmethod
    def Return(self, array: Array_1[ArrayPool_1_T], clearArray: bool = ...) -> None: ...
    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup[ArrayPool_1_T]
    Create_MethodGroup_ArrayPool_1_T = typing.TypeVar('Create_MethodGroup_ArrayPool_1_T')
    class Create_MethodGroup(typing.Generic[Create_MethodGroup_ArrayPool_1_T]):
        Create_MethodGroup_ArrayPool_1_T = ArrayPool_1.Create_MethodGroup_ArrayPool_1_T
        @typing.overload
        def __call__(self) -> ArrayPool_1[Create_MethodGroup_ArrayPool_1_T]:...
        @typing.overload
        def __call__(self, maxArrayLength: int, maxArraysPerBucket: int) -> ArrayPool_1[Create_MethodGroup_ArrayPool_1_T]:...



class IMemoryOwner_GenericClasses(abc.ABCMeta):
    Generic_IMemoryOwner_GenericClasses_IMemoryOwner_1_T = typing.TypeVar('Generic_IMemoryOwner_GenericClasses_IMemoryOwner_1_T')
    def __getitem__(self, types : typing.Type[Generic_IMemoryOwner_GenericClasses_IMemoryOwner_1_T]) -> typing.Type[IMemoryOwner_1[Generic_IMemoryOwner_GenericClasses_IMemoryOwner_1_T]]: ...

IMemoryOwner : IMemoryOwner_GenericClasses

IMemoryOwner_1_T = typing.TypeVar('IMemoryOwner_1_T')
class IMemoryOwner_1(typing.Generic[IMemoryOwner_1_T], IDisposable, typing.Protocol):
    @property
    def Memory(self) -> Memory_1[IMemoryOwner_1_T]: ...


class IPinnable(typing.Protocol):
    @abc.abstractmethod
    def Pin(self, elementIndex: int) -> MemoryHandle: ...
    @abc.abstractmethod
    def Unpin(self) -> None: ...


class MemoryHandle(IDisposable):
    def __init__(self, pointer: clr.Reference[None], handle: GCHandle = ..., pinnable: IPinnable = ...) -> None: ...
    @property
    def Pointer(self) -> clr.Reference[None]: ...
    def Dispose(self) -> None: ...


class MemoryManager_GenericClasses(abc.ABCMeta):
    Generic_MemoryManager_GenericClasses_MemoryManager_1_T = typing.TypeVar('Generic_MemoryManager_GenericClasses_MemoryManager_1_T')
    def __getitem__(self, types : typing.Type[Generic_MemoryManager_GenericClasses_MemoryManager_1_T]) -> typing.Type[MemoryManager_1[Generic_MemoryManager_GenericClasses_MemoryManager_1_T]]: ...

MemoryManager : MemoryManager_GenericClasses

MemoryManager_1_T = typing.TypeVar('MemoryManager_1_T')
class MemoryManager_1(typing.Generic[MemoryManager_1_T], IMemoryOwner_1[MemoryManager_1_T], IPinnable, abc.ABC):
    @property
    def Memory(self) -> Memory_1[MemoryManager_1_T]: ...
    @abc.abstractmethod
    def GetSpan(self) -> Span_1[MemoryManager_1_T]: ...
    @abc.abstractmethod
    def Pin(self, elementIndex: int = ...) -> MemoryHandle: ...
    @abc.abstractmethod
    def Unpin(self) -> None: ...


class OperationStatus(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Done : OperationStatus # 0
    DestinationTooSmall : OperationStatus # 1
    NeedMoreData : OperationStatus # 2
    InvalidData : OperationStatus # 3


class ReadOnlySpanAction_GenericClasses(abc.ABCMeta):
    Generic_ReadOnlySpanAction_GenericClasses_ReadOnlySpanAction_2_T = typing.TypeVar('Generic_ReadOnlySpanAction_GenericClasses_ReadOnlySpanAction_2_T')
    Generic_ReadOnlySpanAction_GenericClasses_ReadOnlySpanAction_2_TArg = typing.TypeVar('Generic_ReadOnlySpanAction_GenericClasses_ReadOnlySpanAction_2_TArg')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ReadOnlySpanAction_GenericClasses_ReadOnlySpanAction_2_T], typing.Type[Generic_ReadOnlySpanAction_GenericClasses_ReadOnlySpanAction_2_TArg]]) -> typing.Type[ReadOnlySpanAction_2[Generic_ReadOnlySpanAction_GenericClasses_ReadOnlySpanAction_2_T, Generic_ReadOnlySpanAction_GenericClasses_ReadOnlySpanAction_2_TArg]]: ...

ReadOnlySpanAction : ReadOnlySpanAction_GenericClasses

ReadOnlySpanAction_2_T = typing.TypeVar('ReadOnlySpanAction_2_T')
ReadOnlySpanAction_2_TArg = typing.TypeVar('ReadOnlySpanAction_2_TArg', contravariant=True)
class ReadOnlySpanAction_2(typing.Generic[ReadOnlySpanAction_2_T, ReadOnlySpanAction_2_TArg], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, span: ReadOnlySpan_1[ReadOnlySpanAction_2_T], arg: ReadOnlySpanAction_2_TArg, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, span: ReadOnlySpan_1[ReadOnlySpanAction_2_T], arg: ReadOnlySpanAction_2_TArg) -> None: ...


class SpanAction_GenericClasses(abc.ABCMeta):
    Generic_SpanAction_GenericClasses_SpanAction_2_T = typing.TypeVar('Generic_SpanAction_GenericClasses_SpanAction_2_T')
    Generic_SpanAction_GenericClasses_SpanAction_2_TArg = typing.TypeVar('Generic_SpanAction_GenericClasses_SpanAction_2_TArg')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_SpanAction_GenericClasses_SpanAction_2_T], typing.Type[Generic_SpanAction_GenericClasses_SpanAction_2_TArg]]) -> typing.Type[SpanAction_2[Generic_SpanAction_GenericClasses_SpanAction_2_T, Generic_SpanAction_GenericClasses_SpanAction_2_TArg]]: ...

SpanAction : SpanAction_GenericClasses

SpanAction_2_T = typing.TypeVar('SpanAction_2_T')
SpanAction_2_TArg = typing.TypeVar('SpanAction_2_TArg', contravariant=True)
class SpanAction_2(typing.Generic[SpanAction_2_T, SpanAction_2_TArg], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, span: Span_1[SpanAction_2_T], arg: SpanAction_2_TArg, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, span: Span_1[SpanAction_2_T], arg: SpanAction_2_TArg) -> None: ...


class StandardFormat(IEquatable_1[StandardFormat]):
    def __init__(self, symbol: str, precision: int = ...) -> None: ...
    MaxPrecision : int
    NoPrecision : int
    @property
    def HasPrecision(self) -> bool: ...
    @property
    def IsDefault(self) -> bool: ...
    @property
    def Precision(self) -> int: ...
    @property
    def Symbol(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: StandardFormat, right: StandardFormat) -> bool: ...
    # Operator not supported op_Implicit(symbol: Char)
    def __ne__(self, left: StandardFormat, right: StandardFormat) -> bool: ...
    def ToString(self) -> str: ...
    @staticmethod
    def TryParse(format: ReadOnlySpan_1[str], result: clr.Reference[StandardFormat]) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: StandardFormat) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, format: ReadOnlySpan_1[str]) -> StandardFormat:...
        @typing.overload
        def __call__(self, format: str) -> StandardFormat:...

