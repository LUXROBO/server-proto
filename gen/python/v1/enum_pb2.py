# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/enum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/enum.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\016com.luxrobo.v1B\tEnumProtoP\001Z\nluxrobo/v1\242\002\003TPX\252\002\nLuxrobo.v1\312\002\nLuxrobo\\v1'),
  serialized_pb=_b('\n\rv1/enum.proto\x12\x02v1*&\n\x0c\x44iscountType\x12\x0b\n\x07PERCENT\x10\x00\x12\t\n\x05VALUE\x10\x01*5\n\x0fProjectCodeType\x12\x0b\n\x07SCRATCH\x10\x00\x12\t\n\x05\x45NTRY\x10\x01\x12\n\n\x06PYMODI\x10\x02*+\n\tVideoType\x12\x07\n\x03HLS\x10\x00\x12\x08\n\x04\x44\x41SH\x10\x01\x12\x0b\n\x07YOUTUBE\x10\x02*Q\n\nLessonType\x12\n\n\x06LESSON\x10\x00\x12\x15\n\x11LESSON_CURRICULUM\x10\x01\x12\x0f\n\x0bLESSON_BOOK\x10\x02\x12\x0f\n\x0bLESSON_NONE\x10\x03*S\n\x0bServiceType\x12\r\n\tNONE_TYPE\x10\x00\x12\x07\n\x03LMS\x10\x01\x12\x0f\n\x0bMAKING_PACK\x10\x02\x12\x0b\n\x07\x43\x45NGAGE\x10\x03\x12\x0e\n\nBRICK_PACK\x10\x04*^\n\x0fLessonLevelType\x12\x0e\n\nNONE_LEVEL\x10\x00\x12\x13\n\x0f\x42\x45GINNING_LEVEL\x10\x01\x12\x16\n\x12INTERMEDIATE_LEVEL\x10\x02\x12\x0e\n\nHIGH_LEVEL\x10\x03*\xa2\x01\n\x0fLessonGroupType\x12\x0e\n\nNONE_GROUP\x10\x00\x12\x16\n\x12PRE_SCHOOLER_GROUP\x10\x01\x12\x1b\n\x17\x45LEMENT_BEGINNING_GROUP\x10\x02\x12\x16\n\x12\x45LEMENT_HIGH_GROUP\x10\x03\x12\x19\n\x15MIDDLE_SCHOOLER_GROUP\x10\x04\x12\x17\n\x13HIGH_SCHOOLER_GROUP\x10\x05*K\n\x12LessonPlanViewType\x12\x19\n\x15LESSON_PLAN_NONE_VIEW\x10\x00\x12\x1a\n\x16LESSON_PLAN_SLIDE_VIEW\x10\x01*a\n\x15LessonPlanContentType\x12\x10\n\x0cNONE_CONTENT\x10\x00\x12\x10\n\x0c\x42\x41SE_CONTENT\x10\x01\x12\x11\n\rVIDEO_CONTENT\x10\x02\x12\x11\n\rMULTI_CONTENT\x10\x03*\xc7\x02\n\x15LessonContentViewType\x12\r\n\tNONE_VIEW\x10\x00\x12\x0e\n\nVIDEO_VIEW\x10\x01\x12\x0f\n\x0b\x43ODING_VIEW\x10\x02\x12\x0f\n\x0bNORMAL_VIEW\x10\x03\x12\x18\n\x14PRACTICE_CODING_VIEW\x10\x04\x12(\n$HORIZON_FULL_VERTICAL_DOWN_HALF_VIEW\x10\x05\x12)\n%VERTICAL_FULL_HORIZON_RIGHT_HALF_VIEW\x10\x06\x12\x16\n\x12VERTICAL_FULL_VIEW\x10\x07\x12\x1a\n\x16VERTICAL_TWO_FULL_VIEW\x10\x08\x12#\n\x1fHORIZON_FULL_VERTICAL_FULL_VIEW\x10\t\x12\x15\n\x11HORIZON_FULL_VIEW\x10\n\x12\x0e\n\nSLIDE_VIEW\x10\x0b*\x1d\n\rTrueFalseType\x12\x05\n\x01T\x10\x00\x12\x05\n\x01\x46\x10\x01*<\n\x11\x43lassroomOpenType\x12\x12\n\x0e\x43LASSROOM_OPEN\x10\x00\x12\x13\n\x0f\x43LASSROOM_CLOSE\x10\x01*:\n\x0eLessonOpenType\x12\x08\n\x04OPEN\x10\x00\x12\t\n\x05\x43LOSE\x10\x01\x12\x07\n\x03\x41LL\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03*J\n\x12LessonPlanDataType\x12\x08\n\x04\x42\x41SE\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\t\n\x05IMAGE\x10\x02\x12\t\n\x05VIDEO\x10\x03\x12\n\n\x06\x43ODING\x10\x04*\xc2\x01\n\x18LessonSummaryElementType\x12\x1a\n\x16\x44\x41TA_STRUCTURE_ELEMENT\x10\x00\x12\x14\n\x10\x41NALYSIS_ELEMENT\x10\x01\x12\x14\n\x10\x41\x42STRACT_ELEMENT\x10\x02\x12\x15\n\x11\x41LGORITHM_ELEMENT\x10\x03\x12\x16\n\x12\x41UTOMATION_ELEMENT\x10\x04\x12\x16\n\x12SIMULATION_ELEMENT\x10\x05\x12\x17\n\x13PARALLELISM_ELEMENT\x10\x06*\x95\x01\n\x12LessonHardwareType\x12\x11\n\rNONE_HARDWARE\x10\x00\x12\x12\n\x0eMODI1_HARDWARE\x10\x01\x12\x12\n\x0eMODI2_HARDWARE\x10\x02\x12\x16\n\x12RASPBERRY_HARDWARE\x10\x03\x12\x15\n\x11MICROBIT_HARDWARE\x10\x04\x12\x15\n\x11HELLO_AI_HARDWARE\x10\x05*K\n\x10LessonCodingType\x12\x10\n\x0c\x45NTRY_CODING\x10\x00\x12\x12\n\x0eSCRATCH_CODING\x10\x01\x12\x11\n\rPYMODI_CODING\x10\x02*\xb7\x02\n\x0c\x43reationType\x12\x08\n\x04\x46REE\x10\x00\x12\x11\n\rBINGO_MACHINE\x10\x01\x12\x13\n\x0fRANDOM_ROULETTE\x10\x02\x12\x1a\n\x16ROTATING_PENCIL_HOLDER\x10\x03\x12\x0c\n\x08JOYTROPE\x10\x04\x12\r\n\tLED_TIMER\x10\x05\x12\r\n\tMOOD_LAMP\x10\x06\x12\x11\n\rLED_METRONIUM\x10\x07\x12\x08\n\x04SAFE\x10\x08\x12\x0b\n\x07\x46ISHING\x10\t\x12\x0f\n\x0bSURFING_BOT\x10\n\x12\r\n\tTONGS_ARM\x10\x0b\x12\n\n\x06RC_CAR\x10\x0c\x12\x0f\n\x0bPIRATE_SHIP\x10\r\x12\x13\n\x0f\x43ROCODILE_TEETH\x10\x0e\x12\x0e\n\nLIGHTHOUSE\x10\x0f\x12\x0e\n\nHELICOPTER\x10\x10\x12\x11\n\rMONSTER_TRUCK\x10\x11*T\n\x1bLivekitParticipantStateType\x12\x0b\n\x07JOINING\x10\x00\x12\n\n\x06JOINED\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x10\n\x0c\x44ISCONNECTED\x10\x03*k\n\x16LivekitTrackSourceType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43\x41MERA\x10\x01\x12\x0e\n\nMICROPHONE\x10\x02\x12\x10\n\x0cSCREEN_SHARE\x10\x03\x12\x16\n\x12SCREEN_SHARE_AUDIO\x10\x04*8\n\x17LivekitVideoQualityType\x12\x07\n\x03LOW\x10\x00\x12\n\n\x06MEDIUM\x10\x01\x12\x08\n\x04HIGH\x10\x02*1\n\rUserLoginType\x12\t\n\x05\x45MAIL\x10\x00\x12\t\n\x05KAKAO\x10\x01\x12\n\n\x06GOOGLE\x10\x02*4\n\x19LivekitDataPacketKindType\x12\x0c\n\x08RELIABLE\x10\x00\x12\t\n\x05LOSSY\x10\x01*1\n\x12\x43ourseProductDType\x12\x0f\n\x0bMERCHANDISE\x10\x00\x12\n\n\x06\x43OURSE\x10\x01*5\n\x19\x43ourseProductPurchaseType\x12\x0c\n\x08PURCHASE\x10\x00\x12\n\n\x06RENTAL\x10\x01*6\n\x16\x43ourseProductStateType\x12\x06\n\x02ON\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SOLDOUT\x10\x02*\x17\n\x0c\x43urrencyType\x12\x07\n\x03KRW\x10\x00\x42I\n\x0e\x63om.luxrobo.v1B\tEnumProtoP\x01Z\nluxrobo/v1\xa2\x02\x03TPX\xaa\x02\nLuxrobo.v1\xca\x02\nLuxrobo\\v1b\x06proto3')
)

