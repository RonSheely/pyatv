# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class SetVolumeMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    volume: builtin___float = ...
    outputDeviceUID: typing___Text = ...

    def __init__(self,
        *,
        volume : typing___Optional[builtin___float] = None,
        outputDeviceUID : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"outputDeviceUID",b"outputDeviceUID",u"volume",b"volume"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"outputDeviceUID",b"outputDeviceUID",u"volume",b"volume"]) -> None: ...
type___SetVolumeMessage = SetVolumeMessage

setVolumeMessage: google___protobuf___descriptor___FieldDescriptor = ...