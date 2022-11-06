// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.8.0
// source: v1/marketing.proto

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

// MarketingPromotionE 프로모션 정보
type MarketingPromotionE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id        string             `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Name      string             `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
	Discount  *DiscountE         `protobuf:"bytes,4,opt,name=discount,proto3" json:"discount,omitempty"`
	Product   *MarketingProductE `protobuf:"bytes,2,opt,name=product,proto3" json:"product,omitempty"`
	StartTime string             `protobuf:"bytes,5,opt,name=startTime,proto3" json:"startTime,omitempty"`
	EndTime   string             `protobuf:"bytes,6,opt,name=endTime,proto3" json:"endTime,omitempty"`
}

func (x *MarketingPromotionE) Reset() {
	*x = MarketingPromotionE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_marketing_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *MarketingPromotionE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MarketingPromotionE) ProtoMessage() {}

func (x *MarketingPromotionE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_marketing_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MarketingPromotionE.ProtoReflect.Descriptor instead.
func (*MarketingPromotionE) Descriptor() ([]byte, []int) {
	return file_v1_marketing_proto_rawDescGZIP(), []int{0}
}

func (x *MarketingPromotionE) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *MarketingPromotionE) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *MarketingPromotionE) GetDiscount() *DiscountE {
	if x != nil {
		return x.Discount
	}
	return nil
}

func (x *MarketingPromotionE) GetProduct() *MarketingProductE {
	if x != nil {
		return x.Product
	}
	return nil
}

func (x *MarketingPromotionE) GetStartTime() string {
	if x != nil {
		return x.StartTime
	}
	return ""
}

func (x *MarketingPromotionE) GetEndTime() string {
	if x != nil {
		return x.EndTime
	}
	return ""
}

// MarketingProductE 마케팅 제품
type MarketingProductE struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id             string  `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Name           string  `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	OriginPrice    *MoneyE `protobuf:"bytes,3,opt,name=originPrice,proto3" json:"originPrice,omitempty"`
	PromotionPrice *MoneyE `protobuf:"bytes,4,opt,name=promotionPrice,proto3" json:"promotionPrice,omitempty"`
}

func (x *MarketingProductE) Reset() {
	*x = MarketingProductE{}
	if protoimpl.UnsafeEnabled {
		mi := &file_v1_marketing_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *MarketingProductE) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MarketingProductE) ProtoMessage() {}

func (x *MarketingProductE) ProtoReflect() protoreflect.Message {
	mi := &file_v1_marketing_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MarketingProductE.ProtoReflect.Descriptor instead.
func (*MarketingProductE) Descriptor() ([]byte, []int) {
	return file_v1_marketing_proto_rawDescGZIP(), []int{1}
}

func (x *MarketingProductE) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *MarketingProductE) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *MarketingProductE) GetOriginPrice() *MoneyE {
	if x != nil {
		return x.OriginPrice
	}
	return nil
}

func (x *MarketingProductE) GetPromotionPrice() *MoneyE {
	if x != nil {
		return x.PromotionPrice
	}
	return nil
}

var File_v1_marketing_proto protoreflect.FileDescriptor