_DISCOUNTTYPE = _descriptor.EnumDescriptor(
  name='DiscountType',
  full_name='v1.DiscountType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PERCENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=21,
  serialized_end=59,
)
_sym_db.RegisterEnumDescriptor(_DISCOUNTTYPE)

DiscountType = enum_type_wrapper.EnumTypeWrapper(_DISCOUNTTYPE)
_PROJECTCODETYPE = _descriptor.EnumDescriptor(
  name='ProjectCodeType',
  full_name='v1.ProjectCodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCRATCH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTRY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PYMODI', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=61,
  serialized_end=114,
)
_sym_db.RegisterEnumDescriptor(_PROJECTCODETYPE)

ProjectCodeType = enum_type_wrapper.EnumTypeWrapper(_PROJECTCODETYPE)
_VIDEOTYPE = _descriptor.EnumDescriptor(
  name='VideoType',
  full_name='v1.VideoType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HLS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DASH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=116,
  serialized_end=159,
)
_sym_db.RegisterEnumDescriptor(_VIDEOTYPE)

VideoType = enum_type_wrapper.EnumTypeWrapper(_VIDEOTYPE)
_LESSONTYPE = _descriptor.EnumDescriptor(
  name='LessonType',
  full_name='v1.LessonType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LESSON', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESSON_CURRICULUM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESSON_BOOK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESSON_NONE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=161,
  serialized_end=242,
)
_sym_db.RegisterEnumDescriptor(_LESSONTYPE)

