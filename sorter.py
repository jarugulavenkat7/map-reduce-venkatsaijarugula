# Venkat Sai Jarugula
# Practice Sorter
originalContent = open("a.txt","r")  # open file, read-only
sorted = open("sortedList.txt", "w") # open file, write
lines = originalContent.readlines()
lines.sort()

for line in lines:
 sorted.write(line)

originalContent.close()
sorted.close()