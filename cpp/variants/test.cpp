

// C++ program to illustrate
// Base & Derived Class
 
#include <cassert>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <locale>
#include <memory>
#include <stdexcept>
using namespace std;
 
// Declare Base Class
class Message_1 {
public:
    int a_1;
};

class Message_2 {
public:
    int a_2;
};

class Message_3 {
public:
    int a_3;
};
 
// Declare Derived Class
class Messages_Project_A : public Message_1, public Message_2 {
    public:
    Messages_Project_A() = default;
};

// Declare Derived Class
class Messages_Project_B : public Message_1, public Message_3 {
    public:
    Messages_Project_B() = default;
};

template <class D>
class Messages{
    public:
    std::unique_ptr<D> p = std::make_unique<D>();
    Messages() = default;
};
 
// Driver Code
int main()
{
    // Initialise a Derived class geeks
    Messages<Messages_Project_B> obj;
    // Assign value to Derived class variable
    obj.p.get()->a_1 = 3;
 
    // Assign value to Base class variable
    // via derived class
    obj.p.get()->a_3 = 10;
 
    cout << "Value from derived class: "
         << obj.p.get()->a_1<< endl;
 
    cout << "Value from base class: "
         << obj.p.get()->a_3 << endl;
 
    return 0;
}
