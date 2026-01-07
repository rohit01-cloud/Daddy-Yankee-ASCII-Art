#Daddy Yankee ASCII-style image

rows = 20
cols = 40

for i in range(rows):
    for j in range(cols):

        # Face outline (oval)
        if ((i == 2 or i == 17) and 10 < j < 30) or \
           ((j == 10 or j == 29) and 2 < i < 17):
            print("*", end="")

        # Eyes
        elif i == 7 and (j == 16 or j == 23):
            print("o", end="")

        # Nose
        elif 9 <= i <= 11 and j == 20:
            print("|", end="")

        # Mouth
        elif i == 13 and 17 < j < 24:
            print("_", end="")

        # Beard
        elif 14 <= i <= 16 and 15 < j < 25:
            print("#", end="")

        else:
            print(" ", end="")
    print()

print("\nDADDY YANKEE")
