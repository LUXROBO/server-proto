# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/classroom_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v1 import base_pb2 as v1_dot_base__pb2
from v1 import classroom_pb2 as v1_dot_classroom__pb2
from v1 import enum_pb2 as v1_dot_enum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/classroom_api.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\016com.luxrobo.v1B\021ClassroomApiProtoP\001Z\nluxrobo/v1\242\002\003TPX\252\002\nLuxrobo.v1\312\002\nLuxrobo\\v1'),
  serialized_pb=_b('\n\x16v1/classroom_api.proto\x12\x02v1\x1a\rv1/base.proto\x1a\x12v1/classroom.proto\x1a\rv1/enum.proto\"D\n\x1c\x43lassroomGraphqlQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x15\n\roperationName\x18\x02 \x01(\t\"G\n\x1d\x43lassroomGraphqlQueryResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\x0e\n\x06result\x18\x02 \x01(\t\"?\n\x18\x43lassroomLessonListWhere\x12\x13\n\x0b\x63lassroomId\x18\x01 \x01(\t\x12\x0e\n\x06userNo\x18\x02 \x01(\x03\"\x96\x01\n\x1a\x43lassroomLessonListRequest\x12\r\n\x05\x66irst\x18\x01 \x01(\x05\x12\r\n\x05\x61\x66ter\x18\x02 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\x1d\n\x07orderBy\x18\x04 \x01(\x0b\x32\x0c.v1.OrderByE\x12+\n\x05where\x18\x05 \x01(\x0b\x32\x1c.v1.ClassroomLessonListWhere\"t\n\x1b\x43lassroomLessonListResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\r\n\x05total\x18\x02 \x01(\x05\x12.\n\x10\x63lassroomLessons\x18\x03 \x03(\x0b\x32\x14.v1.ClassroomLessonE\"R\n\x1c\x43lassroomLessonUpdateRequest\x12\x10\n\x08lessonNo\x18\x01 \x01(\x03\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.v1.LessonOpenType\"7\n\x1d\x43lassroomLessonUpdateResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\"\x8b\x01\n\x1f\x43lassroomLessonGroupListRequest\x12\r\n\x05\x66irst\x18\x01 \x01(\x05\x12\r\n\x05\x61\x66ter\x18\x02 \x01(\t\x12\x1d\n\x07orderBy\x18\x03 \x01(\x0b\x32\x0c.v1.OrderByE\x12+\n\x05where\x18\x04 \x01(\x0b\x32\x1c.v1.ClassroomLessonListWhere\"j\n ClassroomLessonGroupListResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12.\n\x10\x63lassroomLessons\x18\x02 \x03(\x0b\x32\x14.v1.ClassroomLessonE\"\x18\n\x16\x43lassroomHealthRequest\"A\n\x17\x43lassroomHealthResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\x0e\n\x06status\x18\x02 \x01(\x08\x32\xd7\x03\n\x0c\x43lassroomAPI\x12\\\n\x15\x43lassroomGraphqlQuery\x12 .v1.ClassroomGraphqlQueryRequest\x1a!.v1.ClassroomGraphqlQueryResponse\x12V\n\x13\x43lassroomLessonList\x12\x1e.v1.ClassroomLessonListRequest\x1a\x1f.v1.ClassroomLessonListResponse\x12\\\n\x15\x43lassroomLessonUpdate\x12 .v1.ClassroomLessonUpdateRequest\x1a!.v1.ClassroomLessonUpdateResponse\x12\x65\n\x18\x43lassroomLessonGroupList\x12#.v1.ClassroomLessonGroupListRequest\x1a$.v1.ClassroomLessonGroupListResponse\x12L\n\x0f\x43lassroomHealth\x12\x1a.v1.ClassroomHealthRequest\x1a\x1b.v1.ClassroomHealthResponse\"\x00\x42Q\n\x0e\x63om.luxrobo.v1B\x11\x43lassroomApiProtoP\x01Z\nluxrobo/v1\xa2\x02\x03TPX\xaa\x02\nLuxrobo.v1\xca\x02\nLuxrobo\\v1b\x06proto3')
  ,
  dependencies=[v1_dot_base__pb2.DESCRIPTOR,v1_dot_classroom__pb2.DESCRIPTOR,v1_dot_enum__pb2.DESCRIPTOR,])




