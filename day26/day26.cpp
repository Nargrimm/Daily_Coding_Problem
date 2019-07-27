#include <iostream>
#include <list>

//the idea here is to iterate with two iterator, one is k elem ahead of the other
//when the first iterator reach the end we know that the second one is on the k(th) before last element

void remove_x_before_last(std::list<int> &l, int k)
{
  auto it = l.begin();
  std::advance(it, k + 1);
  auto it2 = l.begin();

  while (it != l.end())
  {
    it++;
    it2++;
  }
  l.erase(it2);
}

void print_list(std::list<int> &l)
{
  for (auto it : l)
  {
    std::cout << it << " ";
  }
  std::cout << std::endl;
}

int main(void)
{
  std::list<int> l = {10, 20, 30, 40, 50, 60, 70, 80, 90};
  print_list(l);
  remove_x_before_last(l, 0);
  print_list(l);
  remove_x_before_last(l, 6);
  print_list(l);
}
