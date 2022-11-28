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
goog.exportSymbol('proto.v1.UserDeviceE', null, global);
goog.exportSymbol('proto.v1.UserE', null, global);
goog.exportSymbol('proto.v1.UserProfileE', null, global);
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
proto.v1.UserE = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.v1.UserE.repeatedFields_, null);
};
goog.inherits(proto.v1.UserE, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.UserE.displayName = 'proto.v1.UserE';
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
proto.v1.UserProfileE = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.v1.UserProfileE.repeatedFields_, null);
};
goog.inherits(proto.v1.UserProfileE, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.UserProfileE.displayName = 'proto.v1.UserProfileE';
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
proto.v1.UserDeviceE = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.v1.UserDeviceE, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.UserDeviceE.displayName = 'proto.v1.UserDeviceE';
}

/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.v1.UserE.repeatedFields_ = [4,5];



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
proto.v1.UserE.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.UserE.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.UserE} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UserE.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: jspb.Message.getFieldWithDefault(msg, 1, ""),
    email: jspb.Message.getFieldWithDefault(msg, 2, ""),
    state: jspb.Message.getFieldWithDefault(msg, 3, ""),
    profilesList: jspb.Message.toObjectList(msg.getProfilesList(),
    proto.v1.UserProfileE.toObject, includeInstance),
    devicesList: jspb.Message.toObjectList(msg.getDevicesList(),
    proto.v1.UserDeviceE.toObject, includeInstance),
    lastlogindate: jspb.Message.getFieldWithDefault(msg, 6, ""),
    emailverified: jspb.Message.getBooleanFieldWithDefault(msg, 7, false),
    phoneverified: jspb.Message.getBooleanFieldWithDefault(msg, 8, false),
    createdat: jspb.Message.getFieldWithDefault(msg, 9, 0),
    updatedat: jspb.Message.getFieldWithDefault(msg, 10, 0),
    deletedat: jspb.Message.getFieldWithDefault(msg, 11, 0)
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
 * @return {!proto.v1.UserE}
 */
proto.v1.UserE.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.UserE;
  return proto.v1.UserE.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.UserE} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.UserE}
 */
proto.v1.UserE.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setId(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setEmail(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setState(value);
      break;
    case 4:
      var value = new proto.v1.UserProfileE;
      reader.readMessage(value,proto.v1.UserProfileE.deserializeBinaryFromReader);
      msg.addProfiles(value);
      break;
    case 5:
      var value = new proto.v1.UserDeviceE;
      reader.readMessage(value,proto.v1.UserDeviceE.deserializeBinaryFromReader);
      msg.addDevices(value);
      break;
    case 6:
      var value = /** @type {string} */ (reader.readString());
      msg.setLastlogindate(value);
      break;
    case 7:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setEmailverified(value);
      break;
    case 8:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setPhoneverified(value);
      break;
    case 9:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setCreatedat(value);
      break;
    case 10:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setUpdatedat(value);
      break;
    case 11:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setDeletedat(value);
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
proto.v1.UserE.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.UserE.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.UserE} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UserE.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getEmail();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getState();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getProfilesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      4,
      f,
      proto.v1.UserProfileE.serializeBinaryToWriter
    );
  }
  f = message.getDevicesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      5,
      f,
      proto.v1.UserDeviceE.serializeBinaryToWriter
    );
  }
  f = message.getLastlogindate();
  if (f.length > 0) {
    writer.writeString(
      6,
      f
    );
  }
  f = message.getEmailverified();
  if (f) {
    writer.writeBool(
      7,
      f
    );
  }
  f = message.getPhoneverified();
  if (f) {
    writer.writeBool(
      8,
      f
    );
  }
  f = message.getCreatedat();
  if (f !== 0) {
    writer.writeInt64(
      9,
      f
    );
  }
  f = message.getUpdatedat();
  if (f !== 0) {
    writer.writeInt64(
      10,
      f
    );
  }
  f = message.getDeletedat();
  if (f !== 0) {
    writer.writeInt64(
      11,
      f
    );
  }
};


/**
 * optional string id = 1;
 * @return {string}
 */
