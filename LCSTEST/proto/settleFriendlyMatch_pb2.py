# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: settleFriendlyMatch.proto

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
  name='settleFriendlyMatch.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x19settleFriendlyMatch.proto\"%\n\x13SettleFriendlyMatch\x12\x0e\n\x06result\x18\x01 \x02(\x05')
)




_SETTLEFRIENDLYMATCH = _descriptor.Descriptor(
  name='SettleFriendlyMatch',
  full_name='SettleFriendlyMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SettleFriendlyMatch.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=29,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['SettleFriendlyMatch'] = _SETTLEFRIENDLYMATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SettleFriendlyMatch = _reflection.GeneratedProtocolMessageType('SettleFriendlyMatch', (_message.Message,), dict(
  DESCRIPTOR = _SETTLEFRIENDLYMATCH,
  __module__ = 'settleFriendlyMatch_pb2'
  # @@protoc_insertion_point(class_scope:SettleFriendlyMatch)
  ))
_sym_db.RegisterMessage(SettleFriendlyMatch)


# @@protoc_insertion_point(module_scope)
