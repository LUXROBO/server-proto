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

var v1_base_pb = require('../v1/base_pb.js');
goog.object.extend(proto, v1_base_pb);
goog.exportSymbol('proto.v1.UploadImageE', null, global);
goog.exportSymbol('proto.v1.UploadImagesE', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.v1.UploadImageE = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.v1.UploadImageE, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.UploadImageE.displayName = 'proto.v1.UploadImageE';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.v1.UploadImagesE = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.v1.UploadImagesE.repeatedFields_, null);
};
goog.inherits(proto.v1.UploadImagesE, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.UploadImagesE.displayName = 'proto.v1.UploadImagesE';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.v1.UploadImageE.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.UploadImageE.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.UploadImageE} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UploadImageE.toObject = function(includeInstance, msg) {
  var f, obj = {
    no: jspb.Message.getFieldWithDefault(msg, 1, 0),
    serviceno: jspb.Message.getFieldWithDefault(msg, 2, 0),
    servicetype: jspb.Message.getFieldWithDefault(msg, 3, ""),
    imagekey: jspb.Message.getFieldWithDefault(msg, 4, ""),
    image: (f = msg.getImage()) && v1_base_pb.ImageInfoE.toObject(includeInstance, f),
    idx: jspb.Message.getFieldWithDefault(msg, 6, 0),
    createdat: jspb.Message.getFieldWithDefault(msg, 7, 0),
    updatedat: jspb.Message.getFieldWithDefault(msg, 8, 0)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.v1.UploadImageE}
 */
proto.v1.UploadImageE.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.UploadImageE;
  return proto.v1.UploadImageE.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.UploadImageE} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.UploadImageE}
 */
proto.v1.UploadImageE.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setNo(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setServiceno(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setServicetype(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setImagekey(value);
      break;
    case 5:
      var value = new v1_base_pb.ImageInfoE;
      reader.readMessage(value,v1_base_pb.ImageInfoE.deserializeBinaryFromReader);
      msg.setImage(value);
      break;
    case 6:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setIdx(value);
      break;
    case 7:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setCreatedat(value);
      break;
    case 8:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setUpdatedat(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.v1.UploadImageE.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.UploadImageE.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.UploadImageE} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UploadImageE.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getNo();
  if (f !== 0) {
    writer.writeInt64(
      1,
      f
    );
  }
  f = message.getServiceno();
  if (f !== 0) {
    writer.writeInt64(
      2,
      f
    );
  }
  f = message.getServicetype();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getImagekey();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = message.getImage();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      v1_base_pb.ImageInfoE.serializeBinaryToWriter
    );
  }
  f = message.getIdx();
  if (f !== 0) {
    writer.writeInt32(
      6,
      f
    );
  }
  f = message.getCreatedat();
  if (f !== 0) {
    writer.writeInt64(
      7,
      f
    );
  }
  f = message.getUpdatedat();
  if (f !== 0) {
    writer.writeInt64(
      8,
      f
    );
  }
};


/**
 * optional int64 no = 1;
 * @return {number}
 */
proto.v1.UploadImageE.prototype.getNo = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.v1.UploadImageE.prototype.setNo = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional int64 serviceNo = 2;
 * @return {number}
 */
proto.v1.UploadImageE.prototype.getServiceno = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/** @param {number} value */
proto.v1.UploadImageE.prototype.setServiceno = function(value) {
  jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional string serviceType = 3;
 * @return {string}
 */
proto.v1.UploadImageE.prototype.getServicetype = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/** @param {string} value */
proto.v1.UploadImageE.prototype.setServicetype = function(value) {
  jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * optional string imageKey = 4;
 * @return {string}
 */
proto.v1.UploadImageE.prototype.getImagekey = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/** @param {string} value */
proto.v1.UploadImageE.prototype.setImagekey = function(value) {
  jspb.Message.setProto3StringField(this, 4, value);
};


/**
 * optional ImageInfoE image = 5;
 * @return {?proto.v1.ImageInfoE}
 */
proto.v1.UploadImageE.prototype.getImage = function() {
  return /** @type{?proto.v1.ImageInfoE} */ (
    jspb.Message.getWrapperField(this, v1_base_pb.ImageInfoE, 5));
};


/** @param {?proto.v1.ImageInfoE|undefined} value */
proto.v1.UploadImageE.prototype.setImage = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


/**
 * Clears the message field making it undefined.
 */
proto.v1.UploadImageE.prototype.clearImage = function() {
  this.setImage(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.v1.UploadImageE.prototype.hasImage = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional int32 idx = 6;
 * @return {number}
 */
proto.v1.UploadImageE.prototype.getIdx = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 6, 0));
};


/** @param {number} value */
proto.v1.UploadImageE.prototype.setIdx = function(value) {
  jspb.Message.setProto3IntField(this, 6, value);
};


/**
 * optional int64 createdAt = 7;
 * @return {number}
 */
proto.v1.UploadImageE.prototype.getCreatedat = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 7, 0));
};


/** @param {number} value */
proto.v1.UploadImageE.prototype.setCreatedat = function(value) {
  jspb.Message.setProto3IntField(this, 7, value);
};


/**
 * optional int64 updatedAt = 8;
 * @return {number}
 */
proto.v1.UploadImageE.prototype.getUpdatedat = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 8, 0));
};


/** @param {number} value */
proto.v1.UploadImageE.prototype.setUpdatedat = function(value) {
  jspb.Message.setProto3IntField(this, 8, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.v1.UploadImagesE.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.v1.UploadImagesE.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.UploadImagesE.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.UploadImagesE} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UploadImagesE.toObject = function(includeInstance, msg) {
  var f, obj = {
    imagesList: jspb.Message.toObjectList(msg.getImagesList(),
    proto.v1.UploadImageE.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.v1.UploadImagesE}
 */
proto.v1.UploadImagesE.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.UploadImagesE;
  return proto.v1.UploadImagesE.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.UploadImagesE} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.UploadImagesE}
 */
proto.v1.UploadImagesE.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.v1.UploadImageE;
      reader.readMessage(value,proto.v1.UploadImageE.deserializeBinaryFromReader);
      msg.addImages(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.v1.UploadImagesE.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.UploadImagesE.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.UploadImagesE} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UploadImagesE.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getImagesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.v1.UploadImageE.serializeBinaryToWriter
    );
  }
};


/**
 * repeated UploadImageE images = 1;
 * @return {!Array<!proto.v1.UploadImageE>}
 */
proto.v1.UploadImagesE.prototype.getImagesList = function() {
  return /** @type{!Array<!proto.v1.UploadImageE>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.v1.UploadImageE, 1));
};


/** @param {!Array<!proto.v1.UploadImageE>} value */
proto.v1.UploadImagesE.prototype.setImagesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.v1.UploadImageE=} opt_value
 * @param {number=} opt_index
 * @return {!proto.v1.UploadImageE}
 */
proto.v1.UploadImagesE.prototype.addImages = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.v1.UploadImageE, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 */
proto.v1.UploadImagesE.prototype.clearImagesList = function() {
  this.setImagesList([]);
};


goog.object.extend(exports, proto.v1);
