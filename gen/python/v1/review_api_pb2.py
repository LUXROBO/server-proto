# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/review_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v1 import base_pb2 as v1_dot_base__pb2
from v1 import review_pb2 as v1_dot_review__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/review_api.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\016com.luxrobo.v1B\016ReviewApiProtoP\001Z\nluxrobo/v1\242\002\003TPX\252\002\nLuxrobo.v1\312\002\nLuxrobo\\v1'),
  serialized_pb=_b('\n\x13v1/review_api.proto\x12\x02v1\x1a\rv1/base.proto\x1a\x0fv1/review.proto\"A\n\x19ReviewGraphqlQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x15\n\roperationName\x18\x02 \x01(\t\"D\n\x1aReviewGraphqlQueryResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\x0e\n\x06result\x18\x02 \x01(\t\"\'\n\x12ReviewCountRequest\x12\x11\n\tlessonIds\x18\x01 \x03(\t\"O\n\x13ReviewCountResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12 \n\x06\x63ounts\x18\x02 \x03(\x0b\x32\x10.v1.ReviewCountE\"\x15\n\x13ReviewHealthRequest\">\n\x14ReviewHealthResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12\x0e\n\x06status\x18\x02 \x01(\x08\x32\xe5\x01\n\tReviewAPI\x12S\n\x12ReviewGraphqlQuery\x12\x1d.v1.ReviewGraphqlQueryRequest\x1a\x1e.v1.ReviewGraphqlQueryResponse\x12>\n\x0bReviewCount\x12\x16.v1.ReviewCountRequest\x1a\x17.v1.ReviewCountResponse\x12\x43\n\x0cReviewHealth\x12\x17.v1.ReviewHealthRequest\x1a\x18.v1.ReviewHealthResponse\"\x00\x42N\n\x0e\x63om.luxrobo.v1B\x0eReviewApiProtoP\x01Z\nluxrobo/v1\xa2\x02\x03TPX\xaa\x02\nLuxrobo.v1\xca\x02\nLuxrobo\\v1b\x06proto3')
  ,
  dependencies=[v1_dot_base__pb2.DESCRIPTOR,v1_dot_review__pb2.DESCRIPTOR,])




_REVIEWGRAPHQLQUERYREQUEST = _descriptor.Descriptor(
  name='ReviewGraphqlQueryRequest',
  full_name='v1.ReviewGraphqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='v1.ReviewGraphqlQueryRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operationName', full_name='v1.ReviewGraphqlQueryRequest.operationName', index=1,
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
  serialized_start=59,
  serialized_end=124,
)


_REVIEWGRAPHQLQUERYRESPONSE = _descriptor.Descriptor(
  name='ReviewGraphqlQueryResponse',
  full_name='v1.ReviewGraphqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.ReviewGraphqlQueryResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='v1.ReviewGraphqlQueryResponse.result', index=1,
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
  serialized_start=126,
  serialized_end=194,
)


_REVIEWCOUNTREQUEST = _descriptor.Descriptor(
  name='ReviewCountRequest',
  full_name='v1.ReviewCountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lessonIds', full_name='v1.ReviewCountRequest.lessonIds', index=0,
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
  serialized_start=196,
  serialized_end=235,
)


_REVIEWCOUNTRESPONSE = _descriptor.Descriptor(
  name='ReviewCountResponse',
  full_name='v1.ReviewCountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.ReviewCountResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counts', full_name='v1.ReviewCountResponse.counts', index=1,
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
  serialized_start=237,
  serialized_end=316,
)


_REVIEWHEALTHREQUEST = _descriptor.Descriptor(
  name='ReviewHealthRequest',
  full_name='v1.ReviewHealthRequest',
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
  serialized_start=318,
  serialized_end=339,
)


