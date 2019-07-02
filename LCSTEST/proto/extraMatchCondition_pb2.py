# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: extraMatchCondition.proto

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
  name='extraMatchCondition.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x19\x65xtraMatchCondition.proto\"\x9c\x02\n\x13\x45xtraMatchCondition\x12\x15\n\rneedExtraTime\x18\x01 \x02(\x05\x12\x1b\n\x13needPenaltyShootOut\x18\x02 \x02(\x05\x12\x1a\n\x12homeGoalDifference\x18\x03 \x02(\x05\x12\x14\n\x0chomeGoalsNum\x18\x04 \x02(\x05\x12\x1e\n\x13\x65xtraNonEmptyRounds\x18\x05 \x02(\x05:\x01\x30\x12\x13\n\x08needCard\x18\x06 \x02(\x05:\x01\x30\x12\x1b\n\x10needSevereInjure\x18\x07 \x02(\x05:\x01\x30\x12&\n\x1bneedAutoFreeFormationChange\x18\x08 \x02(\x05:\x01\x30\x12%\n\x17injureChanceCoefficient\x18\t \x01(\x02:\x04\x30.75')
)




_EXTRAMATCHCONDITION = _descriptor.Descriptor(
  name='ExtraMatchCondition',
  full_name='ExtraMatchCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='needExtraTime', full_name='ExtraMatchCondition.needExtraTime', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needPenaltyShootOut', full_name='ExtraMatchCondition.needPenaltyShootOut', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homeGoalDifference', full_name='ExtraMatchCondition.homeGoalDifference', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homeGoalsNum', full_name='ExtraMatchCondition.homeGoalsNum', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraNonEmptyRounds', full_name='ExtraMatchCondition.extraNonEmptyRounds', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needCard', full_name='ExtraMatchCondition.needCard', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needSevereInjure', full_name='ExtraMatchCondition.needSevereInjure', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needAutoFreeFormationChange', full_name='ExtraMatchCondition.needAutoFreeFormationChange', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='injureChanceCoefficient', full_name='ExtraMatchCondition.injureChanceCoefficient', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.75),
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
  serialized_start=30,
  serialized_end=314,
)

DESCRIPTOR.message_types_by_name['ExtraMatchCondition'] = _EXTRAMATCHCONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtraMatchCondition = _reflection.GeneratedProtocolMessageType('ExtraMatchCondition', (_message.Message,), dict(
  DESCRIPTOR = _EXTRAMATCHCONDITION,
  __module__ = 'extraMatchCondition_pb2'
  # @@protoc_insertion_point(class_scope:ExtraMatchCondition)
  ))
_sym_db.RegisterMessage(ExtraMatchCondition)


# @@protoc_insertion_point(module_scope)