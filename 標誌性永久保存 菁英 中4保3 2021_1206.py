import random
#import numpy as np
import copy
#import tensorflow
#import threading
import multiprocessing as mp
#import concurrent.futures
import time
import os

#from itertools import permutations
from itertools import combinations

#Original = [9]  OK
#xyz
#            for descend_cycle in range(2200, 200, -1): 
#                target_remove_count = descend_cycle//100
#return_list =  [[1, 2, 3, 5, 7, 8], [1, 2, 4, 5, 7, 9], [2, 3, 4, 6, 8, 9]]
#check_delete_all = True
#start_time  :  Sat May 29 03:14:19 2021
#finish_time :  Sat May 29 03:14:31 2021
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#AI: {[1,2,3], [4,5,6]}, {[4,5,6], [7,8,9]}, {[1,2,3],[7,8,9]}
#return_list = [[1,2,3, 4,5,6], [4,5,6, 7,8,9], [1,2,3,7,8,9]]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#=================================================================

#Original = [10] OK
#xyz
#            for descend_cycle in range(2200, 200, -1): 
#                target_remove_count = descend_cycle//100
#cycle_times =  1
#return_list =  [[1, 3, 5, 6, 7, 8], [1, 2, 3, 4, 9, 10], [2, 4, 5, 6, 7, 8], [5, 6, 7, 8, 9, 10]]
return_list =  [[1,2,5,6,9,10], [1,2,3,4,7,8], [3,4,5,6,7,8],[3,4,9,10,7,8]]
#check_delete_all = True
#start_time  :  Sat May 29 03:16:03 2021
#finish_time :  Sat May 29 03:16:15 2021
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#AI: [[],[],[],[]]
#return_list = [[1,2,3,4,5,6], [1,2,5,6,9,10], [3,4,5,6,9,10], [1,2,3,4,9,10]]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#=================================================================

#Original = [11] OK
#xyz
#            for descend_cycle in range(2200, 200, -1): 
#                target_remove_count = descend_cycle//100
# #cycle_times =  10
#return_list =  [[1, 2, 5, 8, 9, 10], [2, 4, 5, 6, 7, 11], [1, 3, 6, 8, 9, 11], [1, 4, 7, 8, 9, 10], [2, 3, 4, 5, 7, 10]]
#check_delete_all = True
#start_time  :  Sat May 29 03:18:16 2021
#finish_time :  Sat May 29 03:18:33 2021




#Original = [12] OK
#三合一 
# range(2200, 200, -1): 
# target_remove_count = descend_cycle//100
#cycle_times =  1570
#return_list =  [[1, 2, 3, 4, 5, 6], [1, 4, 7, 10, 11, 12], [5, 6, 7, 10, 11, 12], [1, 4, 5, 6, 8, 9], [2, 3, 7, 8, 9, 10]              
#               , [2, 3, 8, 9, 11, 12]]
#check_delete_all = True
#start_time  :  Sat May 29 03:32:13 2021
#finish_time :  Sat May 29 03:42:05 2021
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#AI: [[1,2,3,4,5,6],[7,8,9,10,11,12],[1,2,3,7,8,9],[4,5,6,10,11,12],[1,2,3,10,11,12],[4,5,6,7,8,9]]
#return_list = [[1,2,3,4,5,6],[7,8,9,10,11,12],[1,2,3,7,8,9],[4,5,6,10,11,12],[1,2,3,10,11,12],[4,5,6,7,8,9]]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#=================================================================

#Original = [13] OK
#三合一 
#            for descend_cycle in range(220, 20, -1): 
#                target_remove_count = descend_cycle//10
#                    select_counter = random.randint(-4,2)
#cycle_times =  29080
#return_list =  [[4, 7, 10, 11, 12, 13], [1, 4, 5, 6, 8, 10], [2, 3, 4, 7, 8, 12], [1, 2, 3, 5, 11, 13], [5, 8, 9, 10, 11, 13]
#               , [1, 6, 7, 8, 9, 12], [1, 2, 4, 5, 9, 10], [2, 3, 6, 9, 11, 13], [3, 5, 6, 7, 10, 12]]
#check_delete_all = True
#start_time  :  Sun May 30 00:17:57 2021
#finish_time :  Sun May 30 05:35:33 2021



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#=================================================================


