# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/livekit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v1 import enum_pb2 as v1_dot_enum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/livekit.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\016com.luxrobo.v1B\014LivekitProtoP\001Z\nluxrobo/v1\242\002\003TPX\252\002\nLuxrobo.v1\312\002\nLuxrobo\\v1'),
  serialized_pb=_b('\n\x10v1/livekit.proto\x12\x02v1\x1a\rv1/enum.proto\"\xd8\x01\n\x0cLivekitRoomE\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x65mptyTimeout\x18\x03 \x01(\x03\x12\x14\n\x0c\x63reationTime\x18\x04 \x01(\x03\x12\x17\n\x0fmaxParticipants\x18\x05 \x01(\x03\x12\x14\n\x0cturnPassword\x18\x06 \x01(\t\x12\'\n\x0c\x65nableCodecs\x18\x07 \x03(\x0b\x32\x11.v1.LivekitCodecE\x12\x10\n\x08metadata\x18\x08 \x01(\t\x12\x17\n\x0fnumParticipants\x18\t \x01(\x03\"/\n\rLivekitCodecE\x12\x0c\n\x04mime\x18\x01 \x01(\t\x12\x10\n\x08\x66mtpLine\x18\x02 \x01(\t\"\xad\x01\n\x13LivekitParticipantE\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12!\n\x06tracks\x18\x05 \x03(\x0b\x32\x11.v1.LivekitTrackE\x12\x10\n\x08metadata\x18\x06 \x01(\t\x12\x10\n\x08joinedAt\x18\x07 \x01(\x03\x12\x13\n\x0bisPublisher\x18\x08 \x01(\x08\"\xf3\x01\n\rLivekitTrackE\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05muted\x18\x04 \x01(\x08\x12\r\n\x05width\x18\x05 \x01(\x03\x12\x0e\n\x06height\x18\x06 \x01(\x03\x12\x11\n\tsimulcast\x18\x07 \x01(\x08\x12\x12\n\ndisableDtx\x18\x08 \x01(\x08\x12*\n\x06source\x18\t \x01(\x0e\x32\x1a.v1.LivekitTrackSourceType\x12&\n\x06layers\x18\n \x03(\x0b\x32\x16.v1.LivekitVideoLayerE\x12\x10\n\x08mimeType\x18\x0b \x01(\t\"r\n\x12LivekitVideoLayerE\x12,\n\x07quality\x18\x01 \x01(\x0e\x32\x1b.v1.LivekitVideoQualityType\x12\r\n\x05width\x18\x02 \x01(\x03\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\x0f\n\x07\x62itrate\x18\x04 \x01(\x03\x42L\n\x0e\x63om.luxrobo.v1B\x0cLivekitProtoP\x01Z\nluxrobo/v1\xa2\x02\x03TPX\xaa\x02\nLuxrobo.v1\xca\x02\nLuxrobo\\v1b\x06proto3')
  ,
  dependencies=[v1_dot_enum__pb2.DESCRIPTOR,])




_LIVEKITROOME = _descriptor.Descriptor(
  name='LivekitRoomE',
  full_name='v1.LivekitRoomE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid', full_name='v1.LivekitRoomE.sid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.LivekitRoomE.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emptyTimeout', full_name='v1.LivekitRoomE.emptyTimeout', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creationTime', full_name='v1.LivekitRoomE.creationTime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxParticipants', full_name='v1.LivekitRoomE.maxParticipants', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='turnPassword', full_name='v1.LivekitRoomE.turnPassword', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enableCodecs', full_name='v1.LivekitRoomE.enableCodecs', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='v1.LivekitRoomE.metadata', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numParticipants', full_name='v1.LivekitRoomE.numParticipants', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=256,
)


_LIVEKITCODECE = _descriptor.Descriptor(
  name='LivekitCodecE',
  full_name='v1.LivekitCodecE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mime', full_name='v1.LivekitCodecE.mime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fmtpLine', full_name='v1.LivekitCodecE.fmtpLine', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=305,
)


_LIVEKITPARTICIPANTE = _descriptor.Descriptor(
  name='LivekitParticipantE',
  full_name='v1.LivekitParticipantE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid', full_name='v1.LivekitParticipantE.sid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identity', full_name='v1.LivekitParticipantE.identity', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.LivekitParticipantE.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='v1.LivekitParticipantE.state', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracks', full_name='v1.LivekitParticipantE.tracks', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='v1.LivekitParticipantE.metadata', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='joinedAt', full_name='v1.LivekitParticipantE.joinedAt', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isPublisher', full_name='v1.LivekitParticipantE.isPublisher', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=481,
)


