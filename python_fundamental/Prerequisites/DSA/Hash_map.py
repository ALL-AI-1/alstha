
# (1) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

#   (a) What was the average temperature in first week of Jan

#   (b) What was the maximum temperature in first 10 days of Jan

#   Figure out data structure that is best for this problem
import csv
import enum
import imp
from traceback import print_tb
with open(r"F:\REAL_PROJECTS\All_AI\nyc_weather.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    result_list = [row["temperature(F)"] for row in reader]
    # Calculate and print the sum of the first 6 temperatures using lambda and map
    print(sum(map(int, result_list[0:6])))
    
        
    # Example: Use map() to convert all temperature strings to integers
    temperatures = list(map(int, result_list))
    print("All temperatures as integers:", temperatures)
    



# (2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

#   (a) What was the temperature on Jan 9?

#   (b) What was the temperature on Jan 4?

#   Figure out data structure that is best for this problem

import csv
dictt={}
with open (r"F:\REAL_PROJECTS\All_AI\nyc_weather.csv",newline='')as csvfile:
    for line in csvfile:
        data=line.split(",")
        key=data[0]
        if key=="date":
            continue
        dictt[key]=int(data[1])
    
print(dictt["Jan 6"])


#Hash function

class Hash:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
    
    def get_hash(self,data):
        hash=0
        for i in data:
            hash+=ord(i)
        hash=hash%100
        return hash

    def __getitem__(self,data):
        h=self.get_hash(data)
        return self.arr[h]

    def __setitem__(self,data,value):
        h=self.get_hash(data)
        self.arr[h]=value

    def delete(self,index):
        self.arr[index]=None

if __name__=="__main__":
    hash=Hash()
    hash['9']="march 6"
    print(hash.arr)

#collision so Chaining

class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]


    
