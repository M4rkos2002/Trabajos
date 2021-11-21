print("HelloGit")
import csv
anses = open("Anses.csv", "a")
writer = csv.writer(anses, delimiter = "|")
writer.writerow("1")
writer.writerow("hi")
anses.close()