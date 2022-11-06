// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.8.0
// source: v1/runnercli.proto

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

// RunnercliSoftwareSpecOSType os spec
type RunnercliSoftwareSpecOSType int32

const (
	RunnercliSoftwareSpecOSType_UBUNTU_18_04 RunnercliSoftwareSpecOSType = 0
)

// Enum value maps for RunnercliSoftwareSpecOSType.
var (
	RunnercliSoftwareSpecOSType_name = map[int32]string{
		0: "UBUNTU_18_04",
	}
	RunnercliSoftwareSpecOSType_value = map[string]int32{
		"UBUNTU_18_04": 0,
	}
)

func (x RunnercliSoftwareSpecOSType) Enum() *RunnercliSoftwareSpecOSType {
	p := new(RunnercliSoftwareSpecOSType)
	*p = x
	return p
}

func (x RunnercliSoftwareSpecOSType) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (RunnercliSoftwareSpecOSType) Descriptor() protoreflect.EnumDescriptor {
	return file_v1_runnercli_proto_enumTypes[0].Descriptor()
}

func (RunnercliSoftwareSpecOSType) Type() protoreflect.EnumType {
	return &file_v1_runnercli_proto_enumTypes[0]
}

func (x RunnercliSoftwareSpecOSType) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use RunnercliSoftwareSpecOSType.Descriptor instead.
func (RunnercliSoftwareSpecOSType) EnumDescriptor() ([]byte, []int) {
	return file_v1_runnercli_proto_rawDescGZIP(), []int{0}
}

// RunnercliSoftwareSpecTemplateType template spec
type RunnercliSoftwareSpecTemplateType int32

const (
	// golang default template
	RunnercliSoftwareSpecTemplateType_GOLANG RunnercliSoftwareSpecTemplateType = 0
	// python default template
	RunnercliSoftwareSpecTemplateType_PYTHON RunnercliSoftwareSpecTemplateType = 1
	// typescript default template
	RunnercliSoftwareSpecTemplateType_TYPESCRIPT RunnercliSoftwareSpecTemplateType = 2
)

// Enum value maps for RunnercliSoftwareSpecTemplateType.
var (
	RunnercliSoftwareSpecTemplateType_name = map[int32]string{
		0: "GOLANG",
		1: "PYTHON",
		2: "TYPESCRIPT",
	}
	RunnercliSoftwareSpecTemplateType_value = map[string]int32{
		"GOLANG":     0,
		"PYTHON":     1,
		"TYPESCRIPT": 2,
	}
)

func (x RunnercliSoftwareSpecTemplateType) Enum() *RunnercliSoftwareSpecTemplateType {
	p := new(RunnercliSoftwareSpecTemplateType)
	*p = x
	return p
}

func (x RunnercliSoftwareSpecTemplateType) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (RunnercliSoftwareSpecTemplateType) Descriptor() protoreflect.EnumDescriptor {
	return file_v1_runnercli_proto_enumTypes[1].Descriptor()
}

func (RunnercliSoftwareSpecTemplateType) Type() protoreflect.EnumType {
	return &file_v1_runnercli_proto_enumTypes[1]
}

func (x RunnercliSoftwareSpecTemplateType) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use RunnercliSoftwareSpecTemplateType.Descriptor instead.
func (RunnercliSoftwareSpecTemplateType) EnumDescriptor() ([]byte, []int) {
	return file_v1_runnercli_proto_rawDescGZIP(), []int{1}
}

// RunnercliContainerE ...
type RunnercliContainerE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id                string                `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Name              string                `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	ImageName         string                `protobuf:"bytes,3,opt,name=imageName,proto3" json:"imageName,omitempty"`
	Namespace         string                `protobuf:"bytes,4,opt,name=namespace,proto3" json:"namespace,omitempty"`
	PodName           string                `protobuf:"bytes,5,opt,name=podName,proto3" json:"podName,omitempty"`
	ContainerName     string                `protobuf:"bytes,6,opt,name=containerName,proto3" json:"containerName,omitempty"`
	AccessLink        *RunnercliAccessLinkE `protobuf:"bytes,7,opt,name=accessLink,proto3" json:"accessLink,omitempty"`
	IsLive            bool                  `protobuf:"varint,8,opt,name=isLive,proto3" json:"isLive,omitempty"`
	Status            string                `protobuf:"bytes,9,opt,name=status,proto3" json:"status,omitempty"`
	CreationTimestamp string                `protobuf:"bytes,10,opt,name=creationTimestamp,proto3" json:"creationTimestamp,omitempty"`
}

