# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: achieveSeriesProcess.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='achieveSeriesProcess.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1a\x61\x63hieveSeriesProcess.proto\"9\n\x14\x41\x63hieveSeriesProcess\x12\x10\n\x08seriesId\x18\x01 \x02(\x05\x12\x0f\n\x07process\x18\x02 \x02(\x05')
)




_ACHIEVESERIESPROCESS = _descriptor.Descriptor(
  name='AchieveSeriesProcess',
  full_name='AchieveSeriesProcess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seriesId', full_name='AchieveSeriesProcess.seriesId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process', full_name='AchieveSeriesProcess.process', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['AchieveSeriesProcess'] = _ACHIEVESERIESPROCESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AchieveSeriesProcess = _reflection.GeneratedProtocolMessageType('AchieveSeriesProcess', (_message.Message,), dict(
  DESCRIPTOR = _ACHIEVESERIESPROCESS,
  __module__ = 'achieveSeriesProcess_pb2'
  # @@protoc_insertion_point(class_scope:AchieveSeriesProcess)
  ))
_sym_db.RegisterMessage(AchieveSeriesProcess)


# @@protoc_insertion_point(module_scope)
