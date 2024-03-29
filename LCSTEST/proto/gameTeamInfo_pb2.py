# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gameTeamInfo.proto

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
  name='gameTeamInfo.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x12gameTeamInfo.proto\"\x96\x03\n\x0cGameTeamInfo\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08roleName\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x05\x12\x12\n\nexperience\x18\x04 \x01(\x05\x12\x0c\n\x04\x63oin\x18\x05 \x01(\x05\x12\x0f\n\x07\x64iamond\x18\x06 \x01(\x05\x12\x0c\n\x04tili\x18\x07 \x01(\x05\x12\x0c\n\x04\x63lub\x18\x08 \x01(\x05\x12\x0c\n\x04icon\x18\t \x01(\x05\x12\x15\n\rtiliReplyTime\x18\n \x01(\t\x12\x0b\n\x03vip\x18\x0b \x01(\x05\x12\x0e\n\x06vipExp\x18\x0c \x01(\x05\x12\x0b\n\x03uid\x18\x0e \x01(\t\x12\x0e\n\x06online\x18\x0f \x01(\x05\x12\x1a\n\x12homeFieldPoloShirt\x18\x15 \x01(\x05\x12\x1e\n\x16visitingFieldPoloShirt\x18\x16 \x01(\x05\x12\x14\n\x0ctiliBuyTimes\x18\x17 \x01(\x05\x12\x15\n\rfirstRecharge\x18\x18 \x01(\x05\x12\x0e\n\x06zhanli\x18\x19 \x01(\x05\x12\x11\n\tguideStep\x18\x1a \x01(\t\x12\x1b\n\x13playerNumLimitLevel\x18\x1b \x01(\x05')
)




_GAMETEAMINFO = _descriptor.Descriptor(
  name='GameTeamInfo',
  full_name='GameTeamInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='GameTeamInfo.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roleName', full_name='GameTeamInfo.roleName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='GameTeamInfo.level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experience', full_name='GameTeamInfo.experience', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coin', full_name='GameTeamInfo.coin', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diamond', full_name='GameTeamInfo.diamond', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tili', full_name='GameTeamInfo.tili', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='club', full_name='GameTeamInfo.club', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='GameTeamInfo.icon', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tiliReplyTime', full_name='GameTeamInfo.tiliReplyTime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vip', full_name='GameTeamInfo.vip', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vipExp', full_name='GameTeamInfo.vipExp', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='GameTeamInfo.uid', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='online', full_name='GameTeamInfo.online', index=13,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homeFieldPoloShirt', full_name='GameTeamInfo.homeFieldPoloShirt', index=14,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visitingFieldPoloShirt', full_name='GameTeamInfo.visitingFieldPoloShirt', index=15,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tiliBuyTimes', full_name='GameTeamInfo.tiliBuyTimes', index=16,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firstRecharge', full_name='GameTeamInfo.firstRecharge', index=17,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zhanli', full_name='GameTeamInfo.zhanli', index=18,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guideStep', full_name='GameTeamInfo.guideStep', index=19,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playerNumLimitLevel', full_name='GameTeamInfo.playerNumLimitLevel', index=20,
      number=27, type=5, cpp_type=1, label=1,
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
  serialized_start=23,
  serialized_end=429,
)

DESCRIPTOR.message_types_by_name['GameTeamInfo'] = _GAMETEAMINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameTeamInfo = _reflection.GeneratedProtocolMessageType('GameTeamInfo', (_message.Message,), dict(
  DESCRIPTOR = _GAMETEAMINFO,
  __module__ = 'gameTeamInfo_pb2'
  # @@protoc_insertion_point(class_scope:GameTeamInfo)
  ))
_sym_db.RegisterMessage(GameTeamInfo)


# @@protoc_insertion_point(module_scope)
