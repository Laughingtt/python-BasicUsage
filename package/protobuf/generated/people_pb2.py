# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: people.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import phone_pb2 as phone__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='people.proto',
  package='com.hello.world',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cpeople.proto\x12\x0f\x63om.hello.world\x1a\x0bphone.proto\"#\n\x06People\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\"\x9f\x02\n\x0bInformation\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0b\n\x03\x62id\x18\x03 \x01(\x01\x12\x1b\n\x13is_shortsightedness\x18\x04 \x01(\x08\x12\r\n\x05hobby\x18\x05 \x03(\t\x12:\n\x07\x66riends\x18\x06 \x03(\x0b\x32).com.hello.world.Information.FriendsEntry\x12\'\n\x06people\x18\x07 \x01(\x0b\x32\x17.com.hello.world.People\x12%\n\x05phone\x18\x08 \x01(\x0b\x32\x16.com.hello.world.Phone\x1a.\n\x0c\x46riendsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x62\x06proto3'
  ,
  dependencies=[phone__pb2.DESCRIPTOR,])




_PEOPLE = _descriptor.Descriptor(
  name='People',
  full_name='com.hello.world.People',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.hello.world.People.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='com.hello.world.People.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=46,
  serialized_end=81,
)


_INFORMATION_FRIENDSENTRY = _descriptor.Descriptor(
  name='FriendsEntry',
  full_name='com.hello.world.Information.FriendsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.hello.world.Information.FriendsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.hello.world.Information.FriendsEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=371,
)

_INFORMATION = _descriptor.Descriptor(
  name='Information',
  full_name='com.hello.world.Information',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.hello.world.Information.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='com.hello.world.Information.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid', full_name='com.hello.world.Information.bid', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_shortsightedness', full_name='com.hello.world.Information.is_shortsightedness', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hobby', full_name='com.hello.world.Information.hobby', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='friends', full_name='com.hello.world.Information.friends', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='people', full_name='com.hello.world.Information.people', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone', full_name='com.hello.world.Information.phone', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_INFORMATION_FRIENDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=371,
)

_INFORMATION_FRIENDSENTRY.containing_type = _INFORMATION
_INFORMATION.fields_by_name['friends'].message_type = _INFORMATION_FRIENDSENTRY
_INFORMATION.fields_by_name['people'].message_type = _PEOPLE
_INFORMATION.fields_by_name['phone'].message_type = phone__pb2._PHONE
DESCRIPTOR.message_types_by_name['People'] = _PEOPLE
DESCRIPTOR.message_types_by_name['Information'] = _INFORMATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

People = _reflection.GeneratedProtocolMessageType('People', (_message.Message,), {
  'DESCRIPTOR' : _PEOPLE,
  '__module__' : 'people_pb2'
  # @@protoc_insertion_point(class_scope:com.hello.world.People)
  })
_sym_db.RegisterMessage(People)

Information = _reflection.GeneratedProtocolMessageType('Information', (_message.Message,), {

  'FriendsEntry' : _reflection.GeneratedProtocolMessageType('FriendsEntry', (_message.Message,), {
    'DESCRIPTOR' : _INFORMATION_FRIENDSENTRY,
    '__module__' : 'people_pb2'
    # @@protoc_insertion_point(class_scope:com.hello.world.Information.FriendsEntry)
    })
  ,
  'DESCRIPTOR' : _INFORMATION,
  '__module__' : 'people_pb2'
  # @@protoc_insertion_point(class_scope:com.hello.world.Information)
  })
_sym_db.RegisterMessage(Information)
_sym_db.RegisterMessage(Information.FriendsEntry)


_INFORMATION_FRIENDSENTRY._options = None
# @@protoc_insertion_point(module_scope)
