# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: phone.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='phone.proto',
  package='com.hello.world',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bphone.proto\x12\x0f\x63om.hello.world\"%\n\x05Phone\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x03\x62\x06proto3'
)




_PHONE = _descriptor.Descriptor(
  name='Phone',
  full_name='com.hello.world.Phone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.hello.world.Phone.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='com.hello.world.Phone.number', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=69,
)

DESCRIPTOR.message_types_by_name['Phone'] = _PHONE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Phone = _reflection.GeneratedProtocolMessageType('Phone', (_message.Message,), {
  'DESCRIPTOR' : _PHONE,
  '__module__' : 'phone_pb2'
  # @@protoc_insertion_point(class_scope:com.hello.world.Phone)
  })
_sym_db.RegisterMessage(Phone)


# @@protoc_insertion_point(module_scope)
