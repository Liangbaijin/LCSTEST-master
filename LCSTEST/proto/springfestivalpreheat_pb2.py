# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: springfestivalpreheat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gameTeamInfo_pb2 as gameTeamInfo__pb2
import gameProperty_pb2 as gameProperty__pb2
import propResp_pb2 as propResp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='springfestivalpreheat.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1bspringfestivalpreheat.proto\x1a\x12gameTeamInfo.proto\x1a\x12gameProperty.proto\x1a\x0epropResp.proto\"#\n!C2GS_GetSpringFestivalPreheatTask\"\x9c\x01\n!GS2C_GetSpringFestivalPreheatTask\x12\r\n\x05title\x18\x01 \x02(\t\x12\x12\n\nremainTime\x18\x02 \x02(\x05\x12\x16\n\x0eunlockTypeList\x18\x03 \x03(\x05\x12,\n\x08taskList\x18\x04 \x03(\x0b\x32\x1a.SpringFestivalPreheatTask\x12\x0e\n\x06mallId\x18\x05 \x02(\x05\"I\n\x19SpringFestivalPreheatTask\x12\x0e\n\x06taskId\x18\x01 \x02(\x05\x12\x0e\n\x06status\x18\x02 \x02(\x05\x12\x0c\n\x04\x64one\x18\x03 \x02(\x05\"%\n#C2GS_GetSpringFestivalPreheatPlayer\"\x84\x01\n#GS2C_GetSpringFestivalPreheatPlayer\x12\r\n\x05title\x18\x01 \x02(\t\x12\x12\n\nremainTime\x18\x02 \x02(\x05\x12\x16\n\x0eunlockRewardId\x18\x03 \x03(\x05\x12\r\n\x05stage\x18\x04 \x02(\x05\x12\x13\n\x0b\x62uyRewardId\x18\x05 \x03(\x05\"Q\n\x1f\x43\x32GS_SpringFestivalBlessCombine\x12\r\n\x05\x63loth\x18\x01 \x02(\x05\x12\r\n\x05shoes\x18\x02 \x02(\x05\x12\x10\n\x08trousers\x18\x03 \x02(\x05\"{\n\x1fGS2C_SpringFestivalBlessCombine\x12\x1f\n\npropRespVo\x18\x01 \x01(\x0b\x32\x0b.PropRespVo\x12\x12\n\nunlockType\x18\x02 \x01(\x05\x12#\n\x0cgameProperty\x18\x03 \x03(\x0b\x32\r.GameProperty\"1\n\x1f\x43\x32GS_CompleteSpringFestivalTask\x12\x0e\n\x06taskId\x18\x01 \x02(\x05\"g\n\x1fGS2C_CompleteSpringFestivalTask\x12\x1f\n\npropRespVo\x18\x01 \x03(\x0b\x32\x0b.PropRespVo\x12#\n\x0cgameTeamInfo\x18\x02 \x01(\x0b\x32\r.GameTeamInfo\"3\n\x1f\x43\x32GS_UnlockSpringFestivalPlayer\x12\x10\n\x08rewardId\x18\x01 \x02(\x05\"U\n\x1fGS2C_UnlockSpringFestivalPlayer\x12#\n\x0cgameProperty\x18\x01 \x03(\x0b\x32\r.GameProperty\x12\r\n\x05stage\x18\x02 \x01(\x05\"0\n\x1c\x43\x32GS_BuySpringFestivalPlayer\x12\x10\n\x08rewardId\x18\x01 \x02(\x05\"d\n\x1cGS2C_BuySpringFestivalPlayer\x12\x1f\n\npropRespVo\x18\x01 \x02(\x0b\x32\x0b.PropRespVo\x12#\n\x0cgameTeamInfo\x18\x02 \x01(\x0b\x32\r.GameTeamInfo\"!\n\x1f\x43\x32GS_SpringFestivalPreheatShare')
  ,
  dependencies=[gameTeamInfo__pb2.DESCRIPTOR,gameProperty__pb2.DESCRIPTOR,propResp__pb2.DESCRIPTOR,])




_C2GS_GETSPRINGFESTIVALPREHEATTASK = _descriptor.Descriptor(
  name='C2GS_GetSpringFestivalPreheatTask',
  full_name='C2GS_GetSpringFestivalPreheatTask',
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
  serialized_start=87,
  serialized_end=122,
)


_GS2C_GETSPRINGFESTIVALPREHEATTASK = _descriptor.Descriptor(
  name='GS2C_GetSpringFestivalPreheatTask',
  full_name='GS2C_GetSpringFestivalPreheatTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='GS2C_GetSpringFestivalPreheatTask.title', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remainTime', full_name='GS2C_GetSpringFestivalPreheatTask.remainTime', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlockTypeList', full_name='GS2C_GetSpringFestivalPreheatTask.unlockTypeList', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskList', full_name='GS2C_GetSpringFestivalPreheatTask.taskList', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mallId', full_name='GS2C_GetSpringFestivalPreheatTask.mallId', index=4,
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
  serialized_start=125,
  serialized_end=281,
)


