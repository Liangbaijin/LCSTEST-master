# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playerAndPropertyResp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gamePlayerInstance_pb2 as gamePlayerInstance__pb2
import gameProperty_pb2 as gameProperty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='playerAndPropertyResp.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1bplayerAndPropertyResp.proto\x1a\x18gamePlayerInstance.proto\x1a\x12gameProperty.proto\"a\n\x17PlayerAndPropertyRespVo\x12)\n\x0cplayerRespVo\x18\x01 \x01(\x0b\x32\x13.GamePlayerInstance\x12\x1b\n\x04list\x18\x02 \x03(\x0b\x32\r.GameProperty')
  ,
  dependencies=[gamePlayerInstance__pb2.DESCRIPTOR,gameProperty__pb2.DESCRIPTOR,])




_PLAYERANDPROPERTYRESPVO = _descriptor.Descriptor(
  name='PlayerAndPropertyRespVo',
  full_name='PlayerAndPropertyRespVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerRespVo', full_name='PlayerAndPropertyRespVo.playerRespVo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='PlayerAndPropertyRespVo.list', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=77,
  serialized_end=174,
)

_PLAYERANDPROPERTYRESPVO.fields_by_name['playerRespVo'].message_type = gamePlayerInstance__pb2._GAMEPLAYERINSTANCE
_PLAYERANDPROPERTYRESPVO.fields_by_name['list'].message_type = gameProperty__pb2._GAMEPROPERTY
DESCRIPTOR.message_types_by_name['PlayerAndPropertyRespVo'] = _PLAYERANDPROPERTYRESPVO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerAndPropertyRespVo = _reflection.GeneratedProtocolMessageType('PlayerAndPropertyRespVo', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERANDPROPERTYRESPVO,
  __module__ = 'playerAndPropertyResp_pb2'
  # @@protoc_insertion_point(class_scope:PlayerAndPropertyRespVo)
  ))
_sym_db.RegisterMessage(PlayerAndPropertyRespVo)


# @@protoc_insertion_point(module_scope)
