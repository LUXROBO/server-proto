# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/stat_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v1 import base_pb2 as v1_dot_base__pb2
from v1 import stat_pb2 as v1_dot_stat__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/stat_api.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\016com.luxrobo.v1B\014StatApiProtoP\001Z\nluxrobo/v1\242\002\003TPX\252\002\nLuxrobo.v1\312\002\nLuxrobo\\v1'),
  serialized_pb=_b('\n\x11v1/stat_api.proto\x12\x02v1\x1a\rv1/base.proto\x1a\rv1/stat.proto\"?\n\x17StatGraphqlQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x15\n\roperationName\x18\x02 \x01(\t\"B\n\x18StatGraphqlQueryResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\x0e\n\x06result\x18\x02 \x01(\t\"2\n\x0fStatViewRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x11\n\tlessonIds\x18\x02 \x03(\t\"L\n\x10StatViewResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12 \n\x05views\x18\x02 \x03(\x0b\x32\x11.v1.StatUserViewE\"\x82\x01\n\x14StatAddLessonRequest\x12\x0f\n\x07ownerId\x18\x01 \x01(\t\x12\x10\n\x08lessonId\x18\x02 \x01(\t\x12\x17\n\x0flessonContentId\x18\x03 \x01(\t\x12\r\n\x05sTime\x18\x04 \x01(\t\x12\r\n\x05\x65Time\x18\x05 \x01(\t\x12\x10\n\x08\x63\x43ontent\x18\x06 \x01(\x05\"?\n\x15StatAddLessonResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\x0e\n\x06result\x18\x02 \x01(\t\"\x86\x01\n\x18StatAddLessonProcRequest\x12\x0f\n\x07ownerId\x18\x01 \x01(\t\x12\x10\n\x08lessonId\x18\x02 \x01(\t\x12\x17\n\x0flessonContentId\x18\x03 \x01(\t\x12\r\n\x05sTime\x18\x04 \x01(\t\x12\r\n\x05\x65Time\x18\x05 \x01(\t\x12\x10\n\x08\x63\x43ontent\x18\x06 \x01(\x05\"C\n\x19StatAddLessonProcResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\x0e\n\x06result\x18\x02 \x01(\t\"(\n\x14StatDelLessonRequest\x12\x10\n\x08lessonNo\x18\x01 \x01(\x03\"/\n\x15StatDelLessonResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\"-\n\rStatListWhere\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06userNo\x18\x02 \x01(\x03\"\x80\x01\n\x0fStatListRequest\x12\r\n\x05\x66irst\x18\x01 \x01(\x05\x12\r\n\x05\x61\x66ter\x18\x02 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\x1d\n\x07orderBy\x18\x04 \x01(\x0b\x32\x0c.v1.OrderByE\x12 \n\x05where\x18\x05 \x01(\x0b\x32\x11.v1.StatListWhere\"L\n\x10StatListResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x11\n\tlessonIds\x18\x03 \x03(\t\".\n\x19StatLessonActivityRequest\x12\x11\n\tlessonIds\x18\x01 \x03(\t\"g\n\x1aStatLessonActivityResponse\x12\x31\n\x10lessonActivities\x18\x01 \x03(\x0b\x32\x17.v1.StatLessonActivityE\x12\x16\n\x03\x65rr\x18\x02 \x01(\x0b\x32\t.v1.Error\"\x13\n\x11StatHealthRequest\"<\n\x12StatHealthResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\x0e\n\x06status\x18\x02 \x01(\x08\x32\xb8\x04\n\x07StatAPI\x12M\n\x10StatGraphqlQuery\x12\x1b.v1.StatGraphqlQueryRequest\x1a\x1c.v1.StatGraphqlQueryResponse\x12\x35\n\x08StatView\x12\x13.v1.StatViewRequest\x1a\x14.v1.StatViewResponse\x12\x44\n\rStatAddLesson\x12\x18.v1.StatAddLessonRequest\x1a\x19.v1.StatAddLessonResponse\x12P\n\x11StatAddLessonProc\x12\x1c.v1.StatAddLessonProcRequest\x1a\x1d.v1.StatAddLessonProcResponse\x12\x44\n\rStatDelLesson\x12\x18.v1.StatDelLessonRequest\x1a\x19.v1.StatDelLessonResponse\x12\x35\n\x08StatList\x12\x13.v1.StatListRequest\x1a\x14.v1.StatListResponse\x12S\n\x12StatLessonActivity\x12\x1d.v1.StatLessonActivityRequest\x1a\x1e.v1.StatLessonActivityResponse\x12=\n\nStatHealth\x12\x15.v1.StatHealthRequest\x1a\x16.v1.StatHealthResponse\"\x00\x42L\n\x0e\x63om.luxrobo.v1B\x0cStatApiProtoP\x01Z\nluxrobo/v1\xa2\x02\x03TPX\xaa\x02\nLuxrobo.v1\xca\x02\nLuxrobo\\v1b\x06proto3')
  ,
  dependencies=[v1_dot_base__pb2.DESCRIPTOR,v1_dot_stat__pb2.DESCRIPTOR,])