LessonType = enum_type_wrapper.EnumTypeWrapper(_LESSONTYPE)
_SERVICETYPE = _descriptor.EnumDescriptor(
  name='ServiceType',
  full_name='v1.ServiceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LMS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAKING_PACK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CENGAGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRICK_PACK', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=244,
  serialized_end=327,
)
_sym_db.RegisterEnumDescriptor(_SERVICETYPE)

ServiceType = enum_type_wrapper.EnumTypeWrapper(_SERVICETYPE)
_LESSONLEVELTYPE = _descriptor.EnumDescriptor(
  name='LessonLevelType',
  full_name='v1.LessonLevelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_LEVEL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEGINNING_LEVEL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERMEDIATE_LEVEL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH_LEVEL', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=329,
  serialized_end=423,
)
_sym_db.RegisterEnumDescriptor(_LESSONLEVELTYPE)

LessonLevelType = enum_type_wrapper.EnumTypeWrapper(_LESSONLEVELTYPE)
_LESSONGROUPTYPE = _descriptor.EnumDescriptor(
  name='LessonGroupType',
  full_name='v1.LessonGroupType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_GROUP', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_SCHOOLER_GROUP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELEMENT_BEGINNING_GROUP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELEMENT_HIGH_GROUP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDDLE_SCHOOLER_GROUP', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH_SCHOOLER_GROUP', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=426,
  serialized_end=588,
)
_sym_db.RegisterEnumDescriptor(_LESSONGROUPTYPE)

LessonGroupType = enum_type_wrapper.EnumTypeWrapper(_LESSONGROUPTYPE)
_LESSONPLANVIEWTYPE = _descriptor.EnumDescriptor(
  name='LessonPlanViewType',
  full_name='v1.LessonPlanViewType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LESSON_PLAN_NONE_VIEW', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESSON_PLAN_SLIDE_VIEW', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=590,
  serialized_end=665,
)
_sym_db.RegisterEnumDescriptor(_LESSONPLANVIEWTYPE)

