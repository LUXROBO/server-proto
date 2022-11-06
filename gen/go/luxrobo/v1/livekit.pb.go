// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.8.0
// source: v1/livekit.proto

package v1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type LivekitRoomE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Sid             string           `protobuf:"bytes,1,opt,name=sid,proto3" json:"sid,omitempty"`
	Name            string           `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	EmptyTimeout    int64            `protobuf:"varint,3,opt,name=emptyTimeout,proto3" json:"emptyTimeout,omitempty"`
	CreationTime    int64            `protobuf:"varint,4,opt,name=creationTime,proto3" json:"creationTime,omitempty"`
	MaxParticipants int64            `protobuf:"varint,5,opt,name=maxParticipants,proto3" json:"maxParticipants,omitempty"`
	TurnPassword    string           `protobuf:"bytes,6,opt,name=turnPassword,proto3" json:"turnPassword,omitempty"`
	EnableCodecs    []*LivekitCodecE `protobuf:"bytes,7,rep,name=enableCodecs,proto3" json:"enableCodecs,omitempty"`
	Metadata        string           `protobuf:"bytes,8,opt,name=metadata,proto3" json:"metadata,omitempty"`
	NumParticipants int64            `protobuf:"varint,9,opt,name=numParticipants,proto3" json:"numParticipants,omitempty"`
}

func (x *LivekitRoomE) Reset() {
	*x = LivekitRoomE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_livekit_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LivekitRoomE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LivekitRoomE) ProtoMessage() {}

func (x *LivekitRoomE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_livekit_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LivekitRoomE.ProtoReflect.Descriptor instead.
func (*LivekitRoomE) Descriptor() ([]byte, []int) {
	return file_v1_livekit_proto_rawDescGZIP(), []int{0}
}

func (x *LivekitRoomE) GetSid() string {
	if x != nil {
		return x.Sid
	}
	return ""
}

func (x *LivekitRoomE) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *LivekitRoomE) GetEmptyTimeout() int64 {
	if x != nil {
		return x.EmptyTimeout
	}
	return 0
}

func (x *LivekitRoomE) GetCreationTime() int64 {
	if x != nil {
		return x.CreationTime
	}
	return 0
}

func (x *LivekitRoomE) GetMaxParticipants() int64 {
	if x != nil {
		return x.MaxParticipants
	}
	return 0
}

func (x *LivekitRoomE) GetTurnPassword() string {
	if x != nil {
		return x.TurnPassword
	}
	return ""
}

func (x *LivekitRoomE) GetEnableCodecs() []*LivekitCodecE {
	if x != nil {
		return x.EnableCodecs
	}
	return nil
}

func (x *LivekitRoomE) GetMetadata() string {
	if x != nil {
		return x.Metadata
	}
	return ""
}

func (x *LivekitRoomE) GetNumParticipants() int64 {
	if x != nil {
		return x.NumParticipants
	}
	return 0
}

type LivekitCodecE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Mime     string `protobuf:"bytes,1,opt,name=mime,proto3" json:"mime,omitempty"`
	FmtpLine string `protobuf:"bytes,2,opt,name=fmtpLine,proto3" json:"fmtpLine,omitempty"`
}

func (x *LivekitCodecE) Reset() {
	*x = LivekitCodecE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_livekit_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LivekitCodecE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LivekitCodecE) ProtoMessage() {}

func (x *LivekitCodecE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_livekit_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LivekitCodecE.ProtoReflect.Descriptor instead.
func (*LivekitCodecE) Descriptor() ([]byte, []int) {
	return file_v1_livekit_proto_rawDescGZIP(), []int{1}
}

func (x *LivekitCodecE) GetMime() string {
	if x != nil {
		return x.Mime
	}
	return ""
}

func (x *LivekitCodecE) GetFmtpLine() string {
	if x != nil {
		return x.FmtpLine
	}
	return ""
}

type LivekitParticipantE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Sid         string           `protobuf:"bytes,1,opt,name=sid,proto3" json:"sid,omitempty"`
	Identity    string           `protobuf:"bytes,2,opt,name=identity,proto3" json:"identity,omitempty"`
	Name        string           `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
	State       string           `protobuf:"bytes,4,opt,name=state,proto3" json:"state,omitempty"`
	Tracks      []*LivekitTrackE `protobuf:"bytes,5,rep,name=tracks,proto3" json:"tracks,omitempty"`
	Metadata    string           `protobuf:"bytes,6,opt,name=metadata,proto3" json:"metadata,omitempty"`
	JoinedAt    int64            `protobuf:"varint,7,opt,name=joinedAt,proto3" json:"joinedAt,omitempty"`
	IsPublisher bool             `protobuf:"varint,8,opt,name=isPublisher,proto3" json:"isPublisher,omitempty"`
}

