#include <iostream>

int main()
{
    int R;
    std::cin >> R;
    int low = 0;  // min
    int high = R; // max
    int mid;
    int total = 0;
    int days = 1;

    while (days <= 85)
    {
        mid = low + (high - low) / 2;
        total = mid * days;

        std::cout<<total<< "\n" << std::flush;

        std::string response;
        std::cin>>response;
        
        if (response=="exact")
        {
            break;
        }
        else if (response=="less")
        {
            high = mid - 1;
        }
        else if (response=="more")
        {
            low = mid + 1;
        }

        days++;
    }
}
