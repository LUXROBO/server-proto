# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/product_pack.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v1 import base_pb2 as v1_dot_base__pb2
from v1 import product_pb2 as v1_dot_product__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/product_pack.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\016com.luxrobo.v1B\020ProductPackProtoP\001Z\nluxrobo/v1\242\002\003TPX\252\002\nLuxrobo.v1\312\002\nLuxrobo\\v1'),
  serialized_pb=_b('\n\x15v1/product_pack.proto\x12\x02v1\x1a\rv1/base.proto\x1a\x10v1/product.proto\"\xc5\x01\n\x0cProductPackE\x12\n\n\x02no\x18\x01 \x01(\x03\x12\x0e\n\x06packNo\x18\x02 \x01(\x03\x12\r\n\x05title\x18\x03 \x01(\t\x12\x10\n\x08subTitle\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65scribe\x18\x05 \x01(\t\x12 \n\x08mainImgs\x18\x06 \x03(\x0b\x32\x0e.v1.ImageInfoE\x12\x1e\n\x08products\x18\x07 \x03(\x0b\x32\x0c.v1.ProductE\x12\x11\n\tcreatedAt\x18\x08 \x01(\t\x12\x11\n\tupdatedAt\x18\t \x01(\tBP\n\x0e\x63om.luxrobo.v1B\x10ProductPackProtoP\x01Z\nluxrobo/v1\xa2\x02\x03TPX\xaa\x02\nLuxrobo.v1\xca\x02\nLuxrobo\\v1b\x06proto3')
  ,
  dependencies=[v1_dot_base__pb2.DESCRIPTOR,v1_dot_product__pb2.DESCRIPTOR,])




_PRODUCTPACKE = _descriptor.Descriptor(
  name='ProductPackE',
  full_name='v1.ProductPackE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no', full_name='v1.ProductPackE.no', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packNo', full_name='v1.ProductPackE.packNo', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='v1.ProductPackE.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subTitle', full_name='v1.ProductPackE.subTitle', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='describe', full_name='v1.ProductPackE.describe', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mainImgs', full_name='v1.ProductPackE.mainImgs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='products', full_name='v1.ProductPackE.products', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createdAt', full_name='v1.ProductPackE.createdAt', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updatedAt', full_name='v1.ProductPackE.updatedAt', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=63,
  serialized_end=260,
)

_PRODUCTPACKE.fields_by_name['mainImgs'].message_type = v1_dot_base__pb2._IMAGEINFOE
_PRODUCTPACKE.fields_by_name['products'].message_type = v1_dot_product__pb2._PRODUCTE
DESCRIPTOR.message_types_by_name['ProductPackE'] = _PRODUCTPACKE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductPackE = _reflection.GeneratedProtocolMessageType('ProductPackE', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTPACKE,
  '__module__' : 'v1.product_pack_pb2'
  # @@protoc_insertion_point(class_scope:v1.ProductPackE)
  })
_sym_db.RegisterMessage(ProductPackE)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
