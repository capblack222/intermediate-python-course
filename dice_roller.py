import random as r
roll=2

def main():
  roll_sum = 0
  for i in range(0,roll):
    n = r.randint(1, 6)
    roll_sum=roll_sum+n
    print(f'You have rolled a {n}')
  print(f'You have rolled a total of {roll_sum}')

if __name__== "__main__":
  main()