# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gameMallDetail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gameMallGoods_pb2 as gameMallGoods__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gameMallDetail.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x14gameMallDetail.proto\x1a\x13gameMallGoods.proto\"\xd1\x01\n\x0eGameMallDetail\x12\x0e\n\x06mallId\x18\x01 \x02(\x05\x12\x10\n\x08mallType\x18\x02 \x02(\x05\x12%\n\rgameMallGoods\x18\x03 \x03(\x0b\x32\x0e.GameMallGoods\x12\x12\n\nrefreshNum\x18\x04 \x01(\x05\x12\x11\n\tcountDown\x18\x05 \x01(\x05\x12\x17\n\x0ftotalRefreshNum\x18\x06 \x01(\x05\x12\x15\n\raddUpCostType\x18\x07 \x01(\x05\x12\x0e\n\x06\x63ostId\x18\x08 \x01(\x05\x12\x0f\n\x07\x65ndTime\x18\t \x01(\x03')
  ,
  dependencies=[gameMallGoods__pb2.DESCRIPTOR,])




_GAMEMALLDETAIL = _descriptor.Descriptor(
  name='GameMallDetail',
  full_name='GameMallDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mallId', full_name='GameMallDetail.mallId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mallType', full_name='GameMallDetail.mallType', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameMallGoods', full_name='GameMallDetail.gameMallGoods', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refreshNum', full_name='GameMallDetail.refreshNum', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='countDown', full_name='GameMallDetail.countDown', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalRefreshNum', full_name='GameMallDetail.totalRefreshNum', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addUpCostType', full_name='GameMallDetail.addUpCostType', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='costId', full_name='GameMallDetail.costId', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='GameMallDetail.endTime', index=8,
      number=9, type=3, cpp_type=2, label=1,
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
  serialized_start=46,
  serialized_end=255,
)

_GAMEMALLDETAIL.fields_by_name['gameMallGoods'].message_type = gameMallGoods__pb2._GAMEMALLGOODS
DESCRIPTOR.message_types_by_name['GameMallDetail'] = _GAMEMALLDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameMallDetail = _reflection.GeneratedProtocolMessageType('GameMallDetail', (_message.Message,), dict(
  DESCRIPTOR = _GAMEMALLDETAIL,
  __module__ = 'gameMallDetail_pb2'
  # @@protoc_insertion_point(class_scope:GameMallDetail)
  ))
_sym_db.RegisterMessage(GameMallDetail)


# @@protoc_insertion_point(module_scope)
