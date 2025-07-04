import random

scores = [100, 200, 300,400,500,600,700,800,900,1000,1001,1002,1010,1100]
rand_list = random.sample(scores, k=len(scores))


highest = 0


for i in range(len(rand_list)):
    if rand_list[i] > highest:
        highest = rand_list[i]

print(highest)
