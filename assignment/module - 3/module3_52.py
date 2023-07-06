#pick a random item from a list or tuple
import random
t = (30, 10, "TutorialsPoint", 20, "python", "code")
print("The given input tuple: ", t)
select = random.choice(t)
print("The generated random tuple item = ", select)