_SPRINGFESTIVALPREHEATTASK = _descriptor.Descriptor(
  name='SpringFestivalPreheatTask',
  full_name='SpringFestivalPreheatTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='SpringFestivalPreheatTask.taskId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='SpringFestivalPreheatTask.status', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='done', full_name='SpringFestivalPreheatTask.done', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=283,
  serialized_end=356,
)


_C2GS_GETSPRINGFESTIVALPREHEATPLAYER = _descriptor.Descriptor(
  name='C2GS_GetSpringFestivalPreheatPlayer',
  full_name='C2GS_GetSpringFestivalPreheatPlayer',
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
  serialized_start=358,
  serialized_end=395,
)


_GS2C_GETSPRINGFESTIVALPREHEATPLAYER = _descriptor.Descriptor(
  name='GS2C_GetSpringFestivalPreheatPlayer',
  full_name='GS2C_GetSpringFestivalPreheatPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='GS2C_GetSpringFestivalPreheatPlayer.title', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remainTime', full_name='GS2C_GetSpringFestivalPreheatPlayer.remainTime', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlockRewardId', full_name='GS2C_GetSpringFestivalPreheatPlayer.unlockRewardId', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage', full_name='GS2C_GetSpringFestivalPreheatPlayer.stage', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buyRewardId', full_name='GS2C_GetSpringFestivalPreheatPlayer.buyRewardId', index=4,
      number=5, type=5, cpp_type=1, label=3,
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
  serialized_start=398,
  serialized_end=530,
)


_C2GS_SPRINGFESTIVALBLESSCOMBINE = _descriptor.Descriptor(
  name='C2GS_SpringFestivalBlessCombine',
  full_name='C2GS_SpringFestivalBlessCombine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloth', full_name='C2GS_SpringFestivalBlessCombine.cloth', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shoes', full_name='C2GS_SpringFestivalBlessCombine.shoes', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trousers', full_name='C2GS_SpringFestivalBlessCombine.trousers', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=532,
  serialized_end=613,
)


_GS2C_SPRINGFESTIVALBLESSCOMBINE = _descriptor.Descriptor(
  name='GS2C_SpringFestivalBlessCombine',
  full_name='GS2C_SpringFestivalBlessCombine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='propRespVo', full_name='GS2C_SpringFestivalBlessCombine.propRespVo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlockType', full_name='GS2C_SpringFestivalBlessCombine.unlockType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameProperty', full_name='GS2C_SpringFestivalBlessCombine.gameProperty', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=615,
  serialized_end=738,
)


_C2GS_COMPLETESPRINGFESTIVALTASK = _descriptor.Descriptor(
  name='C2GS_CompleteSpringFestivalTask',
  full_name='C2GS_CompleteSpringFestivalTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='C2GS_CompleteSpringFestivalTask.taskId', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=740,
  serialized_end=789,
)


_GS2C_COMPLETESPRINGFESTIVALTASK = _descriptor.Descriptor(
  name='GS2C_CompleteSpringFestivalTask',
  full_name='GS2C_CompleteSpringFestivalTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='propRespVo', full_name='GS2C_CompleteSpringFestivalTask.propRespVo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameTeamInfo', full_name='GS2C_CompleteSpringFestivalTask.gameTeamInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=791,
  serialized_end=894,
)


_C2GS_UNLOCKSPRINGFESTIVALPLAYER = _descriptor.Descriptor(
  name='C2GS_UnlockSpringFestivalPlayer',
  full_name='C2GS_UnlockSpringFestivalPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewardId', full_name='C2GS_UnlockSpringFestivalPlayer.rewardId', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=896,
  serialized_end=947,
)


_GS2C_UNLOCKSPRINGFESTIVALPLAYER = _descriptor.Descriptor(
  name='GS2C_UnlockSpringFestivalPlayer',
  full_name='GS2C_UnlockSpringFestivalPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameProperty', full_name='GS2C_UnlockSpringFestivalPlayer.gameProperty', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage', full_name='GS2C_UnlockSpringFestivalPlayer.stage', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=949,
  serialized_end=1034,
)


_C2GS_BUYSPRINGFESTIVALPLAYER = _descriptor.Descriptor(
  name='C2GS_BuySpringFestivalPlayer',
  full_name='C2GS_BuySpringFestivalPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewardId', full_name='C2GS_BuySpringFestivalPlayer.rewardId', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=1036,
  serialized_end=1084,
)