func (x *LivekitParticipantE) Reset() {
	*x = LivekitParticipantE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_livekit_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LivekitParticipantE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LivekitParticipantE) ProtoMessage() {}

func (x *LivekitParticipantE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_livekit_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LivekitParticipantE.ProtoReflect.Descriptor instead.
func (*LivekitParticipantE) Descriptor() ([]byte, []int) {
	return file_v1_livekit_proto_rawDescGZIP(), []int{2}
}

func (x *LivekitParticipantE) GetSid() string {
	if x != nil {
		return x.Sid
	}
	return ""
}

func (x *LivekitParticipantE) GetIdentity() string {
	if x != nil {
		return x.Identity
	}
	return ""
}

func (x *LivekitParticipantE) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *LivekitParticipantE) GetState() string {
	if x != nil {
		return x.State
	}
	return ""
}

func (x *LivekitParticipantE) GetTracks() []*LivekitTrackE {
	if x != nil {
		return x.Tracks
	}
	return nil
}

func (x *LivekitParticipantE) GetMetadata() string {
	if x != nil {
		return x.Metadata
	}
	return ""
}

func (x *LivekitParticipantE) GetJoinedAt() int64 {
	if x != nil {
		return x.JoinedAt
	}
	return 0
}

func (x *LivekitParticipantE) GetIsPublisher() bool {
	if x != nil {
		return x.IsPublisher
	}
	return false
}