_STATGRAPHQLQUERYREQUEST = _descriptor.Descriptor(
  name='StatGraphqlQueryRequest',
  full_name='v1.StatGraphqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='v1.StatGraphqlQueryRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operationName', full_name='v1.StatGraphqlQueryRequest.operationName', index=1,
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
  serialized_start=55,
  serialized_end=118,
)


_STATGRAPHQLQUERYRESPONSE = _descriptor.Descriptor(
  name='StatGraphqlQueryResponse',
  full_name='v1.StatGraphqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.StatGraphqlQueryResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='v1.StatGraphqlQueryResponse.result', index=1,
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
  serialized_start=120,
  serialized_end=186,
)


_STATVIEWREQUEST = _descriptor.Descriptor(
  name='StatViewRequest',
  full_name='v1.StatViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='v1.StatViewRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lessonIds', full_name='v1.StatViewRequest.lessonIds', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=188,
  serialized_end=238,
)


_STATVIEWRESPONSE = _descriptor.Descriptor(
  name='StatViewResponse',
  full_name='v1.StatViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.StatViewResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='views', full_name='v1.StatViewResponse.views', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=240,
  serialized_end=316,
)


_STATADDLESSONREQUEST = _descriptor.Descriptor(
  name='StatAddLessonRequest',
  full_name='v1.StatAddLessonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ownerId', full_name='v1.StatAddLessonRequest.ownerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lessonId', full_name='v1.StatAddLessonRequest.lessonId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lessonContentId', full_name='v1.StatAddLessonRequest.lessonContentId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sTime', full_name='v1.StatAddLessonRequest.sTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eTime', full_name='v1.StatAddLessonRequest.eTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cContent', full_name='v1.StatAddLessonRequest.cContent', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=319,
  serialized_end=449,
)


_STATADDLESSONRESPONSE = _descriptor.Descriptor(
  name='StatAddLessonResponse',
  full_name='v1.StatAddLessonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.StatAddLessonResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='v1.StatAddLessonResponse.result', index=1,
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
  serialized_start=451,
  serialized_end=514,
)


_STATADDLESSONPROCREQUEST = _descriptor.Descriptor(
  name='StatAddLessonProcRequest',
  full_name='v1.StatAddLessonProcRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ownerId', full_name='v1.StatAddLessonProcRequest.ownerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lessonId', full_name='v1.StatAddLessonProcRequest.lessonId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lessonContentId', full_name='v1.StatAddLessonProcRequest.lessonContentId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sTime', full_name='v1.StatAddLessonProcRequest.sTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eTime', full_name='v1.StatAddLessonProcRequest.eTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cContent', full_name='v1.StatAddLessonProcRequest.cContent', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=517,
  serialized_end=651,
)


