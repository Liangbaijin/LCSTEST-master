# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: matchAim.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import playerPveAim_pb2 as playerPveAim__pb2
import tourPveAim_pb2 as tourPveAim__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='matchAim.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0ematchAim.proto\x1a\x12playerPveAim.proto\x1a\x10tourPveAim.proto\"i\n\x08MatchAim\x12#\n\x0cplayerPveAim\x18\x01 \x01(\x0b\x32\r.PlayerPveAim\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x0b\n\x03uid\x18\x03 \x01(\t\x12\x1f\n\ntourPveAim\x18\x04 \x01(\x0b\x32\x0b.TourPveAim')
  ,
  dependencies=[playerPveAim__pb2.DESCRIPTOR,tourPveAim__pb2.DESCRIPTOR,])




_MATCHAIM = _descriptor.Descriptor(
  name='MatchAim',
  full_name='MatchAim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerPveAim', full_name='MatchAim.playerPveAim', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='MatchAim.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='MatchAim.uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tourPveAim', full_name='MatchAim.tourPveAim', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=56,
  serialized_end=161,
)

_MATCHAIM.fields_by_name['playerPveAim'].message_type = playerPveAim__pb2._PLAYERPVEAIM
_MATCHAIM.fields_by_name['tourPveAim'].message_type = tourPveAim__pb2._TOURPVEAIM
DESCRIPTOR.message_types_by_name['MatchAim'] = _MATCHAIM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchAim = _reflection.GeneratedProtocolMessageType('MatchAim', (_message.Message,), dict(
  DESCRIPTOR = _MATCHAIM,
  __module__ = 'matchAim_pb2'
  # @@protoc_insertion_point(class_scope:MatchAim)
  ))
_sym_db.RegisterMessage(MatchAim)


# @@protoc_insertion_point(module_scope)
