BOUNCINESS_INDEX = 0.6

height = float(input("Enter the initial height of the ball: "))
bounces = int(input("Enter the number of bounces: "))

distance = height  # initial drop

for _ in range(bounces):
    bounce_height = height * BOUNCINESS_INDEX
    distance += bounce_height + bounce_height
    height = bounce_height

print(f"Total distance traveled: {distance:.2f}")