LessonPlanViewType = enum_type_wrapper.EnumTypeWrapper(_LESSONPLANVIEWTYPE)
_LESSONPLANCONTENTTYPE = _descriptor.EnumDescriptor(
  name='LessonPlanContentType',
  full_name='v1.LessonPlanContentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_CONTENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BASE_CONTENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_CONTENT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTI_CONTENT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=667,
  serialized_end=764,
)
_sym_db.RegisterEnumDescriptor(_LESSONPLANCONTENTTYPE)

LessonPlanContentType = enum_type_wrapper.EnumTypeWrapper(_LESSONPLANCONTENTTYPE)
_LESSONCONTENTVIEWTYPE = _descriptor.EnumDescriptor(
  name='LessonContentViewType',
  full_name='v1.LessonContentViewType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_VIEW', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_VIEW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CODING_VIEW', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL_VIEW', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRACTICE_CODING_VIEW', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HORIZON_FULL_VERTICAL_DOWN_HALF_VIEW', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERTICAL_FULL_HORIZON_RIGHT_HALF_VIEW', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERTICAL_FULL_VIEW', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERTICAL_TWO_FULL_VIEW', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HORIZON_FULL_VERTICAL_FULL_VIEW', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HORIZON_FULL_VIEW', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLIDE_VIEW', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=767,
  serialized_end=1094,
)
_sym_db.RegisterEnumDescriptor(_LESSONCONTENTVIEWTYPE)

LessonContentViewType = enum_type_wrapper.EnumTypeWrapper(_LESSONCONTENTVIEWTYPE)
_TRUEFALSETYPE = _descriptor.EnumDescriptor(
  name='TrueFalseType',
  full_name='v1.TrueFalseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='T', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1096,
  serialized_end=1125,
)
_sym_db.RegisterEnumDescriptor(_TRUEFALSETYPE)

TrueFalseType = enum_type_wrapper.EnumTypeWrapper(_TRUEFALSETYPE)
_CLASSROOMOPENTYPE = _descriptor.EnumDescriptor(
  name='ClassroomOpenType',
  full_name='v1.ClassroomOpenType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLASSROOM_OPEN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLASSROOM_CLOSE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1127,
  serialized_end=1187,
)
_sym_db.RegisterEnumDescriptor(_CLASSROOMOPENTYPE)

ClassroomOpenType = enum_type_wrapper.EnumTypeWrapper(_CLASSROOMOPENTYPE)
_LESSONOPENTYPE = _descriptor.EnumDescriptor(
  name='LessonOpenType',
  full_name='v1.LessonOpenType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1189,
  serialized_end=1247,
)
_sym_db.RegisterEnumDescriptor(_LESSONOPENTYPE)

LessonOpenType = enum_type_wrapper.EnumTypeWrapper(_LESSONOPENTYPE)
_LESSONPLANDATATYPE = _descriptor.EnumDescriptor(
  name='LessonPlanDataType',
  full_name='v1.LessonPlanDataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BASE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CODING', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1249,
  serialized_end=1323,
)
_sym_db.RegisterEnumDescriptor(_LESSONPLANDATATYPE)

LessonPlanDataType = enum_type_wrapper.EnumTypeWrapper(_LESSONPLANDATATYPE)
_LESSONSUMMARYELEMENTTYPE = _descriptor.EnumDescriptor(
  name='LessonSummaryElementType',
  full_name='v1.LessonSummaryElementType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DATA_STRUCTURE_ELEMENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANALYSIS_ELEMENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABSTRACT_ELEMENT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALGORITHM_ELEMENT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOMATION_ELEMENT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMULATION_ELEMENT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARALLELISM_ELEMENT', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1326,
  serialized_end=1520,
)
_sym_db.RegisterEnumDescriptor(_LESSONSUMMARYELEMENTTYPE)

LessonSummaryElementType = enum_type_wrapper.EnumTypeWrapper(_LESSONSUMMARYELEMENTTYPE)
_LESSONHARDWARETYPE = _descriptor.EnumDescriptor(
  name='LessonHardwareType',
  full_name='v1.LessonHardwareType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_HARDWARE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODI1_HARDWARE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODI2_HARDWARE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RASPBERRY_HARDWARE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MICROBIT_HARDWARE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HELLO_AI_HARDWARE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1523,
  serialized_end=1672,
)
_sym_db.RegisterEnumDescriptor(_LESSONHARDWARETYPE)

