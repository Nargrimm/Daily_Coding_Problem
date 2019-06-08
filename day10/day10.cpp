/**
 *
 * Implement a job scheduler which takes in a function f and an
 * integer n, and calls f after n milliseconds.
 */

#include <chrono>
#include <functional>
#include <iostream>
#include <thread>

template <typename T, typename... Args>
void scheduler(size_t delay, T f, Args... args)
{
  std::this_thread::sleep_for(std::chrono::milliseconds(delay));
  f(args...);
}


void print_integer(int a)
{
  std::cout << "Printing after " << a << " milliseconds" << std::endl;
}

int add(int a, int b)
{
  std::cout << a << " + " << b << " = " << a + b << std::endl;
  return a + b;
}

int main(int argc, char **argv)
{
  scheduler(100, print_integer, 100);
  scheduler(1000, print_integer, 1000);
  scheduler(1500, print_integer, 1500);
  scheduler(1000, add, 3, 2);
  scheduler(100, add, 213, 12);
}