#Original = [14]

#[14]  + 2
#for descend_cycle in range(up_remove_count, 2, -6):
#target_remove_count = descend_cycle
#target_remove_count = 3
#cycle_times =  61921
#return_list =  [[3, 4, 5, 6, 7, 14], [6, 7, 8, 10, 11, 12], [1, 2, 6, 8, 13, 14], [2, 3, 4, 7, 10, 13], [1, 3, 5, 6, 9, 13], 
#                [1, 7, 8, 9, 12, 13], [2, 3, 5, 8, 9, 11], [1, 2, 4, 5, 10, 12], [1, 3, 7, 10, 11, 14], [4, 8, 11, 12, 13, 14], 
#                [5, 7, 9, 10, 13, 14], [2, 3, 6, 9, 12, 14], [1, 4, 6, 8, 9, 11]]
#check_delete_all = True
#start_time  :  Wed Oct 13 22:15:36 2021
#finish_time :  Thu Oct 14 12:47:11 2021
#100 cycle_times: need 1:50
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#[14]  + 3
#for descend_cycle in range(up_remove_count, 2, -6):
#target_remove_count = descend_cycle
#target_remove_count = 3
#cycle_times =  500
#return_list =  [[1, 6, 7, 8, 9, 13], [2, 4, 7, 9, 12, 14], [1, 5, 9, 10, 11, 12], [2, 3, 4, 6, 8, 9], [3, 4, 6, 11, 12, 13], 
#                [1, 2, 3, 6, 10, 14], [2, 5, 6, 7, 11, 13], [3, 4, 7, 8, 10, 11], [3, 5, 6, 7, 8, 12], [1, 2, 4, 5, 8, 12], 
#                [3, 4, 5, 6, 13, 14], [8, 9, 10, 11, 13, 14], [1, 2, 4, 10, 12, 13], [1, 4, 7, 10, 11, 14]]
#check_delete_all = True
#start_time  :  Wed Oct 13 03:24:53 2021
#finish_time :  Wed Oct 13 03:34:40 2021
#100 cycle_times: need 1:50
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#=================================================================



#Original = [15] 
#[15]  + 3
#for descend_cycle in range(up_remove_count, 2, -6):
#target_remove_count = descend_cycle
#target_remove_count = 3
#cycle_times =  46200
#return_list =  [[4, 7, 10, 12, 13, 14], [2, 5, 9, 12, 13, 14], [5, 6, 8, 10, 11, 13], [1, 3, 4, 5, 10, 12], [3, 6, 7, 9, 13, 15], 
#                [2, 4, 5, 12, 14, 15], [1, 3, 6, 7, 11, 12], [1, 3, 4, 8, 13, 15], [2, 3, 5, 8, 10, 11], [2, 4, 5, 7, 9, 11], 
#                [1, 5, 6, 7, 8, 14], [1, 2, 6, 9, 10, 15], [2, 3, 6, 9, 11, 14], [4, 8, 9, 11, 12, 15], [1, 4, 11, 13, 14, 15], 
#                [3, 7, 8, 10, 14, 15], [2, 4, 7, 8, 12, 13]]
#check_delete_all = True
#start_time  :  Wed Oct 13 17:13:42 2021
#finish_time :  Thu Oct 14 07:37:45 2021
#100 cycle_times: need 1:49
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[15]  + 2
#for w in range( length4*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = -1
# remove Combination_List_6element if dick[i] == 0
#xyz
#escape from dead loop = 1500
#cycle_times =  4300

