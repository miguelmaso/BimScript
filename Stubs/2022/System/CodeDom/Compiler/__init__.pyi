import typing
from System import Attribute, IFormatProvider, Array_1, ReadOnlyMemory_1
from System.IO import TextWriter
from System.Text import Encoding, StringBuilder
from System.Threading.Tasks import ValueTask, Task
from System.Threading import CancellationToken

class GeneratedCodeAttribute(Attribute):
    def __init__(self, tool: str, version: str) -> None: ...
    @property
    def Tool(self) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Version(self) -> str: ...


class IndentedTextWriter(TextWriter):
    @typing.overload
    def __init__(self, writer: TextWriter) -> None: ...
    @typing.overload
    def __init__(self, writer: TextWriter, tabString: str) -> None: ...
    DefaultTabString : str
    @property
    def Encoding(self) -> Encoding: ...
    @property
    def FormatProvider(self) -> IFormatProvider: ...
    @property
    def Indent(self) -> int: ...
    @Indent.setter
    def Indent(self, value: int) -> int: ...
    @property
    def InnerWriter(self) -> TextWriter: ...
    @property
    def NewLine(self) -> str: ...
    @NewLine.setter
    def NewLine(self, value: str) -> str: ...
    def Close(self) -> None: ...
    def DisposeAsync(self) -> ValueTask: ...
    def Flush(self) -> None: ...
    def FlushAsync(self) -> Task: ...
    def WriteLineNoTabs(self, s: str) -> None: ...
    def WriteLineNoTabsAsync(self, s: str) -> Task: ...
    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> None:...
        # Method Write(value : Single) was skipped since it collides with above method
        # Method Write(value : Int32) was skipped since it collides with above method
        # Method Write(value : Int64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, s: str) -> None:...
        # Method Write(value : Char) was skipped since it collides with above method
        @typing.overload
        def __call__(self, buffer: Array_1[str]) -> None:...
        # Method Write(value : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> None:...
        @typing.overload
        def __call__(self, format: str, arg: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any) -> None:...
        @typing.overload
        def __call__(self, buffer: Array_1[str], index: int, count: int) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any, arg1: typing.Any) -> None:...

    # Skipped WriteAsync due to it being static, abstract and generic.

    WriteAsync : WriteAsync_MethodGroup
    class WriteAsync_MethodGroup:
        @typing.overload
        def __call__(self, value: str) -> Task:...
        # Method WriteAsync(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, buffer: ReadOnlyMemory_1[str], cancellationToken: CancellationToken = ...) -> Task:...
        @typing.overload
        def __call__(self, value: StringBuilder, cancellationToken: CancellationToken = ...) -> Task:...
        @typing.overload
        def __call__(self, buffer: Array_1[str], index: int, count: int) -> Task:...

    # Skipped WriteLine due to it being static, abstract and generic.

    WriteLine : WriteLine_MethodGroup
    class WriteLine_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, value: float) -> None:...
        # Method WriteLine(value : Single) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: str) -> None:...
        # Method WriteLine(value : Int32) was skipped since it collides with above method
        # Method WriteLine(value : Int64) was skipped since it collides with above method
        # Method WriteLine(value : UInt32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, buffer: Array_1[str]) -> None:...
        # Method WriteLine(s : String) was skipped since it collides with above method
        # Method WriteLine(value : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: typing.Any) -> None:...
        @typing.overload
        def __call__(self, format: str, arg: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any) -> None:...
        @typing.overload
        def __call__(self, buffer: Array_1[str], index: int, count: int) -> None:...
        @typing.overload
        def __call__(self, format: str, arg0: typing.Any, arg1: typing.Any) -> None:...

    # Skipped WriteLineAsync due to it being static, abstract and generic.

    WriteLineAsync : WriteLineAsync_MethodGroup
    class WriteLineAsync_MethodGroup:
        @typing.overload
        def __call__(self) -> Task:...
        @typing.overload
        def __call__(self, value: str) -> Task:...
        # Method WriteLineAsync(value : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, buffer: ReadOnlyMemory_1[str], cancellationToken: CancellationToken = ...) -> Task:...
        @typing.overload
        def __call__(self, value: StringBuilder, cancellationToken: CancellationToken = ...) -> Task:...
        @typing.overload
        def __call__(self, buffer: Array_1[str], index: int, count: int) -> Task:...


