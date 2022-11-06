# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ai/predict.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ai/predict.proto',
  package='predict',
  syntax='proto3',
  serialized_options=_b('\n\023com.luxrobo.predictB\021RecommendApiProtoP\001Z\017luxrobo/predict\242\002\003TPX\252\002\017Luxrobo.predict\312\002\017Luxrobo\\predict'),
  serialized_pb=_b('\n\x10\x61i/predict.proto\x12\x07predict\"%\n\x07Numbers\x12\x0c\n\x04unum\x18\x01 \x01(\x05\x12\x0c\n\x04qnum\x18\x02 \x01(\x05\"<\n\x0bPredictions\x12\x10\n\x08passrate\x18\x01 \x01(\x02\x12\x0c\n\x04time\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x03 \x01(\x02\x32\x43\n\tPredictor\x12\x36\n\nGetPredict\x12\x10.predict.Numbers\x1a\x14.predict.Predictions\"\x00\x42\x65\n\x13\x63om.luxrobo.predictB\x11RecommendApiProtoP\x01Z\x0fluxrobo/predict\xa2\x02\x03TPX\xaa\x02\x0fLuxrobo.predict\xca\x02\x0fLuxrobo\\predictb\x06proto3')
)




_NUMBERS = _descriptor.Descriptor(
  name='Numbers',
  full_name='predict.Numbers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unum', full_name='predict.Numbers.unum', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qnum', full_name='predict.Numbers.qnum', index=1,
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
  serialized_start=29,
  serialized_end=66,
)


_PREDICTIONS = _descriptor.Descriptor(
  name='Predictions',
  full_name='predict.Predictions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='passrate', full_name='predict.Predictions.passrate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='predict.Predictions.time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='predict.Predictions.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=68,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['Numbers'] = _NUMBERS
DESCRIPTOR.message_types_by_name['Predictions'] = _PREDICTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Numbers = _reflection.GeneratedProtocolMessageType('Numbers', (_message.Message,), {
  'DESCRIPTOR' : _NUMBERS,
  '__module__' : 'ai.predict_pb2'
  # @@protoc_insertion_point(class_scope:predict.Numbers)
  })
_sym_db.RegisterMessage(Numbers)

Predictions = _reflection.GeneratedProtocolMessageType('Predictions', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONS,
  '__module__' : 'ai.predict_pb2'
  # @@protoc_insertion_point(class_scope:predict.Predictions)
  })
_sym_db.RegisterMessage(Predictions)


DESCRIPTOR._options = None

_PREDICTOR = _descriptor.ServiceDescriptor(
  name='Predictor',
  full_name='predict.Predictor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=130,
  serialized_end=197,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPredict',
    full_name='predict.Predictor.GetPredict',
    index=0,
    containing_service=None,
    input_type=_NUMBERS,
    output_type=_PREDICTIONS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICTOR)

DESCRIPTOR.services_by_name['Predictor'] = _PREDICTOR

# @@protoc_insertion_point(module_scope)
