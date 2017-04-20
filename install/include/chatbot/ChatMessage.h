// Generated by gencpp from file chatbot/ChatMessage.msg
// DO NOT EDIT!


#ifndef CHATBOT_MESSAGE_CHATMESSAGE_H
#define CHATBOT_MESSAGE_CHATMESSAGE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace chatbot
{
template <class ContainerAllocator>
struct ChatMessage_
{
  typedef ChatMessage_<ContainerAllocator> Type;

  ChatMessage_()
    : utterance()
    , confidence(0)  {
    }
  ChatMessage_(const ContainerAllocator& _alloc)
    : utterance(_alloc)
    , confidence(0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _utterance_type;
  _utterance_type utterance;

   typedef uint8_t _confidence_type;
  _confidence_type confidence;




  typedef boost::shared_ptr< ::chatbot::ChatMessage_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::chatbot::ChatMessage_<ContainerAllocator> const> ConstPtr;

}; // struct ChatMessage_

typedef ::chatbot::ChatMessage_<std::allocator<void> > ChatMessage;

typedef boost::shared_ptr< ::chatbot::ChatMessage > ChatMessagePtr;
typedef boost::shared_ptr< ::chatbot::ChatMessage const> ChatMessageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::chatbot::ChatMessage_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::chatbot::ChatMessage_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace chatbot

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'chatbot': ['/home/icog-labs/hansonrobotics/HEAD/src/chatbot/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::chatbot::ChatMessage_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::chatbot::ChatMessage_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::chatbot::ChatMessage_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::chatbot::ChatMessage_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::chatbot::ChatMessage_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::chatbot::ChatMessage_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::chatbot::ChatMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "522e7b49288c831e97c7f4e96555af58";
  }

  static const char* value(const ::chatbot::ChatMessage_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x522e7b49288c831eULL;
  static const uint64_t static_value2 = 0x97c7f4e96555af58ULL;
};

template<class ContainerAllocator>
struct DataType< ::chatbot::ChatMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "chatbot/ChatMessage";
  }

  static const char* value(const ::chatbot::ChatMessage_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::chatbot::ChatMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string utterance\n\
uint8 confidence\n\
";
  }

  static const char* value(const ::chatbot::ChatMessage_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::chatbot::ChatMessage_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.utterance);
      stream.next(m.confidence);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ChatMessage_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::chatbot::ChatMessage_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::chatbot::ChatMessage_<ContainerAllocator>& v)
  {
    s << indent << "utterance: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.utterance);
    s << indent << "confidence: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.confidence);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CHATBOT_MESSAGE_CHATMESSAGE_H