proto.v1.UserE.prototype.getId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/** @param {string} value */
proto.v1.UserE.prototype.setId = function(value) {
  jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string email = 2;
 * @return {string}
 */
proto.v1.UserE.prototype.getEmail = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/** @param {string} value */
proto.v1.UserE.prototype.setEmail = function(value) {
  jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional string state = 3;
 * @return {string}
 */
proto.v1.UserE.prototype.getState = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/** @param {string} value */
proto.v1.UserE.prototype.setState = function(value) {
  jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * repeated UserProfileE profiles = 4;
 * @return {!Array<!proto.v1.UserProfileE>}
 */
proto.v1.UserE.prototype.getProfilesList = function() {
  return /** @type{!Array<!proto.v1.UserProfileE>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.v1.UserProfileE, 4));
};


/** @param {!Array<!proto.v1.UserProfileE>} value */
proto.v1.UserE.prototype.setProfilesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 4, value);
};


/**
 * @param {!proto.v1.UserProfileE=} opt_value
 * @param {number=} opt_index
 * @return {!proto.v1.UserProfileE}
 */
proto.v1.UserE.prototype.addProfiles = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 4, opt_value, proto.v1.UserProfileE, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 */
proto.v1.UserE.prototype.clearProfilesList = function() {
  this.setProfilesList([]);
};


/**
 * repeated UserDeviceE devices = 5;
 * @return {!Array<!proto.v1.UserDeviceE>}
 */
proto.v1.UserE.prototype.getDevicesList = function() {
  return /** @type{!Array<!proto.v1.UserDeviceE>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.v1.UserDeviceE, 5));
};


/** @param {!Array<!proto.v1.UserDeviceE>} value */
proto.v1.UserE.prototype.setDevicesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 5, value);
};


/**
 * @param {!proto.v1.UserDeviceE=} opt_value
 * @param {number=} opt_index
 * @return {!proto.v1.UserDeviceE}
 */
proto.v1.UserE.prototype.addDevices = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 5, opt_value, proto.v1.UserDeviceE, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 */
proto.v1.UserE.prototype.clearDevicesList = function() {
  this.setDevicesList([]);
};


/**
 * optional string lastLoginDate = 6;
 * @return {string}
 */
proto.v1.UserE.prototype.getLastlogindate = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 6, ""));
};


/** @param {string} value */
proto.v1.UserE.prototype.setLastlogindate = function(value) {
  jspb.Message.setProto3StringField(this, 6, value);
};


/**
 * optional bool emailVerified = 7;
 * @return {boolean}
 */
proto.v1.UserE.prototype.getEmailverified = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 7, false));
};


/** @param {boolean} value */
proto.v1.UserE.prototype.setEmailverified = function(value) {
  jspb.Message.setProto3BooleanField(this, 7, value);
};


/**
 * optional bool phoneVerified = 8;
 * @return {boolean}
 */
proto.v1.UserE.prototype.getPhoneverified = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 8, false));
};


/** @param {boolean} value */
proto.v1.UserE.prototype.setPhoneverified = function(value) {
  jspb.Message.setProto3BooleanField(this, 8, value);
};


/**
 * optional int64 createdAt = 9;
 * @return {number}
 */
proto.v1.UserE.prototype.getCreatedat = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 9, 0));
};


/** @param {number} value */
proto.v1.UserE.prototype.setCreatedat = function(value) {
  jspb.Message.setProto3IntField(this, 9, value);
};


/**
 * optional int64 updatedAt = 10;
 * @return {number}
 */
proto.v1.UserE.prototype.getUpdatedat = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 10, 0));
};


/** @param {number} value */
proto.v1.UserE.prototype.setUpdatedat = function(value) {
  jspb.Message.setProto3IntField(this, 10, value);
};


/**
 * optional int64 deletedAt = 11;
 * @return {number}
 */
proto.v1.UserE.prototype.getDeletedat = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 11, 0));
};


/** @param {number} value */
proto.v1.UserE.prototype.setDeletedat = function(value) {
  jspb.Message.setProto3IntField(this, 11, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.v1.UserProfileE.repeatedFields_ = [8];



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
proto.v1.UserProfileE.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.UserProfileE.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.UserProfileE} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UserProfileE.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: jspb.Message.getFieldWithDefault(msg, 1, ""),
    name: jspb.Message.getFieldWithDefault(msg, 2, ""),
    phone: jspb.Message.getFieldWithDefault(msg, 3, ""),
    birth: jspb.Message.getFieldWithDefault(msg, 4, ""),
    role: jspb.Message.getFieldWithDefault(msg, 5, ""),
    roleval: jspb.Message.getFieldWithDefault(msg, 6, 0),
    avatar: (f = msg.getAvatar()) && v1_base_pb.ImageInfoE.toObject(includeInstance, f),
    codingtypesList: (f = jspb.Message.getRepeatedField(msg, 8)) == null ? undefined : f,
    createdat: jspb.Message.getFieldWithDefault(msg, 9, 0),
    updatedat: jspb.Message.getFieldWithDefault(msg, 10, 0)
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
 * @return {!proto.v1.UserProfileE}
 */
proto.v1.UserProfileE.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.UserProfileE;
  return proto.v1.UserProfileE.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.UserProfileE} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.UserProfileE}
 */
proto.v1.UserProfileE.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setId(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setName(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setPhone(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setBirth(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setRole(value);
      break;
    case 6:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setRoleval(value);
      break;
    case 7:
      var value = new v1_base_pb.ImageInfoE;
      reader.readMessage(value,v1_base_pb.ImageInfoE.deserializeBinaryFromReader);
      msg.setAvatar(value);
      break;
    case 8:
      var value = /** @type {string} */ (reader.readString());
      msg.addCodingtypes(value);
      break;
    case 9:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setCreatedat(value);
      break;
    case 10:
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
proto.v1.UserProfileE.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.UserProfileE.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.UserProfileE} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UserProfileE.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getName();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getPhone();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getBirth();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = message.getRole();
  if (f.length > 0) {
    writer.writeString(
      5,
      f
    );
  }
  f = message.getRoleval();
  if (f !== 0) {
    writer.writeInt64(
      6,
      f
    );
  }
  f = message.getAvatar();
  if (f != null) {
    writer.writeMessage(
      7,
      f,
      v1_base_pb.ImageInfoE.serializeBinaryToWriter
    );
  }
  f = message.getCodingtypesList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      8,
      f
    );
  }
  f = message.getCreatedat();
  if (f !== 0) {
    writer.writeInt64(
      9,
      f
    );
  }
  f = message.getUpdatedat();
  if (f !== 0) {
    writer.writeInt64(
      10,
      f
    );
  }
};


