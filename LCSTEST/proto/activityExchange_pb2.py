# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: activityExchange.proto

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
  name='activityExchange.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x16\x61\x63tivityExchange.proto\"\x9b\x01\n\x10\x45xchangeActivity\x12\x12\n\nactivityId\x18\x01 \x02(\x05\x12\x15\n\ractivityTitle\x18\x02 \x02(\t\x12\x14\n\x0c\x61\x63tivityDesc\x18\x03 \x02(\t\x12\x11\n\tstartTime\x18\x04 \x02(\t\x12\x0f\n\x07\x65ndTime\x18\x05 \x02(\t\x12\"\n\x08products\x18\x06 \x03(\x0b\x32\x10.ExchangeProduct\"}\n\x0f\x45xchangeProduct\x12\x11\n\tproductId\x18\x01 \x02(\x05\x12\x13\n\x0bproductCost\x18\x02 \x02(\t\x12\x0f\n\x07product\x18\x03 \x02(\t\x12\x15\n\rexchangeCount\x18\x04 \x02(\x05\x12\x1a\n\x12totalExchangeCount\x18\x05 \x02(\x05')
)




_EXCHANGEACTIVITY = _descriptor.Descriptor(
  name='ExchangeActivity',
  full_name='ExchangeActivity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='ExchangeActivity.activityId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activityTitle', full_name='ExchangeActivity.activityTitle', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activityDesc', full_name='ExchangeActivity.activityDesc', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='ExchangeActivity.startTime', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='ExchangeActivity.endTime', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='products', full_name='ExchangeActivity.products', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=27,
  serialized_end=182,
)


_EXCHANGEPRODUCT = _descriptor.Descriptor(
  name='ExchangeProduct',
  full_name='ExchangeProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='productId', full_name='ExchangeProduct.productId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='productCost', full_name='ExchangeProduct.productCost', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='ExchangeProduct.product', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchangeCount', full_name='ExchangeProduct.exchangeCount', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalExchangeCount', full_name='ExchangeProduct.totalExchangeCount', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=184,
  serialized_end=309,
)

_EXCHANGEACTIVITY.fields_by_name['products'].message_type = _EXCHANGEPRODUCT
DESCRIPTOR.message_types_by_name['ExchangeActivity'] = _EXCHANGEACTIVITY
DESCRIPTOR.message_types_by_name['ExchangeProduct'] = _EXCHANGEPRODUCT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExchangeActivity = _reflection.GeneratedProtocolMessageType('ExchangeActivity', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEACTIVITY,
  __module__ = 'activityExchange_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeActivity)
  ))
_sym_db.RegisterMessage(ExchangeActivity)

ExchangeProduct = _reflection.GeneratedProtocolMessageType('ExchangeProduct', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEPRODUCT,
  __module__ = 'activityExchange_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeProduct)
  ))
_sym_db.RegisterMessage(ExchangeProduct)


# @@protoc_insertion_point(module_scope)