#return_list =  [[2, 4, 6, 7, 8, 15], [1, 5, 9, 11, 14, 15], [1, 3, 4, 7, 9, 12], [1, 5, 7, 8, 10, 13], [6, 7, 10, 11, 12, 14]
#               , [1, 2, 3, 6, 10, 15], [2, 4, 8, 10, 11, 12], [1, 2, 5, 12, 13, 14], [3, 4, 8, 13, 14, 15], [2, 7, 9, 10, 11, 13]
#               , [2, 3, 5, 7, 8, 9], [3, 4, 5, 6, 11, 13], [3, 5, 10, 11, 12, 15], [6, 8, 9, 12, 13, 15], [4, 5, 6, 9, 10, 14]
#               , [1, 3, 6, 8, 11, 14]]
#check_delete_all = True
#start_time  :  2021-12-04 09:10:11.934933
#finish_time :  2021-12-04 10:37:05.999073
#delta time  :  1:26:54.064140  (運氣好，非一般情況)
#=================================================================



#Original = [16] 
#[16]  + 6
#for descend_cycle in range(up_remove_count, 2, -6):
#target_remove_count = descend_cycle
#target_remove_count = 3
#cycle_times =  1637
#return_list =  [[5, 7, 8, 10, 12, 15], [1, 3, 9, 11, 12, 15], [1, 2, 4, 8, 13, 14], [5, 9, 10, 13, 14, 15], [4, 6, 7, 8, 9, 10], 
#               [1, 3, 6, 8, 11, 12], [4, 5, 6, 8, 15, 16], [6, 7, 9, 12, 14, 16], [2, 3, 7, 11, 13, 16], [1, 2, 5, 6, 9, 16], 
#               [5, 6, 10, 11, 13, 15], [3, 4, 10, 11, 14, 16], [2, 4, 9, 12, 13, 15], [2, 3, 6, 9, 10, 15], [1, 2, 5, 7, 10, 14], 
#               [3, 4, 5, 7, 11, 12], [3, 5, 8, 9, 14, 16], [1, 2, 10, 12, 13, 16], [2, 5, 6, 8, 11, 16], [1, 7, 13, 14, 15, 16], 
#               [2, 3, 8, 11, 13, 14], [1, 3, 4, 5, 6, 10]]
#check_delete_all = True
#start_time  :  Fri Oct 15 19:11:37 2021
#finish_time :  Fri Oct 15 20:02:51 2021


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[16]  + 5
#for w in range( length4*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = -1
# remove Combination_List_6element if dick[i] == 0
#xyz
#escape from dead loop = 1500
#cycle_times =  9
#return_list =  [[1, 2, 7, 12, 15, 16], [1, 9, 10, 11, 13, 16], [1, 3, 4, 5, 8, 10], [4, 6, 7, 9, 14, 15], [2, 3, 8, 11, 14, 16]
#               , [2, 6, 8, 12, 13, 14], [3, 5, 7, 9, 13, 14], [5, 6, 8, 11, 15, 16], [4, 5, 7, 10, 11, 12], [2, 4, 5, 10, 13, 15]
#               , [1, 3, 11, 12, 13, 15], [2, 3, 4, 6, 9, 12], [1, 5, 6, 9, 10, 14], [1, 4, 7, 8, 13, 16], [6, 8, 9, 10, 12, 15]
#               ,[2, 3, 6, 7, 10, 16], [1, 4, 6, 7, 11, 14], [2, 5, 9, 12, 14, 16], [3, 4, 13, 14, 15, 16], [2, 5, 7, 8, 9, 11]
#               , [3, 7, 8, 10, 14, 15]]
#check_delete_all = True
#start_time  :  2021-11-30 17:33:38.042695
#finish_time :  2021-11-30 17:36:28.778108
#delta time  :  0:02:50.735413

#=================================================================




