/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

goog.exportSymbol('proto.v1.ClassroomOpenType', null, global);
goog.exportSymbol('proto.v1.CourseProductDType', null, global);
goog.exportSymbol('proto.v1.CourseProductPurchaseType', null, global);
goog.exportSymbol('proto.v1.CourseProductStateType', null, global);
goog.exportSymbol('proto.v1.CreationType', null, global);
goog.exportSymbol('proto.v1.CurrencyType', null, global);
goog.exportSymbol('proto.v1.DiscountType', null, global);
goog.exportSymbol('proto.v1.LessonCodingType', null, global);
goog.exportSymbol('proto.v1.LessonContentViewType', null, global);
goog.exportSymbol('proto.v1.LessonGroupType', null, global);
goog.exportSymbol('proto.v1.LessonHardwareType', null, global);
goog.exportSymbol('proto.v1.LessonLevelType', null, global);
goog.exportSymbol('proto.v1.LessonOpenType', null, global);
goog.exportSymbol('proto.v1.LessonPlanContentType', null, global);
goog.exportSymbol('proto.v1.LessonPlanDataType', null, global);
goog.exportSymbol('proto.v1.LessonPlanViewType', null, global);
goog.exportSymbol('proto.v1.LessonSummaryElementType', null, global);
goog.exportSymbol('proto.v1.LessonType', null, global);
goog.exportSymbol('proto.v1.LivekitDataPacketKindType', null, global);
goog.exportSymbol('proto.v1.LivekitParticipantStateType', null, global);
goog.exportSymbol('proto.v1.LivekitTrackSourceType', null, global);
goog.exportSymbol('proto.v1.LivekitVideoQualityType', null, global);
goog.exportSymbol('proto.v1.ProjectCodeType', null, global);
goog.exportSymbol('proto.v1.ServiceType', null, global);
goog.exportSymbol('proto.v1.TrueFalseType', null, global);
goog.exportSymbol('proto.v1.UserLoginType', null, global);
goog.exportSymbol('proto.v1.VideoType', null, global);
/**
 * @enum {number}
 */
proto.v1.DiscountType = {
  PERCENT: 0,
  VALUE: 1
};

/**
 * @enum {number}
 */
proto.v1.ProjectCodeType = {
  SCRATCH: 0,
  ENTRY: 1,
  PYMODI: 2
};

/**
 * @enum {number}
 */
proto.v1.VideoType = {
  HLS: 0,
  DASH: 1,
  YOUTUBE: 2
};

/**
 * @enum {number}
 */
proto.v1.LessonType = {
  LESSON: 0,
  LESSON_CURRICULUM: 1,
  LESSON_BOOK: 2,
  LESSON_NONE: 3
};

/**
 * @enum {number}
 */
proto.v1.ServiceType = {
  NONE_TYPE: 0,
  LMS: 1,
  MAKING_PACK: 2,
  CENGAGE: 3,
  BRICK_PACK: 4
};

/**
 * @enum {number}
 */
proto.v1.LessonLevelType = {
  NONE_LEVEL: 0,
  BEGINNING_LEVEL: 1,
  INTERMEDIATE_LEVEL: 2,
  HIGH_LEVEL: 3
};

/**
 * @enum {number}
 */
proto.v1.LessonGroupType = {
  NONE_GROUP: 0,
  PRE_SCHOOLER_GROUP: 1,
  ELEMENT_BEGINNING_GROUP: 2,
  ELEMENT_HIGH_GROUP: 3,
  MIDDLE_SCHOOLER_GROUP: 4,
  HIGH_SCHOOLER_GROUP: 5
};

/**
 * @enum {number}
 */
proto.v1.LessonPlanViewType = {
  LESSON_PLAN_NONE_VIEW: 0,
  LESSON_PLAN_SLIDE_VIEW: 1
};

/**
 * @enum {number}
 */
proto.v1.LessonPlanContentType = {
  NONE_CONTENT: 0,
  BASE_CONTENT: 1,
  VIDEO_CONTENT: 2,
  MULTI_CONTENT: 3
};

/**
 * @enum {number}
 */