type LivekitTrackE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Sid        string                 `protobuf:"bytes,1,opt,name=sid,proto3" json:"sid,omitempty"`
	Type       string                 `protobuf:"bytes,2,opt,name=type,proto3" json:"type,omitempty"`
	Name       string                 `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
	Muted      bool                   `protobuf:"varint,4,opt,name=muted,proto3" json:"muted,omitempty"`
	Width      int64                  `protobuf:"varint,5,opt,name=width,proto3" json:"width,omitempty"`
	Height     int64                  `protobuf:"varint,6,opt,name=height,proto3" json:"height,omitempty"`
	Simulcast  bool                   `protobuf:"varint,7,opt,name=simulcast,proto3" json:"simulcast,omitempty"`
	DisableDtx bool                   `protobuf:"varint,8,opt,name=disableDtx,proto3" json:"disableDtx,omitempty"`
	Source     LivekitTrackSourceType `protobuf:"varint,9,opt,name=source,proto3,enum=v1.LivekitTrackSourceType" json:"source,omitempty"`
	Layers     []*LivekitVideoLayerE  `protobuf:"bytes,10,rep,name=layers,proto3" json:"layers,omitempty"`
	MimeType   string                 `protobuf:"bytes,11,opt,name=mimeType,proto3" json:"mimeType,omitempty"`
}

func (x *LivekitTrackE) Reset() {
	*x = LivekitTrackE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_livekit_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LivekitTrackE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LivekitTrackE) ProtoMessage() {}

func (x *LivekitTrackE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_livekit_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LivekitTrackE.ProtoReflect.Descriptor instead.
func (*LivekitTrackE) Descriptor() ([]byte, []int) {
	return file_v1_livekit_proto_rawDescGZIP(), []int{3}
}

func (x *LivekitTrackE) GetSid() string {
	if x != nil {
		return x.Sid
	}
	return ""
}

func (x *LivekitTrackE) GetType() string {
	if x != nil {
		return x.Type
	}
	return ""
}

func (x *LivekitTrackE) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *LivekitTrackE) GetMuted() bool {
	if x != nil {
		return x.Muted
	}
	return false
}

func (x *LivekitTrackE) GetWidth() int64 {
	if x != nil {
		return x.Width
	}
	return 0
}

func (x *LivekitTrackE) GetHeight() int64 {
	if x != nil {
		return x.Height
	}
	return 0
}

func (x *LivekitTrackE) GetSimulcast() bool {
	if x != nil {
		return x.Simulcast
	}
	return false
}

func (x *LivekitTrackE) GetDisableDtx() bool {
	if x != nil {
		return x.DisableDtx
	}
	return false
}

func (x *LivekitTrackE) GetSource() LivekitTrackSourceType {
	if x != nil {
		return x.Source
	}
	return LivekitTrackSourceType_UNKNOWN
}

func (x *LivekitTrackE) GetLayers() []*LivekitVideoLayerE {
	if x != nil {
		return x.Layers
	}
	return nil
}

func (x *LivekitTrackE) GetMimeType() string {
	if x != nil {
		return x.MimeType
	}
	return ""
}

type LivekitVideoLayerE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Quality LivekitVideoQualityType `protobuf:"varint,1,opt,name=quality,proto3,enum=v1.LivekitVideoQualityType" json:"quality,omitempty"`
	Width   int64                   `protobuf:"varint,2,opt,name=width,proto3" json:"width,omitempty"`
	Height  int64                   `protobuf:"varint,3,opt,name=height,proto3" json:"height,omitempty"`
	Bitrate int64                   `protobuf:"varint,4,opt,name=bitrate,proto3" json:"bitrate,omitempty"`
}

func (x *LivekitVideoLayerE) Reset() {
	*x = LivekitVideoLayerE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_livekit_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LivekitVideoLayerE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LivekitVideoLayerE) ProtoMessage() {}

func (x *LivekitVideoLayerE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_livekit_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LivekitVideoLayerE.ProtoReflect.Descriptor instead.
func (*LivekitVideoLayerE) Descriptor() ([]byte, []int) {
	return file_v1_livekit_proto_rawDescGZIP(), []int{4}
}

func (x *LivekitVideoLayerE) GetQuality() LivekitVideoQualityType {
	if x != nil {
		return x.Quality
	}
	return LivekitVideoQualityType_LOW
}

func (x *LivekitVideoLayerE) GetWidth() int64 {
	if x != nil {
		return x.Width
	}
	return 0
}

func (x *LivekitVideoLayerE) GetHeight() int64 {
	if x != nil {
		return x.Height
	}
	return 0
}

func (x *LivekitVideoLayerE) GetBitrate() int64 {
	if x != nil {
		return x.Bitrate
	}
	return 0
}

var File_v1_livekit_proto protoreflect.FileDescriptor

var file_v1_livekit_proto_rawDesc = []byte{
	0x0a, 0x10, 0x76, 0x31, 0x2f, 0x6c, 0x69, 0x76, 0x65, 0x6b, 0x69, 0x74, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x02, 0x76, 0x31, 0x1a, 0x0d, 0x76, 0x31, 0x2f, 0x65, 0x6e, 0x75, 0x6d, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xc7, 0x02, 0x0a, 0x0c, 0x4c, 0x69, 0x76, 0x65, 0x6b, 0x69,
	0x74, 0x52, 0x6f, 0x6f, 0x6d, 0x45, 0x12, 0x10, 0x0a, 0x03, 0x73, 0x69, 0x64, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x03, 0x73, 0x69, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x22, 0x0a, 0x0c,
	0x65, 0x6d, 0x70, 0x74, 0x79, 0x54, 0x69, 0x6d, 0x65, 0x6f, 0x75, 0x74, 0x18, 0x03, 0x20, 0x01,
	0x28, 0x03, 0x52, 0x0c, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x54, 0x69, 0x6d, 0x65, 0x6f, 0x75, 0x74,
	0x12, 0x22, 0x0a, 0x0c, 0x63, 0x72, 0x65, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x69, 0x6d, 0x65,
	0x18, 0x04, 0x20, 0x01, 0x28, 0x03, 0x52, 0x0c, 0x63, 0x72, 0x65, 0x61, 0x74, 0x69, 0x6f, 0x6e,
	0x54, 0x69, 0x6d, 0x65, 0x12, 0x28, 0x0a, 0x0f, 0x6d, 0x61, 0x78, 0x50, 0x61, 0x72, 0x74, 0x69,
	0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x73, 0x18, 0x05, 0x20, 0x01, 0x28, 0x03, 0x52, 0x0f, 0x6d,
	0x61, 0x78, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x73, 0x12, 0x22,
	0x0a, 0x0c, 0x74, 0x75, 0x72, 0x6e, 0x50, 0x61, 0x73, 0x73, 0x77, 0x6f, 0x72, 0x64, 0x18, 0x06,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x74, 0x75, 0x72, 0x6e, 0x50, 0x61, 0x73, 0x73, 0x77, 0x6f,
	0x72, 0x64, 0x12, 0x35, 0x0a, 0x0c, 0x65, 0x6e, 0x61, 0x62, 0x6c, 0x65, 0x43, 0x6f, 0x64, 0x65,
	0x63, 0x73, 0x18, 0x07, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x11, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69,
	0x76, 0x65, 0x6b, 0x69, 0x74, 0x43, 0x6f, 0x64, 0x65, 0x63, 0x45, 0x52, 0x0c, 0x65, 0x6e, 0x61,
	0x62, 0x6c, 0x65, 0x43, 0x6f, 0x64, 0x65, 0x63, 0x73, 0x12, 0x1a, 0x0a, 0x08, 0x6d, 0x65, 0x74,
	0x61, 0x64, 0x61, 0x74, 0x61, 0x18, 0x08, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x6d, 0x65, 0x74,
	0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x28, 0x0a, 0x0f, 0x6e, 0x75, 0x6d, 0x50, 0x61, 0x72, 0x74,
	0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x73, 0x18, 0x09, 0x20, 0x01, 0x28, 0x03, 0x52, 0x0f,
	0x6e, 0x75, 0x6d, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x73, 0x22,
	0x3f, 0x0a, 0x0d, 0x4c, 0x69, 0x76, 0x65, 0x6b, 0x69, 0x74, 0x43, 0x6f, 0x64, 0x65, 0x63, 0x45,
	0x12, 0x12, 0x0a, 0x04, 0x6d, 0x69, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04,
	0x6d, 0x69, 0x6d, 0x65, 0x12, 0x1a, 0x0a, 0x08, 0x66, 0x6d, 0x74, 0x70, 0x4c, 0x69, 0x6e, 0x65,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x66, 0x6d, 0x74, 0x70, 0x4c, 0x69, 0x6e, 0x65,
	0x22, 0xf2, 0x01, 0x0a, 0x13, 0x4c, 0x69, 0x76, 0x65, 0x6b, 0x69, 0x74, 0x50, 0x61, 0x72, 0x74,
	0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x45, 0x12, 0x10, 0x0a, 0x03, 0x73, 0x69, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x73, 0x69, 0x64, 0x12, 0x1a, 0x0a, 0x08, 0x69, 0x64,
	0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x69, 0x64,
	0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x14, 0x0a, 0x05, 0x73, 0x74,
	0x61, 0x74, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x73, 0x74, 0x61, 0x74, 0x65,
	0x12, 0x29, 0x0a, 0x06, 0x74, 0x72, 0x61, 0x63, 0x6b, 0x73, 0x18, 0x05, 0x20, 0x03, 0x28, 0x0b,
	0x32, 0x11, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69, 0x76, 0x65, 0x6b, 0x69, 0x74, 0x54, 0x72, 0x61,
	0x63, 0x6b, 0x45, 0x52, 0x06, 0x74, 0x72, 0x61, 0x63, 0x6b, 0x73, 0x12, 0x1a, 0x0a, 0x08, 0x6d,
	0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x6d,
	0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x1a, 0x0a, 0x08, 0x6a, 0x6f, 0x69, 0x6e, 0x65,
	0x64, 0x41, 0x74, 0x18, 0x07, 0x20, 0x01, 0x28, 0x03, 0x52, 0x08, 0x6a, 0x6f, 0x69, 0x6e, 0x65,
	0x64, 0x41, 0x74, 0x12, 0x20, 0x0a, 0x0b, 0x69, 0x73, 0x50, 0x75, 0x62, 0x6c, 0x69, 0x73, 0x68,
	0x65, 0x72, 0x18, 0x08, 0x20, 0x01, 0x28, 0x08, 0x52, 0x0b, 0x69, 0x73, 0x50, 0x75, 0x62, 0x6c,
	0x69, 0x73, 0x68, 0x65, 0x72, 0x22, 0xcb, 0x02, 0x0a, 0x0d, 0x4c, 0x69, 0x76, 0x65, 0x6b, 0x69,
	0x74, 0x54, 0x72, 0x61, 0x63, 0x6b, 0x45, 0x12, 0x10, 0x0a, 0x03, 0x73, 0x69, 0x64, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x73, 0x69, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x74, 0x79, 0x70,
	0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x74, 0x79, 0x70, 0x65, 0x12, 0x12, 0x0a,
	0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d,
	0x65, 0x12, 0x14, 0x0a, 0x05, 0x6d, 0x75, 0x74, 0x65, 0x64, 0x18, 0x04, 0x20, 0x01, 0x28, 0x08,
	0x52, 0x05, 0x6d, 0x75, 0x74, 0x65, 0x64, 0x12, 0x14, 0x0a, 0x05, 0x77, 0x69, 0x64, 0x74, 0x68,
	0x18, 0x05, 0x20, 0x01, 0x28, 0x03, 0x52, 0x05, 0x77, 0x69, 0x64, 0x74, 0x68, 0x12, 0x16, 0x0a,
	0x06, 0x68, 0x65, 0x69, 0x67, 0x68, 0x74, 0x18, 0x06, 0x20, 0x01, 0x28, 0x03, 0x52, 0x06, 0x68,
	0x65, 0x69, 0x67, 0x68, 0x74, 0x12, 0x1c, 0x0a, 0x09, 0x73, 0x69, 0x6d, 0x75, 0x6c, 0x63, 0x61,
	0x73, 0x74, 0x18, 0x07, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09, 0x73, 0x69, 0x6d, 0x75, 0x6c, 0x63,
	0x61, 0x73, 0x74, 0x12, 0x1e, 0x0a, 0x0a, 0x64, 0x69, 0x73, 0x61, 0x62, 0x6c, 0x65, 0x44, 0x74,
	0x78, 0x18, 0x08, 0x20, 0x01, 0x28, 0x08, 0x52, 0x0a, 0x64, 0x69, 0x73, 0x61, 0x62, 0x6c, 0x65,
	0x44, 0x74, 0x78, 0x12, 0x32, 0x0a, 0x06, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x18, 0x09, 0x20,
	0x01, 0x28, 0x0e, 0x32, 0x1a, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69, 0x76, 0x65, 0x6b, 0x69, 0x74,
	0x54, 0x72, 0x61, 0x63, 0x6b, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x54, 0x79, 0x70, 0x65, 0x52,
	0x06, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x12, 0x2e, 0x0a, 0x06, 0x6c, 0x61, 0x79, 0x65, 0x72,
	0x73, 0x18, 0x0a, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x16, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69, 0x76,
	0x65, 0x6b, 0x69, 0x74, 0x56, 0x69, 0x64, 0x65, 0x6f, 0x4c, 0x61, 0x79, 0x65, 0x72, 0x45, 0x52,
	0x06, 0x6c, 0x61, 0x79, 0x65, 0x72, 0x73, 0x12, 0x1a, 0x0a, 0x08, 0x6d, 0x69, 0x6d, 0x65, 0x54,
	0x79, 0x70, 0x65, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x6d, 0x69, 0x6d, 0x65, 0x54,
	0x79, 0x70, 0x65, 0x22, 0x93, 0x01, 0x0a, 0x12, 0x4c, 0x69, 0x76, 0x65, 0x6b, 0x69, 0x74, 0x56,
	0x69, 0x64, 0x65, 0x6f, 0x4c, 0x61, 0x79, 0x65, 0x72, 0x45, 0x12, 0x35, 0x0a, 0x07, 0x71, 0x75,
	0x61, 0x6c, 0x69, 0x74, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x1b, 0x2e, 0x76, 0x31,
	0x2e, 0x4c, 0x69, 0x76, 0x65, 0x6b, 0x69, 0x74, 0x56, 0x69, 0x64, 0x65, 0x6f, 0x51, 0x75, 0x61,
	0x6c, 0x69, 0x74, 0x79, 0x54, 0x79, 0x70, 0x65, 0x52, 0x07, 0x71, 0x75, 0x61, 0x6c, 0x69, 0x74,
	0x79, 0x12, 0x14, 0x0a, 0x05, 0x77, 0x69, 0x64, 0x74, 0x68, 0x18, 0x02, 0x20, 0x01, 0x28, 0x03,
	0x52, 0x05, 0x77, 0x69, 0x64, 0x74, 0x68, 0x12, 0x16, 0x0a, 0x06, 0x68, 0x65, 0x69, 0x67, 0x68,
	0x74, 0x18, 0x03, 0x20, 0x01, 0x28, 0x03, 0x52, 0x06, 0x68, 0x65, 0x69, 0x67, 0x68, 0x74, 0x12,
	0x18, 0x0a, 0x07, 0x62, 0x69, 0x74, 0x72, 0x61, 0x74, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x03,
	0x52, 0x07, 0x62, 0x69, 0x74, 0x72, 0x61, 0x74, 0x65, 0x42, 0x4c, 0x0a, 0x0e, 0x63, 0x6f, 0x6d,
	0x2e, 0x6c, 0x75, 0x78, 0x72, 0x6f, 0x62, 0x6f, 0x2e, 0x76, 0x31, 0x42, 0x0c, 0x4c, 0x69, 0x76,
	0x65, 0x6b, 0x69, 0x74, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x0a, 0x6c, 0x75, 0x78,
	0x72, 0x6f, 0x62, 0x6f, 0x2f, 0x76, 0x31, 0xa2, 0x02, 0x03, 0x54, 0x50, 0x58, 0xaa, 0x02, 0x0a,
	0x4c, 0x75, 0x78, 0x72, 0x6f, 0x62, 0x6f, 0x2e, 0x76, 0x31, 0xca, 0x02, 0x0a, 0x4c, 0x75, 0x78,
	0x72, 0x6f, 0x62, 0x6f, 0x5c, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_v1_livekit_proto_rawDescOnce sync.Once
	file_v1_livekit_proto_rawDescData = file_v1_livekit_proto_rawDesc
)

func file_v1_livekit_proto_rawDescGZIP() []byte {
	file_v1_livekit_proto_rawDescOnce.Do(func() {
		file_v1_livekit_proto_rawDescData = protoimpl.X.CompressGZIP(file_v1_livekit_proto_rawDescData)
	})
	return file_v1_livekit_proto_rawDescData
}

var file_v1_livekit_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_v1_livekit_proto_goTypes = []interface{}{
	(*LivekitRoomE)(nil),         // 0: v1.LivekitRoomE
	(*LivekitCodecE)(nil),        // 1: v1.LivekitCodecE
	(*LivekitParticipantE)(nil),  // 2: v1.LivekitParticipantE
	(*LivekitTrackE)(nil),        // 3: v1.LivekitTrackE
	(*LivekitVideoLayerE)(nil),   // 4: v1.LivekitVideoLayerE
	(LivekitTrackSourceType)(0),  // 5: v1.LivekitTrackSourceType
	(LivekitVideoQualityType)(0), // 6: v1.LivekitVideoQualityType
}
var file_v1_livekit_proto_depIdxs = []int32{
	1, // 0: v1.LivekitRoomE.enableCodecs:type_name -> v1.LivekitCodecE
	3, // 1: v1.LivekitParticipantE.tracks:type_name -> v1.LivekitTrackE
	5, // 2: v1.LivekitTrackE.source:type_name -> v1.LivekitTrackSourceType
	4, // 3: v1.LivekitTrackE.layers:type_name -> v1.LivekitVideoLayerE
	6, // 4: v1.LivekitVideoLayerE.quality:type_name -> v1.LivekitVideoQualityType
	5, // [5:5] is the sub-list for method output_type
	5, // [5:5] is the sub-list for method input_type
	5, // [5:5] is the sub-list for extension type_name
	5, // [5:5] is the sub-list for extension extendee
	0, // [0:5] is the sub-list for field type_name
}

func init() { file_v1_livekit_proto_init() }
func file_v1_livekit_proto_init() {
	if File_v1_livekit_proto != nil {
		return
	}
	file_v1_enum_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_v1_livekit_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LivekitRoomE); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_v1_livekit_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LivekitCodecE); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_v1_livekit_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LivekitParticipantE); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_v1_livekit_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LivekitTrackE); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_v1_livekit_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LivekitVideoLayerE); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_v1_livekit_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_v1_livekit_proto_goTypes,
		DependencyIndexes: file_v1_livekit_proto_depIdxs,
		MessageInfos:      file_v1_livekit_proto_msgTypes,
	}.Build()
	File_v1_livekit_proto = out.File
	file_v1_livekit_proto_rawDesc = nil
	file_v1_livekit_proto_goTypes = nil
	file_v1_livekit_proto_depIdxs = nil
}