_CLASSROOMGRAPHQLQUERYREQUEST = _descriptor.Descriptor(
  name='ClassroomGraphqlQueryRequest',
  full_name='v1.ClassroomGraphqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='v1.ClassroomGraphqlQueryRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operationName', full_name='v1.ClassroomGraphqlQueryRequest.operationName', index=1,
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
  serialized_start=80,
  serialized_end=148,
)


_CLASSROOMGRAPHQLQUERYRESPONSE = _descriptor.Descriptor(
  name='ClassroomGraphqlQueryResponse',
  full_name='v1.ClassroomGraphqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.ClassroomGraphqlQueryResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='v1.ClassroomGraphqlQueryResponse.result', index=1,
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
  serialized_start=150,
  serialized_end=221,
)


_CLASSROOMLESSONLISTWHERE = _descriptor.Descriptor(
  name='ClassroomLessonListWhere',
  full_name='v1.ClassroomLessonListWhere',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classroomId', full_name='v1.ClassroomLessonListWhere.classroomId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userNo', full_name='v1.ClassroomLessonListWhere.userNo', index=1,
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
  serialized_start=223,
  serialized_end=286,
)


_CLASSROOMLESSONLISTREQUEST = _descriptor.Descriptor(
  name='ClassroomLessonListRequest',
  full_name='v1.ClassroomLessonListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='v1.ClassroomLessonListRequest.first', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='after', full_name='v1.ClassroomLessonListRequest.after', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='v1.ClassroomLessonListRequest.offset', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderBy', full_name='v1.ClassroomLessonListRequest.orderBy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='where', full_name='v1.ClassroomLessonListRequest.where', index=4,
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
  serialized_start=289,
  serialized_end=439,
)


_CLASSROOMLESSONLISTRESPONSE = _descriptor.Descriptor(
  name='ClassroomLessonListResponse',
  full_name='v1.ClassroomLessonListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.ClassroomLessonListResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='v1.ClassroomLessonListResponse.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classroomLessons', full_name='v1.ClassroomLessonListResponse.classroomLessons', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=441,
  serialized_end=557,
)


_CLASSROOMLESSONUPDATEREQUEST = _descriptor.Descriptor(
  name='ClassroomLessonUpdateRequest',
  full_name='v1.ClassroomLessonUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lessonNo', full_name='v1.ClassroomLessonUpdateRequest.lessonNo', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='v1.ClassroomLessonUpdateRequest.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=559,
  serialized_end=641,
)


_CLASSROOMLESSONUPDATERESPONSE = _descriptor.Descriptor(
  name='ClassroomLessonUpdateResponse',
  full_name='v1.ClassroomLessonUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.ClassroomLessonUpdateResponse.err', index=0,
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
  serialized_start=643,
  serialized_end=698,
)


_CLASSROOMLESSONGROUPLISTREQUEST = _descriptor.Descriptor(
  name='ClassroomLessonGroupListRequest',
  full_name='v1.ClassroomLessonGroupListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='v1.ClassroomLessonGroupListRequest.first', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='after', full_name='v1.ClassroomLessonGroupListRequest.after', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderBy', full_name='v1.ClassroomLessonGroupListRequest.orderBy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='where', full_name='v1.ClassroomLessonGroupListRequest.where', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=701,
  serialized_end=840,
)


_CLASSROOMLESSONGROUPLISTRESPONSE = _descriptor.Descriptor(
  name='ClassroomLessonGroupListResponse',
  full_name='v1.ClassroomLessonGroupListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.ClassroomLessonGroupListResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classroomLessons', full_name='v1.ClassroomLessonGroupListResponse.classroomLessons', index=1,
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
  serialized_start=842,
  serialized_end=948,
)


