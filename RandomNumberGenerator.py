import numpy as np

PowerBall = []
PowerBallNumber = 0

while len(PowerBall) < 5:
    PowerBall.append(np.random.randint(1,70))
    PowerBallNumber = np.random.randint(1,27)
    PowerBall = set(PowerBall)
    PowerBall = sorted(PowerBall)

print(f"The the winning Power Ball numbers for today are {PowerBall} {PowerBallNumber} just kidding this is not true at all hahaha")