LessonHardwareType = enum_type_wrapper.EnumTypeWrapper(_LESSONHARDWARETYPE)
_LESSONCODINGTYPE = _descriptor.EnumDescriptor(
  name='LessonCodingType',
  full_name='v1.LessonCodingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENTRY_CODING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCRATCH_CODING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PYMODI_CODING', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1674,
  serialized_end=1749,
)
_sym_db.RegisterEnumDescriptor(_LESSONCODINGTYPE)

LessonCodingType = enum_type_wrapper.EnumTypeWrapper(_LESSONCODINGTYPE)
_CREATIONTYPE = _descriptor.EnumDescriptor(
  name='CreationType',
  full_name='v1.CreationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FREE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINGO_MACHINE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANDOM_ROULETTE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTATING_PENCIL_HOLDER', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOYTROPE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LED_TIMER', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOOD_LAMP', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LED_METRONIUM', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAFE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FISHING', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SURFING_BOT', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TONGS_ARM', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RC_CAR', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PIRATE_SHIP', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROCODILE_TEETH', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIGHTHOUSE', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HELICOPTER', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONSTER_TRUCK', index=17, number=17,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1752,
  serialized_end=2063,
)
_sym_db.RegisterEnumDescriptor(_CREATIONTYPE)

CreationType = enum_type_wrapper.EnumTypeWrapper(_CREATIONTYPE)
_LIVEKITPARTICIPANTSTATETYPE = _descriptor.EnumDescriptor(
  name='LivekitParticipantStateType',
  full_name='v1.LivekitParticipantStateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOINING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOINED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCONNECTED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2065,
  serialized_end=2149,
)
_sym_db.RegisterEnumDescriptor(_LIVEKITPARTICIPANTSTATETYPE)

LivekitParticipantStateType = enum_type_wrapper.EnumTypeWrapper(_LIVEKITPARTICIPANTSTATETYPE)
_LIVEKITTRACKSOURCETYPE = _descriptor.EnumDescriptor(
  name='LivekitTrackSourceType',
  full_name='v1.LivekitTrackSourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMERA', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MICROPHONE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCREEN_SHARE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCREEN_SHARE_AUDIO', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2151,
  serialized_end=2258,
)
_sym_db.RegisterEnumDescriptor(_LIVEKITTRACKSOURCETYPE)

LivekitTrackSourceType = enum_type_wrapper.EnumTypeWrapper(_LIVEKITTRACKSOURCETYPE)
_LIVEKITVIDEOQUALITYTYPE = _descriptor.EnumDescriptor(
  name='LivekitVideoQualityType',
  full_name='v1.LivekitVideoQualityType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOW', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2260,
  serialized_end=2316,
)
_sym_db.RegisterEnumDescriptor(_LIVEKITVIDEOQUALITYTYPE)

LivekitVideoQualityType = enum_type_wrapper.EnumTypeWrapper(_LIVEKITVIDEOQUALITYTYPE)
_USERLOGINTYPE = _descriptor.EnumDescriptor(
  name='UserLoginType',
  full_name='v1.UserLoginType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KAKAO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2318,
  serialized_end=2367,
)
_sym_db.RegisterEnumDescriptor(_USERLOGINTYPE)

UserLoginType = enum_type_wrapper.EnumTypeWrapper(_USERLOGINTYPE)
_LIVEKITDATAPACKETKINDTYPE = _descriptor.EnumDescriptor(
  name='LivekitDataPacketKindType',
  full_name='v1.LivekitDataPacketKindType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RELIABLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOSSY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2369,
  serialized_end=2421,
)
_sym_db.RegisterEnumDescriptor(_LIVEKITDATAPACKETKINDTYPE)

LivekitDataPacketKindType = enum_type_wrapper.EnumTypeWrapper(_LIVEKITDATAPACKETKINDTYPE)
_COURSEPRODUCTDTYPE = _descriptor.EnumDescriptor(
  name='CourseProductDType',
  full_name='v1.CourseProductDType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MERCHANDISE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COURSE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2423,
  serialized_end=2472,
)
_sym_db.RegisterEnumDescriptor(_COURSEPRODUCTDTYPE)

