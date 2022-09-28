

from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()


p1_score = 0
p2_score = 0



while True:
  p1 = input("player 1 > ")
  print()
  p2 = input("player 2 > ")
  print()

  if (p1 == 'R' and p2 == 'S') or (p1 == 'S' and p2 == 'P') or (p1 == 'P' and p2 == 'R'):
    p1_score += 1

  elif (p1 == 'P' and p2 == 'S') or (p1 == 'S' and p2 == 'R') or (p1 == 'R' and p2 =='P'):
    p2_score += 1

  print("\nWhooo!!! Player 1 has ", p1_score," wins")
  print("\nWhooo!!! Player 2 has ", p2_score," wins")
  if p1_score == 3 or p2_score == 3:
    print("Thanks for playing")
    exit()

  else:
    continue  


    
  

  

  

  