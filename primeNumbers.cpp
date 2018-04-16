/*
Write a program which generates the first 100 prime numbers
* @author  Francesco Fresta
* @version 1.0, April 2018
*/

#include <iostream>
using namespace std;

void prime_numbers(){
  for (int number=2; number<=97; number++) //2 is the first prime number while 97 is the last one. Why waste time to check if 1 and 98-99-100 are prime numbers?
  {
    int divider = 2, reminder = 0; //I have just to check if the number is divisibile for itself
    while(number>divider)
    {
      reminder = number % divider; //save the reminder
      if (reminder == 0) break; //it the reminder is 0 it is not a prime number so go to the next number
      divider++; //otherwise increase the divider
    }
    //here if the condition is met it means the reminder was never 0 so the number can be divided just for 1 and itself, this is the definition of a prime number
    if(number == divider) cout << "The number" << number << " is prime" <<endl;
  }
}
int main()
    {
    prime_numbers();
    return 0;
    }
