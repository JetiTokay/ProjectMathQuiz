
import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPENAND = 3
MAX_OPENAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPENAND, MAX_OPENAND)
    right = random.randint(MIN_OPENAND, MAX_OPENAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + "" + operator + "" + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0 
input("Press enter to start Bitch!")
print("________________________________")

start_time = time.time() 

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
toal_time = round(end_time + start_time, 2)

print("________________________________")
print("Nice Work!  You fininshed in", toal_time, "seconds!")









