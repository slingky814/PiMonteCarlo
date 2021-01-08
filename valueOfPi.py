import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#radius of the circle inside the square
radius = 50
trials = [i for i in range(1,1000)]
df = pd.DataFrame(columns=["Darts", "Value"], index = trials)

for i in range(0,len(trials)):
    darts_thrown, darts_in_circle = 0,0
    for j in range(1,len(trials)):
        x = random.randint(0,50)
        y = random.randint(0,50)
        if (y**2+x**2)**.5 <= radius:
            darts_in_circle += 1
        darts_thrown += 1
    df.loc[i] = [i,(darts_in_circle/darts_thrown)*4]

#plot the results
plt.scatter(df.Darts, df.Value, s = 5, c = "blue")
plt.axhline(y=3.14, c = "red")
plt.xlabel("Darts")
plt.ylabel("Value of Pi")
plt.show()
