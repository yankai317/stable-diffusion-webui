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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eproto/sd.proto\"\xf9\x01\n\x11SdText2ImgRequest\x12\x0e\n\x06prompt\x18\x01 \x01(\t\x12\x17\n\x0fnegative_prompt\x18\x02 \x01(\t\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x0c\n\x04seed\x18\x05 \x01(\x05\x12\r\n\x05steps\x18\x06 \x01(\x05\x12\x12\n\nbatch_size\x18\x07 \x01(\x05\x12\x11\n\tenable_hr\x18\x08 \x01(\x08\x12\x10\n\x08hr_scale\x18\t \x01(\x02\x12\x13\n\x0bhr_upscaler\x18\n \x01(\t\x12\x11\n\tcfg_scale\x18\x0b \x01(\x02\x12\x1e\n\x16\x64isable_default_prompt\x18\x0c \x01(\x08\"\xff\x01\n\x10SdImg2ImgRequest\x12\x15\n\rbase64_images\x18\x01 \x03(\t\x12\x0c\n\x04mask\x18\x02 \x01(\t\x12\x0e\n\x06prompt\x18\x03 \x01(\t\x12\x17\n\x0fnegative_prompt\x18\x04 \x01(\t\x12\r\n\x05width\x18\x05 \x01(\x05\x12\x0e\n\x06height\x18\x06 \x01(\x05\x12\x0c\n\x04seed\x18\x07 \x01(\x05\x12\r\n\x05steps\x18\x08 \x01(\x05\x12\x12\n\nbatch_size\x18\t \x01(\x05\x12\x1a\n\x12\x64\x65noising_strength\x18\n \x01(\x02\x12\x11\n\tcfg_scale\x18\x0b \x01(\x02\x12\x1e\n\x16\x64isable_default_prompt\x18\x0c \x01(\x08\"V\n\x10SdUpscaleRequest\x12\x14\n\x0c\x62\x61se64_image\x18\x01 \x01(\t\x12\x18\n\x10upscaling_resize\x18\x02 \x01(\x05\x12\x12\n\nupscaler_1\x18\x03 \x01(\t\"\xde\x01\n\x10SdImgFuseRequest\x12\x15\n\rbase64_images\x18\x01 \x03(\t\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x17\n\x0fnegative_prompt\x18\x03 \x01(\t\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12\x0c\n\x04seed\x18\x06 \x01(\x05\x12\r\n\x05steps\x18\x07 \x01(\x05\x12\x12\n\nbatch_size\x18\x08 \x01(\x05\x12\x1a\n\x12\x64\x65noising_strength\x18\t \x01(\x02\x12\x1e\n\x16\x64isable_default_prompt\x18\n \x01(\x08\"\x90\x02\n\x11SdCtrl2ImgRequest\x12\x14\n\x0c\x62\x61se64_image\x18\x01 \x01(\t\x12\x12\n\nperference\x18\x02 \x01(\t\x12\x0e\n\x06prompt\x18\x03 \x01(\t\x12\x17\n\x0fnegative_prompt\x18\x04 \x01(\t\x12\r\n\x05width\x18\x05 \x01(\x05\x12\x0e\n\x06height\x18\x06 \x01(\x05\x12\x0c\n\x04seed\x18\x07 \x01(\x05\x12\r\n\x05steps\x18\x08 \x01(\x05\x12\x12\n\nbatch_size\x18\t \x01(\x05\x12\x11\n\tenable_hr\x18\n \x01(\x08\x12\x10\n\x08hr_scale\x18\x0b \x01(\x02\x12\x13\n\x0bhr_upscaler\x18\x0c \x01(\t\x12\x1e\n\x16\x64isable_default_prompt\x18\r \x01(\x08\",\n\x14SdInterrogateRequest\x12\x14\n\x0c\x62\x61se64_image\x18\x01 \x01(\t\"j\n\x12SdNormalizeRequest\x12\x14\n\x0c\x62\x61se64_image\x18\x01 \x01(\t\x12\x0e\n\x06resize\x18\x02 \x01(\x08\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\r\n\x05model\x18\x04 \x01(\t\x12\x11\n\tthreshold\x18\x05 \x01(\x05\"f\n\x0eSdCannyRequest\x12\x14\n\x0c\x62\x61se64_image\x18\x01 \x01(\t\x12\x15\n\rlow_threshold\x18\x02 \x01(\x05\x12\x16\n\x0ehigh_threshold\x18\x03 \x01(\x05\x12\x0f\n\x07reverse\x18\x04 \x01(\x08\"\xb5\x01\n\x10SdAnydoorRequest\x12\r\n\x05image\x18\x01 \x01(\t\x12\x0c\n\x04mask\x18\x02 \x01(\t\x12\x11\n\tref_image\x18\x03 \x01(\t\x12\x10\n\x08ref_mask\x18\x04 \x01(\t\x12\x10\n\x08strength\x18\x05 \x01(\x02\x12\x12\n\nddim_steps\x18\x06 \x01(\x05\x12\r\n\x05scale\x18\x07 \x01(\x02\x12\x0c\n\x04seed\x18\x08 \x01(\x05\x12\x1c\n\x14\x65nable_shape_control\x18\t \x01(\x08\"=\n\nSdResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x0e\n\x06\x62\x61se64\x18\x03 \x03(\t\"@\n\rSdStrResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x0e\n\x06prompt\x18\x03 \x01(\t\"F\n\x12SdAsynTaskResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x0f\n\x07task_id\x18\x03 \x01(\t\"!\n\x0eSdQueryRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t2\xfe\x05\n\tSdService\x12-\n\x08text2img\x12\x12.SdText2ImgRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07img2img\x12\x11.SdImg2ImgRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07upscale\x12\x11.SdUpscaleRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07imgfuse\x12\x11.SdImgFuseRequest\x1a\x0b.SdResponse\"\x00\x12-\n\x08\x63trl2img\x12\x12.SdCtrl2ImgRequest\x1a\x0b.SdResponse\"\x00\x12\x36\n\x0binterrogate\x12\x15.SdInterrogateRequest\x1a\x0e.SdStrResponse\"\x00\x12/\n\tnormalize\x12\x13.SdNormalizeRequest\x1a\x0b.SdResponse\"\x00\x12\'\n\x05\x63\x61nny\x12\x0f.SdCannyRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07\x61nydoor\x12\x11.SdAnydoorRequest\x1a\x0b.SdResponse\"\x00\x12:\n\rtext2img_asyn\x12\x12.SdText2ImgRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12\x38\n\x0cimg2img_asyn\x12\x11.SdImg2ImgRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12\x38\n\x0cupscale_asyn\x12\x11.SdUpscaleRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12\x38\n\x0cimgfuse_asyn\x12\x11.SdImgFuseRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12:\n\rctrl2img_asyn\x12\x12.SdCtrl2ImgRequest\x1a\x13.SdAsynTaskResponse\"\x00\x12\'\n\x05query\x12\x0f.SdQueryRequest\x1a\x0b.SdResponse\"\x00\x32\xae\x03\n\x08SdEngine\x12-\n\x08text2img\x12\x12.SdText2ImgRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07img2img\x12\x11.SdImg2ImgRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07upscale\x12\x11.SdUpscaleRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07imgfuse\x12\x11.SdImgFuseRequest\x1a\x0b.SdResponse\"\x00\x12-\n\x08\x63trl2img\x12\x12.SdCtrl2ImgRequest\x1a\x0b.SdResponse\"\x00\x12\x36\n\x0binterrogate\x12\x15.SdInterrogateRequest\x1a\x0e.SdStrResponse\"\x00\x12/\n\tnormalize\x12\x13.SdNormalizeRequest\x1a\x0b.SdResponse\"\x00\x12\'\n\x05\x63\x61nny\x12\x0f.SdCannyRequest\x1a\x0b.SdResponse\"\x00\x12+\n\x07\x61nydoor\x12\x11.SdAnydoorRequest\x1a\x0b.SdResponse\"\x00\x42\x03\x80\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.sd_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\200\001\001'
  _globals['_SDTEXT2IMGREQUEST']._serialized_start=19
  _globals['_SDTEXT2IMGREQUEST']._serialized_end=268
  _globals['_SDIMG2IMGREQUEST']._serialized_start=271
  _globals['_SDIMG2IMGREQUEST']._serialized_end=526
  _globals['_SDUPSCALEREQUEST']._serialized_start=528
  _globals['_SDUPSCALEREQUEST']._serialized_end=614
  _globals['_SDIMGFUSEREQUEST']._serialized_start=617
  _globals['_SDIMGFUSEREQUEST']._serialized_end=839
  _globals['_SDCTRL2IMGREQUEST']._serialized_start=842
  _globals['_SDCTRL2IMGREQUEST']._serialized_end=1114
  _globals['_SDINTERROGATEREQUEST']._serialized_start=1116
  _globals['_SDINTERROGATEREQUEST']._serialized_end=1160
  _globals['_SDNORMALIZEREQUEST']._serialized_start=1162
  _globals['_SDNORMALIZEREQUEST']._serialized_end=1268
  _globals['_SDCANNYREQUEST']._serialized_start=1270
  _globals['_SDCANNYREQUEST']._serialized_end=1372
  _globals['_SDANYDOORREQUEST']._serialized_start=1375
  _globals['_SDANYDOORREQUEST']._serialized_end=1556
  _globals['_SDRESPONSE']._serialized_start=1558
  _globals['_SDRESPONSE']._serialized_end=1619
  _globals['_SDSTRRESPONSE']._serialized_start=1621
  _globals['_SDSTRRESPONSE']._serialized_end=1685
  _globals['_SDASYNTASKRESPONSE']._serialized_start=1687
  _globals['_SDASYNTASKRESPONSE']._serialized_end=1757
  _globals['_SDQUERYREQUEST']._serialized_start=1759
  _globals['_SDQUERYREQUEST']._serialized_end=1792
  _globals['_SDSERVICE']._serialized_start=1795
  _globals['_SDSERVICE']._serialized_end=2561
  _globals['_SDENGINE']._serialized_start=2564
  _globals['_SDENGINE']._serialized_end=2994
# @@protoc_insertion_point(module_scope)
