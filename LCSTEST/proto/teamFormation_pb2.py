# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: teamFormation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import teamPlayerFormation_pb2 as teamPlayerFormation__pb2
import teamFormationGrid_pb2 as teamFormationGrid__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='teamFormation.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x13teamFormation.proto\x1a\x19teamPlayerFormation.proto\x1a\x17teamFormationGrid.proto\"i\n\rTeamFormation\x12-\n\x0fplayerFormation\x18\x01 \x02(\x0b\x32\x14.TeamPlayerFormation\x12)\n\rformationGrid\x18\x02 \x02(\x0b\x32\x12.TeamFormationGrid')
  ,
  dependencies=[teamPlayerFormation__pb2.DESCRIPTOR,teamFormationGrid__pb2.DESCRIPTOR,])




_TEAMFORMATION = _descriptor.Descriptor(
  name='TeamFormation',
  full_name='TeamFormation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerFormation', full_name='TeamFormation.playerFormation', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formationGrid', full_name='TeamFormation.formationGrid', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=75,
  serialized_end=180,
)

_TEAMFORMATION.fields_by_name['playerFormation'].message_type = teamPlayerFormation__pb2._TEAMPLAYERFORMATION
_TEAMFORMATION.fields_by_name['formationGrid'].message_type = teamFormationGrid__pb2._TEAMFORMATIONGRID
DESCRIPTOR.message_types_by_name['TeamFormation'] = _TEAMFORMATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TeamFormation = _reflection.GeneratedProtocolMessageType('TeamFormation', (_message.Message,), dict(
  DESCRIPTOR = _TEAMFORMATION,
  __module__ = 'teamFormation_pb2'
  # @@protoc_insertion_point(class_scope:TeamFormation)
  ))
_sym_db.RegisterMessage(TeamFormation)


# @@protoc_insertion_point(module_scope)