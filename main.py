#MapPlot.py
#Name: Mia Garcia
#Date: 4/23/26
#Assignment: Lab 10

import matplotlib.pyplot as plt

trials = []
reaction_times = []

with open('reaction_time_data.csv', 'r') as file:
    next(file)  

    for line in file:
        parts = line.strip().split(',')

        trial = int(parts[0])
        reaction_time = float(parts[1])

        if reaction_time > 0 and reaction_time < 1000:  
            trials.append(trial)
            reaction_times.append(reaction_time)

plt.plot(trials, reaction_times, marker='o')

plt.xlabel("Trial Number")
plt.ylabel("Reaction Time (ms)")
plt.title("Reaction Time Across Trials")

plt.savefig("reaction_time_graph.png")
plt.show()