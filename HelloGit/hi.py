print("HelloGit")
import csv
anses = open("Anses.csv", "a")
writer = csv.writer(anses, delimiter = "|")
writer.writerow("1")
writer.writerow("hi")
anses.close()

from matplotlib import pyplot as plt
plt.arrow(1.5,1.5,1,2)
plt.show()