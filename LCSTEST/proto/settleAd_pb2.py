# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: settleAd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gameUserAdvertMedia_pb2 as gameUserAdvertMedia__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='settleAd.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0esettleAd.proto\x1a\x19gameUserAdvertMedia.proto\"M\n\x08SettleAd\x12\x0e\n\x06result\x18\x01 \x02(\x05\x12\x31\n\x13gameUserAdvertMedia\x18\x02 \x01(\x0b\x32\x14.GameUserAdvertMedia')
  ,
  dependencies=[gameUserAdvertMedia__pb2.DESCRIPTOR,])




_SETTLEAD = _descriptor.Descriptor(
  name='SettleAd',
  full_name='SettleAd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SettleAd.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameUserAdvertMedia', full_name='SettleAd.gameUserAdvertMedia', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=45,
  serialized_end=122,
)

_SETTLEAD.fields_by_name['gameUserAdvertMedia'].message_type = gameUserAdvertMedia__pb2._GAMEUSERADVERTMEDIA
DESCRIPTOR.message_types_by_name['SettleAd'] = _SETTLEAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SettleAd = _reflection.GeneratedProtocolMessageType('SettleAd', (_message.Message,), dict(
  DESCRIPTOR = _SETTLEAD,
  __module__ = 'settleAd_pb2'
  # @@protoc_insertion_point(class_scope:SettleAd)
  ))
_sym_db.RegisterMessage(SettleAd)


# @@protoc_insertion_point(module_scope)
