from pandas import DataFrame
import pandas as pd

#create, read and update a csv
rulers = ['Lannisters', 'Targaryen', 'Stark', 'Bolton']
soldiers = [15000, 20803, 11245, 0]
armySet = list(zip(rulers, soldiers))
df = DataFrame(data=armySet, columns=['House', 'Soldiers'])
print(armySet)
print(df)
#TO CSV
df.to_csv('file_name.csv')

#read = pd.read_csv(r'File_name.csv')
#print (read)

#read1 = pd.DataFrame(read, columns= ['House'])
#print (read1)

# updating the column value/data
df.loc[3, 'House'] = 'KAME HOUSE'

df.to_csv('file_name.csv')

read3 = pd.read_csv(r'File_name.csv')
print(read3)




#zip method merge first element of a list with 1st elem of another list and so on...
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
type(zipped)

print(list(zipped))

