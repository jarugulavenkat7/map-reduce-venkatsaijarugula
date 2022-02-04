# Venkat Sai Jarugula - Reducer using standard input and output

import sys

thisKey = ""
thisValue = 0.0

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    City, Gross_Income = datalist

    if City != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = City 
      thisValue = 0.0
  
    # apply the aggregation function
    thisValue += float(Gross_Income)

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)