_STATADDLESSONPROCRESPONSE = _descriptor.Descriptor(
  name='StatAddLessonProcResponse',
  full_name='v1.StatAddLessonProcResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.StatAddLessonProcResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='v1.StatAddLessonProcResponse.result', index=1,
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
  serialized_start=653,
  serialized_end=720,
)


_STATDELLESSONREQUEST = _descriptor.Descriptor(
  name='StatDelLessonRequest',
  full_name='v1.StatDelLessonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lessonNo', full_name='v1.StatDelLessonRequest.lessonNo', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=722,
  serialized_end=762,
)


_STATDELLESSONRESPONSE = _descriptor.Descriptor(
  name='StatDelLessonResponse',
  full_name='v1.StatDelLessonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.StatDelLessonResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=764,
  serialized_end=811,
)


_STATLISTWHERE = _descriptor.Descriptor(
  name='StatListWhere',
  full_name='v1.StatListWhere',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='v1.StatListWhere.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userNo', full_name='v1.StatListWhere.userNo', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=813,
  serialized_end=858,
)


_STATLISTREQUEST = _descriptor.Descriptor(
  name='StatListRequest',
  full_name='v1.StatListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='v1.StatListRequest.first', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='after', full_name='v1.StatListRequest.after', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='v1.StatListRequest.offset', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderBy', full_name='v1.StatListRequest.orderBy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='where', full_name='v1.StatListRequest.where', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=861,
  serialized_end=989,
)


_STATLISTRESPONSE = _descriptor.Descriptor(
  name='StatListResponse',
  full_name='v1.StatListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.StatListResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='v1.StatListResponse.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lessonIds', full_name='v1.StatListResponse.lessonIds', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=991,
  serialized_end=1067,
)


_STATLESSONACTIVITYREQUEST = _descriptor.Descriptor(
  name='StatLessonActivityRequest',
  full_name='v1.StatLessonActivityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lessonIds', full_name='v1.StatLessonActivityRequest.lessonIds', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1069,
  serialized_end=1115,
)


_STATLESSONACTIVITYRESPONSE = _descriptor.Descriptor(
  name='StatLessonActivityResponse',
  full_name='v1.StatLessonActivityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lessonActivities', full_name='v1.StatLessonActivityResponse.lessonActivities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.StatLessonActivityResponse.err', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1117,
  serialized_end=1220,
)


_STATHEALTHREQUEST = _descriptor.Descriptor(
  name='StatHealthRequest',
  full_name='v1.StatHealthRequest',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1222,
  serialized_end=1241,
)


_STATHEALTHRESPONSE = _descriptor.Descriptor(
  name='StatHealthResponse',
  full_name='v1.StatHealthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.StatHealthResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='v1.StatHealthResponse.status', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=1243,
  serialized_end=1303,
)

_STATGRAPHQLQUERYRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_STATVIEWRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_STATVIEWRESPONSE.fields_by_name['views'].message_type = v1_dot_stat__pb2._STATUSERVIEWE
_STATADDLESSONRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_STATADDLESSONPROCRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_STATDELLESSONRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_STATLISTREQUEST.fields_by_name['orderBy'].message_type = v1_dot_base__pb2._ORDERBYE
_STATLISTREQUEST.fields_by_name['where'].message_type = _STATLISTWHERE
_STATLISTRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_STATLESSONACTIVITYRESPONSE.fields_by_name['lessonActivities'].message_type = v1_dot_stat__pb2._STATLESSONACTIVITYE
_STATLESSONACTIVITYRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_STATHEALTHRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
DESCRIPTOR.message_types_by_name['StatGraphqlQueryRequest'] = _STATGRAPHQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['StatGraphqlQueryResponse'] = _STATGRAPHQLQUERYRESPONSE
DESCRIPTOR.message_types_by_name['StatViewRequest'] = _STATVIEWREQUEST
DESCRIPTOR.message_types_by_name['StatViewResponse'] = _STATVIEWRESPONSE
DESCRIPTOR.message_types_by_name['StatAddLessonRequest'] = _STATADDLESSONREQUEST
DESCRIPTOR.message_types_by_name['StatAddLessonResponse'] = _STATADDLESSONRESPONSE
DESCRIPTOR.message_types_by_name['StatAddLessonProcRequest'] = _STATADDLESSONPROCREQUEST
DESCRIPTOR.message_types_by_name['StatAddLessonProcResponse'] = _STATADDLESSONPROCRESPONSE
DESCRIPTOR.message_types_by_name['StatDelLessonRequest'] = _STATDELLESSONREQUEST
DESCRIPTOR.message_types_by_name['StatDelLessonResponse'] = _STATDELLESSONRESPONSE
DESCRIPTOR.message_types_by_name['StatListWhere'] = _STATLISTWHERE
DESCRIPTOR.message_types_by_name['StatListRequest'] = _STATLISTREQUEST
DESCRIPTOR.message_types_by_name['StatListResponse'] = _STATLISTRESPONSE
DESCRIPTOR.message_types_by_name['StatLessonActivityRequest'] = _STATLESSONACTIVITYREQUEST
DESCRIPTOR.message_types_by_name['StatLessonActivityResponse'] = _STATLESSONACTIVITYRESPONSE
DESCRIPTOR.message_types_by_name['StatHealthRequest'] = _STATHEALTHREQUEST
DESCRIPTOR.message_types_by_name['StatHealthResponse'] = _STATHEALTHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatGraphqlQueryRequest = _reflection.GeneratedProtocolMessageType('StatGraphqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATGRAPHQLQUERYREQUEST,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatGraphqlQueryRequest)
  })
_sym_db.RegisterMessage(StatGraphqlQueryRequest)

StatGraphqlQueryResponse = _reflection.GeneratedProtocolMessageType('StatGraphqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATGRAPHQLQUERYRESPONSE,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatGraphqlQueryResponse)
  })
_sym_db.RegisterMessage(StatGraphqlQueryResponse)

StatViewRequest = _reflection.GeneratedProtocolMessageType('StatViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATVIEWREQUEST,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatViewRequest)
  })
_sym_db.RegisterMessage(StatViewRequest)

StatViewResponse = _reflection.GeneratedProtocolMessageType('StatViewResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATVIEWRESPONSE,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatViewResponse)
  })
_sym_db.RegisterMessage(StatViewResponse)

StatAddLessonRequest = _reflection.GeneratedProtocolMessageType('StatAddLessonRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATADDLESSONREQUEST,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatAddLessonRequest)
  })
_sym_db.RegisterMessage(StatAddLessonRequest)

StatAddLessonResponse = _reflection.GeneratedProtocolMessageType('StatAddLessonResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATADDLESSONRESPONSE,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatAddLessonResponse)
  })
_sym_db.RegisterMessage(StatAddLessonResponse)

StatAddLessonProcRequest = _reflection.GeneratedProtocolMessageType('StatAddLessonProcRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATADDLESSONPROCREQUEST,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatAddLessonProcRequest)
  })
_sym_db.RegisterMessage(StatAddLessonProcRequest)

StatAddLessonProcResponse = _reflection.GeneratedProtocolMessageType('StatAddLessonProcResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATADDLESSONPROCRESPONSE,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatAddLessonProcResponse)
  })
_sym_db.RegisterMessage(StatAddLessonProcResponse)

StatDelLessonRequest = _reflection.GeneratedProtocolMessageType('StatDelLessonRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATDELLESSONREQUEST,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatDelLessonRequest)
  })
_sym_db.RegisterMessage(StatDelLessonRequest)

