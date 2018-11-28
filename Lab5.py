# -*- coding: utf-8 -*-
"""
Created and modified by: Matthew Iglesias
80591632
Diego Aguirre 
T.A. Anitha Nath
"""
class Heap:
    def __init__(self):
        self.heap_array = []
            
    def insert(self,k):
        self.heap_array.append(k)
        i = (len(self.heap_array) - 1) ##Percolate up from last index
        while (i - 1) // 2 >= 0:
            if self.heap_array[i] < self.heap_array[(i - 1) // 2]:
                temp = self.heap_array[(i-1) //2]
                self.heap_array[(i-1) //2] = self.heap_array[i]##swap
                self.heap_array[i] = temp
            i = i // 2
        return self.heap_array
            
    def extract_min(self):
        if self.isEmpty():
            return -1
        
        self.heap_array[0] = self.heap_array[len(self.heap_array) - 1]##sets last element from heap to root
        self.heap_array = self.heap_array[:-1] ##Reduces the size of list
        
        i = 0
        while(i * 2) < len(self.heap_array) - 1:
            if self.heap_array[i * 2] > self.heap_array[i * 2 + 1]:
                ex_min = (i *2 + 1)
            else:
                ex_min = (i * 2)
            if self.heap_array[i] > self.heap_array[ex_min]:
                val = self.heap_array[i]
                self.heap_array[i] = self.heap_array[ex_min]
                self.heap_array[ex_min] = val
            i = ex_min
        return self.heap_array
        
    def isEmpty(self):
        return len(self.heap_array)== 0
                
    
def main():
    h = Heap() 
    user_input = int(input("How many numbers do you want to input: "))
    for num_list in range(0,user_input): ##Creates the list size user_input
        user_number = int(input("Input a number: "))
        heap_list = [user_number]
        for item in heap_list:
            print("heap_list ----> ",h.insert(item)) ##appends into Heap
    for ex_min in range(0,user_input):
        user_em = str(input("Do you want to extract the min? "))
        if user_em == "yes":
            print(h.extract_min()) ##Extracts min element from Heap
        else:
            print("Done.")
            return
    return 
        
main()