var file_v1_marketing_proto_rawDesc = []byte{
	0x0a, 0x12, 0x76, 0x31, 0x2f, 0x6d, 0x61, 0x72, 0x6b, 0x65, 0x74, 0x69, 0x6e, 0x67, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x02, 0x76, 0x31, 0x1a, 0x0d, 0x76, 0x31, 0x2f, 0x62, 0x61, 0x73,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xcd, 0x01, 0x0a, 0x13, 0x4d, 0x61, 0x72, 0x6b,
	0x65, 0x74, 0x69, 0x6e, 0x67, 0x50, 0x72, 0x6f, 0x6d, 0x6f, 0x74, 0x69, 0x6f, 0x6e, 0x45, 0x12,
	0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x12,
	0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e,
	0x61, 0x6d, 0x65, 0x12, 0x29, 0x0a, 0x08, 0x64, 0x69, 0x73, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x18,
	0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0d, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x69, 0x73, 0x63, 0x6f,
	0x75, 0x6e, 0x74, 0x45, 0x52, 0x08, 0x64, 0x69, 0x73, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x12, 0x2f,
	0x0a, 0x07, 0x70, 0x72, 0x6f, 0x64, 0x75, 0x63, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x15, 0x2e, 0x76, 0x31, 0x2e, 0x4d, 0x61, 0x72, 0x6b, 0x65, 0x74, 0x69, 0x6e, 0x67, 0x50, 0x72,
	0x6f, 0x64, 0x75, 0x63, 0x74, 0x45, 0x52, 0x07, 0x70, 0x72, 0x6f, 0x64, 0x75, 0x63, 0x74, 0x12,
	0x1c, 0x0a, 0x09, 0x73, 0x74, 0x61, 0x72, 0x74, 0x54, 0x69, 0x6d, 0x65, 0x18, 0x05, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x09, 0x73, 0x74, 0x61, 0x72, 0x74, 0x54, 0x69, 0x6d, 0x65, 0x12, 0x18, 0x0a,
	0x07, 0x65, 0x6e, 0x64, 0x54, 0x69, 0x6d, 0x65, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07,
	0x65, 0x6e, 0x64, 0x54, 0x69, 0x6d, 0x65, 0x22, 0x99, 0x01, 0x0a, 0x11, 0x4d, 0x61, 0x72, 0x6b,
	0x65, 0x74, 0x69, 0x6e, 0x67, 0x50, 0x72, 0x6f, 0x64, 0x75, 0x63, 0x74, 0x45, 0x12, 0x0e, 0x0a,
	0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x12, 0x12, 0x0a,
	0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d,
	0x65, 0x12, 0x2c, 0x0a, 0x0b, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x50, 0x72, 0x69, 0x63, 0x65,
	0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0a, 0x2e, 0x76, 0x31, 0x2e, 0x4d, 0x6f, 0x6e, 0x65,
	0x79, 0x45, 0x52, 0x0b, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x50, 0x72, 0x69, 0x63, 0x65, 0x12,
	0x32, 0x0a, 0x0e, 0x70, 0x72, 0x6f, 0x6d, 0x6f, 0x74, 0x69, 0x6f, 0x6e, 0x50, 0x72, 0x69, 0x63,
	0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0a, 0x2e, 0x76, 0x31, 0x2e, 0x4d, 0x6f, 0x6e,
	0x65, 0x79, 0x45, 0x52, 0x0e, 0x70, 0x72, 0x6f, 0x6d, 0x6f, 0x74, 0x69, 0x6f, 0x6e, 0x50, 0x72,
	0x69, 0x63, 0x65, 0x42, 0x51, 0x0a, 0x0e, 0x63, 0x6f, 0x6d, 0x2e, 0x6c, 0x75, 0x78, 0x72, 0x6f,
	0x62, 0x6f, 0x2e, 0x76, 0x31, 0x42, 0x11, 0x4d, 0x61, 0x72, 0x6b, 0x65, 0x74, 0x69, 0x6e, 0x67,
	0x41, 0x70, 0x69, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x0a, 0x6c, 0x75, 0x78, 0x72,
	0x6f, 0x62, 0x6f, 0x2f, 0x76, 0x31, 0xa2, 0x02, 0x03, 0x54, 0x50, 0x58, 0xaa, 0x02, 0x0a, 0x4c,
	0x75, 0x78, 0x72, 0x6f, 0x62, 0x6f, 0x2e, 0x76, 0x31, 0xca, 0x02, 0x0a, 0x4c, 0x75, 0x78, 0x72,
	0x6f, 0x62, 0x6f, 0x5c, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_v1_marketing_proto_rawDescOnce sync.Once
	file_v1_marketing_proto_rawDescData = file_v1_marketing_proto_rawDesc
)

func file_v1_marketing_proto_rawDescGZIP() []byte {
	file_v1_marketing_proto_rawDescOnce.Do(func() {
		file_v1_marketing_proto_rawDescData = protoimpl.X.CompressGZIP(file_v1_marketing_proto_rawDescData)
	})
	return file_v1_marketing_proto_rawDescData
}

var file_v1_marketing_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_v1_marketing_proto_goTypes = []interface{}{
	(*MarketingPromotionE)(nil), // 0: v1.MarketingPromotionE
	(*MarketingProductE)(nil),   // 1: v1.MarketingProductE
	(*DiscountE)(nil),           // 2: v1.DiscountE
	(*MoneyE)(nil),              // 3: v1.MoneyE
}
var file_v1_marketing_proto_depIdxs = []int32{
	2, // 0: v1.MarketingPromotionE.discount:type_name -> v1.DiscountE
	1, // 1: v1.MarketingPromotionE.product:type_name -> v1.MarketingProductE
	3, // 2: v1.MarketingProductE.originPrice:type_name -> v1.MoneyE
	3, // 3: v1.MarketingProductE.promotionPrice:type_name -> v1.MoneyE
	4, // [4:4] is the sub-list for method output_type
	4, // [4:4] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_v1_marketing_proto_init() }
func file_v1_marketing_proto_init() {
	if File_v1_marketing_proto != nil {
		return
	}
	file_v1_base_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_v1_marketing_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*MarketingPromotionE); i {
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
		file_v1_marketing_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*MarketingProductE); i {
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
			RawDescriptor: file_v1_marketing_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_v1_marketing_proto_goTypes,
		DependencyIndexes: file_v1_marketing_proto_depIdxs,
		MessageInfos:      file_v1_marketing_proto_msgTypes,
	}.Build()
	File_v1_marketing_proto = out.File
	file_v1_marketing_proto_rawDesc = nil
	file_v1_marketing_proto_goTypes = nil
	file_v1_marketing_proto_depIdxs = nil
}
