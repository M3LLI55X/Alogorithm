#include<iostream>
#include<algorithm>
int main(int argc, char const *argv[])
{
    std::string message;
    std::cin>> message;
    bool isbPresent = (message.find('b') != std::string::npos);
    bool iskPresent = (message.find('k') != std::string::npos);
    
    if (isbPresent&& iskPresent)
    {
        std::cout<<"boki" <<std::endl;
    }else if (isbPresent&& ! iskPresent)
    {
        std::cout<<"boba" <<std::endl;
        /* code */
    }else if (!isbPresent&& iskPresent)
    {
        std::cout<<"kiki" <<std::endl;
    }else
    {
        std::cout<<"none" <<std::endl;
    }
}