_CLASSROOMHEALTHREQUEST = _descriptor.Descriptor(
  name='ClassroomHealthRequest',
  full_name='v1.ClassroomHealthRequest',
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
  serialized_start=950,
  serialized_end=974,
)


_CLASSROOMHEALTHRESPONSE = _descriptor.Descriptor(
  name='ClassroomHealthResponse',
  full_name='v1.ClassroomHealthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.ClassroomHealthResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='v1.ClassroomHealthResponse.status', index=1,
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
  serialized_start=976,
  serialized_end=1041,
)

_CLASSROOMGRAPHQLQUERYRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_CLASSROOMLESSONLISTREQUEST.fields_by_name['orderBy'].message_type = v1_dot_base__pb2._ORDERBYE
_CLASSROOMLESSONLISTREQUEST.fields_by_name['where'].message_type = _CLASSROOMLESSONLISTWHERE
_CLASSROOMLESSONLISTRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_CLASSROOMLESSONLISTRESPONSE.fields_by_name['classroomLessons'].message_type = v1_dot_classroom__pb2._CLASSROOMLESSONE
_CLASSROOMLESSONUPDATEREQUEST.fields_by_name['type'].enum_type = v1_dot_enum__pb2._LESSONOPENTYPE
_CLASSROOMLESSONUPDATERESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_CLASSROOMLESSONGROUPLISTREQUEST.fields_by_name['orderBy'].message_type = v1_dot_base__pb2._ORDERBYE
_CLASSROOMLESSONGROUPLISTREQUEST.fields_by_name['where'].message_type = _CLASSROOMLESSONLISTWHERE
_CLASSROOMLESSONGROUPLISTRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_CLASSROOMLESSONGROUPLISTRESPONSE.fields_by_name['classroomLessons'].message_type = v1_dot_classroom__pb2._CLASSROOMLESSONE
_CLASSROOMHEALTHRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
DESCRIPTOR.message_types_by_name['ClassroomGraphqlQueryRequest'] = _CLASSROOMGRAPHQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['ClassroomGraphqlQueryResponse'] = _CLASSROOMGRAPHQLQUERYRESPONSE
DESCRIPTOR.message_types_by_name['ClassroomLessonListWhere'] = _CLASSROOMLESSONLISTWHERE
DESCRIPTOR.message_types_by_name['ClassroomLessonListRequest'] = _CLASSROOMLESSONLISTREQUEST
DESCRIPTOR.message_types_by_name['ClassroomLessonListResponse'] = _CLASSROOMLESSONLISTRESPONSE
DESCRIPTOR.message_types_by_name['ClassroomLessonUpdateRequest'] = _CLASSROOMLESSONUPDATEREQUEST
DESCRIPTOR.message_types_by_name['ClassroomLessonUpdateResponse'] = _CLASSROOMLESSONUPDATERESPONSE
DESCRIPTOR.message_types_by_name['ClassroomLessonGroupListRequest'] = _CLASSROOMLESSONGROUPLISTREQUEST
DESCRIPTOR.message_types_by_name['ClassroomLessonGroupListResponse'] = _CLASSROOMLESSONGROUPLISTRESPONSE
DESCRIPTOR.message_types_by_name['ClassroomHealthRequest'] = _CLASSROOMHEALTHREQUEST
DESCRIPTOR.message_types_by_name['ClassroomHealthResponse'] = _CLASSROOMHEALTHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassroomGraphqlQueryRequest = _reflection.GeneratedProtocolMessageType('ClassroomGraphqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMGRAPHQLQUERYREQUEST,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomGraphqlQueryRequest)
  })
_sym_db.RegisterMessage(ClassroomGraphqlQueryRequest)

ClassroomGraphqlQueryResponse = _reflection.GeneratedProtocolMessageType('ClassroomGraphqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMGRAPHQLQUERYRESPONSE,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomGraphqlQueryResponse)
  })
_sym_db.RegisterMessage(ClassroomGraphqlQueryResponse)

ClassroomLessonListWhere = _reflection.GeneratedProtocolMessageType('ClassroomLessonListWhere', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMLESSONLISTWHERE,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomLessonListWhere)
  })
