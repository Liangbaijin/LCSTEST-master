# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: guildMemberInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gameTeamInfo_pb2 as gameTeamInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='guildMemberInfo.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x15guildMemberInfo.proto\x1a\x12gameTeamInfo.proto\"\x90\x01\n\x0fGuildMemberInfo\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12#\n\x0cgameTeamInfo\x18\x02 \x02(\x0b\x32\r.GameTeamInfo\x12\x1a\n\x12weeklyContribution\x18\x03 \x01(\x05\x12\x19\n\x11totalContribution\x18\x04 \x01(\x05\x12\x11\n\tapplyTime\x18\x05 \x01(\t')
  ,
  dependencies=[gameTeamInfo__pb2.DESCRIPTOR,])




_GUILDMEMBERINFO = _descriptor.Descriptor(
  name='GuildMemberInfo',
  full_name='GuildMemberInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='GuildMemberInfo.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameTeamInfo', full_name='GuildMemberInfo.gameTeamInfo', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weeklyContribution', full_name='GuildMemberInfo.weeklyContribution', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalContribution', full_name='GuildMemberInfo.totalContribution', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='applyTime', full_name='GuildMemberInfo.applyTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=190,
)

_GUILDMEMBERINFO.fields_by_name['gameTeamInfo'].message_type = gameTeamInfo__pb2._GAMETEAMINFO
DESCRIPTOR.message_types_by_name['GuildMemberInfo'] = _GUILDMEMBERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GuildMemberInfo = _reflection.GeneratedProtocolMessageType('GuildMemberInfo', (_message.Message,), dict(
  DESCRIPTOR = _GUILDMEMBERINFO,
  __module__ = 'guildMemberInfo_pb2'
  # @@protoc_insertion_point(class_scope:GuildMemberInfo)
  ))
_sym_db.RegisterMessage(GuildMemberInfo)


# @@protoc_insertion_point(module_scope)
