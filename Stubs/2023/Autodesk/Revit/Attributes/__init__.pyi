import typing
from System import Attribute

class JournalingAttribute(Attribute):
    def __init__(self, mode: JournalingMode) -> None: ...
    @property
    def Mode(self) -> JournalingMode: ...
    @property
    def TypeId(self) -> typing.Any: ...


class JournalingMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    UsingCommandData : JournalingMode # 0
    NoCommandData : JournalingMode # 1


class RegenerationAttribute(Attribute):
    def __init__(self, option: RegenerationOption) -> None: ...
    @property
    def Option(self) -> RegenerationOption: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RegenerationOption(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Manual : RegenerationOption # 0


class TransactionAttribute(Attribute):
    def __init__(self, mode: TransactionMode) -> None: ...
    @property
    def Mode(self) -> TransactionMode: ...
    @property
    def TypeId(self) -> typing.Any: ...


class TransactionMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Manual : TransactionMode # 1
    ReadOnly : TransactionMode # 2

