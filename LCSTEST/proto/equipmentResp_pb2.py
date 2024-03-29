# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipmentResp.proto

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
import gameUserEquipment_pb2 as gameUserEquipment__pb2
import gameTeamInfo_pb2 as gameTeamInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='equipmentResp.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x13\x65quipmentResp.proto\x1a\x18gamePlayerInstance.proto\x1a\x17gameUserEquipment.proto\x1a\x12gameTeamInfo.proto\"\xcc\x01\n\x0f\x45quipmentRespVo\x12\'\n\x0b\x65quipRespVo\x18\x01 \x01(\x0b\x32\x12.GameUserEquipment\x12)\n\x12gameTeamInfoRespVo\x18\x02 \x01(\x0b\x32\r.GameTeamInfo\x12\x15\n\rremianPropNum\x18\x03 \x01(\x05\x12&\n\taPlayerId\x18\x04 \x01(\x0b\x32\x13.GamePlayerInstance\x12&\n\tbPlayerId\x18\x05 \x01(\x0b\x32\x13.GamePlayerInstance')
  ,
  dependencies=[gamePlayerInstance__pb2.DESCRIPTOR,gameUserEquipment__pb2.DESCRIPTOR,gameTeamInfo__pb2.DESCRIPTOR,])




_EQUIPMENTRESPVO = _descriptor.Descriptor(
  name='EquipmentRespVo',
  full_name='EquipmentRespVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipRespVo', full_name='EquipmentRespVo.equipRespVo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameTeamInfoRespVo', full_name='EquipmentRespVo.gameTeamInfoRespVo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remianPropNum', full_name='EquipmentRespVo.remianPropNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aPlayerId', full_name='EquipmentRespVo.aPlayerId', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bPlayerId', full_name='EquipmentRespVo.bPlayerId', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=95,
  serialized_end=299,
)

_EQUIPMENTRESPVO.fields_by_name['equipRespVo'].message_type = gameUserEquipment__pb2._GAMEUSEREQUIPMENT
_EQUIPMENTRESPVO.fields_by_name['gameTeamInfoRespVo'].message_type = gameTeamInfo__pb2._GAMETEAMINFO
_EQUIPMENTRESPVO.fields_by_name['aPlayerId'].message_type = gamePlayerInstance__pb2._GAMEPLAYERINSTANCE
_EQUIPMENTRESPVO.fields_by_name['bPlayerId'].message_type = gamePlayerInstance__pb2._GAMEPLAYERINSTANCE
DESCRIPTOR.message_types_by_name['EquipmentRespVo'] = _EQUIPMENTRESPVO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentRespVo = _reflection.GeneratedProtocolMessageType('EquipmentRespVo', (_message.Message,), dict(
  DESCRIPTOR = _EQUIPMENTRESPVO,
  __module__ = 'equipmentResp_pb2'
  # @@protoc_insertion_point(class_scope:EquipmentRespVo)
  ))
_sym_db.RegisterMessage(EquipmentRespVo)


# @@protoc_insertion_point(module_scope)
