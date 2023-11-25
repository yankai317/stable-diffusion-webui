# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/sd.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eproto/sd.proto\"\xc6\x01\n\x11SdText2ImgRequest\x12\x0e\n\x06prompt\x18\x01 \x01(\t\x12\x17\n\x0fnegative_prompt\x18\x02 \x01(\t\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x0c\n\x04seed\x18\x05 \x01(\x05\x12\r\n\x05steps\x18\x06 \x01(\x05\x12\x12\n\nbatch_size\x18\x07 \x01(\x05\x12\x11\n\tenable_hr\x18\x08 \x01(\x08\x12\x10\n\x08hr_scale\x18\t \x01(\x02\x12\x13\n\x0bhr_upscaler\x18\n \x01(\t\"\xcc\x01\n\x10SdImg2ImgRequest\x12\x15\n\rbase64_images\x18\x01 \x03(\t\x12\x0c\n\x04mask\x18\x02 \x01(\t\x12\x0e\n\x06prompt\x18\x03 \x01(\t\x12\x17\n\x0fnegative_prompt\x18\x04 \x01(\t\x12\r\n\x05width\x18\x05 \x01(\x05\x12\x0e\n\x06height\x18\x06 \x01(\x05\x12\x0c\n\x04seed\x18\x07 \x01(\x05\x12\r\n\x05steps\x18\x08 \x01(\x05\x12\x12\n\nbatch_size\x18\t \x01(\x05\x12\x1a\n\x12\x64\x65noising_strength\x18\n \x01(\x02\"V\n\x10SdUpscaleRequest\x12\x14\n\x0c\x62\x61se64_image\x18\x01 \x01(\t\x12\x18\n\x10upscaling_resize\x18\x02 \x01(\x05\x12\x12\n\nupscaler_1\x18\x03 \x01(\t\"\xbe\x01\n\x10SdImgFuseRequest\x12\x15\n\rbase64_images\x18\x01 \x03(\t\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x17\n\x0fnegative_prompt\x18\x03 \x01(\t\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12\x0c\n\x04seed\x18\x06 \x01(\x05\x12\r\n\x05steps\x18\x07 \x01(\x05\x12\x12\n\nbatch_size\x18\x08 \x01(\x05\x12\x1a\n\x12\x64\x65noising_strength\x18\t \x01(\x02\"\xf0\x01\n\x11SdCtrl2ImgRequest\x12\x14\n\x0c\x62\x61se64_image\x18\x01 \x01(\t\x12\x12\n\nperference\x18\x02 \x01(\t\x12\x0e\n\x06prompt\x18\x03 \x01(\t\x12\x17\n\x0fnegative_prompt\x18\x04 \x01(\t\x12\r\n\x05width\x18\x05 \x01(\x05\x12\x0e\n\x06height\x18\x06 \x01(\x05\x12\x0c\n\x04seed\x18\x07 \x01(\x05\x12\r\n\x05steps\x18\x08 \x01(\x05\x12\x12\n\nbatch_size\x18\t \x01(\x05\x12\x11\n\tenable_hr\x18\n \x01(\x08\x12\x10\n\x08hr_scale\x18\x0b \x01(\x02\x12\x13\n\x0bhr_upscaler\x18\x0c \x01(\t\"=\n\nSdResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x0e\n\x06\x62\x61se64\x18\x03 \x03(\t\"F\n\x12SdAsynTaskResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x0f\n\x07task_id\x18\x03 \x01(\t\"!\n\x0eSdQueryRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t2\xbf\x04\n\tSdService\x12-\n\x08text2img\x12\x12.SdText2ImgRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07img2img\x12\x11.SdImg2ImgRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07upscale\x12\x11.SdUpscaleRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07imgfuse\x12\x11.SdImgFuseRequest\x1a\x0b.SdResponse\"\x00\x12-\n\x08\x63trl2img\x12\x12.SdCtrl2ImgRequest\x1a\x0b.SdResponse\"\x00\x12:\n\rtext2img_asyn\x12\x12.SdText2ImgRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12\x38\n\x0cimg2img_asyn\x12\x11.SdImg2ImgRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12\x38\n\x0cupscale_asyn\x12\x11.SdUpscaleRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12\x38\n\x0cimgfuse_asyn\x12\x11.SdImgFuseRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12:\n\rctrl2img_asyn\x12\x12.SdCtrl2ImgRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12\'\n\x05query\x12\x0f.SdQueryRequest\x1a\x0b.SdResponse\"\x00\x32\xef\x01\n\x08SdEngine\x12-\n\x08text2img\x12\x12.SdText2ImgRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07img2img\x12\x11.SdImg2ImgRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07upscale\x12\x11.SdUpscaleRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07imgfuse\x12\x11.SdImgFuseRequest\x1a\x0b.SdResponse\"\x00\x12-\n\x08\x63trl2img\x12\x12.SdCtrl2ImgRequest\x1a\x0b.SdResponse\"\x00\x42\x03\x80\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.sd_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\200\001\001'
  _globals['_SDTEXT2IMGREQUEST']._serialized_start=19
  _globals['_SDTEXT2IMGREQUEST']._serialized_end=217
  _globals['_SDIMG2IMGREQUEST']._serialized_start=220
  _globals['_SDIMG2IMGREQUEST']._serialized_end=424
  _globals['_SDUPSCALEREQUEST']._serialized_start=426
  _globals['_SDUPSCALEREQUEST']._serialized_end=512
  _globals['_SDIMGFUSEREQUEST']._serialized_start=515
  _globals['_SDIMGFUSEREQUEST']._serialized_end=705
  _globals['_SDCTRL2IMGREQUEST']._serialized_start=708
  _globals['_SDCTRL2IMGREQUEST']._serialized_end=948
  _globals['_SDRESPONSE']._serialized_start=950
  _globals['_SDRESPONSE']._serialized_end=1011
  _globals['_SDASYNTASKRESPONSE']._serialized_start=1013
  _globals['_SDASYNTASKRESPONSE']._serialized_end=1083
  _globals['_SDQUERYREQUEST']._serialized_start=1085
  _globals['_SDQUERYREQUEST']._serialized_end=1118
  _globals['_SDSERVICE']._serialized_start=1121
  _globals['_SDSERVICE']._serialized_end=1696
  _globals['_SDENGINE']._serialized_start=1699
  _globals['_SDENGINE']._serialized_end=1938
# @@protoc_insertion_point(module_scope)
