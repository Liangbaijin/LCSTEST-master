# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gameUserDaySignIn_pb2 as gameUserDaySignIn__pb2
import gameUserDaySignInPackage_pb2 as gameUserDaySignInPackage__pb2
import gameCommonDaySignIn_pb2 as gameCommonDaySignIn__pb2
import gameCommonDaySignInPackage_pb2 as gameCommonDaySignInPackage__pb2
import teaminfoAndPropListResp_pb2 as teaminfoAndPropListResp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='signin.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0csignin.proto\x1a\x17gameUserDaySignIn.proto\x1a\x1egameUserDaySignInPackage.proto\x1a\x19gameCommonDaySignIn.proto\x1a gameCommonDaySignInPackage.proto\x1a\x1dteaminfoAndPropListResp.proto\"\x19\n\x17\x43\x32GS_OpenSignInHomePage\"\xd8\x01\n\x17GS2C_OpenSignInHomePage\x12-\n\x11gameUserDaySignIn\x18\x01 \x01(\x0b\x32\x12.GameUserDaySignIn\x12\x31\n\x13gameCommonDaySignIn\x18\x03 \x03(\x0b\x32\x14.GameCommonDaySignIn\x12?\n\x1agameCommonDaySignInPackage\x18\x04 \x03(\x0b\x32\x1b.GameCommonDaySignInPackage\x12\x0b\n\x03num\x18\x05 \x01(\x05\x12\r\n\x05month\x18\x06 \x01(\x05\"\r\n\x0b\x43\x32GS_SignIn\"L\n\x0bGS2C_SignIn\x12=\n\x19teamInfoAndPropListRespVo\x18\x01 \x01(\x0b\x32\x1a.TeamInfoAndPropListRespVo\"\x10\n\x0e\x43\x32GS_AddSignIn\"O\n\x0eGS2C_AddSignIn\x12=\n\x19teamInfoAndPropListRespVo\x18\x01 \x01(\x0b\x32\x1a.TeamInfoAndPropListRespVo\"\x12\n\x10\x43\x32GS_AddUpSignIn\"Q\n\x10GS2C_AddUpSignIn\x12=\n\x19teamInfoAndPropListRespVo\x18\x01 \x01(\x0b\x32\x1a.TeamInfoAndPropListRespVo')
  ,
  dependencies=[gameUserDaySignIn__pb2.DESCRIPTOR,gameUserDaySignInPackage__pb2.DESCRIPTOR,gameCommonDaySignIn__pb2.DESCRIPTOR,gameCommonDaySignInPackage__pb2.DESCRIPTOR,teaminfoAndPropListResp__pb2.DESCRIPTOR,])




_C2GS_OPENSIGNINHOMEPAGE = _descriptor.Descriptor(
  name='C2GS_OpenSignInHomePage',
  full_name='C2GS_OpenSignInHomePage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=165,
  serialized_end=190,
)


_GS2C_OPENSIGNINHOMEPAGE = _descriptor.Descriptor(
  name='GS2C_OpenSignInHomePage',
  full_name='GS2C_OpenSignInHomePage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameUserDaySignIn', full_name='GS2C_OpenSignInHomePage.gameUserDaySignIn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameCommonDaySignIn', full_name='GS2C_OpenSignInHomePage.gameCommonDaySignIn', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameCommonDaySignInPackage', full_name='GS2C_OpenSignInHomePage.gameCommonDaySignInPackage', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='GS2C_OpenSignInHomePage.num', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='GS2C_OpenSignInHomePage.month', index=4,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=193,
  serialized_end=409,
)


_C2GS_SIGNIN = _descriptor.Descriptor(
  name='C2GS_SignIn',
  full_name='C2GS_SignIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=411,
  serialized_end=424,
)


_GS2C_SIGNIN = _descriptor.Descriptor(
  name='GS2C_SignIn',
  full_name='GS2C_SignIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamInfoAndPropListRespVo', full_name='GS2C_SignIn.teamInfoAndPropListRespVo', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=426,
  serialized_end=502,
)


_C2GS_ADDSIGNIN = _descriptor.Descriptor(
  name='C2GS_AddSignIn',
  full_name='C2GS_AddSignIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=504,
  serialized_end=520,
)


_GS2C_ADDSIGNIN = _descriptor.Descriptor(
  name='GS2C_AddSignIn',
  full_name='GS2C_AddSignIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamInfoAndPropListRespVo', full_name='GS2C_AddSignIn.teamInfoAndPropListRespVo', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=522,
  serialized_end=601,
)


_C2GS_ADDUPSIGNIN = _descriptor.Descriptor(
  name='C2GS_AddUpSignIn',
  full_name='C2GS_AddUpSignIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=603,
  serialized_end=621,
)


