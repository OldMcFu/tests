// main.cpp
#include <iostream>
#include <vector>
#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>
#include <sstream>

std::string HexToBytesString(const std::string& hex) {
  std::string bytes;

  for (unsigned int i = 0; i < hex.length(); i += 2) {
    std::string byteString = hex.substr(i, 2);
    char byte = (char) strtol(byteString.c_str(), NULL, 16);
    bytes.push_back(byte);
  }
  return bytes;
}

int main()
{
  //Only for Tests
    std::string s;
    for (size_t i = 0; i < 256; i++)
    {
      std::stringstream sstream;
      sstream << std::hex << i;
      std::string result = sstream.str();
      if(result.size() == 1)
      {
        s += "0";
        s += (result);
      }
      else
      {
        s += (result);
      }
      
    }

    std::cout << s << "\n\n" <<std::endl;

    // String Hex to Bytes to String
    s.erase(std::remove_if(s.begin(), s.end(), ::isspace), s.end());
    std::cout << HexToBytesString(s) << "\n\n" <<std::endl;

  return 0;
}