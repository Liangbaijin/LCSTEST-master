# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: activityPackage.proto

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
  name='activityPackage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x15\x61\x63tivityPackage.proto\"N\n\x0f\x41\x63tivityPackage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\tpackageId\x18\x02 \x02(\x05\x12\x0c\n\x04\x64\x61ys\x18\x03 \x02(\x05\x12\x0e\n\x06status\x18\x04 \x02(\x05')
)




_ACTIVITYPACKAGE = _descriptor.Descriptor(
  name='ActivityPackage',
  full_name='ActivityPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ActivityPackage.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='ActivityPackage.packageId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='days', full_name='ActivityPackage.days', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ActivityPackage.status', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['ActivityPackage'] = _ACTIVITYPACKAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActivityPackage = _reflection.GeneratedProtocolMessageType('ActivityPackage', (_message.Message,), dict(
  DESCRIPTOR = _ACTIVITYPACKAGE,
  __module__ = 'activityPackage_pb2'
  # @@protoc_insertion_point(class_scope:ActivityPackage)
  ))
_sym_db.RegisterMessage(ActivityPackage)


# @@protoc_insertion_point(module_scope)
