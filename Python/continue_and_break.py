# This program prints every character
# of the string

for char in "computer" :
       print(char)
print("Finished the for loop\n")

# This program shows the use of continue
# statement in a for loop

for char in "computer" :
       if char == "p" :
              continue
       print(char)
print("Finished the for loop with a continue\n")

# This program shows the use of break
# statement in a for loop

for char in "computer" :
       if char == "p" :
              break
       print(char)
print("Finished the for loop with a break\n")
