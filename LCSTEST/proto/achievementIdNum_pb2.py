# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: achievementIdNum.proto

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
  name='achievementIdNum.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x16\x61\x63hievementIdNum.proto\"6\n\x10\x41\x63hievementIdNum\x12\x15\n\rachievementId\x18\x01 \x02(\x05\x12\x0b\n\x03num\x18\x02 \x02(\x05')
)




_ACHIEVEMENTIDNUM = _descriptor.Descriptor(
  name='AchievementIdNum',
  full_name='AchievementIdNum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='achievementId', full_name='AchievementIdNum.achievementId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='AchievementIdNum.num', index=1,
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
  serialized_start=26,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['AchievementIdNum'] = _ACHIEVEMENTIDNUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AchievementIdNum = _reflection.GeneratedProtocolMessageType('AchievementIdNum', (_message.Message,), dict(
  DESCRIPTOR = _ACHIEVEMENTIDNUM,
  __module__ = 'achievementIdNum_pb2'
  # @@protoc_insertion_point(class_scope:AchievementIdNum)
  ))
_sym_db.RegisterMessage(AchievementIdNum)


# @@protoc_insertion_point(module_scope)