_GS2C_BUYSPRINGFESTIVALPLAYER = _descriptor.Descriptor(
  name='GS2C_BuySpringFestivalPlayer',
  full_name='GS2C_BuySpringFestivalPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='propRespVo', full_name='GS2C_BuySpringFestivalPlayer.propRespVo', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameTeamInfo', full_name='GS2C_BuySpringFestivalPlayer.gameTeamInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1086,
  serialized_end=1186,
)


_C2GS_SPRINGFESTIVALPREHEATSHARE = _descriptor.Descriptor(
  name='C2GS_SpringFestivalPreheatShare',
  full_name='C2GS_SpringFestivalPreheatShare',
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
  serialized_start=1188,
  serialized_end=1221,
)

_GS2C_GETSPRINGFESTIVALPREHEATTASK.fields_by_name['taskList'].message_type = _SPRINGFESTIVALPREHEATTASK
_GS2C_SPRINGFESTIVALBLESSCOMBINE.fields_by_name['propRespVo'].message_type = propResp__pb2._PROPRESPVO
_GS2C_SPRINGFESTIVALBLESSCOMBINE.fields_by_name['gameProperty'].message_type = gameProperty__pb2._GAMEPROPERTY
_GS2C_COMPLETESPRINGFESTIVALTASK.fields_by_name['propRespVo'].message_type = propResp__pb2._PROPRESPVO
_GS2C_COMPLETESPRINGFESTIVALTASK.fields_by_name['gameTeamInfo'].message_type = gameTeamInfo__pb2._GAMETEAMINFO
_GS2C_UNLOCKSPRINGFESTIVALPLAYER.fields_by_name['gameProperty'].message_type = gameProperty__pb2._GAMEPROPERTY
_GS2C_BUYSPRINGFESTIVALPLAYER.fields_by_name['propRespVo'].message_type = propResp__pb2._PROPRESPVO
_GS2C_BUYSPRINGFESTIVALPLAYER.fields_by_name['gameTeamInfo'].message_type = gameTeamInfo__pb2._GAMETEAMINFO
DESCRIPTOR.message_types_by_name['C2GS_GetSpringFestivalPreheatTask'] = _C2GS_GETSPRINGFESTIVALPREHEATTASK
DESCRIPTOR.message_types_by_name['GS2C_GetSpringFestivalPreheatTask'] = _GS2C_GETSPRINGFESTIVALPREHEATTASK
DESCRIPTOR.message_types_by_name['SpringFestivalPreheatTask'] = _SPRINGFESTIVALPREHEATTASK
DESCRIPTOR.message_types_by_name['C2GS_GetSpringFestivalPreheatPlayer'] = _C2GS_GETSPRINGFESTIVALPREHEATPLAYER
DESCRIPTOR.message_types_by_name['GS2C_GetSpringFestivalPreheatPlayer'] = _GS2C_GETSPRINGFESTIVALPREHEATPLAYER
DESCRIPTOR.message_types_by_name['C2GS_SpringFestivalBlessCombine'] = _C2GS_SPRINGFESTIVALBLESSCOMBINE
DESCRIPTOR.message_types_by_name['GS2C_SpringFestivalBlessCombine'] = _GS2C_SPRINGFESTIVALBLESSCOMBINE
DESCRIPTOR.message_types_by_name['C2GS_CompleteSpringFestivalTask'] = _C2GS_COMPLETESPRINGFESTIVALTASK
DESCRIPTOR.message_types_by_name['GS2C_CompleteSpringFestivalTask'] = _GS2C_COMPLETESPRINGFESTIVALTASK
DESCRIPTOR.message_types_by_name['C2GS_UnlockSpringFestivalPlayer'] = _C2GS_UNLOCKSPRINGFESTIVALPLAYER
DESCRIPTOR.message_types_by_name['GS2C_UnlockSpringFestivalPlayer'] = _GS2C_UNLOCKSPRINGFESTIVALPLAYER
DESCRIPTOR.message_types_by_name['C2GS_BuySpringFestivalPlayer'] = _C2GS_BUYSPRINGFESTIVALPLAYER
DESCRIPTOR.message_types_by_name['GS2C_BuySpringFestivalPlayer'] = _GS2C_BUYSPRINGFESTIVALPLAYER
DESCRIPTOR.message_types_by_name['C2GS_SpringFestivalPreheatShare'] = _C2GS_SPRINGFESTIVALPREHEATSHARE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2GS_GetSpringFestivalPreheatTask = _reflection.GeneratedProtocolMessageType('C2GS_GetSpringFestivalPreheatTask', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_GETSPRINGFESTIVALPREHEATTASK,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_GetSpringFestivalPreheatTask)
  ))
_sym_db.RegisterMessage(C2GS_GetSpringFestivalPreheatTask)

