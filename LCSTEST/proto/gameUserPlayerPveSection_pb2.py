# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gameUserPlayerPveSection.proto

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
  name='gameUserPlayerPveSection.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1egameUserPlayerPveSection.proto\"\x9a\x01\n\x18GameUserPlayerPveSection\x12\x0c\n\x04type\x18\n \x01(\x05\x12\x11\n\tsectionId\x18\x01 \x01(\x05\x12\x13\n\x0bsectionStar\x18\x02 \x01(\x05\x12\x12\n\npackage1Id\x18\x03 \x01(\x05\x12\x12\n\npackage2Id\x18\x04 \x01(\x05\x12\x12\n\npackage3Id\x18\x05 \x01(\x05\x12\x0c\n\x04over\x18\x0b \x01(\x05')
)




_GAMEUSERPLAYERPVESECTION = _descriptor.Descriptor(
  name='GameUserPlayerPveSection',
  full_name='GameUserPlayerPveSection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GameUserPlayerPveSection.type', index=0,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionId', full_name='GameUserPlayerPveSection.sectionId', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionStar', full_name='GameUserPlayerPveSection.sectionStar', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package1Id', full_name='GameUserPlayerPveSection.package1Id', index=3,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package2Id', full_name='GameUserPlayerPveSection.package2Id', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package3Id', full_name='GameUserPlayerPveSection.package3Id', index=5,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='over', full_name='GameUserPlayerPveSection.over', index=6,
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
  serialized_start=35,
  serialized_end=189,
)

DESCRIPTOR.message_types_by_name['GameUserPlayerPveSection'] = _GAMEUSERPLAYERPVESECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameUserPlayerPveSection = _reflection.GeneratedProtocolMessageType('GameUserPlayerPveSection', (_message.Message,), dict(
  DESCRIPTOR = _GAMEUSERPLAYERPVESECTION,
  __module__ = 'gameUserPlayerPveSection_pb2'
  # @@protoc_insertion_point(class_scope:GameUserPlayerPveSection)
  ))
_sym_db.RegisterMessage(GameUserPlayerPveSection)


# @@protoc_insertion_point(module_scope)
