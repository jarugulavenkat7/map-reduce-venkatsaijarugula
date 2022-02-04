# Venkat Sai Jarugula - Mapper using standard input and output

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 7) : 
    Branch,City,Customer,Gender,Product_Line,Payment,Gross_Income = datalist

    # print intermediate key-value pairs to standard output
    print(City,"\t",Gross_Income)