_REVIEWHEALTHRESPONSE = _descriptor.Descriptor(
  name='ReviewHealthResponse',
  full_name='v1.ReviewHealthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.ReviewHealthResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='v1.ReviewHealthResponse.status', index=1,
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
  serialized_start=341,
  serialized_end=403,
)

_REVIEWGRAPHQLQUERYRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_REVIEWCOUNTRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_REVIEWCOUNTRESPONSE.fields_by_name['counts'].message_type = v1_dot_review__pb2._REVIEWCOUNTE
_REVIEWHEALTHRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
DESCRIPTOR.message_types_by_name['ReviewGraphqlQueryRequest'] = _REVIEWGRAPHQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['ReviewGraphqlQueryResponse'] = _REVIEWGRAPHQLQUERYRESPONSE
DESCRIPTOR.message_types_by_name['ReviewCountRequest'] = _REVIEWCOUNTREQUEST
DESCRIPTOR.message_types_by_name['ReviewCountResponse'] = _REVIEWCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['ReviewHealthRequest'] = _REVIEWHEALTHREQUEST
DESCRIPTOR.message_types_by_name['ReviewHealthResponse'] = _REVIEWHEALTHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReviewGraphqlQueryRequest = _reflection.GeneratedProtocolMessageType('ReviewGraphqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWGRAPHQLQUERYREQUEST,
  '__module__' : 'v1.review_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ReviewGraphqlQueryRequest)
  })
_sym_db.RegisterMessage(ReviewGraphqlQueryRequest)

ReviewGraphqlQueryResponse = _reflection.GeneratedProtocolMessageType('ReviewGraphqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWGRAPHQLQUERYRESPONSE,
  '__module__' : 'v1.review_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ReviewGraphqlQueryResponse)
  })
_sym_db.RegisterMessage(ReviewGraphqlQueryResponse)

ReviewCountRequest = _reflection.GeneratedProtocolMessageType('ReviewCountRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWCOUNTREQUEST,
  '__module__' : 'v1.review_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ReviewCountRequest)
  })
_sym_db.RegisterMessage(ReviewCountRequest)

ReviewCountResponse = _reflection.GeneratedProtocolMessageType('ReviewCountResponse', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWCOUNTRESPONSE,
  '__module__' : 'v1.review_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ReviewCountResponse)
  })
_sym_db.RegisterMessage(ReviewCountResponse)

ReviewHealthRequest = _reflection.GeneratedProtocolMessageType('ReviewHealthRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWHEALTHREQUEST,
  '__module__' : 'v1.review_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ReviewHealthRequest)
  })
_sym_db.RegisterMessage(ReviewHealthRequest)

ReviewHealthResponse = _reflection.GeneratedProtocolMessageType('ReviewHealthResponse', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWHEALTHRESPONSE,
  '__module__' : 'v1.review_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.ReviewHealthResponse)
  })
_sym_db.RegisterMessage(ReviewHealthResponse)


DESCRIPTOR._options = None

_REVIEWAPI = _descriptor.ServiceDescriptor(
  name='ReviewAPI',
  full_name='v1.ReviewAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=406,
  serialized_end=635,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReviewGraphqlQuery',
    full_name='v1.ReviewAPI.ReviewGraphqlQuery',
    index=0,
    containing_service=None,
    input_type=_REVIEWGRAPHQLQUERYREQUEST,
    output_type=_REVIEWGRAPHQLQUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReviewCount',
    full_name='v1.ReviewAPI.ReviewCount',
    index=1,
    containing_service=None,
    input_type=_REVIEWCOUNTREQUEST,
    output_type=_REVIEWCOUNTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReviewHealth',
    full_name='v1.ReviewAPI.ReviewHealth',
    index=2,
    containing_service=None,
    input_type=_REVIEWHEALTHREQUEST,
    output_type=_REVIEWHEALTHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REVIEWAPI)

DESCRIPTOR.services_by_name['ReviewAPI'] = _REVIEWAPI

# @@protoc_insertion_point(module_scope)