#Original = [17] 
#[17]  + 8
#for descend_cycle in range(up_remove_count, 2, -6):
#target_remove_count = descend_cycle
#target_remove_count = 3
#cycle_times =  3826
#return_list =  [[5, 10, 13, 14, 15, 16], [3, 4, 5, 7, 16, 17], [1, 3, 6, 11, 13, 15], [2, 4, 7, 9, 14, 15], [2, 8, 9, 10, 12, 17], 
#               [4, 12, 13, 15, 16, 17], [3, 6, 7, 10, 12, 16], [2, 3, 8, 15, 16, 17], [1, 2, 3, 7, 13, 15], [5, 8, 11, 12, 13, 15], 
#               [4, 7, 10, 11, 16, 17], [1, 2, 6, 12, 14, 16], [3, 5, 9, 13, 14, 16], [2, 4, 5, 6, 8, 9], [1, 3, 4, 10, 14, 17], 
#               [1, 8, 9, 10, 11, 16], [5, 6, 7, 11, 14, 17], [3, 4, 6, 8, 10, 13], [2, 3, 5, 9, 10, 11], [1, 4, 7, 9, 12, 13], 
#               [1, 7, 8, 13, 14, 17], [3, 6, 9, 11, 15, 17], [3, 4, 8, 11, 12, 14], [1, 2, 4, 11, 13, 17], [1, 3, 5, 8, 9, 15], 
#               [1, 2, 5, 6, 7, 12], [2, 6, 7, 8, 10, 15], [1, 5, 6, 10, 12, 14]]
#check_delete_all = True
#start_time  :  Wed Oct 17 15:46:42 2021
#finish_time :  Sun Oct 17 20:40:04 2021

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#=================================================================



bet_number7 = 10
cpus = os.cpu_count()
cpus = 1



dict = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0}
trial_dict            = {9:3,   10:4,   11:5,   12:6,   13:9,   14:11,  15:14,  16:16,  17:20,  18:25,  19:31,  20:38, 21:45}
max_remove_count_dict = {9:75,  10:95,  11:115, 12:135, 13:155, 14:175, 15:195, 16:215, 17:235, 18:255, 19:275, 20:295, 21:300}
min_remove_count_dict = {9:18,  10:4,   11:7,   12:13,  13:4,   14:4,   15:4,   16:4,   17:4,   18:4, 19:4,  20:4, 21:0}
combination_size_dict = {9:126, 10:210, 11:330, 12:495, 13:715, 14:1001, 15:1365, 16:1820, 17:2380, 18:3060, 19:3876, 20:4845, 21:0}
min_ending_section = 18
exclusive = []
inclusive = []

def check_delete_all( target_list ):
    Original = []
    remove_count = 0
    for i in range(bet_number7):
        Original.append(i+1)
    Combination_List_4element = list(combinations(Original ,4))
    for x in target_list:
        three = list(combinations(x ,3))
        for c in three:
            dup_Combination_List_4element = copy.deepcopy(Combination_List_4element)
            for d4 in dup_Combination_List_4element:
                if set(c) <= set(d4):
                    Combination_List_4element.remove(d4)
                    remove_count = remove_count + 1
    print("remove_count", remove_count)
    print("Combination_List_4element", Combination_List_4element)
    if (len(Combination_List_4element) == 0):
        return True
    else:
        return False

