# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/search.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/search.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\016com.luxrobo.v1B\013SearchProtoP\001Z\nluxrobo/v1\242\002\003TPX\252\002\nLuxrobo.v1\312\002\nLuxrobo\\v1'),
  serialized_pb=_b('\n\x0fv1/search.proto\x12\x02v1\")\n\nSearchTagE\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x42K\n\x0e\x63om.luxrobo.v1B\x0bSearchProtoP\x01Z\nluxrobo/v1\xa2\x02\x03TPX\xaa\x02\nLuxrobo.v1\xca\x02\nLuxrobo\\v1b\x06proto3')
)




_SEARCHTAGE = _descriptor.Descriptor(
  name='SearchTagE',
  full_name='v1.SearchTagE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.SearchTagE.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='v1.SearchTagE.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=23,
  serialized_end=64,
)

DESCRIPTOR.message_types_by_name['SearchTagE'] = _SEARCHTAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchTagE = _reflection.GeneratedProtocolMessageType('SearchTagE', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHTAGE,
  '__module__' : 'v1.search_pb2'
  # @@protoc_insertion_point(class_scope:v1.SearchTagE)
  })
_sym_db.RegisterMessage(SearchTagE)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
