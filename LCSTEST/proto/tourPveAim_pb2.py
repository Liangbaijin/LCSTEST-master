# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tourPveAim.proto

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
  name='tourPveAim.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x10tourPveAim.proto\"6\n\nTourPveAim\x12\x0c\n\x04grid\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x0e\n\x06tourId\x18\x03 \x01(\x05')
)




_TOURPVEAIM = _descriptor.Descriptor(
  name='TourPveAim',
  full_name='TourPveAim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grid', full_name='TourPveAim.grid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='TourPveAim.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tourId', full_name='TourPveAim.tourId', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=20,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['TourPveAim'] = _TOURPVEAIM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TourPveAim = _reflection.GeneratedProtocolMessageType('TourPveAim', (_message.Message,), dict(
  DESCRIPTOR = _TOURPVEAIM,
  __module__ = 'tourPveAim_pb2'
  # @@protoc_insertion_point(class_scope:TourPveAim)
  ))
_sym_db.RegisterMessage(TourPveAim)


# @@protoc_insertion_point(module_scope)
