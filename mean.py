import sys

sum=0
n=0

#another comment
#I was able to access your file-Todd

#sum total values
for num in open('data.txt'):
  sum += float(num)
  n += 1

print sum/n