CourseProductDType = enum_type_wrapper.EnumTypeWrapper(_COURSEPRODUCTDTYPE)
_COURSEPRODUCTPURCHASETYPE = _descriptor.EnumDescriptor(
  name='CourseProductPurchaseType',
  full_name='v1.CourseProductPurchaseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PURCHASE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RENTAL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2474,
  serialized_end=2527,
)
_sym_db.RegisterEnumDescriptor(_COURSEPRODUCTPURCHASETYPE)

CourseProductPurchaseType = enum_type_wrapper.EnumTypeWrapper(_COURSEPRODUCTPURCHASETYPE)
_COURSEPRODUCTSTATETYPE = _descriptor.EnumDescriptor(
  name='CourseProductStateType',
  full_name='v1.CourseProductStateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ON', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOLDOUT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2529,
  serialized_end=2583,
)
_sym_db.RegisterEnumDescriptor(_COURSEPRODUCTSTATETYPE)

CourseProductStateType = enum_type_wrapper.EnumTypeWrapper(_COURSEPRODUCTSTATETYPE)
_CURRENCYTYPE = _descriptor.EnumDescriptor(
  name='CurrencyType',
  full_name='v1.CurrencyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KRW', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2585,
  serialized_end=2608,
)
_sym_db.RegisterEnumDescriptor(_CURRENCYTYPE)

CurrencyType = enum_type_wrapper.EnumTypeWrapper(_CURRENCYTYPE)
PERCENT = 0
VALUE = 1
SCRATCH = 0
ENTRY = 1
PYMODI = 2
HLS = 0
DASH = 1
YOUTUBE = 2
LESSON = 0
LESSON_CURRICULUM = 1
LESSON_BOOK = 2
LESSON_NONE = 3
NONE_TYPE = 0
LMS = 1
MAKING_PACK = 2
CENGAGE = 3
BRICK_PACK = 4
NONE_LEVEL = 0
BEGINNING_LEVEL = 1
INTERMEDIATE_LEVEL = 2
HIGH_LEVEL = 3
NONE_GROUP = 0
PRE_SCHOOLER_GROUP = 1
ELEMENT_BEGINNING_GROUP = 2
ELEMENT_HIGH_GROUP = 3
MIDDLE_SCHOOLER_GROUP = 4
HIGH_SCHOOLER_GROUP = 5
LESSON_PLAN_NONE_VIEW = 0
LESSON_PLAN_SLIDE_VIEW = 1
NONE_CONTENT = 0
BASE_CONTENT = 1
VIDEO_CONTENT = 2
MULTI_CONTENT = 3
NONE_VIEW = 0
VIDEO_VIEW = 1
CODING_VIEW = 2
NORMAL_VIEW = 3
PRACTICE_CODING_VIEW = 4
HORIZON_FULL_VERTICAL_DOWN_HALF_VIEW = 5
VERTICAL_FULL_HORIZON_RIGHT_HALF_VIEW = 6
VERTICAL_FULL_VIEW = 7
VERTICAL_TWO_FULL_VIEW = 8
HORIZON_FULL_VERTICAL_FULL_VIEW = 9
HORIZON_FULL_VIEW = 10
SLIDE_VIEW = 11
T = 0
F = 1
CLASSROOM_OPEN = 0
CLASSROOM_CLOSE = 1
OPEN = 0
CLOSE = 1
ALL = 2
DELETE = 3
BASE = 0
TEXT = 1
IMAGE = 2
VIDEO = 3
CODING = 4
DATA_STRUCTURE_ELEMENT = 0
ANALYSIS_ELEMENT = 1
ABSTRACT_ELEMENT = 2
ALGORITHM_ELEMENT = 3
AUTOMATION_ELEMENT = 4
SIMULATION_ELEMENT = 5
PARALLELISM_ELEMENT = 6
NONE_HARDWARE = 0
MODI1_HARDWARE = 1
MODI2_HARDWARE = 2
RASPBERRY_HARDWARE = 3
MICROBIT_HARDWARE = 4
HELLO_AI_HARDWARE = 5
ENTRY_CODING = 0
SCRATCH_CODING = 1
PYMODI_CODING = 2
FREE = 0
BINGO_MACHINE = 1
RANDOM_ROULETTE = 2
ROTATING_PENCIL_HOLDER = 3
JOYTROPE = 4
LED_TIMER = 5
MOOD_LAMP = 6
LED_METRONIUM = 7
SAFE = 8
FISHING = 9
SURFING_BOT = 10
TONGS_ARM = 11
RC_CAR = 12
PIRATE_SHIP = 13
CROCODILE_TEETH = 14
LIGHTHOUSE = 15
HELICOPTER = 16
MONSTER_TRUCK = 17
JOINING = 0
JOINED = 1
ACTIVE = 2
DISCONNECTED = 3
UNKNOWN = 0
CAMERA = 1
MICROPHONE = 2
SCREEN_SHARE = 3
SCREEN_SHARE_AUDIO = 4
LOW = 0
MEDIUM = 1
HIGH = 2
EMAIL = 0
KAKAO = 1
GOOGLE = 2
RELIABLE = 0
LOSSY = 1
MERCHANDISE = 0
COURSE = 1
PURCHASE = 0
RENTAL = 1
ON = 0
OFF = 1
SOLDOUT = 2
KRW = 0