_LIVEKITTRACKE = _descriptor.Descriptor(
  name='LivekitTrackE',
  full_name='v1.LivekitTrackE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid', full_name='v1.LivekitTrackE.sid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='v1.LivekitTrackE.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.LivekitTrackE.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='muted', full_name='v1.LivekitTrackE.muted', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='v1.LivekitTrackE.width', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='v1.LivekitTrackE.height', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='simulcast', full_name='v1.LivekitTrackE.simulcast', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disableDtx', full_name='v1.LivekitTrackE.disableDtx', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='v1.LivekitTrackE.source', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layers', full_name='v1.LivekitTrackE.layers', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mimeType', full_name='v1.LivekitTrackE.mimeType', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=727,
)


_LIVEKITVIDEOLAYERE = _descriptor.Descriptor(
  name='LivekitVideoLayerE',
  full_name='v1.LivekitVideoLayerE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quality', full_name='v1.LivekitVideoLayerE.quality', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='v1.LivekitVideoLayerE.width', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='v1.LivekitVideoLayerE.height', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bitrate', full_name='v1.LivekitVideoLayerE.bitrate', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=843,
)

_LIVEKITROOME.fields_by_name['enableCodecs'].message_type = _LIVEKITCODECE
_LIVEKITPARTICIPANTE.fields_by_name['tracks'].message_type = _LIVEKITTRACKE
_LIVEKITTRACKE.fields_by_name['source'].enum_type = v1_dot_enum__pb2._LIVEKITTRACKSOURCETYPE
_LIVEKITTRACKE.fields_by_name['layers'].message_type = _LIVEKITVIDEOLAYERE
_LIVEKITVIDEOLAYERE.fields_by_name['quality'].enum_type = v1_dot_enum__pb2._LIVEKITVIDEOQUALITYTYPE
DESCRIPTOR.message_types_by_name['LivekitRoomE'] = _LIVEKITROOME
DESCRIPTOR.message_types_by_name['LivekitCodecE'] = _LIVEKITCODECE
DESCRIPTOR.message_types_by_name['LivekitParticipantE'] = _LIVEKITPARTICIPANTE
DESCRIPTOR.message_types_by_name['LivekitTrackE'] = _LIVEKITTRACKE
DESCRIPTOR.message_types_by_name['LivekitVideoLayerE'] = _LIVEKITVIDEOLAYERE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LivekitRoomE = _reflection.GeneratedProtocolMessageType('LivekitRoomE', (_message.Message,), {
  'DESCRIPTOR' : _LIVEKITROOME,
  '__module__' : 'v1.livekit_pb2'
  # @@protoc_insertion_point(class_scope:v1.LivekitRoomE)
  })
_sym_db.RegisterMessage(LivekitRoomE)

LivekitCodecE = _reflection.GeneratedProtocolMessageType('LivekitCodecE', (_message.Message,), {
  'DESCRIPTOR' : _LIVEKITCODECE,
  '__module__' : 'v1.livekit_pb2'
  # @@protoc_insertion_point(class_scope:v1.LivekitCodecE)
  })
_sym_db.RegisterMessage(LivekitCodecE)

LivekitParticipantE = _reflection.GeneratedProtocolMessageType('LivekitParticipantE', (_message.Message,), {
  'DESCRIPTOR' : _LIVEKITPARTICIPANTE,
  '__module__' : 'v1.livekit_pb2'
  # @@protoc_insertion_point(class_scope:v1.LivekitParticipantE)
  })
_sym_db.RegisterMessage(LivekitParticipantE)

LivekitTrackE = _reflection.GeneratedProtocolMessageType('LivekitTrackE', (_message.Message,), {
  'DESCRIPTOR' : _LIVEKITTRACKE,
  '__module__' : 'v1.livekit_pb2'
  # @@protoc_insertion_point(class_scope:v1.LivekitTrackE)
  })
_sym_db.RegisterMessage(LivekitTrackE)

LivekitVideoLayerE = _reflection.GeneratedProtocolMessageType('LivekitVideoLayerE', (_message.Message,), {
  'DESCRIPTOR' : _LIVEKITVIDEOLAYERE,
  '__module__' : 'v1.livekit_pb2'
  # @@protoc_insertion_point(class_scope:v1.LivekitVideoLayerE)
  })
_sym_db.RegisterMessage(LivekitVideoLayerE)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