proto.v1.LessonContentViewType = {
  NONE_VIEW: 0,
  VIDEO_VIEW: 1,
  CODING_VIEW: 2,
  NORMAL_VIEW: 3,
  PRACTICE_CODING_VIEW: 4,
  HORIZON_FULL_VERTICAL_DOWN_HALF_VIEW: 5,
  VERTICAL_FULL_HORIZON_RIGHT_HALF_VIEW: 6,
  VERTICAL_FULL_VIEW: 7,
  VERTICAL_TWO_FULL_VIEW: 8,
  HORIZON_FULL_VERTICAL_FULL_VIEW: 9,
  HORIZON_FULL_VIEW: 10,
  SLIDE_VIEW: 11
};

/**
 * @enum {number}
 */
proto.v1.TrueFalseType = {
  T: 0,
  F: 1
};

/**
 * @enum {number}
 */
proto.v1.ClassroomOpenType = {
  CLASSROOM_OPEN: 0,
  CLASSROOM_CLOSE: 1
};

/**
 * @enum {number}
 */
proto.v1.LessonOpenType = {
  OPEN: 0,
  CLOSE: 1,
  ALL: 2,
  DELETE: 3
};

/**
 * @enum {number}
 */
proto.v1.LessonPlanDataType = {
  BASE: 0,
  TEXT: 1,
  IMAGE: 2,
  VIDEO: 3,
  CODING: 4
};

/**
 * @enum {number}
 */
proto.v1.LessonSummaryElementType = {
  DATA_STRUCTURE_ELEMENT: 0,
  ANALYSIS_ELEMENT: 1,
  ABSTRACT_ELEMENT: 2,
  ALGORITHM_ELEMENT: 3,
  AUTOMATION_ELEMENT: 4,
  SIMULATION_ELEMENT: 5,
  PARALLELISM_ELEMENT: 6
};

/**
 * @enum {number}
 */
proto.v1.LessonHardwareType = {
  NONE_HARDWARE: 0,
  MODI1_HARDWARE: 1,
  MODI2_HARDWARE: 2,
  RASPBERRY_HARDWARE: 3,
  MICROBIT_HARDWARE: 4,
  HELLO_AI_HARDWARE: 5
};

/**
 * @enum {number}
 */
proto.v1.LessonCodingType = {
  ENTRY_CODING: 0,
  SCRATCH_CODING: 1,
  PYMODI_CODING: 2
};

/**
 * @enum {number}
 */
proto.v1.CreationType = {
  FREE: 0,
  BINGO_MACHINE: 1,
  RANDOM_ROULETTE: 2,
  ROTATING_PENCIL_HOLDER: 3,
  JOYTROPE: 4,
  LED_TIMER: 5,
  MOOD_LAMP: 6,
  LED_METRONIUM: 7,
  SAFE: 8,
  FISHING: 9,
  SURFING_BOT: 10,
  TONGS_ARM: 11,
  RC_CAR: 12,
  PIRATE_SHIP: 13,
  CROCODILE_TEETH: 14,
  LIGHTHOUSE: 15,
  HELICOPTER: 16,
  MONSTER_TRUCK: 17
};

/**
 * @enum {number}
 */
proto.v1.LivekitParticipantStateType = {
  JOINING: 0,
  JOINED: 1,
  ACTIVE: 2,
  DISCONNECTED: 3
};

/**
 * @enum {number}
 */
proto.v1.LivekitTrackSourceType = {
  UNKNOWN: 0,
  CAMERA: 1,
  MICROPHONE: 2,
  SCREEN_SHARE: 3,
  SCREEN_SHARE_AUDIO: 4
};

/**
 * @enum {number}
 */
proto.v1.LivekitVideoQualityType = {
  LOW: 0,
  MEDIUM: 1,
  HIGH: 2
};

/**
 * @enum {number}
 */
proto.v1.UserLoginType = {
  EMAIL: 0,
  KAKAO: 1,
  GOOGLE: 2
};

/**
 * @enum {number}
 */
proto.v1.LivekitDataPacketKindType = {
  RELIABLE: 0,
  LOSSY: 1
};

/**
 * @enum {number}
 */
proto.v1.CourseProductDType = {
  MERCHANDISE: 0,
  COURSE: 1
};

/**
 * @enum {number}
 */
proto.v1.CourseProductPurchaseType = {
  PURCHASE: 0,
  RENTAL: 1
};

/**
 * @enum {number}
 */
proto.v1.CourseProductStateType = {
  ON: 0,
  OFF: 1,
  SOLDOUT: 2
};

/**
 * @enum {number}
 */
proto.v1.CurrencyType = {
  KRW: 0
};

goog.object.extend(exports, proto.v1);
