// Generated by gencpp from file facial_puppetry/land_marks.msg
// DO NOT EDIT!


#ifndef FACIAL_PUPPETRY_MESSAGE_LAND_MARKS_H
#define FACIAL_PUPPETRY_MESSAGE_LAND_MARKS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace facial_puppetry
{
template <class ContainerAllocator>
struct land_marks_
{
  typedef land_marks_<ContainerAllocator> Type;

  land_marks_()
    : dlib_val()
    , max_ref()
    , distX(0.0)
    , distY(0.0)
    , distW(0.0)
    , distH(0.0)  {
    }
  land_marks_(const ContainerAllocator& _alloc)
    : dlib_val(_alloc)
    , max_ref(_alloc)
    , distX(0.0)
    , distY(0.0)
    , distW(0.0)
    , distH(0.0)  {
  (void)_alloc;
    }



   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _dlib_val_type;
  _dlib_val_type dlib_val;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _max_ref_type;
  _max_ref_type max_ref;

   typedef float _distX_type;
  _distX_type distX;

   typedef float _distY_type;
  _distY_type distY;

   typedef float _distW_type;
  _distW_type distW;

   typedef float _distH_type;
  _distH_type distH;




  typedef boost::shared_ptr< ::facial_puppetry::land_marks_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::facial_puppetry::land_marks_<ContainerAllocator> const> ConstPtr;

}; // struct land_marks_

typedef ::facial_puppetry::land_marks_<std::allocator<void> > land_marks;

typedef boost::shared_ptr< ::facial_puppetry::land_marks > land_marksPtr;
typedef boost::shared_ptr< ::facial_puppetry::land_marks const> land_marksConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::facial_puppetry::land_marks_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::facial_puppetry::land_marks_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace facial_puppetry

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'facial_puppetry': ['/home/icog-labs/hansonrobotics/HEAD/src/vision/facial_puppeteery/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::facial_puppetry::land_marks_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::facial_puppetry::land_marks_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::facial_puppetry::land_marks_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::facial_puppetry::land_marks_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::facial_puppetry::land_marks_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::facial_puppetry::land_marks_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::facial_puppetry::land_marks_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f6d1fcaa4d346ffd01a06e016371d2ee";
  }

  static const char* value(const ::facial_puppetry::land_marks_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf6d1fcaa4d346ffdULL;
  static const uint64_t static_value2 = 0x01a06e016371d2eeULL;
};

template<class ContainerAllocator>
struct DataType< ::facial_puppetry::land_marks_<ContainerAllocator> >
{
  static const char* value()
  {
    return "facial_puppetry/land_marks";
  }

  static const char* value(const ::facial_puppetry::land_marks_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::facial_puppetry::land_marks_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32[] dlib_val\n\
float32[] max_ref\n\
float32 distX\n\
float32 distY\n\
float32 distW\n\
float32 distH\n\
";
  }

  static const char* value(const ::facial_puppetry::land_marks_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::facial_puppetry::land_marks_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.dlib_val);
      stream.next(m.max_ref);
      stream.next(m.distX);
      stream.next(m.distY);
      stream.next(m.distW);
      stream.next(m.distH);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct land_marks_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::facial_puppetry::land_marks_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::facial_puppetry::land_marks_<ContainerAllocator>& v)
  {
    s << indent << "dlib_val[]" << std::endl;
    for (size_t i = 0; i < v.dlib_val.size(); ++i)
    {
      s << indent << "  dlib_val[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.dlib_val[i]);
    }
    s << indent << "max_ref[]" << std::endl;
    for (size_t i = 0; i < v.max_ref.size(); ++i)
    {
      s << indent << "  max_ref[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.max_ref[i]);
    }
    s << indent << "distX: ";
    Printer<float>::stream(s, indent + "  ", v.distX);
    s << indent << "distY: ";
    Printer<float>::stream(s, indent + "  ", v.distY);
    s << indent << "distW: ";
    Printer<float>::stream(s, indent + "  ", v.distW);
    s << indent << "distH: ";
    Printer<float>::stream(s, indent + "  ", v.distH);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FACIAL_PUPPETRY_MESSAGE_LAND_MARKS_H