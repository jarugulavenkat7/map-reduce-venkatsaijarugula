sortedContent = open("sortedList.txt","r")
reducedContent = open("reducedList.txt", "w")

thisKey = ""
thisValue = 0.0

for line in sortedContent:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      reducedContent.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
reducedContent.write(thisKey + '\t' + str(thisValue)+'\n')

sortedContent.close()
reducedContent.close()