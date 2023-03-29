import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("1.Rock")
print("2.Paper ")
print("3.Scissors")
num=int(input("Enter a choice\n"))

if(num==1):
  print(rock)
elif(num==2):
  print(paper)
elif(num==3):
  print(scissors)
  
num_comp=random.randint(1,3)
if((num_comp==1) and (num==1)):
  print(rock)
  print("Draw")
elif((num_comp==2) and (num==2)):
  print(paper)
  print("Draw")
elif((num_comp==3) and (num==3)):
  print(scissors)
  print("Draw")
elif((num_comp==1) and (num==2)):
  print(rock)
  print("You Win")
elif((num_comp==1) and (num==3)):
  print(rock)
  print("You lose")
elif((num_comp==2) and (num==1)):
  print(paper)
  print("You lose")
elif((num_comp==2) and (num==3)):
  print(paper)
  print("You Win")
elif((num_comp==3) and (num==1)):
  print(scissors)
  print("You win")
elif((num_comp==3) and (num==2)):
  print(scissors)
  print("You lose")



  