_sym_db.RegisterMessage(ClassroomLessonListWhere)

ClassroomLessonListRequest = _reflection.GeneratedProtocolMessageType('ClassroomLessonListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMLESSONLISTREQUEST,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomLessonListRequest)
  })
_sym_db.RegisterMessage(ClassroomLessonListRequest)

ClassroomLessonListResponse = _reflection.GeneratedProtocolMessageType('ClassroomLessonListResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMLESSONLISTRESPONSE,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomLessonListResponse)
  })
_sym_db.RegisterMessage(ClassroomLessonListResponse)

ClassroomLessonUpdateRequest = _reflection.GeneratedProtocolMessageType('ClassroomLessonUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMLESSONUPDATEREQUEST,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomLessonUpdateRequest)
  })
_sym_db.RegisterMessage(ClassroomLessonUpdateRequest)

ClassroomLessonUpdateResponse = _reflection.GeneratedProtocolMessageType('ClassroomLessonUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMLESSONUPDATERESPONSE,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomLessonUpdateResponse)
  })
_sym_db.RegisterMessage(ClassroomLessonUpdateResponse)

ClassroomLessonGroupListRequest = _reflection.GeneratedProtocolMessageType('ClassroomLessonGroupListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMLESSONGROUPLISTREQUEST,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomLessonGroupListRequest)
  })
_sym_db.RegisterMessage(ClassroomLessonGroupListRequest)

ClassroomLessonGroupListResponse = _reflection.GeneratedProtocolMessageType('ClassroomLessonGroupListResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMLESSONGROUPLISTRESPONSE,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomLessonGroupListResponse)
  })
_sym_db.RegisterMessage(ClassroomLessonGroupListResponse)

ClassroomHealthRequest = _reflection.GeneratedProtocolMessageType('ClassroomHealthRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMHEALTHREQUEST,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomHealthRequest)
  })
_sym_db.RegisterMessage(ClassroomHealthRequest)

ClassroomHealthResponse = _reflection.GeneratedProtocolMessageType('ClassroomHealthResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLASSROOMHEALTHRESPONSE,
  '__module__' : 'v1.classroom_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ClassroomHealthResponse)
  })
_sym_db.RegisterMessage(ClassroomHealthResponse)


DESCRIPTOR._options = None

_CLASSROOMAPI = _descriptor.ServiceDescriptor(
  name='ClassroomAPI',
  full_name='v1.ClassroomAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1044,
  serialized_end=1515,
  methods=[
  _descriptor.MethodDescriptor(
    name='ClassroomGraphqlQuery',
    full_name='v1.ClassroomAPI.ClassroomGraphqlQuery',
    index=0,
    containing_service=None,
    input_type=_CLASSROOMGRAPHQLQUERYREQUEST,
    output_type=_CLASSROOMGRAPHQLQUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClassroomLessonList',
    full_name='v1.ClassroomAPI.ClassroomLessonList',
    index=1,
    containing_service=None,
    input_type=_CLASSROOMLESSONLISTREQUEST,
    output_type=_CLASSROOMLESSONLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClassroomLessonUpdate',
    full_name='v1.ClassroomAPI.ClassroomLessonUpdate',
    index=2,
    containing_service=None,
    input_type=_CLASSROOMLESSONUPDATEREQUEST,
    output_type=_CLASSROOMLESSONUPDATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClassroomLessonGroupList',
    full_name='v1.ClassroomAPI.ClassroomLessonGroupList',
    index=3,
    containing_service=None,
    input_type=_CLASSROOMLESSONGROUPLISTREQUEST,
    output_type=_CLASSROOMLESSONGROUPLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClassroomHealth',
    full_name='v1.ClassroomAPI.ClassroomHealth',
    index=4,
    containing_service=None,
    input_type=_CLASSROOMHEALTHREQUEST,
    output_type=_CLASSROOMHEALTHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLASSROOMAPI)

DESCRIPTOR.services_by_name['ClassroomAPI'] = _CLASSROOMAPI

# @@protoc_insertion_point(module_scope)
