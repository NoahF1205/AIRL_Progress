# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kortex_driver/GetAllSafetyInformationRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import kortex_driver.msg

class GetAllSafetyInformationRequest(genpy.Message):
  _md5sum = "fa3403cd5897c9698bc0fdcb2a453fbc"
  _type = "kortex_driver/GetAllSafetyInformationRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """Empty input

================================================================================
MSG: kortex_driver/Empty
"""
  __slots__ = ['input']
  _slot_types = ['kortex_driver/Empty']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       input

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetAllSafetyInformationRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.input is None:
        self.input = kortex_driver.msg.Empty()
    else:
      self.input = kortex_driver.msg.Empty()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.input is None:
        self.input = kortex_driver.msg.Empty()
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.input is None:
        self.input = kortex_driver.msg.Empty()
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kortex_driver/GetAllSafetyInformationResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import kortex_driver.msg

class GetAllSafetyInformationResponse(genpy.Message):
  _md5sum = "93c578a5c13fe995b1d1d665a7cf5337"
  _type = "kortex_driver/GetAllSafetyInformationResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """SafetyInformationList output

================================================================================
MSG: kortex_driver/SafetyInformationList

SafetyInformation[] information
================================================================================
MSG: kortex_driver/SafetyInformation

SafetyHandle handle
bool can_change_safety_state
bool has_warning_threshold
bool has_error_threshold
uint32 limit_type
float32 default_warning_threshold
float32 default_error_threshold
float32 upper_hard_limit
float32 lower_hard_limit
uint32 status
uint32 unit
================================================================================
MSG: kortex_driver/SafetyHandle

uint32 identifier"""
  __slots__ = ['output']
  _slot_types = ['kortex_driver/SafetyInformationList']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       output

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetAllSafetyInformationResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.output is None:
        self.output = kortex_driver.msg.SafetyInformationList()
    else:
      self.output = kortex_driver.msg.SafetyInformationList()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.output.information)
      buff.write(_struct_I.pack(length))
      for val1 in self.output.information:
        _v1 = val1.handle
        _x = _v1.identifier
        buff.write(_get_struct_I().pack(_x))
        _x = val1
        buff.write(_get_struct_3BI4f2I().pack(_x.can_change_safety_state, _x.has_warning_threshold, _x.has_error_threshold, _x.limit_type, _x.default_warning_threshold, _x.default_error_threshold, _x.upper_hard_limit, _x.lower_hard_limit, _x.status, _x.unit))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.output is None:
        self.output = kortex_driver.msg.SafetyInformationList()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.output.information = []
      for i in range(0, length):
        val1 = kortex_driver.msg.SafetyInformation()
        _v2 = val1.handle
        start = end
        end += 4
        (_v2.identifier,) = _get_struct_I().unpack(str[start:end])
        _x = val1
        start = end
        end += 31
        (_x.can_change_safety_state, _x.has_warning_threshold, _x.has_error_threshold, _x.limit_type, _x.default_warning_threshold, _x.default_error_threshold, _x.upper_hard_limit, _x.lower_hard_limit, _x.status, _x.unit,) = _get_struct_3BI4f2I().unpack(str[start:end])
        val1.can_change_safety_state = bool(val1.can_change_safety_state)
        val1.has_warning_threshold = bool(val1.has_warning_threshold)
        val1.has_error_threshold = bool(val1.has_error_threshold)
        self.output.information.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.output.information)
      buff.write(_struct_I.pack(length))
      for val1 in self.output.information:
        _v3 = val1.handle
        _x = _v3.identifier
        buff.write(_get_struct_I().pack(_x))
        _x = val1
        buff.write(_get_struct_3BI4f2I().pack(_x.can_change_safety_state, _x.has_warning_threshold, _x.has_error_threshold, _x.limit_type, _x.default_warning_threshold, _x.default_error_threshold, _x.upper_hard_limit, _x.lower_hard_limit, _x.status, _x.unit))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.output is None:
        self.output = kortex_driver.msg.SafetyInformationList()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.output.information = []
      for i in range(0, length):
        val1 = kortex_driver.msg.SafetyInformation()
        _v4 = val1.handle
        start = end
        end += 4
        (_v4.identifier,) = _get_struct_I().unpack(str[start:end])
        _x = val1
        start = end
        end += 31
        (_x.can_change_safety_state, _x.has_warning_threshold, _x.has_error_threshold, _x.limit_type, _x.default_warning_threshold, _x.default_error_threshold, _x.upper_hard_limit, _x.lower_hard_limit, _x.status, _x.unit,) = _get_struct_3BI4f2I().unpack(str[start:end])
        val1.can_change_safety_state = bool(val1.can_change_safety_state)
        val1.has_warning_threshold = bool(val1.has_warning_threshold)
        val1.has_error_threshold = bool(val1.has_error_threshold)
        self.output.information.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3BI4f2I = None
def _get_struct_3BI4f2I():
    global _struct_3BI4f2I
    if _struct_3BI4f2I is None:
        _struct_3BI4f2I = struct.Struct("<3BI4f2I")
    return _struct_3BI4f2I
class GetAllSafetyInformation(object):
  _type          = 'kortex_driver/GetAllSafetyInformation'
  _md5sum = '6cd621443d851423fb32151d65f5f576'
  _request_class  = GetAllSafetyInformationRequest
  _response_class = GetAllSafetyInformationResponse