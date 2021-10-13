#include <iostream>
using namespace std;
int main()
{
    int BY;
    int current_year = 2021;
    cout << "Please enter your birth year\n";
    cin >> BY;
    cout << "Your age is " << current_year - BY << endl;
    return 0;
}
