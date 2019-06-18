#include <iostream>
#include <random>

double monte_carlo()
{
  size_t inside = 0;
  size_t counter = 0;
  double min = 0;
  double max = 1.0;
  std::uniform_real_distribution<double> unif(min, max);
  std::default_random_engine engine;
  for (int i = 0; i < 100000000; i++)
  {
    double x = unif(engine);
    double y = unif(engine);
    if (x * x + y * y <= 1)
    {
      inside += 1;
    }
    counter += 1;
  } 
  return (4 * ((double)inside / (double)counter));
}

int main(void)
{
  std::cout.precision(17);
  std::cout <<  monte_carlo() << std::endl;
  return 0;
}