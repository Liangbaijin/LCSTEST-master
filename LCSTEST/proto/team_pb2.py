# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: team.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import teamFormation_pb2 as teamFormation__pb2
import teamTactics_pb2 as teamTactics__pb2
import teamKeyPlayer_pb2 as teamKeyPlayer__pb2
import teamMemberInfo_pb2 as teamMemberInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='team.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nteam.proto\x1a\x13teamFormation.proto\x1a\x11teamTactics.proto\x1a\x13teamKeyPlayer.proto\x1a\x14teamMemberInfo.proto\"\xd8\x01\n\x04Team\x12\x16\n\x07isRobot\x18\x01 \x01(\x08:\x05\x66\x61lse\x12%\n\rteamFormation\x18\x02 \x01(\x0b\x32\x0e.TeamFormation\x12\x1f\n\nteamMember\x18\x03 \x03(\x0b\x32\x0b.TeamMember\x12\x17\n\x0foriginalTactics\x18\x04 \x02(\t\x12\x1d\n\x07tactics\x18\x05 \x03(\x0b\x32\x0c.TeamTactics\x12\"\n\nkeyPlayers\x18\x06 \x03(\x0b\x32\x0e.TeamKeyPlayer\x12\x14\n\x0cteamCapacity\x18\x07 \x01(\x01')
  ,
  dependencies=[teamFormation__pb2.DESCRIPTOR,teamTactics__pb2.DESCRIPTOR,teamKeyPlayer__pb2.DESCRIPTOR,teamMemberInfo__pb2.DESCRIPTOR,])




_TEAM = _descriptor.Descriptor(
  name='Team',
  full_name='Team',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isRobot', full_name='Team.isRobot', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='teamFormation', full_name='Team.teamFormation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='teamMember', full_name='Team.teamMember', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='originalTactics', full_name='Team.originalTactics', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tactics', full_name='Team.tactics', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyPlayers', full_name='Team.keyPlayers', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='teamCapacity', full_name='Team.teamCapacity', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=98,
  serialized_end=314,
)

_TEAM.fields_by_name['teamFormation'].message_type = teamFormation__pb2._TEAMFORMATION
_TEAM.fields_by_name['teamMember'].message_type = teamMemberInfo__pb2._TEAMMEMBER
_TEAM.fields_by_name['tactics'].message_type = teamTactics__pb2._TEAMTACTICS
_TEAM.fields_by_name['keyPlayers'].message_type = teamKeyPlayer__pb2._TEAMKEYPLAYER
DESCRIPTOR.message_types_by_name['Team'] = _TEAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Team = _reflection.GeneratedProtocolMessageType('Team', (_message.Message,), dict(
  DESCRIPTOR = _TEAM,
  __module__ = 'team_pb2'
  # @@protoc_insertion_point(class_scope:Team)
  ))
_sym_db.RegisterMessage(Team)


# @@protoc_insertion_point(module_scope)
