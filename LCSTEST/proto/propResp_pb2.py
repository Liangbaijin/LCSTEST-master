# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: propResp.proto

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
import gameUserDebris_pb2 as gameUserDebris__pb2
import gameUserEquipment_pb2 as gameUserEquipment__pb2
import gameProperty_pb2 as gameProperty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='propResp.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0epropResp.proto\x1a\x18gamePlayerInstance.proto\x1a\x14gameUserDebris.proto\x1a\x17gameUserEquipment.proto\x1a\x12gameProperty.proto\"\xa6\x02\n\nPropRespVo\x12\x0e\n\x06propId\x18\x01 \x01(\x05\x12\x10\n\x08propType\x18\x02 \x01(\x05\x12\x0f\n\x07propNum\x18\x03 \x01(\x05\x12/\n\x12gamePlayerInstance\x18\x04 \x01(\x0b\x32\x13.GamePlayerInstance\x12\'\n\x0egameUserDebris\x18\x05 \x01(\x0b\x32\x0f.GameUserDebris\x12-\n\x11gameUserEquipment\x18\x06 \x01(\x0b\x32\x12.GameUserEquipment\x12\x13\n\x0byingchaoNum\x18\x07 \x01(\x05\x12\x10\n\x08xijiaNum\x18\x08 \x01(\x05\x12\x10\n\x08yijiaNum\x18\t \x01(\x05\x12\x10\n\x08\x64\x65jiaNum\x18\n \x01(\x05\x12\x11\n\tshijieNum\x18\x0b \x01(\x05')
  ,
  dependencies=[gamePlayerInstance__pb2.DESCRIPTOR,gameUserDebris__pb2.DESCRIPTOR,gameUserEquipment__pb2.DESCRIPTOR,gameProperty__pb2.DESCRIPTOR,])




_PROPRESPVO = _descriptor.Descriptor(
  name='PropRespVo',
  full_name='PropRespVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='propId', full_name='PropRespVo.propId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='propType', full_name='PropRespVo.propType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='propNum', full_name='PropRespVo.propNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gamePlayerInstance', full_name='PropRespVo.gamePlayerInstance', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameUserDebris', full_name='PropRespVo.gameUserDebris', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameUserEquipment', full_name='PropRespVo.gameUserEquipment', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yingchaoNum', full_name='PropRespVo.yingchaoNum', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xijiaNum', full_name='PropRespVo.xijiaNum', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yijiaNum', full_name='PropRespVo.yijiaNum', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dejiaNum', full_name='PropRespVo.dejiaNum', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shijieNum', full_name='PropRespVo.shijieNum', index=10,
      number=11, type=5, cpp_type=1, label=1,
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
  serialized_start=112,
  serialized_end=406,
)

_PROPRESPVO.fields_by_name['gamePlayerInstance'].message_type = gamePlayerInstance__pb2._GAMEPLAYERINSTANCE
_PROPRESPVO.fields_by_name['gameUserDebris'].message_type = gameUserDebris__pb2._GAMEUSERDEBRIS
_PROPRESPVO.fields_by_name['gameUserEquipment'].message_type = gameUserEquipment__pb2._GAMEUSEREQUIPMENT
DESCRIPTOR.message_types_by_name['PropRespVo'] = _PROPRESPVO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PropRespVo = _reflection.GeneratedProtocolMessageType('PropRespVo', (_message.Message,), dict(
  DESCRIPTOR = _PROPRESPVO,
  __module__ = 'propResp_pb2'
  # @@protoc_insertion_point(class_scope:PropRespVo)
  ))
_sym_db.RegisterMessage(PropRespVo)


# @@protoc_insertion_point(module_scope)
