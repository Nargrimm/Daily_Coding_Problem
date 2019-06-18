import random

def monte_carlo():
  inside = 0
  counter = 0
  for i in range(0, 10000000):
    x2 = random.random()**2
    y2 = random.random()**2
    if x2 + y2 <= 1:
      inside += 1
    counter += 1
  return (4 * (inside / counter))


pi_approx = monte_carlo()

print(pi_approx)