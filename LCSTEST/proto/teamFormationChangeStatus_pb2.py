# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: teamFormationChangeStatus.proto

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
  name='teamFormationChangeStatus.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1fteamFormationChangeStatus.proto\"o\n\x19TeamFormationChangeStatus\x12\x19\n\x11needLockFormation\x18\x01 \x02(\x05\x12\x1a\n\x12willOnPlayerIdList\x18\x02 \x03(\x05\x12\x1b\n\x13willOffPlayerIdList\x18\x03 \x03(\x05')
)




_TEAMFORMATIONCHANGESTATUS = _descriptor.Descriptor(
  name='TeamFormationChangeStatus',
  full_name='TeamFormationChangeStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='needLockFormation', full_name='TeamFormationChangeStatus.needLockFormation', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='willOnPlayerIdList', full_name='TeamFormationChangeStatus.willOnPlayerIdList', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='willOffPlayerIdList', full_name='TeamFormationChangeStatus.willOffPlayerIdList', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=35,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['TeamFormationChangeStatus'] = _TEAMFORMATIONCHANGESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TeamFormationChangeStatus = _reflection.GeneratedProtocolMessageType('TeamFormationChangeStatus', (_message.Message,), dict(
  DESCRIPTOR = _TEAMFORMATIONCHANGESTATUS,
  __module__ = 'teamFormationChangeStatus_pb2'
  # @@protoc_insertion_point(class_scope:TeamFormationChangeStatus)
  ))
_sym_db.RegisterMessage(TeamFormationChangeStatus)


# @@protoc_insertion_point(module_scope)