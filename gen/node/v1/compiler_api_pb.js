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
goog.exportSymbol('proto.v1.CompilerHealthRequest', null, global);
goog.exportSymbol('proto.v1.CompilerHealthResponse', null, global);
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
proto.v1.CompilerHealthRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.v1.CompilerHealthRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.CompilerHealthRequest.displayName = 'proto.v1.CompilerHealthRequest';
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
proto.v1.CompilerHealthResponse = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.v1.CompilerHealthResponse, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.v1.CompilerHealthResponse.displayName = 'proto.v1.CompilerHealthResponse';
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
proto.v1.CompilerHealthRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.CompilerHealthRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.CompilerHealthRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.CompilerHealthRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.v1.CompilerHealthRequest}
 */
proto.v1.CompilerHealthRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.CompilerHealthRequest;
  return proto.v1.CompilerHealthRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.CompilerHealthRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.CompilerHealthRequest}
 */
proto.v1.CompilerHealthRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.v1.CompilerHealthRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.CompilerHealthRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.CompilerHealthRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.CompilerHealthRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.v1.CompilerHealthResponse.prototype.toObject = function(opt_includeInstance) {
  return proto.v1.CompilerHealthResponse.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.v1.CompilerHealthResponse} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.CompilerHealthResponse.toObject = function(includeInstance, msg) {
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
 * @return {!proto.v1.CompilerHealthResponse}
 */
proto.v1.CompilerHealthResponse.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.v1.CompilerHealthResponse;
  return proto.v1.CompilerHealthResponse.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.v1.CompilerHealthResponse} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.v1.CompilerHealthResponse}
 */
proto.v1.CompilerHealthResponse.deserializeBinaryFromReader = function(msg, reader) {
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
proto.v1.CompilerHealthResponse.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.v1.CompilerHealthResponse.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.v1.CompilerHealthResponse} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.v1.CompilerHealthResponse.serializeBinaryToWriter = function(message, writer) {
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
proto.v1.CompilerHealthResponse.prototype.getErr = function() {
  return /** @type{?proto.v1.Error} */ (
    jspb.Message.getWrapperField(this, v1_base_pb.Error, 1));
};


/** @param {?proto.v1.Error|undefined} value */
proto.v1.CompilerHealthResponse.prototype.setErr = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


/**
 * Clears the message field making it undefined.
 */
proto.v1.CompilerHealthResponse.prototype.clearErr = function() {
  this.setErr(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.v1.CompilerHealthResponse.prototype.hasErr = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional bool status = 2;
 * @return {boolean}
 */
proto.v1.CompilerHealthResponse.prototype.getStatus = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 2, false));
};


/** @param {boolean} value */
proto.v1.CompilerHealthResponse.prototype.setStatus = function(value) {
  jspb.Message.setProto3BooleanField(this, 2, value);
};


goog.object.extend(exports, proto.v1);
