#include<iostream>
#include<algorithm>
#include<cmath>
int main(int argc, char const *argv[])
{
    int altitude;
    int ve;
    std::cin>> altitude >> ve;
    
    if (ve>=0 && ve<=180)
    {
        std::cout<<"safe"<<std::endl;
    }else if (ve>180)
    {
        if (ve<270)
        {
            int deg=270-ve;
            int s= altitude/sin(deg);
            std::cout<< s<<std::endl;

        }else if (ve>270)
        {
            int deg=ve-270;
            int s =altitude/cos(deg);
            std::cout<<s <<std::endl;
        }else if (ve=270)
        {
            std::cout<<altitude <<std::endl;
        }
        
    }
    return 0;
}