_GS2C_ADDUPSIGNIN = _descriptor.Descriptor(
  name='GS2C_AddUpSignIn',
  full_name='GS2C_AddUpSignIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamInfoAndPropListRespVo', full_name='GS2C_AddUpSignIn.teamInfoAndPropListRespVo', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=623,
  serialized_end=704,
)

_GS2C_OPENSIGNINHOMEPAGE.fields_by_name['gameUserDaySignIn'].message_type = gameUserDaySignIn__pb2._GAMEUSERDAYSIGNIN
_GS2C_OPENSIGNINHOMEPAGE.fields_by_name['gameCommonDaySignIn'].message_type = gameCommonDaySignIn__pb2._GAMECOMMONDAYSIGNIN
_GS2C_OPENSIGNINHOMEPAGE.fields_by_name['gameCommonDaySignInPackage'].message_type = gameCommonDaySignInPackage__pb2._GAMECOMMONDAYSIGNINPACKAGE
_GS2C_SIGNIN.fields_by_name['teamInfoAndPropListRespVo'].message_type = teaminfoAndPropListResp__pb2._TEAMINFOANDPROPLISTRESPVO
_GS2C_ADDSIGNIN.fields_by_name['teamInfoAndPropListRespVo'].message_type = teaminfoAndPropListResp__pb2._TEAMINFOANDPROPLISTRESPVO
_GS2C_ADDUPSIGNIN.fields_by_name['teamInfoAndPropListRespVo'].message_type = teaminfoAndPropListResp__pb2._TEAMINFOANDPROPLISTRESPVO
DESCRIPTOR.message_types_by_name['C2GS_OpenSignInHomePage'] = _C2GS_OPENSIGNINHOMEPAGE
DESCRIPTOR.message_types_by_name['GS2C_OpenSignInHomePage'] = _GS2C_OPENSIGNINHOMEPAGE
DESCRIPTOR.message_types_by_name['C2GS_SignIn'] = _C2GS_SIGNIN
DESCRIPTOR.message_types_by_name['GS2C_SignIn'] = _GS2C_SIGNIN
DESCRIPTOR.message_types_by_name['C2GS_AddSignIn'] = _C2GS_ADDSIGNIN
DESCRIPTOR.message_types_by_name['GS2C_AddSignIn'] = _GS2C_ADDSIGNIN
DESCRIPTOR.message_types_by_name['C2GS_AddUpSignIn'] = _C2GS_ADDUPSIGNIN
DESCRIPTOR.message_types_by_name['GS2C_AddUpSignIn'] = _GS2C_ADDUPSIGNIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2GS_OpenSignInHomePage = _reflection.GeneratedProtocolMessageType('C2GS_OpenSignInHomePage', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_OPENSIGNINHOMEPAGE,
  __module__ = 'signin_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_OpenSignInHomePage)
  ))
_sym_db.RegisterMessage(C2GS_OpenSignInHomePage)

GS2C_OpenSignInHomePage = _reflection.GeneratedProtocolMessageType('GS2C_OpenSignInHomePage', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_OPENSIGNINHOMEPAGE,
  __module__ = 'signin_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_OpenSignInHomePage)
  ))
_sym_db.RegisterMessage(GS2C_OpenSignInHomePage)

C2GS_SignIn = _reflection.GeneratedProtocolMessageType('C2GS_SignIn', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_SIGNIN,
  __module__ = 'signin_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_SignIn)
  ))
_sym_db.RegisterMessage(C2GS_SignIn)

GS2C_SignIn = _reflection.GeneratedProtocolMessageType('GS2C_SignIn', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_SIGNIN,
  __module__ = 'signin_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_SignIn)
  ))
_sym_db.RegisterMessage(GS2C_SignIn)

C2GS_AddSignIn = _reflection.GeneratedProtocolMessageType('C2GS_AddSignIn', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_ADDSIGNIN,
  __module__ = 'signin_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_AddSignIn)
  ))
_sym_db.RegisterMessage(C2GS_AddSignIn)

GS2C_AddSignIn = _reflection.GeneratedProtocolMessageType('GS2C_AddSignIn', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_ADDSIGNIN,
  __module__ = 'signin_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_AddSignIn)
  ))
_sym_db.RegisterMessage(GS2C_AddSignIn)

C2GS_AddUpSignIn = _reflection.GeneratedProtocolMessageType('C2GS_AddUpSignIn', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_ADDUPSIGNIN,
  __module__ = 'signin_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_AddUpSignIn)
  ))
_sym_db.RegisterMessage(C2GS_AddUpSignIn)

GS2C_AddUpSignIn = _reflection.GeneratedProtocolMessageType('GS2C_AddUpSignIn', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_ADDUPSIGNIN,
  __module__ = 'signin_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_AddUpSignIn)
  ))
_sym_db.RegisterMessage(GS2C_AddUpSignIn)


# @@protoc_insertion_point(module_scope)
