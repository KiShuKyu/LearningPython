# Assign Grade

marks = 81

if marks >= 101:
    print("Please enter your marks again")
    exit()

if 90 <= marks <= 100:
    print(f"According to your marks {marks}, Grade = A ")
elif 80 <= marks <= 89:
    print(f"According to your marks {marks}, Grade = B ")
elif 70 <= marks <= 79:
    print(f"According to your marks {marks}, Grade = C ")
elif 60 <= marks <= 69:
    print(f"According to your marks {marks}, Grade = D ")
else:
    print(f"According to your marks {marks}, Grade = F ")
