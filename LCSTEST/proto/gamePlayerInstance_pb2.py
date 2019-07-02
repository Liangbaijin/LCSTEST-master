# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gamePlayerInstance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import playerZhanli_pb2 as playerZhanli__pb2
import gamePlayerInstanceBase_pb2 as gamePlayerInstanceBase__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gamePlayerInstance.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x18gamePlayerInstance.proto\x1a\x12playerZhanli.proto\x1a\x1cgamePlayerInstanceBase.proto\"\x84\x01\n\x12GamePlayerInstance\x12)\n\x08instance\x18\x01 \x01(\x0b\x32\x17.GamePlayerInstanceBase\x12\x1b\n\x04\x61ttr\x18\x02 \x01(\x0b\x32\r.PlayerZhanli\x12\x0e\n\x06zhanli\x18\x03 \x02(\x05\x12\x16\n\x0epositionSeries\x18\x04 \x02(\x05')
  ,
  dependencies=[playerZhanli__pb2.DESCRIPTOR,gamePlayerInstanceBase__pb2.DESCRIPTOR,])




_GAMEPLAYERINSTANCE = _descriptor.Descriptor(
  name='GamePlayerInstance',
  full_name='GamePlayerInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='GamePlayerInstance.instance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr', full_name='GamePlayerInstance.attr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zhanli', full_name='GamePlayerInstance.zhanli', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positionSeries', full_name='GamePlayerInstance.positionSeries', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=79,
  serialized_end=211,
)

_GAMEPLAYERINSTANCE.fields_by_name['instance'].message_type = gamePlayerInstanceBase__pb2._GAMEPLAYERINSTANCEBASE
_GAMEPLAYERINSTANCE.fields_by_name['attr'].message_type = playerZhanli__pb2._PLAYERZHANLI
DESCRIPTOR.message_types_by_name['GamePlayerInstance'] = _GAMEPLAYERINSTANCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GamePlayerInstance = _reflection.GeneratedProtocolMessageType('GamePlayerInstance', (_message.Message,), dict(
  DESCRIPTOR = _GAMEPLAYERINSTANCE,
  __module__ = 'gamePlayerInstance_pb2'
  # @@protoc_insertion_point(class_scope:GamePlayerInstance)
  ))
_sym_db.RegisterMessage(GamePlayerInstance)


# @@protoc_insertion_point(module_scope)
