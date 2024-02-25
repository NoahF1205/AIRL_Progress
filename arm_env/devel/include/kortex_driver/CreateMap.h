// Generated by gencpp from file kortex_driver/CreateMap.msg
// DO NOT EDIT!


#ifndef KORTEX_DRIVER_MESSAGE_CREATEMAP_H
#define KORTEX_DRIVER_MESSAGE_CREATEMAP_H

#include <ros/service_traits.h>


#include <kortex_driver/CreateMapRequest.h>
#include <kortex_driver/CreateMapResponse.h>


namespace kortex_driver
{

struct CreateMap
{

typedef CreateMapRequest Request;
typedef CreateMapResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct CreateMap
} // namespace kortex_driver


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::kortex_driver::CreateMap > {
  static const char* value()
  {
    return "2cd2faeb0b189ebb1e692139094333a8";
  }

  static const char* value(const ::kortex_driver::CreateMap&) { return value(); }
};

template<>
struct DataType< ::kortex_driver::CreateMap > {
  static const char* value()
  {
    return "kortex_driver/CreateMap";
  }

  static const char* value(const ::kortex_driver::CreateMap&) { return value(); }
};


// service_traits::MD5Sum< ::kortex_driver::CreateMapRequest> should match
// service_traits::MD5Sum< ::kortex_driver::CreateMap >
template<>
struct MD5Sum< ::kortex_driver::CreateMapRequest>
{
  static const char* value()
  {
    return MD5Sum< ::kortex_driver::CreateMap >::value();
  }
  static const char* value(const ::kortex_driver::CreateMapRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::kortex_driver::CreateMapRequest> should match
// service_traits::DataType< ::kortex_driver::CreateMap >
template<>
struct DataType< ::kortex_driver::CreateMapRequest>
{
  static const char* value()
  {
    return DataType< ::kortex_driver::CreateMap >::value();
  }
  static const char* value(const ::kortex_driver::CreateMapRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::kortex_driver::CreateMapResponse> should match
// service_traits::MD5Sum< ::kortex_driver::CreateMap >
template<>
struct MD5Sum< ::kortex_driver::CreateMapResponse>
{
  static const char* value()
  {
    return MD5Sum< ::kortex_driver::CreateMap >::value();
  }
  static const char* value(const ::kortex_driver::CreateMapResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::kortex_driver::CreateMapResponse> should match
// service_traits::DataType< ::kortex_driver::CreateMap >
template<>
struct DataType< ::kortex_driver::CreateMapResponse>
{
  static const char* value()
  {
    return DataType< ::kortex_driver::CreateMap >::value();
  }
  static const char* value(const ::kortex_driver::CreateMapResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // KORTEX_DRIVER_MESSAGE_CREATEMAP_H