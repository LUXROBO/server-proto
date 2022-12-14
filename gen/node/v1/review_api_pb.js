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
var v1_review_pb = require('../v1/review_pb.js');
goog.object.extend(proto, v1_review_pb);
goog.exportSymbol('proto.v1.ReviewCountRequest', null, global);
goog.exportSymbol('proto.v1.ReviewCountResponse', null, global);
goog.exportSymbol('proto.v1.ReviewGraphqlQueryRequest', null, global);
goog.exportSymbol('proto.v1.ReviewGraphqlQueryResponse', null, global);
goog.exportSymbol('proto.v1.ReviewHealthRequest', null, global);
goog.exportSymbol('proto.v1.ReviewHealthResponse', null, global);
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
proto.v1.ReviewGraphqlQueryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.v1.ReviewGraphqlQueryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.ReviewGraphqlQueryRequest.displayName = 'proto.v1.ReviewGraphqlQueryRequest';
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
proto.v1.ReviewGraphqlQueryResponse = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.v1.ReviewGraphqlQueryResponse, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.ReviewGraphqlQueryResponse.displayName = 'proto.v1.ReviewGraphqlQueryResponse';
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
proto.v1.ReviewCountRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.v1.ReviewCountRequest.repeatedFields_, null);
};
goog.inherits(proto.v1.ReviewCountRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.ReviewCountRequest.displayName = 'proto.v1.ReviewCountRequest';
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
proto.v1.ReviewCountResponse = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.v1.ReviewCountResponse.repeatedFields_, null);
};
goog.inherits(proto.v1.ReviewCountResponse, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.ReviewCountResponse.displayName = 'proto.v1.ReviewCountResponse';
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
proto.v1.ReviewHealthRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.v1.ReviewHealthRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.ReviewHealthRequest.displayName = 'proto.v1.ReviewHealthRequest';
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
proto.v1.ReviewHealthResponse = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.v1.ReviewHealthResponse, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.ReviewHealthResponse.displayName = 'proto.v1.ReviewHealthResponse';
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
proto.v1.ReviewGraphqlQueryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.ReviewGraphqlQueryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.ReviewGraphqlQueryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewGraphqlQueryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    query: jspb.Message.getFieldWithDefault(msg, 1, ""),
    operationname: jspb.Message.getFieldWithDefault(msg, 2, "")
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
 * @return {!proto.v1.ReviewGraphqlQueryRequest}
 */
proto.v1.ReviewGraphqlQueryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.ReviewGraphqlQueryRequest;
  return proto.v1.ReviewGraphqlQueryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.ReviewGraphqlQueryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.ReviewGraphqlQueryRequest}
 */
proto.v1.ReviewGraphqlQueryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setQuery(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setOperationname(value);
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
proto.v1.ReviewGraphqlQueryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.ReviewGraphqlQueryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.ReviewGraphqlQueryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewGraphqlQueryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getQuery();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getOperationname();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
};


/**
 * optional string query = 1;
 * @return {string}
 */
proto.v1.ReviewGraphqlQueryRequest.prototype.getQuery = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/** @param {string} value */
proto.v1.ReviewGraphqlQueryRequest.prototype.setQuery = function(value) {
  jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string operationName = 2;
 * @return {string}
 */
proto.v1.ReviewGraphqlQueryRequest.prototype.getOperationname = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/** @param {string} value */
proto.v1.ReviewGraphqlQueryRequest.prototype.setOperationname = function(value) {
  jspb.Message.setProto3StringField(this, 2, value);
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
proto.v1.ReviewGraphqlQueryResponse.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.ReviewGraphqlQueryResponse.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.ReviewGraphqlQueryResponse} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewGraphqlQueryResponse.toObject = function(includeInstance, msg) {
  var f, obj = {
    err: (f = msg.getErr()) && v1_base_pb.Error.toObject(includeInstance, f),
    result: jspb.Message.getFieldWithDefault(msg, 2, "")
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
 * @return {!proto.v1.ReviewGraphqlQueryResponse}
 */
proto.v1.ReviewGraphqlQueryResponse.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.ReviewGraphqlQueryResponse;
  return proto.v1.ReviewGraphqlQueryResponse.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.ReviewGraphqlQueryResponse} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.ReviewGraphqlQueryResponse}
 */
proto.v1.ReviewGraphqlQueryResponse.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new v1_base_pb.Error;
      reader.readMessage(value,v1_base_pb.Error.deserializeBinaryFromReader);
      msg.setErr(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setResult(value);
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
proto.v1.ReviewGraphqlQueryResponse.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.ReviewGraphqlQueryResponse.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.ReviewGraphqlQueryResponse} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewGraphqlQueryResponse.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getErr();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      v1_base_pb.Error.serializeBinaryToWriter
    );
  }
  f = message.getResult();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
};