GS2C_GetSpringFestivalPreheatTask = _reflection.GeneratedProtocolMessageType('GS2C_GetSpringFestivalPreheatTask', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_GETSPRINGFESTIVALPREHEATTASK,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_GetSpringFestivalPreheatTask)
  ))
_sym_db.RegisterMessage(GS2C_GetSpringFestivalPreheatTask)

SpringFestivalPreheatTask = _reflection.GeneratedProtocolMessageType('SpringFestivalPreheatTask', (_message.Message,), dict(
  DESCRIPTOR = _SPRINGFESTIVALPREHEATTASK,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:SpringFestivalPreheatTask)
  ))
_sym_db.RegisterMessage(SpringFestivalPreheatTask)

C2GS_GetSpringFestivalPreheatPlayer = _reflection.GeneratedProtocolMessageType('C2GS_GetSpringFestivalPreheatPlayer', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_GETSPRINGFESTIVALPREHEATPLAYER,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_GetSpringFestivalPreheatPlayer)
  ))
_sym_db.RegisterMessage(C2GS_GetSpringFestivalPreheatPlayer)

GS2C_GetSpringFestivalPreheatPlayer = _reflection.GeneratedProtocolMessageType('GS2C_GetSpringFestivalPreheatPlayer', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_GETSPRINGFESTIVALPREHEATPLAYER,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_GetSpringFestivalPreheatPlayer)
  ))
_sym_db.RegisterMessage(GS2C_GetSpringFestivalPreheatPlayer)

C2GS_SpringFestivalBlessCombine = _reflection.GeneratedProtocolMessageType('C2GS_SpringFestivalBlessCombine', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_SPRINGFESTIVALBLESSCOMBINE,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_SpringFestivalBlessCombine)
  ))
_sym_db.RegisterMessage(C2GS_SpringFestivalBlessCombine)

GS2C_SpringFestivalBlessCombine = _reflection.GeneratedProtocolMessageType('GS2C_SpringFestivalBlessCombine', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_SPRINGFESTIVALBLESSCOMBINE,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_SpringFestivalBlessCombine)
  ))
_sym_db.RegisterMessage(GS2C_SpringFestivalBlessCombine)

C2GS_CompleteSpringFestivalTask = _reflection.GeneratedProtocolMessageType('C2GS_CompleteSpringFestivalTask', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_COMPLETESPRINGFESTIVALTASK,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_CompleteSpringFestivalTask)
  ))
_sym_db.RegisterMessage(C2GS_CompleteSpringFestivalTask)

GS2C_CompleteSpringFestivalTask = _reflection.GeneratedProtocolMessageType('GS2C_CompleteSpringFestivalTask', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_COMPLETESPRINGFESTIVALTASK,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_CompleteSpringFestivalTask)
  ))
_sym_db.RegisterMessage(GS2C_CompleteSpringFestivalTask)

C2GS_UnlockSpringFestivalPlayer = _reflection.GeneratedProtocolMessageType('C2GS_UnlockSpringFestivalPlayer', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_UNLOCKSPRINGFESTIVALPLAYER,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_UnlockSpringFestivalPlayer)
  ))
_sym_db.RegisterMessage(C2GS_UnlockSpringFestivalPlayer)

GS2C_UnlockSpringFestivalPlayer = _reflection.GeneratedProtocolMessageType('GS2C_UnlockSpringFestivalPlayer', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_UNLOCKSPRINGFESTIVALPLAYER,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_UnlockSpringFestivalPlayer)
  ))
_sym_db.RegisterMessage(GS2C_UnlockSpringFestivalPlayer)

C2GS_BuySpringFestivalPlayer = _reflection.GeneratedProtocolMessageType('C2GS_BuySpringFestivalPlayer', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_BUYSPRINGFESTIVALPLAYER,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_BuySpringFestivalPlayer)
  ))
_sym_db.RegisterMessage(C2GS_BuySpringFestivalPlayer)

GS2C_BuySpringFestivalPlayer = _reflection.GeneratedProtocolMessageType('GS2C_BuySpringFestivalPlayer', (_message.Message,), dict(
  DESCRIPTOR = _GS2C_BUYSPRINGFESTIVALPLAYER,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:GS2C_BuySpringFestivalPlayer)
  ))
_sym_db.RegisterMessage(GS2C_BuySpringFestivalPlayer)

C2GS_SpringFestivalPreheatShare = _reflection.GeneratedProtocolMessageType('C2GS_SpringFestivalPreheatShare', (_message.Message,), dict(
  DESCRIPTOR = _C2GS_SPRINGFESTIVALPREHEATSHARE,
  __module__ = 'springfestivalpreheat_pb2'
  # @@protoc_insertion_point(class_scope:C2GS_SpringFestivalPreheatShare)
  ))
_sym_db.RegisterMessage(C2GS_SpringFestivalPreheatShare)


# @@protoc_insertion_point(module_scope)