/**
 * optional string id = 1;
 * @return {string}
 */
proto.v1.UserProfileE.prototype.getId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/** @param {string} value */
proto.v1.UserProfileE.prototype.setId = function(value) {
  jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string name = 2;
 * @return {string}
 */
proto.v1.UserProfileE.prototype.getName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/** @param {string} value */
proto.v1.UserProfileE.prototype.setName = function(value) {
  jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional string phone = 3;
 * @return {string}
 */
proto.v1.UserProfileE.prototype.getPhone = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/** @param {string} value */
proto.v1.UserProfileE.prototype.setPhone = function(value) {
  jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * optional string birth = 4;
 * @return {string}
 */
proto.v1.UserProfileE.prototype.getBirth = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/** @param {string} value */
proto.v1.UserProfileE.prototype.setBirth = function(value) {
  jspb.Message.setProto3StringField(this, 4, value);
};


/**
 * optional string role = 5;
 * @return {string}
 */
proto.v1.UserProfileE.prototype.getRole = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 5, ""));
};


/** @param {string} value */
proto.v1.UserProfileE.prototype.setRole = function(value) {
  jspb.Message.setProto3StringField(this, 5, value);
};


/**
 * optional int64 roleVal = 6;
 * @return {number}
 */
proto.v1.UserProfileE.prototype.getRoleval = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 6, 0));
};


/** @param {number} value */
proto.v1.UserProfileE.prototype.setRoleval = function(value) {
  jspb.Message.setProto3IntField(this, 6, value);
};


/**
 * optional ImageInfoE avatar = 7;
 * @return {?proto.v1.ImageInfoE}
 */
proto.v1.UserProfileE.prototype.getAvatar = function() {
  return /** @type{?proto.v1.ImageInfoE} */ (
    jspb.Message.getWrapperField(this, v1_base_pb.ImageInfoE, 7));
};


/** @param {?proto.v1.ImageInfoE|undefined} value */
proto.v1.UserProfileE.prototype.setAvatar = function(value) {
  jspb.Message.setWrapperField(this, 7, value);
};


/**
 * Clears the message field making it undefined.
 */
proto.v1.UserProfileE.prototype.clearAvatar = function() {
  this.setAvatar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.v1.UserProfileE.prototype.hasAvatar = function() {
  return jspb.Message.getField(this, 7) != null;
};


/**
 * repeated string codingTypes = 8;
 * @return {!Array<string>}
 */
proto.v1.UserProfileE.prototype.getCodingtypesList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 8));
};


/** @param {!Array<string>} value */
proto.v1.UserProfileE.prototype.setCodingtypesList = function(value) {
  jspb.Message.setField(this, 8, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 */
proto.v1.UserProfileE.prototype.addCodingtypes = function(value, opt_index) {
  jspb.Message.addToRepeatedField(this, 8, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 */
proto.v1.UserProfileE.prototype.clearCodingtypesList = function() {
  this.setCodingtypesList([]);
};


/**
 * optional int64 createdAt = 9;
 * @return {number}
 */
proto.v1.UserProfileE.prototype.getCreatedat = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 9, 0));
};


/** @param {number} value */
proto.v1.UserProfileE.prototype.setCreatedat = function(value) {
  jspb.Message.setProto3IntField(this, 9, value);
};


/**
 * optional int64 updatedAt = 10;
 * @return {number}
 */
proto.v1.UserProfileE.prototype.getUpdatedat = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 10, 0));
};


/** @param {number} value */
proto.v1.UserProfileE.prototype.setUpdatedat = function(value) {
  jspb.Message.setProto3IntField(this, 10, value);
};





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
proto.v1.UserDeviceE.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.UserDeviceE.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.UserDeviceE} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UserDeviceE.toObject = function(includeInstance, msg) {
  var f, obj = {
    uuid: jspb.Message.getFieldWithDefault(msg, 1, "")
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
 * @return {!proto.v1.UserDeviceE}
 */
proto.v1.UserDeviceE.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.UserDeviceE;
  return proto.v1.UserDeviceE.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.UserDeviceE} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.UserDeviceE}
 */
proto.v1.UserDeviceE.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setUuid(value);
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
proto.v1.UserDeviceE.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.UserDeviceE.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.UserDeviceE} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.UserDeviceE.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getUuid();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
};


/**
 * optional string uuid = 1;
 * @return {string}
 */
proto.v1.UserDeviceE.prototype.getUuid = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/** @param {string} value */
proto.v1.UserDeviceE.prototype.setUuid = function(value) {
  jspb.Message.setProto3StringField(this, 1, value);
};


goog.object.extend(exports, proto.v1);
