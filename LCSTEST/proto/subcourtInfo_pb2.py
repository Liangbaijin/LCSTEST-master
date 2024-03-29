# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subcourtInfo.proto

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
  name='subcourtInfo.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x12subcourtInfo.proto\"\xb7\x01\n\x0cSubcourtInfo\x12\x14\n\x0csubcourtType\x18\x01 \x02(\x05\x12\x0f\n\x07\x65ndTime\x18\x02 \x02(\t\x12\x12\n\nremainTime\x18\x03 \x02(\x05\x12\x13\n\x0b\x63omPlayerId\x18\x04 \x01(\x05\x12\x13\n\x0bleftStaffId\x18\x05 \x01(\x05\x12\x14\n\x0crightStaffId\x18\x06 \x01(\x05\x12\n\n\x02\x63\x64\x18\x07 \x02(\x05\x12\x0f\n\x07statusA\x18\x08 \x01(\x05\x12\x0f\n\x07statusB\x18\t \x01(\x05')
)




_SUBCOURTINFO = _descriptor.Descriptor(
  name='SubcourtInfo',
  full_name='SubcourtInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subcourtType', full_name='SubcourtInfo.subcourtType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='SubcourtInfo.endTime', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remainTime', full_name='SubcourtInfo.remainTime', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comPlayerId', full_name='SubcourtInfo.comPlayerId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leftStaffId', full_name='SubcourtInfo.leftStaffId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rightStaffId', full_name='SubcourtInfo.rightStaffId', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cd', full_name='SubcourtInfo.cd', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statusA', full_name='SubcourtInfo.statusA', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statusB', full_name='SubcourtInfo.statusB', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=23,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['SubcourtInfo'] = _SUBCOURTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubcourtInfo = _reflection.GeneratedProtocolMessageType('SubcourtInfo', (_message.Message,), dict(
  DESCRIPTOR = _SUBCOURTINFO,
  __module__ = 'subcourtInfo_pb2'
  # @@protoc_insertion_point(class_scope:SubcourtInfo)
  ))
_sym_db.RegisterMessage(SubcourtInfo)


# @@protoc_insertion_point(module_scope)