def section_matching_function( index_start ):
    #stop_others = False
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    Original = []
    for i in range(bet_number7):
        Original.append(i+1)
    #print("Original : ", Original)
    try_set_number = trial_dict[bet_number7]
    #print("try_set_number : ", try_set_number)
    
    Combination_List_3element = list(combinations(Original ,3))
    Combination_List_6element = list(combinations(Original ,6))
    #reverse_Combination_List_6element = copy.deepcopy(Combination_List_6element)
    #reverse_Combination_List_6element.reverse()

    length = 0
    close = False
    #terminator = False
    cycle_times = 0    
    set6 = []
   
    print("Thread", index_start)
  
    length3 = len(Combination_List_3element)
    length6 = len(Combination_List_6element)
    #try_set_number = try_set_number + 5
    #print(Combination_List_6element[0], reverse_Combination_List_6element[0], Combination_List_6element[length*3//4] )
    #print("len(Combination_List_6element)",len(Combination_List_6element) )
    #while ((terminator == False) & (close == False)):

    remove_count = 0

 
    set6.append(Combination_List_6element[0])
    three = list(combinations(set6[0] ,3))
    for c in three:
        if c in Combination_List_3element:
            Combination_List_3element.remove(c)
            remove_count = remove_count + 1



    while (close == False):
        #當最後剩下的list，集合元素大於六，但無法倆倆構成六元素的list，就會再重跑一次while迴圈
        Combination_List_3element = list(combinations(Original ,3))
        set6 = []
        remove_count = 0
        cycle_times += 1
        
        set6.append(Combination_List_6element[0])
        three = list(combinations(set6[0] ,3))
        for c in three:
            if c in Combination_List_3element:
                Combination_List_3element.remove(c)
                remove_count = remove_count + 1

        #set6.append(Combination_List_6element[length6-1])   
        #three = list(combinations(set6[1] ,3))
        #for c in three:
        #    if c in Combination_List_3element:
        #        Combination_List_3element.remove(c)
        #        remove_count = remove_count + 1


        inner_exit = False
        for target_remove_count in range(20, 1, -1 ):         

        #for target_remove_count in range(20, 1, -1 ): 
            #print("*", target_remove_count)
            #if (target_remove_count > len(Combination_List_3element)):
            print("***", target_remove_count , len(Combination_List_3element))
            #    break

            if (close == True):
                break
            if (inner_exit == True):
                break
            ending_section = False
            #set_Combination_List_3element = set()
            for     w in range(    len(Combination_List_3element)**2 ):
                if (len(Combination_List_3element) < 10 ):
                    set_Combination_List_3element = set()
                    for p in Combination_List_3element:
                        set_Combination_List_3element = set_Combination_List_3element.union(p)
                    if (len(set_Combination_List_3element) <= 6):
                        ending_section = True
                        #print("++++set", set_Combination_List_3element)    
                    #else:
                        #print("++++set", set_Combination_List_3element)            
                    #    print("------Combination_List_3element = ",Combination_List_3element)  
                if (ending_section == False):
                    x = Combination_List_3element[random.randint(0,len(Combination_List_3element)-1)]
                    y = Combination_List_3element[random.randint(0,len(Combination_List_3element)-1)]
                    z = Combination_List_3element[random.randint(0,len(Combination_List_3element)-1)]
                    remove_count = 0
                    remove_list = []
                    uni = list(set(x).union(set(y)).union(set(z)))
                    #uni = list(   set(x).union(set(y) )  )
                    uni.sort()
                    if (len(uni)==6):
                        #Lst_uni = uni 
                        three = list(combinations(uni ,3))
                        for c in three:
                            if c in Combination_List_3element:
                                Combination_List_3element.remove(c)
                                remove_list.append(c) 
                                remove_count = remove_count + 1
                                #print("c = ", c)
                        if remove_count < target_remove_count:    
                            for k in remove_list:
                                Combination_List_3element.append(k)
                        else:
                            set6.append(uni)    
                            print("*", target_remove_count)
                            #print("*Combination_List_3element = ",len(Combination_List_3element), Combination_List_3element)
                            #print("*set6 = ",len(set6), set6)
                else:
                    Combination_List_3element = []
                    uni =  list(set_Combination_List_3element)            
                    uni.sort()
                    set6.append(uni)   

                if (len(Combination_List_3element)==0):  
                    print("AAA  target_remove_count = ", target_remove_count)       
                    print("------Combination_List_3element = ",len(Combination_List_3element))
                    print("------set6 = ",len(set6), set6)
                    print("------cycle_times = ",  cycle_times )
                    print("")  
                    close = True
                    break      

                if (try_set_number  == len(set6)):
                    print(">>>>>>>set6 = ",len(set6))
                    print(">>>>>>>Combination_List_3element = ",len(Combination_List_3element) )
                    inner_exit = True
                    break            
            #print("BBB  target_remove_count = ", target_remove_count)       
            #print("Combination_List_3element = ",len(Combination_List_3element))
            #print("set6 = ", set6)    
            #print("")     

            if ((cycle_times%30000) == 0): 
                print()
                print("**************************************************************")
                print("Thread: ", index_start)
                print("time : ", time.ctime())   
                print("Combination_List_3element = ",len(Combination_List_3element), Combination_List_3element)
                print("set6 = ",len(set6), set6)
                print("cycle_times = ",  cycle_times )

    print("===================================================================")
    print("===============Combination_List_3element = ",len(Combination_List_3element), Combination_List_3element)
    print("===============set6 = ",len(set6), set6)

    return set6

# end of section_matching_function
#P===========================================================