func (x *RunnercliContainerE) Reset() {
	*x = RunnercliContainerE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_runnercli_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RunnercliContainerE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RunnercliContainerE) ProtoMessage() {}

func (x *RunnercliContainerE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_runnercli_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RunnercliContainerE.ProtoReflect.Descriptor instead.
func (*RunnercliContainerE) Descriptor() ([]byte, []int) {
	return file_v1_runnercli_proto_rawDescGZIP(), []int{0}
}

func (x *RunnercliContainerE) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *RunnercliContainerE) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *RunnercliContainerE) GetImageName() string {
	if x != nil {
		return x.ImageName
	}
	return ""
}

func (x *RunnercliContainerE) GetNamespace() string {
	if x != nil {
		return x.Namespace
	}
	return ""
}

func (x *RunnercliContainerE) GetPodName() string {
	if x != nil {
		return x.PodName
	}
	return ""
}

func (x *RunnercliContainerE) GetContainerName() string {
	if x != nil {
		return x.ContainerName
	}
	return ""
}

func (x *RunnercliContainerE) GetAccessLink() *RunnercliAccessLinkE {
	if x != nil {
		return x.AccessLink
	}
	return nil
}

func (x *RunnercliContainerE) GetIsLive() bool {
	if x != nil {
		return x.IsLive
	}
	return false
}

func (x *RunnercliContainerE) GetStatus() string {
	if x != nil {
		return x.Status
	}
	return ""
}

func (x *RunnercliContainerE) GetCreationTimestamp() string {
	if x != nil {
		return x.CreationTimestamp
	}
	return ""
}

// RunnercliAccessLinkE 링크주소
type RunnercliAccessLinkE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Workspace string `protobuf:"bytes,1,opt,name=workspace,proto3" json:"workspace,omitempty"`
	Terminal  string `protobuf:"bytes,2,opt,name=terminal,proto3" json:"terminal,omitempty"`
}

func (x *RunnercliAccessLinkE) Reset() {
	*x = RunnercliAccessLinkE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_runnercli_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RunnercliAccessLinkE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RunnercliAccessLinkE) ProtoMessage() {}

func (x *RunnercliAccessLinkE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_runnercli_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RunnercliAccessLinkE.ProtoReflect.Descriptor instead.
func (*RunnercliAccessLinkE) Descriptor() ([]byte, []int) {
	return file_v1_runnercli_proto_rawDescGZIP(), []int{1}
}

func (x *RunnercliAccessLinkE) GetWorkspace() string {
	if x != nil {
		return x.Workspace
	}
	return ""
}

func (x *RunnercliAccessLinkE) GetTerminal() string {
	if x != nil {
		return x.Terminal
	}
	return ""
}

// RunnercliPodE ...
type RunnercliPodE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ObjectMeta      *RunnercliObjectMetaE `protobuf:"bytes,1,opt,name=objectMeta,proto3" json:"objectMeta,omitempty"`
	TypeMeta        *RunnercliTypeMetaE   `protobuf:"bytes,2,opt,name=typeMeta,proto3" json:"typeMeta,omitempty"`
	Status          string                `protobuf:"bytes,3,opt,name=status,proto3" json:"status,omitempty"`
	RestartCount    int32                 `protobuf:"varint,4,opt,name=restartCount,proto3" json:"restartCount,omitempty"`
	NodeName        string                `protobuf:"bytes,5,opt,name=nodeName,proto3" json:"nodeName,omitempty"`
	ContainerImages []string              `protobuf:"bytes,6,rep,name=containerImages,proto3" json:"containerImages,omitempty"`
}

