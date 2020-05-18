#include <iostream>
using namespace std;

int main()
//This can be the new comment
//The comment is here>>>>>>> 3211f6e04905167c14bc849d3c04c40b87967372
{
    int year; // This is the year in integer form

    cout << "Enter a year: ";
    cin >> year;

    if (year % 4 == 0)
    {
        if (year % 100 == 0)
        {
            if (year % 400 == 0)
                cout << year << " is a leap year.";
            else
                cout << year << " is not a leap year.";
        }
        else
            cout << year << " is a leap year.";
    }
    else
        cout << year << " is not a leap year.";

    return 0;
}
