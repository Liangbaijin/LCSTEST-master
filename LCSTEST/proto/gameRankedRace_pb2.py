# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gameRankedRace.proto

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
  name='gameRankedRace.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x14gameRankedRace.proto\"\xfa\x01\n\x0eGameRankedRace\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04rank\x18\x03 \x02(\x05\x12\x13\n\x0bhistoryRank\x18\x04 \x02(\x05\x12\r\n\x05score\x18\x05 \x02(\x05\x12\x13\n\x0b\x62\x65LikeCount\x18\x06 \x02(\x05\x12\x0e\n\x06zhanli\x18\x07 \x02(\x05\x12\x0c\n\x04name\x18\x08 \x02(\t\x12\x0b\n\x03vip\x18\t \x02(\x05\x12\x0c\n\x04\x63lub\x18\n \x01(\x05\x12\x11\n\trankedNum\x18\x0c \x01(\x05\x12\x15\n\rrankedEndTime\x18\r \x01(\x03\x12\x14\n\x0c\x62uyBattleNum\x18\x0e \x01(\x05\x12\x0c\n\x04icon\x18\x0f \x02(\x05\x12\r\n\x05level\x18\x10 \x02(\x05')
)




_GAMERANKEDRACE = _descriptor.Descriptor(
  name='GameRankedRace',
  full_name='GameRankedRace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='GameRankedRace.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='GameRankedRace.rank', index=1,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='historyRank', full_name='GameRankedRace.historyRank', index=2,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='GameRankedRace.score', index=3,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beLikeCount', full_name='GameRankedRace.beLikeCount', index=4,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zhanli', full_name='GameRankedRace.zhanli', index=5,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='GameRankedRace.name', index=6,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vip', full_name='GameRankedRace.vip', index=7,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='club', full_name='GameRankedRace.club', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rankedNum', full_name='GameRankedRace.rankedNum', index=9,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rankedEndTime', full_name='GameRankedRace.rankedEndTime', index=10,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buyBattleNum', full_name='GameRankedRace.buyBattleNum', index=11,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='GameRankedRace.icon', index=12,
      number=15, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='GameRankedRace.level', index=13,
      number=16, type=5, cpp_type=1, label=2,
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
  serialized_start=25,
  serialized_end=275,
)

DESCRIPTOR.message_types_by_name['GameRankedRace'] = _GAMERANKEDRACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameRankedRace = _reflection.GeneratedProtocolMessageType('GameRankedRace', (_message.Message,), dict(
  DESCRIPTOR = _GAMERANKEDRACE,
  __module__ = 'gameRankedRace_pb2'
  # @@protoc_insertion_point(class_scope:GameRankedRace)
  ))
_sym_db.RegisterMessage(GameRankedRace)


# @@protoc_insertion_point(module_scope)