func (x *RunnercliPodE) Reset() {
	*x = RunnercliPodE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_runnercli_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RunnercliPodE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RunnercliPodE) ProtoMessage() {}

func (x *RunnercliPodE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_runnercli_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RunnercliPodE.ProtoReflect.Descriptor instead.
func (*RunnercliPodE) Descriptor() ([]byte, []int) {
	return file_v1_runnercli_proto_rawDescGZIP(), []int{2}
}

func (x *RunnercliPodE) GetObjectMeta() *RunnercliObjectMetaE {
	if x != nil {
		return x.ObjectMeta
	}
	return nil
}

func (x *RunnercliPodE) GetTypeMeta() *RunnercliTypeMetaE {
	if x != nil {
		return x.TypeMeta
	}
	return nil
}

func (x *RunnercliPodE) GetStatus() string {
	if x != nil {
		return x.Status
	}
	return ""
}

func (x *RunnercliPodE) GetRestartCount() int32 {
	if x != nil {
		return x.RestartCount
	}
	return 0
}

func (x *RunnercliPodE) GetNodeName() string {
	if x != nil {
		return x.NodeName
	}
	return ""
}

func (x *RunnercliPodE) GetContainerImages() []string {
	if x != nil {
		return x.ContainerImages
	}
	return nil
}

// RunnercliObjectMetaE ...
type RunnercliObjectMetaE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Uid               string            `protobuf:"bytes,1,opt,name=uid,proto3" json:"uid,omitempty"`
	Name              string            `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Namespace         string            `protobuf:"bytes,3,opt,name=namespace,proto3" json:"namespace,omitempty"`
	CreationTimestamp string            `protobuf:"bytes,4,opt,name=creationTimestamp,proto3" json:"creationTimestamp,omitempty"`
	Labels            map[string]string `protobuf:"bytes,5,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *RunnercliObjectMetaE) Reset() {
	*x = RunnercliObjectMetaE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_runnercli_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RunnercliObjectMetaE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RunnercliObjectMetaE) ProtoMessage() {}

func (x *RunnercliObjectMetaE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_runnercli_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RunnercliObjectMetaE.ProtoReflect.Descriptor instead.
func (*RunnercliObjectMetaE) Descriptor() ([]byte, []int) {
	return file_v1_runnercli_proto_rawDescGZIP(), []int{3}
}

func (x *RunnercliObjectMetaE) GetUid() string {
	if x != nil {
		return x.Uid
	}
	return ""
}

func (x *RunnercliObjectMetaE) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *RunnercliObjectMetaE) GetNamespace() string {
	if x != nil {
		return x.Namespace
	}
	return ""
}

func (x *RunnercliObjectMetaE) GetCreationTimestamp() string {
	if x != nil {
		return x.CreationTimestamp
	}
	return ""
}

func (x *RunnercliObjectMetaE) GetLabels() map[string]string {
	if x != nil {
		return x.Labels
	}
	return nil
}

// RunnercliTypeMetaE ...
type RunnercliTypeMetaE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Kind string `protobuf:"bytes,1,opt,name=kind,proto3" json:"kind,omitempty"`
}

func (x *RunnercliTypeMetaE) Reset() {
	*x = RunnercliTypeMetaE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_runnercli_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RunnercliTypeMetaE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RunnercliTypeMetaE) ProtoMessage() {}

func (x *RunnercliTypeMetaE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_runnercli_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RunnercliTypeMetaE.ProtoReflect.Descriptor instead.
func (*RunnercliTypeMetaE) Descriptor() ([]byte, []int) {
	return file_v1_runnercli_proto_rawDescGZIP(), []int{4}
}

func (x *RunnercliTypeMetaE) GetKind() string {
	if x != nil {
		return x.Kind
	}
	return ""
}

// RunnercliSoftwareSpecE 소프트웨어 스펙
type RunnercliSoftwareSpecE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Os       RunnercliSoftwareSpecOSType       `protobuf:"varint,1,opt,name=os,proto3,enum=v1.RunnercliSoftwareSpecOSType" json:"os,omitempty"`
	Template RunnercliSoftwareSpecTemplateType `protobuf:"varint,2,opt,name=template,proto3,enum=v1.RunnercliSoftwareSpecTemplateType" json:"template,omitempty"`
}

