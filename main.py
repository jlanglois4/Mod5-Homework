word = input(f"Enter word: ")
array = []
for num in range(len(word)):
    if num % 2 == 0:
        array.append(word[num])
print("".join(array))

color_input = input("What is the noun for red, blue, and green?")
tire_input = input("What part of the car needs to touch the ground for the car to move?")

british_count = 0
american_count = 0

if color_input.count("color") > 0:
    american_count += 1
elif color_input.count("colour") > 0:
    british_count += 1

if tire_input.count("tire") > 0:
    american_count += 1
elif tire_input.count("tyre") > 0:
    british_count += 1

if american_count == 2:
    print("You are American.")
elif british_count == 2:
    print("You are British.")
else:
    print("You are not very good at answering quizzes...")
