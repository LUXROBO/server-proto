# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/marketing_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v1 import base_pb2 as v1_dot_base__pb2
from v1 import marketing_pb2 as v1_dot_marketing__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/marketing_api.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\016com.luxrobo.v1B\021MarketingApiProtoP\001Z\nluxrobo/v1\242\002\003TPX\252\002\nLuxrobo.v1\312\002\nLuxrobo\\v1'),
  serialized_pb=_b('\n\x16v1/marketing_api.proto\x12\x02v1\x1a\rv1/base.proto\x1a\x12v1/marketing.proto\"2\n\x1cMarketingPromotionMapRequest\x12\x12\n\nproductIds\x18\x01 \x03(\t\"\xd0\x01\n\x1dMarketingPromotionMapResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12I\n\x0cmapPromotion\x18\x02 \x03(\x0b\x32\x33.v1.MarketingPromotionMapResponse.MapPromotionEntry\x1aL\n\x11MapPromotionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.v1.MarketingPromotionE:\x02\x38\x01\"4\n!MarketingCouponDownloadMapRequest\x12\x0f\n\x07userIds\x18\x01 \x03(\t\"\xee\x01\n\"MarketingCouponDownloadMapResponse\x12\x16\n\x03\x65rr\x18\x01 \x01(\x0b\x32\t.v1.Error\x12X\n\x11mapCouponDownload\x18\x02 \x03(\x0b\x32=.v1.MarketingCouponDownloadMapResponse.MapCouponDownloadEntry\x1aV\n\x16MapCouponDownloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.v1.MarketingCouponDownloadE:\x02\x38\x01\x32\xd9\x01\n\x0cMarketingAPI\x12\\\n\x15MarketingPromotionMap\x12 .v1.MarketingPromotionMapRequest\x1a!.v1.MarketingPromotionMapResponse\x12k\n\x1aMarketingCouponDownloadMap\x12%.v1.MarketingCouponDownloadMapRequest\x1a&.v1.MarketingCouponDownloadMapResponseBQ\n\x0e\x63om.luxrobo.v1B\x11MarketingApiProtoP\x01Z\nluxrobo/v1\xa2\x02\x03TPX\xaa\x02\nLuxrobo.v1\xca\x02\nLuxrobo\\v1b\x06proto3')
  ,
  dependencies=[v1_dot_base__pb2.DESCRIPTOR,v1_dot_marketing__pb2.DESCRIPTOR,])




_MARKETINGPROMOTIONMAPREQUEST = _descriptor.Descriptor(
  name='MarketingPromotionMapRequest',
  full_name='v1.MarketingPromotionMapRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='productIds', full_name='v1.MarketingPromotionMapRequest.productIds', index=0,
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
  serialized_start=65,
  serialized_end=115,
)


_MARKETINGPROMOTIONMAPRESPONSE_MAPPROMOTIONENTRY = _descriptor.Descriptor(
  name='MapPromotionEntry',
  full_name='v1.MarketingPromotionMapResponse.MapPromotionEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.MarketingPromotionMapResponse.MapPromotionEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.MarketingPromotionMapResponse.MapPromotionEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=326,
)

_MARKETINGPROMOTIONMAPRESPONSE = _descriptor.Descriptor(
  name='MarketingPromotionMapResponse',
  full_name='v1.MarketingPromotionMapResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.MarketingPromotionMapResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapPromotion', full_name='v1.MarketingPromotionMapResponse.mapPromotion', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MARKETINGPROMOTIONMAPRESPONSE_MAPPROMOTIONENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=326,
)


_MARKETINGCOUPONDOWNLOADMAPREQUEST = _descriptor.Descriptor(
  name='MarketingCouponDownloadMapRequest',
  full_name='v1.MarketingCouponDownloadMapRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userIds', full_name='v1.MarketingCouponDownloadMapRequest.userIds', index=0,
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
  serialized_start=328,
  serialized_end=380,
)


_MARKETINGCOUPONDOWNLOADMAPRESPONSE_MAPCOUPONDOWNLOADENTRY = _descriptor.Descriptor(
  name='MapCouponDownloadEntry',
  full_name='v1.MarketingCouponDownloadMapResponse.MapCouponDownloadEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.MarketingCouponDownloadMapResponse.MapCouponDownloadEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.MarketingCouponDownloadMapResponse.MapCouponDownloadEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=621,
)

_MARKETINGCOUPONDOWNLOADMAPRESPONSE = _descriptor.Descriptor(
  name='MarketingCouponDownloadMapResponse',
  full_name='v1.MarketingCouponDownloadMapResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='v1.MarketingCouponDownloadMapResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapCouponDownload', full_name='v1.MarketingCouponDownloadMapResponse.mapCouponDownload', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MARKETINGCOUPONDOWNLOADMAPRESPONSE_MAPCOUPONDOWNLOADENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=621,
)

