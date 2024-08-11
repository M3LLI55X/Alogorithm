#include<iostream>
#include<string>
int main(int argc, char const *argv[])
{
    std::string message;
    std::cin >> message;
    int length=message.length();
    std::cout<<length<<std::endl;
    return 0;
}
