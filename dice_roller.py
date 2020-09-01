import random as r
roll=int(input('How many dice do you want to roll? :'))

def main():
  roll_sum = 0
  dice_size=int(input('Enter the no of sides in your die:'))
  for i in range(0,roll):
    n = r.randint(1, 6)
    if n==1:
      print(f'You have rolled a {n}! Critical Failure!')
    elif n==dice_size:
      print(f'You have rolled a {n}! Critical Success!')
    else:
      print(f'You have rolled a {n}!')
    roll_sum=roll_sum+n

  print(f'You have rolled a total of {roll_sum}')

if __name__== "__main__":
  main()