_MARKETINGPROMOTIONMAPRESPONSE_MAPPROMOTIONENTRY.fields_by_name['value'].message_type = v1_dot_marketing__pb2._MARKETINGPROMOTIONE
_MARKETINGPROMOTIONMAPRESPONSE_MAPPROMOTIONENTRY.containing_type = _MARKETINGPROMOTIONMAPRESPONSE
_MARKETINGPROMOTIONMAPRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_MARKETINGPROMOTIONMAPRESPONSE.fields_by_name['mapPromotion'].message_type = _MARKETINGPROMOTIONMAPRESPONSE_MAPPROMOTIONENTRY
_MARKETINGCOUPONDOWNLOADMAPRESPONSE_MAPCOUPONDOWNLOADENTRY.fields_by_name['value'].message_type = v1_dot_marketing__pb2._MARKETINGCOUPONDOWNLOADE
_MARKETINGCOUPONDOWNLOADMAPRESPONSE_MAPCOUPONDOWNLOADENTRY.containing_type = _MARKETINGCOUPONDOWNLOADMAPRESPONSE
_MARKETINGCOUPONDOWNLOADMAPRESPONSE.fields_by_name['err'].message_type = v1_dot_base__pb2._ERROR
_MARKETINGCOUPONDOWNLOADMAPRESPONSE.fields_by_name['mapCouponDownload'].message_type = _MARKETINGCOUPONDOWNLOADMAPRESPONSE_MAPCOUPONDOWNLOADENTRY
DESCRIPTOR.message_types_by_name['MarketingPromotionMapRequest'] = _MARKETINGPROMOTIONMAPREQUEST
DESCRIPTOR.message_types_by_name['MarketingPromotionMapResponse'] = _MARKETINGPROMOTIONMAPRESPONSE
DESCRIPTOR.message_types_by_name['MarketingCouponDownloadMapRequest'] = _MARKETINGCOUPONDOWNLOADMAPREQUEST
DESCRIPTOR.message_types_by_name['MarketingCouponDownloadMapResponse'] = _MARKETINGCOUPONDOWNLOADMAPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MarketingPromotionMapRequest = _reflection.GeneratedProtocolMessageType('MarketingPromotionMapRequest', (_message.Message,), {
  'DESCRIPTOR' : _MARKETINGPROMOTIONMAPREQUEST,
  '__module__' : 'v1.marketing_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.MarketingPromotionMapRequest)
  })
_sym_db.RegisterMessage(MarketingPromotionMapRequest)

MarketingPromotionMapResponse = _reflection.GeneratedProtocolMessageType('MarketingPromotionMapResponse', (_message.Message,), {

  'MapPromotionEntry' : _reflection.GeneratedProtocolMessageType('MapPromotionEntry', (_message.Message,), {
    'DESCRIPTOR' : _MARKETINGPROMOTIONMAPRESPONSE_MAPPROMOTIONENTRY,
    '__module__' : 'v1.marketing_api_pb2'
    # @@protoc_insertion_point(class_scope:v1.MarketingPromotionMapResponse.MapPromotionEntry)
    })
  ,
  'DESCRIPTOR' : _MARKETINGPROMOTIONMAPRESPONSE,
  '__module__' : 'v1.marketing_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.MarketingPromotionMapResponse)
  })
_sym_db.RegisterMessage(MarketingPromotionMapResponse)
_sym_db.RegisterMessage(MarketingPromotionMapResponse.MapPromotionEntry)

MarketingCouponDownloadMapRequest = _reflection.GeneratedProtocolMessageType('MarketingCouponDownloadMapRequest', (_message.Message,), {
  'DESCRIPTOR' : _MARKETINGCOUPONDOWNLOADMAPREQUEST,
  '__module__' : 'v1.marketing_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.MarketingCouponDownloadMapRequest)
  })
_sym_db.RegisterMessage(MarketingCouponDownloadMapRequest)

MarketingCouponDownloadMapResponse = _reflection.GeneratedProtocolMessageType('MarketingCouponDownloadMapResponse', (_message.Message,), {

  'MapCouponDownloadEntry' : _reflection.GeneratedProtocolMessageType('MapCouponDownloadEntry', (_message.Message,), {
    'DESCRIPTOR' : _MARKETINGCOUPONDOWNLOADMAPRESPONSE_MAPCOUPONDOWNLOADENTRY,
    '__module__' : 'v1.marketing_api_pb2'
    # @@protoc_insertion_point(class_scope:v1.MarketingCouponDownloadMapResponse.MapCouponDownloadEntry)
    })
  ,
  'DESCRIPTOR' : _MARKETINGCOUPONDOWNLOADMAPRESPONSE,
  '__module__' : 'v1.marketing_api_pb2'
  # @@protoc_insertion_point(class_scope:v1.MarketingCouponDownloadMapResponse)
  })
_sym_db.RegisterMessage(MarketingCouponDownloadMapResponse)
_sym_db.RegisterMessage(MarketingCouponDownloadMapResponse.MapCouponDownloadEntry)


DESCRIPTOR._options = None
_MARKETINGPROMOTIONMAPRESPONSE_MAPPROMOTIONENTRY._options = None
_MARKETINGCOUPONDOWNLOADMAPRESPONSE_MAPCOUPONDOWNLOADENTRY._options = None

_MARKETINGAPI = _descriptor.ServiceDescriptor(
  name='MarketingAPI',
  full_name='v1.MarketingAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=624,
  serialized_end=841,
  methods=[
  _descriptor.MethodDescriptor(
    name='MarketingPromotionMap',
    full_name='v1.MarketingAPI.MarketingPromotionMap',
    index=0,
    containing_service=None,
    input_type=_MARKETINGPROMOTIONMAPREQUEST,
    output_type=_MARKETINGPROMOTIONMAPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MarketingCouponDownloadMap',
    full_name='v1.MarketingAPI.MarketingCouponDownloadMap',
    index=1,
    containing_service=None,
    input_type=_MARKETINGCOUPONDOWNLOADMAPREQUEST,
    output_type=_MARKETINGCOUPONDOWNLOADMAPRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MARKETINGAPI)

DESCRIPTOR.services_by_name['MarketingAPI'] = _MARKETINGAPI

# @@protoc_insertion_point(module_scope)
