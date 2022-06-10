def sonic(x):
  print(" good call, I will double your money")
  return x+x

def mario(x):
  print(" good call, I will triple your money")
  return x*3

def daxter(x):
  print(" like professor Nimri, he thought he was funny, but isn't -$5")
  return x-5

def DonkeyKong(x):
  print(" good call, but mario is better, I'll call mario for you")
  return mario(x)

print("===== welcome to the vegas video game character game function ====")
print("==== type in a function name after a famous game character, and see how much money you win")

dollars = sonic(10)
print("you win " + str(dollars) + " dollars!")