StatDelLessonResponse = _reflection.GeneratedProtocolMessageType('StatDelLessonResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATDELLESSONRESPONSE,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatDelLessonResponse)
  })
_sym_db.RegisterMessage(StatDelLessonResponse)

StatListWhere = _reflection.GeneratedProtocolMessageType('StatListWhere', (_message.Message,), {
  'DESCRIPTOR' : _STATLISTWHERE,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatListWhere)
  })
_sym_db.RegisterMessage(StatListWhere)

StatListRequest = _reflection.GeneratedProtocolMessageType('StatListRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATLISTREQUEST,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatListRequest)
  })
_sym_db.RegisterMessage(StatListRequest)

StatListResponse = _reflection.GeneratedProtocolMessageType('StatListResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATLISTRESPONSE,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatListResponse)
  })
_sym_db.RegisterMessage(StatListResponse)

StatLessonActivityRequest = _reflection.GeneratedProtocolMessageType('StatLessonActivityRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATLESSONACTIVITYREQUEST,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatLessonActivityRequest)
  })
_sym_db.RegisterMessage(StatLessonActivityRequest)

StatLessonActivityResponse = _reflection.GeneratedProtocolMessageType('StatLessonActivityResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATLESSONACTIVITYRESPONSE,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatLessonActivityResponse)
  })
_sym_db.RegisterMessage(StatLessonActivityResponse)

StatHealthRequest = _reflection.GeneratedProtocolMessageType('StatHealthRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATHEALTHREQUEST,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatHealthRequest)
  })
_sym_db.RegisterMessage(StatHealthRequest)

StatHealthResponse = _reflection.GeneratedProtocolMessageType('StatHealthResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATHEALTHRESPONSE,
  '__module__' : 'v1.stat_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.StatHealthResponse)
  })
_sym_db.RegisterMessage(StatHealthResponse)


DESCRIPTOR._options = None

_STATAPI = _descriptor.ServiceDescriptor(
  name='StatAPI',
  full_name='v1.StatAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1306,
  serialized_end=1874,
  methods=[
  _descriptor.MethodDescriptor(
    name='StatGraphqlQuery',
    full_name='v1.StatAPI.StatGraphqlQuery',
    index=0,
    containing_service=None,
    input_type=_STATGRAPHQLQUERYREQUEST,
    output_type=_STATGRAPHQLQUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StatView',
    full_name='v1.StatAPI.StatView',
    index=1,
    containing_service=None,
    input_type=_STATVIEWREQUEST,
    output_type=_STATVIEWRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StatAddLesson',
    full_name='v1.StatAPI.StatAddLesson',
    index=2,
    containing_service=None,
    input_type=_STATADDLESSONREQUEST,
    output_type=_STATADDLESSONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StatAddLessonProc',
    full_name='v1.StatAPI.StatAddLessonProc',
    index=3,
    containing_service=None,
    input_type=_STATADDLESSONPROCREQUEST,
    output_type=_STATADDLESSONPROCRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StatDelLesson',
    full_name='v1.StatAPI.StatDelLesson',
    index=4,
    containing_service=None,
    input_type=_STATDELLESSONREQUEST,
    output_type=_STATDELLESSONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StatList',
    full_name='v1.StatAPI.StatList',
    index=5,
    containing_service=None,
    input_type=_STATLISTREQUEST,
    output_type=_STATLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StatLessonActivity',
    full_name='v1.StatAPI.StatLessonActivity',
    index=6,
    containing_service=None,
    input_type=_STATLESSONACTIVITYREQUEST,
    output_type=_STATLESSONACTIVITYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StatHealth',
    full_name='v1.StatAPI.StatHealth',
    index=7,
    containing_service=None,
    input_type=_STATHEALTHREQUEST,
    output_type=_STATHEALTHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATAPI)

DESCRIPTOR.services_by_name['StatAPI'] = _STATAPI

# @@protoc_insertion_point(module_scope)