/**
 * optional Error err = 1;
 * @return {?proto.v1.Error}
 */
proto.v1.ReviewGraphqlQueryResponse.prototype.getErr = function() {
  return /** @type{?proto.v1.Error} */ (
    jspb.Message.getWrapperField(this, v1_base_pb.Error, 1));
};


/** @param {?proto.v1.Error|undefined} value */
proto.v1.ReviewGraphqlQueryResponse.prototype.setErr = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


/**
 * Clears the message field making it undefined.
 */
proto.v1.ReviewGraphqlQueryResponse.prototype.clearErr = function() {
  this.setErr(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.v1.ReviewGraphqlQueryResponse.prototype.hasErr = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional string result = 2;
 * @return {string}
 */
proto.v1.ReviewGraphqlQueryResponse.prototype.getResult = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/** @param {string} value */
proto.v1.ReviewGraphqlQueryResponse.prototype.setResult = function(value) {
  jspb.Message.setProto3StringField(this, 2, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.v1.ReviewCountRequest.repeatedFields_ = [1];



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
proto.v1.ReviewCountRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.ReviewCountRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.ReviewCountRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewCountRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    lessonidsList: (f = jspb.Message.getRepeatedField(msg, 1)) == null ? undefined : f
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
 * @return {!proto.v1.ReviewCountRequest}
 */
proto.v1.ReviewCountRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.ReviewCountRequest;
  return proto.v1.ReviewCountRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.ReviewCountRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.ReviewCountRequest}
 */
proto.v1.ReviewCountRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.addLessonids(value);
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
proto.v1.ReviewCountRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.ReviewCountRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.ReviewCountRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewCountRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLessonidsList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      1,
      f
    );
  }
};


/**
 * repeated string lessonIds = 1;
 * @return {!Array<string>}
 */
proto.v1.ReviewCountRequest.prototype.getLessonidsList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 1));
};


/** @param {!Array<string>} value */
proto.v1.ReviewCountRequest.prototype.setLessonidsList = function(value) {
  jspb.Message.setField(this, 1, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 */
proto.v1.ReviewCountRequest.prototype.addLessonids = function(value, opt_index) {
  jspb.Message.addToRepeatedField(this, 1, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 */
proto.v1.ReviewCountRequest.prototype.clearLessonidsList = function() {
  this.setLessonidsList([]);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.v1.ReviewCountResponse.repeatedFields_ = [2];



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
proto.v1.ReviewCountResponse.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.ReviewCountResponse.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.ReviewCountResponse} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewCountResponse.toObject = function(includeInstance, msg) {
  var f, obj = {
    err: (f = msg.getErr()) && v1_base_pb.Error.toObject(includeInstance, f),
    countsList: jspb.Message.toObjectList(msg.getCountsList(),
    v1_review_pb.ReviewCountE.toObject, includeInstance)
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
 * @return {!proto.v1.ReviewCountResponse}
 */
proto.v1.ReviewCountResponse.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.ReviewCountResponse;
  return proto.v1.ReviewCountResponse.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.ReviewCountResponse} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.ReviewCountResponse}
 */
proto.v1.ReviewCountResponse.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new v1_base_pb.Error;
      reader.readMessage(value,v1_base_pb.Error.deserializeBinaryFromReader);
      msg.setErr(value);
      break;
    case 2:
      var value = new v1_review_pb.ReviewCountE;
      reader.readMessage(value,v1_review_pb.ReviewCountE.deserializeBinaryFromReader);
      msg.addCounts(value);
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
proto.v1.ReviewCountResponse.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.ReviewCountResponse.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.ReviewCountResponse} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewCountResponse.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getErr();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      v1_base_pb.Error.serializeBinaryToWriter
    );
  }
  f = message.getCountsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      2,
      f,
      v1_review_pb.ReviewCountE.serializeBinaryToWriter
    );
  }
};