DESCRIPTOR.enum_types_by_name['DiscountType'] = _DISCOUNTTYPE
DESCRIPTOR.enum_types_by_name['ProjectCodeType'] = _PROJECTCODETYPE
DESCRIPTOR.enum_types_by_name['VideoType'] = _VIDEOTYPE
DESCRIPTOR.enum_types_by_name['LessonType'] = _LESSONTYPE
DESCRIPTOR.enum_types_by_name['ServiceType'] = _SERVICETYPE
DESCRIPTOR.enum_types_by_name['LessonLevelType'] = _LESSONLEVELTYPE
DESCRIPTOR.enum_types_by_name['LessonGroupType'] = _LESSONGROUPTYPE
DESCRIPTOR.enum_types_by_name['LessonPlanViewType'] = _LESSONPLANVIEWTYPE
DESCRIPTOR.enum_types_by_name['LessonPlanContentType'] = _LESSONPLANCONTENTTYPE
DESCRIPTOR.enum_types_by_name['LessonContentViewType'] = _LESSONCONTENTVIEWTYPE
DESCRIPTOR.enum_types_by_name['TrueFalseType'] = _TRUEFALSETYPE
DESCRIPTOR.enum_types_by_name['ClassroomOpenType'] = _CLASSROOMOPENTYPE
DESCRIPTOR.enum_types_by_name['LessonOpenType'] = _LESSONOPENTYPE
DESCRIPTOR.enum_types_by_name['LessonPlanDataType'] = _LESSONPLANDATATYPE
DESCRIPTOR.enum_types_by_name['LessonSummaryElementType'] = _LESSONSUMMARYELEMENTTYPE
DESCRIPTOR.enum_types_by_name['LessonHardwareType'] = _LESSONHARDWARETYPE
DESCRIPTOR.enum_types_by_name['LessonCodingType'] = _LESSONCODINGTYPE
DESCRIPTOR.enum_types_by_name['CreationType'] = _CREATIONTYPE
DESCRIPTOR.enum_types_by_name['LivekitParticipantStateType'] = _LIVEKITPARTICIPANTSTATETYPE
DESCRIPTOR.enum_types_by_name['LivekitTrackSourceType'] = _LIVEKITTRACKSOURCETYPE
DESCRIPTOR.enum_types_by_name['LivekitVideoQualityType'] = _LIVEKITVIDEOQUALITYTYPE
DESCRIPTOR.enum_types_by_name['UserLoginType'] = _USERLOGINTYPE
DESCRIPTOR.enum_types_by_name['LivekitDataPacketKindType'] = _LIVEKITDATAPACKETKINDTYPE
DESCRIPTOR.enum_types_by_name['CourseProductDType'] = _COURSEPRODUCTDTYPE
DESCRIPTOR.enum_types_by_name['CourseProductPurchaseType'] = _COURSEPRODUCTPURCHASETYPE
DESCRIPTOR.enum_types_by_name['CourseProductStateType'] = _COURSEPRODUCTSTATETYPE
DESCRIPTOR.enum_types_by_name['CurrencyType'] = _CURRENCYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