func (x *RunnercliSoftwareSpecE) Reset() {
	*x = RunnercliSoftwareSpecE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_runnercli_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RunnercliSoftwareSpecE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RunnercliSoftwareSpecE) ProtoMessage() {}

func (x *RunnercliSoftwareSpecE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_runnercli_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RunnercliSoftwareSpecE.ProtoReflect.Descriptor instead.
func (*RunnercliSoftwareSpecE) Descriptor() ([]byte, []int) {
	return file_v1_runnercli_proto_rawDescGZIP(), []int{5}
}

func (x *RunnercliSoftwareSpecE) GetOs() RunnercliSoftwareSpecOSType {
	if x != nil {
		return x.Os
	}
	return RunnercliSoftwareSpecOSType_UBUNTU_18_04
}

func (x *RunnercliSoftwareSpecE) GetTemplate() RunnercliSoftwareSpecTemplateType {
	if x != nil {
		return x.Template
	}
	return RunnercliSoftwareSpecTemplateType_GOLANG
}

var File_v1_runnercli_proto protoreflect.FileDescriptor

var file_v1_runnercli_proto_rawDesc = []byte{
	0x0a, 0x12, 0x76, 0x31, 0x2f, 0x72, 0x75, 0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x02, 0x76, 0x31, 0x22, 0xcd, 0x02, 0x0a, 0x13, 0x52, 0x75, 0x6e,
	0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x43, 0x6f, 0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x45,
	0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64,
	0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x12, 0x1c, 0x0a, 0x09, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x4e, 0x61, 0x6d,
	0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x4e, 0x61,
	0x6d, 0x65, 0x12, 0x1c, 0x0a, 0x09, 0x6e, 0x61, 0x6d, 0x65, 0x73, 0x70, 0x61, 0x63, 0x65, 0x18,
	0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x6e, 0x61, 0x6d, 0x65, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x12, 0x18, 0x0a, 0x07, 0x70, 0x6f, 0x64, 0x4e, 0x61, 0x6d, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x07, 0x70, 0x6f, 0x64, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x24, 0x0a, 0x0d, 0x63, 0x6f,
	0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x4e, 0x61, 0x6d, 0x65, 0x18, 0x06, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x0d, 0x63, 0x6f, 0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x4e, 0x61, 0x6d, 0x65,
	0x12, 0x38, 0x0a, 0x0a, 0x61, 0x63, 0x63, 0x65, 0x73, 0x73, 0x4c, 0x69, 0x6e, 0x6b, 0x18, 0x07,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x18, 0x2e, 0x76, 0x31, 0x2e, 0x52, 0x75, 0x6e, 0x6e, 0x65, 0x72,
	0x63, 0x6c, 0x69, 0x41, 0x63, 0x63, 0x65, 0x73, 0x73, 0x4c, 0x69, 0x6e, 0x6b, 0x45, 0x52, 0x0a,
	0x61, 0x63, 0x63, 0x65, 0x73, 0x73, 0x4c, 0x69, 0x6e, 0x6b, 0x12, 0x16, 0x0a, 0x06, 0x69, 0x73,
	0x4c, 0x69, 0x76, 0x65, 0x18, 0x08, 0x20, 0x01, 0x28, 0x08, 0x52, 0x06, 0x69, 0x73, 0x4c, 0x69,
	0x76, 0x65, 0x12, 0x16, 0x0a, 0x06, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x18, 0x09, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x06, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x12, 0x2c, 0x0a, 0x11, 0x63, 0x72,
	0x65, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18,
	0x0a, 0x20, 0x01, 0x28, 0x09, 0x52, 0x11, 0x63, 0x72, 0x65, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54,
	0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x22, 0x50, 0x0a, 0x14, 0x52, 0x75, 0x6e, 0x6e,
	0x65, 0x72, 0x63, 0x6c, 0x69, 0x41, 0x63, 0x63, 0x65, 0x73, 0x73, 0x4c, 0x69, 0x6e, 0x6b, 0x45,
	0x12, 0x1c, 0x0a, 0x09, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x09, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x12, 0x1a,
	0x0a, 0x08, 0x74, 0x65, 0x72, 0x6d, 0x69, 0x6e, 0x61, 0x6c, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x08, 0x74, 0x65, 0x72, 0x6d, 0x69, 0x6e, 0x61, 0x6c, 0x22, 0xff, 0x01, 0x0a, 0x0d, 0x52,
	0x75, 0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x50, 0x6f, 0x64, 0x45, 0x12, 0x38, 0x0a, 0x0a,
	0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x4d, 0x65, 0x74, 0x61, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x18, 0x2e, 0x76, 0x31, 0x2e, 0x52, 0x75, 0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x4f,
	0x62, 0x6a, 0x65, 0x63, 0x74, 0x4d, 0x65, 0x74, 0x61, 0x45, 0x52, 0x0a, 0x6f, 0x62, 0x6a, 0x65,
	0x63, 0x74, 0x4d, 0x65, 0x74, 0x61, 0x12, 0x32, 0x0a, 0x08, 0x74, 0x79, 0x70, 0x65, 0x4d, 0x65,
	0x74, 0x61, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x16, 0x2e, 0x76, 0x31, 0x2e, 0x52, 0x75,
	0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x54, 0x79, 0x70, 0x65, 0x4d, 0x65, 0x74, 0x61, 0x45,
	0x52, 0x08, 0x74, 0x79, 0x70, 0x65, 0x4d, 0x65, 0x74, 0x61, 0x12, 0x16, 0x0a, 0x06, 0x73, 0x74,
	0x61, 0x74, 0x75, 0x73, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x73, 0x74, 0x61, 0x74,
	0x75, 0x73, 0x12, 0x22, 0x0a, 0x0c, 0x72, 0x65, 0x73, 0x74, 0x61, 0x72, 0x74, 0x43, 0x6f, 0x75,
	0x6e, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0c, 0x72, 0x65, 0x73, 0x74, 0x61, 0x72,
	0x74, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x12, 0x1a, 0x0a, 0x08, 0x6e, 0x6f, 0x64, 0x65, 0x4e, 0x61,
	0x6d, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x6e, 0x6f, 0x64, 0x65, 0x4e, 0x61,
	0x6d, 0x65, 0x12, 0x28, 0x0a, 0x0f, 0x63, 0x6f, 0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x49,
	0x6d, 0x61, 0x67, 0x65, 0x73, 0x18, 0x06, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0f, 0x63, 0x6f, 0x6e,
	0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x73, 0x22, 0x81, 0x02, 0x0a,
	0x14, 0x52, 0x75, 0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74,
	0x4d, 0x65, 0x74, 0x61, 0x45, 0x12, 0x10, 0x0a, 0x03, 0x75, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x03, 0x75, 0x69, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x1c, 0x0a, 0x09, 0x6e,
	0x61, 0x6d, 0x65, 0x73, 0x70, 0x61, 0x63, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09,
	0x6e, 0x61, 0x6d, 0x65, 0x73, 0x70, 0x61, 0x63, 0x65, 0x12, 0x2c, 0x0a, 0x11, 0x63, 0x72, 0x65,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18, 0x04,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x11, 0x63, 0x72, 0x65, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x69,
	0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x12, 0x3c, 0x0a, 0x06, 0x6c, 0x61, 0x62, 0x65, 0x6c,
	0x73, 0x18, 0x05, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x76, 0x31, 0x2e, 0x52, 0x75, 0x6e,
	0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x4d, 0x65, 0x74, 0x61,
	0x45, 0x2e, 0x4c, 0x61, 0x62, 0x65, 0x6c, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x06, 0x6c,
	0x61, 0x62, 0x65, 0x6c, 0x73, 0x1a, 0x39, 0x0a, 0x0b, 0x4c, 0x61, 0x62, 0x65, 0x6c, 0x73, 0x45,
	0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x14, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01,
	0x22, 0x28, 0x0a, 0x12, 0x52, 0x75, 0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x54, 0x79, 0x70,
	0x65, 0x4d, 0x65, 0x74, 0x61, 0x45, 0x12, 0x12, 0x0a, 0x04, 0x6b, 0x69, 0x6e, 0x64, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6b, 0x69, 0x6e, 0x64, 0x22, 0x8c, 0x01, 0x0a, 0x16, 0x52,
	0x75, 0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x53, 0x6f, 0x66, 0x74, 0x77, 0x61, 0x72, 0x65,
	0x53, 0x70, 0x65, 0x63, 0x45, 0x12, 0x2f, 0x0a, 0x02, 0x6f, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0e, 0x32, 0x1f, 0x2e, 0x76, 0x31, 0x2e, 0x52, 0x75, 0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69,
	0x53, 0x6f, 0x66, 0x74, 0x77, 0x61, 0x72, 0x65, 0x53, 0x70, 0x65, 0x63, 0x4f, 0x53, 0x54, 0x79,
	0x70, 0x65, 0x52, 0x02, 0x6f, 0x73, 0x12, 0x41, 0x0a, 0x08, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61,
	0x74, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x25, 0x2e, 0x76, 0x31, 0x2e, 0x52, 0x75,
	0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x53, 0x6f, 0x66, 0x74, 0x77, 0x61, 0x72, 0x65, 0x53,
	0x70, 0x65, 0x63, 0x54, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x54, 0x79, 0x70, 0x65, 0x52,
	0x08, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x2a, 0x2f, 0x0a, 0x1b, 0x52, 0x75, 0x6e,
	0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x53, 0x6f, 0x66, 0x74, 0x77, 0x61, 0x72, 0x65, 0x53, 0x70,
	0x65, 0x63, 0x4f, 0x53, 0x54, 0x79, 0x70, 0x65, 0x12, 0x10, 0x0a, 0x0c, 0x55, 0x42, 0x55, 0x4e,
	0x54, 0x55, 0x5f, 0x31, 0x38, 0x5f, 0x30, 0x34, 0x10, 0x00, 0x2a, 0x4b, 0x0a, 0x21, 0x52, 0x75,
	0x6e, 0x6e, 0x65, 0x72, 0x63, 0x6c, 0x69, 0x53, 0x6f, 0x66, 0x74, 0x77, 0x61, 0x72, 0x65, 0x53,
	0x70, 0x65, 0x63, 0x54, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x54, 0x79, 0x70, 0x65, 0x12,
	0x0a, 0x0a, 0x06, 0x47, 0x4f, 0x4c, 0x41, 0x4e, 0x47, 0x10, 0x00, 0x12, 0x0a, 0x0a, 0x06, 0x50,
	0x59, 0x54, 0x48, 0x4f, 0x4e, 0x10, 0x01, 0x12, 0x0e, 0x0a, 0x0a, 0x54, 0x59, 0x50, 0x45, 0x53,
	0x43, 0x52, 0x49, 0x50, 0x54, 0x10, 0x02, 0x42, 0x4e, 0x0a, 0x0e, 0x63, 0x6f, 0x6d, 0x2e, 0x6c,
	0x75, 0x78, 0x72, 0x6f, 0x62, 0x6f, 0x2e, 0x76, 0x31, 0x42, 0x0e, 0x52, 0x75, 0x6e, 0x6e, 0x65,
	0x72, 0x63, 0x6c, 0x69, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x0a, 0x6c, 0x75, 0x78,
	0x72, 0x6f, 0x62, 0x6f, 0x2f, 0x76, 0x31, 0xa2, 0x02, 0x03, 0x54, 0x50, 0x58, 0xaa, 0x02, 0x0a,
	0x4c, 0x75, 0x78, 0x72, 0x6f, 0x62, 0x6f, 0x2e, 0x76, 0x31, 0xca, 0x02, 0x0a, 0x4c, 0x75, 0x78,
	0x72, 0x6f, 0x62, 0x6f, 0x5c, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_v1_runnercli_proto_rawDescOnce sync.Once
	file_v1_runnercli_proto_rawDescData = file_v1_runnercli_proto_rawDesc
)

func file_v1_runnercli_proto_rawDescGZIP() []byte {
	file_v1_runnercli_proto_rawDescOnce.Do(func() {
		file_v1_runnercli_proto_rawDescData = protoimpl.X.CompressGZIP(file_v1_runnercli_proto_rawDescData)
	})
	return file_v1_runnercli_proto_rawDescData
}

var file_v1_runnercli_proto_enumTypes = make([]protoimpl.EnumInfo, 2)
var file_v1_runnercli_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_v1_runnercli_proto_goTypes = []interface{}{
	(RunnercliSoftwareSpecOSType)(0),       // 0: v1.RunnercliSoftwareSpecOSType
	(RunnercliSoftwareSpecTemplateType)(0), // 1: v1.RunnercliSoftwareSpecTemplateType
	(*RunnercliContainerE)(nil),            // 2: v1.RunnercliContainerE
	(*RunnercliAccessLinkE)(nil),           // 3: v1.RunnercliAccessLinkE
	(*RunnercliPodE)(nil),                  // 4: v1.RunnercliPodE
	(*RunnercliObjectMetaE)(nil),           // 5: v1.RunnercliObjectMetaE
	(*RunnercliTypeMetaE)(nil),             // 6: v1.RunnercliTypeMetaE
	(*RunnercliSoftwareSpecE)(nil),         // 7: v1.RunnercliSoftwareSpecE
	nil,                                    // 8: v1.RunnercliObjectMetaE.LabelsEntry
}
var file_v1_runnercli_proto_depIdxs = []int32{
	3, // 0: v1.RunnercliContainerE.accessLink:type_name -> v1.RunnercliAccessLinkE
	5, // 1: v1.RunnercliPodE.objectMeta:type_name -> v1.RunnercliObjectMetaE
	6, // 2: v1.RunnercliPodE.typeMeta:type_name -> v1.RunnercliTypeMetaE
	8, // 3: v1.RunnercliObjectMetaE.labels:type_name -> v1.RunnercliObjectMetaE.LabelsEntry
	0, // 4: v1.RunnercliSoftwareSpecE.os:type_name -> v1.RunnercliSoftwareSpecOSType
	1, // 5: v1.RunnercliSoftwareSpecE.template:type_name -> v1.RunnercliSoftwareSpecTemplateType
	6, // [6:6] is the sub-list for method output_type
	6, // [6:6] is the sub-list for method input_type
	6, // [6:6] is the sub-list for extension type_name
	6, // [6:6] is the sub-list for extension extendee
	0, // [0:6] is the sub-list for field type_name
}

func init() { file_v1_runnercli_proto_init() }
func file_v1_runnercli_proto_init() {
	if File_v1_runnercli_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_v1_runnercli_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RunnercliContainerE); i {
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
		file_v1_runnercli_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RunnercliAccessLinkE); i {
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
		file_v1_runnercli_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RunnercliPodE); i {
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
		file_v1_runnercli_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RunnercliObjectMetaE); i {
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
		file_v1_runnercli_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RunnercliTypeMetaE); i {
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
		file_v1_runnercli_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RunnercliSoftwareSpecE); i {
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
			RawDescriptor: file_v1_runnercli_proto_rawDesc,
			NumEnums:      2,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_v1_runnercli_proto_goTypes,
		DependencyIndexes: file_v1_runnercli_proto_depIdxs,
		EnumInfos:         file_v1_runnercli_proto_enumTypes,
		MessageInfos:      file_v1_runnercli_proto_msgTypes,
	}.Build()
	File_v1_runnercli_proto = out.File
	file_v1_runnercli_proto_rawDesc = nil
	file_v1_runnercli_proto_goTypes = nil
	file_v1_runnercli_proto_depIdxs = nil
}