def mapper(length, choosen_list, buy_list):

    mapped_number = []  

    for t in buy_list:
        #print(t)
        temp = []
        for u in t:
            temp.append(choosen_list[u-1])
        #print(temp)
        mapped_number.append(temp)
        #print("NNN")
    #print("mapped_number", mapped_number)    
    return mapped_number

# end of mapper
#P===========================================================
#dict = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,12:0, 13:0, 14:0, 15:0, 16:0, 17:0}
#appeartimes = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])

def generate_original_number(bet_number7, exclusive):


    try_set_number = 0

    Original = []
    for i in range(bet_number7):
        Original.append(i+1)
    print("Original : ", Original)
    try_set_number = trial_dict[bet_number7]
    print("try_set_number : ", try_set_number)



    exclusive = exclusive + inclusive

    Appear3 = []
    digit_used = [0,0,0,0,0]

    for i in inclusive:
        if  i >= 40:
            digit_used[4] = digit_used[4] + 1
        if  (i < 40) & (i >= 30):
            digit_used[3] = digit_used[3] + 1
        if  (i < 30) & (i >= 20):
            digit_used[2] = digit_used[2] + 1
        if  (i < 20) & (i >= 10):
            digit_used[1] = digit_used[1] + 1
        if  (i < 10):
            digit_used[0] = digit_used[0] + 1
            
    print("digit_used" , digit_used )

    generate_number7 = bet_number7 - len(inclusive)
    digit_limit = [10,10,10,10,10] #0,1,2,3,4
    digit_available = digit_limit
    print("digit_limit" , digit_limit )

    for i in range(5):
        digit_available[i] = digit_limit[i] - digit_used[i]
    print("digit_available" , digit_available )

    print("generate_number7" , generate_number7 )
    Appear3 = inclusive

    while len(Appear3) < bet_number7:  
        i = random.randint(1,49)
        if ( i not in Appear3 ) & ( i not in exclusive ) :
            if  i >= 40:
                if digit_available[4] > 0:
                    digit_available[4] = digit_available[4] -1
                    Appear3.append(i) 
                    #print("Appear3", Appear3)
            if  (i < 40) & (i >= 30):
                if digit_available[3] > 0:
                    digit_available[3] = digit_available[3] -1                 
                    Appear3.append(i)   
                    #print("Appear3", Appear3)  
            if  (i < 30) & (i >= 20):
                if digit_available[2] > 0:
                    digit_available[2] = digit_available[2] -1                 
                    Appear3.append(i)     
                    #print("Appear3", Appear3)
            if  (i < 20) & (i >= 10):
                if digit_available[1] > 0:
                    digit_available[1] = digit_available[1] -1                 
                    Appear3.append(i)       
                    #print("Appear3", Appear3)
            if  (i < 10):
                if digit_available[0] > 0:
                    digit_available[0] = digit_available[0] -1                 
                    Appear3.append(i)     
                    #print("Appear3", Appear3)
                
    Appear3.sort()
    #Appear3 = [1,2,3,4,5,6,7,8]
    print( Appear3)
    print("=====generate_original_number===============================================")            
    print("")       

    return Appear3

# end of generate_original_number
#P===========================================================
if __name__=='__main__':
    
    original_number =  []
    original_number = generate_original_number(bet_number7, exclusive)  


    #cpus = os.cpu_count()
    #cpus = 1
    print("cpus :", cpus)
    #pool = Process.Pool(4)
    print('main parent process:', os.getppid())
    print('main process id:', os.getpid())
    #return_list = []
    mapped_list = []


    pool = mp.Pool(cpus)



    if (check_delete_all(return_list) == True):
        print("check_delete_all = True")
    else:
        print("check_delete_all = False")

    #print(">>>>>>> success return_list", return_list )            
    for i in range (cpus):
        mapped_list = mapper(len(return_list), original_number, return_list)
        print(">>>>>>> success mapped_list", mapped_list )

    #print(len(mapped_list))
    L = len(mapped_list)
    Y = L*50
    print("Answer number = ", original_number)
    print()
    print("大樂透中4保3 :", bet_number7, "個號碼，" , Y, "元", "4期共", Y*4, "元" )
    print("===========================================")
