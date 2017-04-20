# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cmt_tracker_msgs/Object.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import sensor_msgs.msg
import opencv_apps.msg
import std_msgs.msg

class Object(genpy.Message):
  _md5sum = "232560d9417be3244e13955b54eafc19"
  _type = "cmt_tracker_msgs/Object"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
sensor_msgs/RegionOfInterest object
std_msgs/Int32 id
std_msgs/String obj_states
std_msgs/Float64 obj_accuracy
opencv_apps/Point2DArray feature_point
geometry_msgs/Pose pose
std_msgs/String tool_used_for_detection
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: sensor_msgs/RegionOfInterest
# This message is used to specify a region of interest within an image.
#
# When used to specify the ROI setting of the camera when the image was
# taken, the height and width fields should either match the height and
# width fields for the associated image; or height = width = 0
# indicates that the full resolution image was captured.

uint32 x_offset  # Leftmost pixel of the ROI
                 # (0 if the ROI includes the left edge of the image)
uint32 y_offset  # Topmost pixel of the ROI
                 # (0 if the ROI includes the top edge of the image)
uint32 height    # Height of ROI
uint32 width     # Width of ROI

# True if a distinct rectified ROI should be calculated from the "raw"
# ROI in this message. Typically this should be False if the full image
# is captured (ROI not used), and True if a subwindow is captured (ROI
# used).
bool do_rectify

================================================================================
MSG: std_msgs/Int32
int32 data
================================================================================
MSG: std_msgs/String
string data

================================================================================
MSG: std_msgs/Float64
float64 data
================================================================================
MSG: opencv_apps/Point2DArray
Point2D[] points

================================================================================
MSG: opencv_apps/Point2D
float64 x
float64 y


================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','object','id','obj_states','obj_accuracy','feature_point','pose','tool_used_for_detection']
  _slot_types = ['std_msgs/Header','sensor_msgs/RegionOfInterest','std_msgs/Int32','std_msgs/String','std_msgs/Float64','opencv_apps/Point2DArray','geometry_msgs/Pose','std_msgs/String']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,object,id,obj_states,obj_accuracy,feature_point,pose,tool_used_for_detection

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Object, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.object is None:
        self.object = sensor_msgs.msg.RegionOfInterest()
      if self.id is None:
        self.id = std_msgs.msg.Int32()
      if self.obj_states is None:
        self.obj_states = std_msgs.msg.String()
      if self.obj_accuracy is None:
        self.obj_accuracy = std_msgs.msg.Float64()
      if self.feature_point is None:
        self.feature_point = opencv_apps.msg.Point2DArray()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.tool_used_for_detection is None:
        self.tool_used_for_detection = std_msgs.msg.String()
    else:
      self.header = std_msgs.msg.Header()
      self.object = sensor_msgs.msg.RegionOfInterest()
      self.id = std_msgs.msg.Int32()
      self.obj_states = std_msgs.msg.String()
      self.obj_accuracy = std_msgs.msg.Float64()
      self.feature_point = opencv_apps.msg.Point2DArray()
      self.pose = geometry_msgs.msg.Pose()
      self.tool_used_for_detection = std_msgs.msg.String()

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
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4IBi.pack(_x.object.x_offset, _x.object.y_offset, _x.object.height, _x.object.width, _x.object.do_rectify, _x.id.data))
      _x = self.obj_states.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.obj_accuracy.data))
      length = len(self.feature_point.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.feature_point.points:
        _x = val1
        buff.write(_struct_2d.pack(_x.x, _x.y))
      _x = self
      buff.write(_struct_7d.pack(_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w))
      _x = self.tool_used_for_detection.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.object is None:
        self.object = sensor_msgs.msg.RegionOfInterest()
      if self.id is None:
        self.id = std_msgs.msg.Int32()
      if self.obj_states is None:
        self.obj_states = std_msgs.msg.String()
      if self.obj_accuracy is None:
        self.obj_accuracy = std_msgs.msg.Float64()
      if self.feature_point is None:
        self.feature_point = opencv_apps.msg.Point2DArray()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.tool_used_for_detection is None:
        self.tool_used_for_detection = std_msgs.msg.String()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 21
      (_x.object.x_offset, _x.object.y_offset, _x.object.height, _x.object.width, _x.object.do_rectify, _x.id.data,) = _struct_4IBi.unpack(str[start:end])
      self.object.do_rectify = bool(self.object.do_rectify)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.obj_states.data = str[start:end].decode('utf-8')
      else:
        self.obj_states.data = str[start:end]
      start = end
      end += 8
      (self.obj_accuracy.data,) = _struct_d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.feature_point.points = []
      for i in range(0, length):
        val1 = opencv_apps.msg.Point2D()
        _x = val1
        start = end
        end += 16
        (_x.x, _x.y,) = _struct_2d.unpack(str[start:end])
        self.feature_point.points.append(val1)
      _x = self
      start = end
      end += 56
      (_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tool_used_for_detection.data = str[start:end].decode('utf-8')
      else:
        self.tool_used_for_detection.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4IBi.pack(_x.object.x_offset, _x.object.y_offset, _x.object.height, _x.object.width, _x.object.do_rectify, _x.id.data))
      _x = self.obj_states.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.obj_accuracy.data))
      length = len(self.feature_point.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.feature_point.points:
        _x = val1
        buff.write(_struct_2d.pack(_x.x, _x.y))
      _x = self
      buff.write(_struct_7d.pack(_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w))
      _x = self.tool_used_for_detection.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.object is None:
        self.object = sensor_msgs.msg.RegionOfInterest()
      if self.id is None:
        self.id = std_msgs.msg.Int32()
      if self.obj_states is None:
        self.obj_states = std_msgs.msg.String()
      if self.obj_accuracy is None:
        self.obj_accuracy = std_msgs.msg.Float64()
      if self.feature_point is None:
        self.feature_point = opencv_apps.msg.Point2DArray()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.tool_used_for_detection is None:
        self.tool_used_for_detection = std_msgs.msg.String()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 21
      (_x.object.x_offset, _x.object.y_offset, _x.object.height, _x.object.width, _x.object.do_rectify, _x.id.data,) = _struct_4IBi.unpack(str[start:end])
      self.object.do_rectify = bool(self.object.do_rectify)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.obj_states.data = str[start:end].decode('utf-8')
      else:
        self.obj_states.data = str[start:end]
      start = end
      end += 8
      (self.obj_accuracy.data,) = _struct_d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.feature_point.points = []
      for i in range(0, length):
        val1 = opencv_apps.msg.Point2D()
        _x = val1
        start = end
        end += 16
        (_x.x, _x.y,) = _struct_2d.unpack(str[start:end])
        self.feature_point.points.append(val1)
      _x = self
      start = end
      end += 56
      (_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tool_used_for_detection.data = str[start:end].decode('utf-8')
      else:
        self.tool_used_for_detection.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2d = struct.Struct("<2d")
_struct_3I = struct.Struct("<3I")
_struct_7d = struct.Struct("<7d")
_struct_4IBi = struct.Struct("<4IBi")
_struct_d = struct.Struct("<d")