/**
 * optional Error err = 1;
 * @return {?proto.v1.Error}
 */
proto.v1.ReviewCountResponse.prototype.getErr = function() {
  return /** @type{?proto.v1.Error} */ (
    jspb.Message.getWrapperField(this, v1_base_pb.Error, 1));
};


/** @param {?proto.v1.Error|undefined} value */
proto.v1.ReviewCountResponse.prototype.setErr = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


/**
 * Clears the message field making it undefined.
 */
proto.v1.ReviewCountResponse.prototype.clearErr = function() {
  this.setErr(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.v1.ReviewCountResponse.prototype.hasErr = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * repeated ReviewCountE counts = 2;
 * @return {!Array<!proto.v1.ReviewCountE>}
 */
proto.v1.ReviewCountResponse.prototype.getCountsList = function() {
  return /** @type{!Array<!proto.v1.ReviewCountE>} */ (
    jspb.Message.getRepeatedWrapperField(this, v1_review_pb.ReviewCountE, 2));
};


/** @param {!Array<!proto.v1.ReviewCountE>} value */
proto.v1.ReviewCountResponse.prototype.setCountsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 2, value);
};


/**
 * @param {!proto.v1.ReviewCountE=} opt_value
 * @param {number=} opt_index
 * @return {!proto.v1.ReviewCountE}
 */
proto.v1.ReviewCountResponse.prototype.addCounts = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 2, opt_value, proto.v1.ReviewCountE, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 */
proto.v1.ReviewCountResponse.prototype.clearCountsList = function() {
  this.setCountsList([]);
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
proto.v1.ReviewHealthRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.ReviewHealthRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.ReviewHealthRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewHealthRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

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
 * @return {!proto.v1.ReviewHealthRequest}
 */
proto.v1.ReviewHealthRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.ReviewHealthRequest;
  return proto.v1.ReviewHealthRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.ReviewHealthRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.ReviewHealthRequest}
 */
proto.v1.ReviewHealthRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
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
proto.v1.ReviewHealthRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.ReviewHealthRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.ReviewHealthRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewHealthRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
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
proto.v1.ReviewHealthResponse.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.ReviewHealthResponse.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.ReviewHealthResponse} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewHealthResponse.toObject = function(includeInstance, msg) {
  var f, obj = {
    err: (f = msg.getErr()) && v1_base_pb.Error.toObject(includeInstance, f),
    status: jspb.Message.getBooleanFieldWithDefault(msg, 2, false)
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
 * @return {!proto.v1.ReviewHealthResponse}
 */
proto.v1.ReviewHealthResponse.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.ReviewHealthResponse;
  return proto.v1.ReviewHealthResponse.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.ReviewHealthResponse} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.ReviewHealthResponse}
 */
proto.v1.ReviewHealthResponse.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new v1_base_pb.Error;
      reader.readMessage(value,v1_base_pb.Error.deserializeBinaryFromReader);
      msg.setErr(value);
      break;
    case 2:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setStatus(value);
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
proto.v1.ReviewHealthResponse.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.ReviewHealthResponse.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.ReviewHealthResponse} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.ReviewHealthResponse.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getErr();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      v1_base_pb.Error.serializeBinaryToWriter
    );
  }
  f = message.getStatus();
  if (f) {
    writer.writeBool(
      2,
      f
    );
  }
};


/**
 * optional Error err = 1;
 * @return {?proto.v1.Error}
 */
proto.v1.ReviewHealthResponse.prototype.getErr = function() {
  return /** @type{?proto.v1.Error} */ (
    jspb.Message.getWrapperField(this, v1_base_pb.Error, 1));
};


/** @param {?proto.v1.Error|undefined} value */
proto.v1.ReviewHealthResponse.prototype.setErr = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


/**
 * Clears the message field making it undefined.
 */
proto.v1.ReviewHealthResponse.prototype.clearErr = function() {
  this.setErr(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.v1.ReviewHealthResponse.prototype.hasErr = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional bool status = 2;
 * @return {boolean}
 */
proto.v1.ReviewHealthResponse.prototype.getStatus = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 2, false));
};


/** @param {boolean} value */
proto.v1.ReviewHealthResponse.prototype.setStatus = function(value) {
  jspb.Message.setProto3BooleanField(this, 2, value);
};


goog.object.extend(exports, proto.v1);
