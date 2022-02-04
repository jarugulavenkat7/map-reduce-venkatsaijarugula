# map-reduce-venkatsaijarugula
Learning map reduce

## Description of data :
- This Data Set consists details of all the ***Supermarket sales***. This data consists of Historical record of sales data in 3 different supermarkets. The different attributes of data are Branch,City,Customer,Gender,Product_Line,Payment and Gross_Income
- I took the Dataset from ***[https://www.kaggle.com/aungpyaeap/supermarket-sales?select=supermarket_sales+-+Sheet1.csv](https://www.kaggle.com/aungpyaeap/supermarket-sales?select=supermarket_sales+-+Sheet1.csv)*** 

## Study:
- Using the super market dataset, I want to find the total gross amount from the  historical sales of supermarket company which has recorded in 3 different branches for 3 months data. 

## Execution process:
- At first, the 21mapper.py file maps and extracts the data from the supermarket_sales.csv  file.Later the output is sorted and sent to the 21reducer.py file, which reduces the data and adds data into the JarugulaVenkatSaiOutput.txt

## Powershell Command Used:
- ***cat supermarket_sales.csv | python 21mapper.py | sort | python 21reducer.py > VenkatSaiJarugulaOutput.txt***

## Summary:
- By examining the final output, it can be observed that the city Naypyitaw has the maximum total gross income when compared to the other two states Mandalay and Yangon. 


![chart](chart.JPG)
