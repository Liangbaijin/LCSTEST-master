# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: teaminfoAndPropListResp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import propResp_pb2 as propResp__pb2
import gameTeamInfo_pb2 as gameTeamInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='teaminfoAndPropListResp.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1dteaminfoAndPropListResp.proto\x1a\x0epropResp.proto\x1a\x12gameTeamInfo.proto\"a\n\x19TeamInfoAndPropListRespVo\x12\x1f\n\npropRespVo\x18\x01 \x03(\x0b\x32\x0b.PropRespVo\x12#\n\x0cgameTeamInfo\x18\x02 \x01(\x0b\x32\r.GameTeamInfo')
  ,
  dependencies=[propResp__pb2.DESCRIPTOR,gameTeamInfo__pb2.DESCRIPTOR,])




_TEAMINFOANDPROPLISTRESPVO = _descriptor.Descriptor(
  name='TeamInfoAndPropListRespVo',
  full_name='TeamInfoAndPropListRespVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='propRespVo', full_name='TeamInfoAndPropListRespVo.propRespVo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameTeamInfo', full_name='TeamInfoAndPropListRespVo.gameTeamInfo', index=1,
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
  serialized_start=69,
  serialized_end=166,
)

_TEAMINFOANDPROPLISTRESPVO.fields_by_name['propRespVo'].message_type = propResp__pb2._PROPRESPVO
_TEAMINFOANDPROPLISTRESPVO.fields_by_name['gameTeamInfo'].message_type = gameTeamInfo__pb2._GAMETEAMINFO
DESCRIPTOR.message_types_by_name['TeamInfoAndPropListRespVo'] = _TEAMINFOANDPROPLISTRESPVO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TeamInfoAndPropListRespVo = _reflection.GeneratedProtocolMessageType('TeamInfoAndPropListRespVo', (_message.Message,), dict(
  DESCRIPTOR = _TEAMINFOANDPROPLISTRESPVO,
  __module__ = 'teaminfoAndPropListResp_pb2'
  # @@protoc_insertion_point(class_scope:TeamInfoAndPropListRespVo)
  ))
_sym_db.RegisterMessage(TeamInfoAndPropListRespVo)


# @@protoc_insertion_point(module_scope)
