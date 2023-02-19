import random
#from numba import jit
import numpy as np
import copy
#import tensorflow
import threading
import multiprocessing as mp
import concurrent.futures
#import time
import datetime
import os
import collections
from itertools import permutations
from itertools import combinations
import sys

#Original = [12] OK
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = -1
# remove Combination_List_6element if dick[i] == 0
#xyz
#escape from dead loop = 1500
#cycle_times =  1
#return_list =  [[2, 5, 6, 7, 10, 11], [1, 3, 4, 8, 9, 12]]
#check_delete_all = True
#start_time  :  2021-12-04 11:22:11.113351
#finish_time :  2021-12-04 11:22:11.928107
#delta time  :  0:00:00.814756


#=================================================================


#Original = [13] OK
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = -1
# remove Combination_List_6element if dick[i] == 0
#xyz
#escape from dead loop = 1500
#cycle_times =  1
#return_list =  [[2, 6, 7, 8, 12, 13], [1, 3, 5, 8, 10, 12], [2, 4, 7, 9, 10, 11], [1, 3, 6, 9, 11, 13], [3, 4, 5, 6, 7, 13]]
#check_delete_all = True
#start_time  :  2021-12-04 11:27:24.338478
#finish_time :  2021-12-04 11:27:25.316316
#delta time  :  0:00:00.977838

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#=================================================================


#Original = [14]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[14]  
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = -1
# remove Combination_List_6element if dick[i] == 0
#xyz
#escape from dead loop = 1500
#cycle_times =  601
#return_list =  [[2, 3, 5, 6, 7, 8], [4, 9, 11, 12, 13, 14], [1, 3, 4, 8, 9, 10], [1, 6, 7, 10, 12, 13], [1, 2, 5, 10, 11, 14]]
#check_delete_all = True
#start_time  :  2021-12-04 11:28:56.095119
#finish_time :  2021-12-04 11:29:18.487585
#delta time  :  0:00:22.392466
#[14]
#by get_one_function
#delta time  :  0:01:06.791096
#---------------------------------------------
#start_time  :  2022-12-16 22:39:41.994411
#finish_time :  2022-12-16 22:40:45.009849
#delta time  :  0:01:03.015438
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#start_time  :  2022-12-16 23:22:00.794991
#finish_time :  2022-12-16 23:23:56.093259
#delta time  :  0:01:55.298268
#=================================================================



#Original = [15] 

#[15]  
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = -1
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#escape from dead loop = 1500
#cycle_times =  1

#return_list =  [[2, 4, 7, 8, 10, 14], [1, 2, 3, 6, 7, 11], [3, 5, 6, 10, 13, 14], [3, 9, 10, 11, 12, 15], [1, 2, 7, 9, 13, 14]
#               , [4, 5, 6, 8, 9, 11], [1, 4, 8, 12, 13, 15], [2, 5, 7, 12, 14, 15]]
#check_delete_all = True
#start_time  :  2021-12-04 11:47:13.550689
#finish_time :  2021-12-04 11:47:15.547304
#delta time  :  0:00:01.996615

#return_list =  [[1, 3, 7, 8, 10, 13], [7, 8, 9, 13, 14, 15], [4, 5, 7, 9, 10, 12], [2, 5, 6, 9, 11, 14], [6, 10, 11, 12, 13, 15]
#               , [1, 2, 4, 6, 8, 12], [1, 2, 3, 4, 5, 15], [3, 4, 11, 12, 13, 14]]
#check_delete_all = True
#start_time  :  2022-06-02 01:21:14.535423
#finish_time :  2022-06-02 01:25:16.913007
#delta time  :  0:04:02.377584
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#random.shuffle(Combination_List_5element)
#random.shuffle(Combination_List_6element)
#for w in range( length5*10 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = random.randint(-5,4)
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#escape from dead loop = 1500
#cycle_times =  1738
#return_list =  [[6, 8, 10, 11, 14, 15], [2, 3, 8, 10, 11, 12], [2, 4, 6, 8, 9, 13], [2, 4, 5, 7, 13, 15], [1, 3, 5, 7, 11, 14]
#               , [1, 3, 9, 12, 13, 15], [5, 6, 7, 9, 10, 12], [1, 4, 10, 12, 13, 14]]
#check_delete_all = True
#start_time  :  2021-12-14 20:42:12.232421
#finish_time :  2021-12-14 21:39:25.493426
#delta time  :  0:57:13.261005
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[15]  
#by get_one_function
#cycle_times =  2
#return_list =  [[1, 2, 5, 6, 13, 14], [7, 8, 9, 10, 11, 12], (3, 4, 6, 8, 14, 15), (1, 3, 4, 10, 13, 15), (2, 5, 7, 9, 12, 15), (3, 4, 7, 9, 11, 12), (2, 3, 4, 5, 8, 10), (1, 7, 10, 11, 13, 15)]
#check_delete_all = True
#start_time  :  2022-12-16 23:26:03.075785
#finish_time :  2022-12-16 23:32:07.457300
#delta time  :  0:06:04.381515
#=================================================================



#Original = [16] 
#[16]  + 3
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
# select_counter = random.randint(-5,4)
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#escape from dead loop = 10000
#cycle_times =  1728
#return_list =  [[2, 5, 6, 9, 14, 16], [3, 5, 11, 12, 13, 14], [1, 2, 3, 7, 8, 14], [1, 3, 4, 9, 12, 15], [7, 8, 9, 10, 11, 13]
#               , [1, 2, 5, 8, 10, 12], [1, 4, 6, 7, 10, 16], [2, 4, 11, 13, 15, 16], [6, 8, 10, 11, 14, 15], [5, 6, 7, 12, 15, 16]
#               , [3, 4, 6, 8, 13, 16]]
#check_delete_all = True
#start_time  :  2021-12-04 19:25:50.954703
#finish_time :  2021-12-04 21:03:25.156003
#delta time  :  1:37:34.201300
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[16]
# select_counter = 0
# time usage:  0:01:14.587703
#return_list =  [
# [3, 4, 5, 6, 13, 14], [1, 2, 3, 4, 15, 16], [1, 2, 3, 4, 11, 12], [9, 10, 11, 12, 15, 16], [7, 8, 9, 10, 13, 14], 
# [5, 6, 7, 8, 9, 10], [1, 2, 5, 6, 13, 14], [7, 8, 11, 12, 15, 16]]

#delta time  :  0:04:48.519367
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[16]
# #by get_one_function

#=================================================================




#Original = [17] 
#[17]  + 3
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
# select_counter = random.randint(-5,4)
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#escape from dead loop = 1500
#cycle_times =  3691
#return_list =  [[2, 9, 10, 12, 14, 15], [1, 2, 3, 6, 14, 16], [4, 6, 8, 9, 10, 13], [5, 6, 11, 12, 13, 14], [1, 7, 8, 11, 15, 16]
#               , [1, 3, 9, 13, 15, 17], [2, 3, 5, 8, 12, 17], [1, 4, 5, 7, 8, 14], [3, 4, 7, 12, 15, 16], [3, 5, 9, 10, 11, 17]
#               , [2, 5, 7, 13, 16, 17], [1, 2, 4, 6, 11, 17], [6, 7, 10, 15, 16, 17], [7, 9, 10, 12, 14, 16]]
#check_delete_all = True
#start_time  :  2021-12-05 16:27:48.703694
#finish_time :  2021-12-05 19:05:56.259616
#delta time  :  2:38:07.555922
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#=================================================================
#Original = [18] 
#[18] + 6
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
# select_counter = random.randint(-5,4)
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#escape from dead loop = 1500
#cycle_times =  2140
#return_list =  [[2, 3, 6, 13, 17, 18], [4, 5, 8, 9, 13, 17], [1, 10, 11, 12, 13, 14], [2, 3, 8, 9, 11, 14], [1, 3, 6, 8, 12, 15]
#               , [5, 9, 11, 13, 15, 18], [2, 4, 5, 10, 12, 16], [1, 7, 12, 16, 17, 18], [5, 6, 7, 11, 14, 17], [1, 3, 4, 7, 11, 18]
#               , [2, 4, 7, 14, 15, 18], [7, 8, 10, 13, 15, 16], [1, 2, 9, 10, 15, 17], [3, 4, 14, 15, 16, 17], [4, 6, 8, 9, 10, 18]
#               , [3, 5, 7, 9, 12, 13], [1, 2, 6, 9, 11, 16], [2, 5, 7, 8, 14, 18]]
#check_delete_all = True
#start_time  :  2021-12-05 08:48:13.512293
#finish_time :  2021-12-05 11:31:38.200956
#delta time  :  2:43:24.688663
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[18] 
#by get_one_function()
#ratio = int(combination6_size/up_remove_count)+1
#cycle_times =  1
#return_list =  [[7, 8, 13, 14, 17, 18], [5, 6, 9, 10, 15, 16], [1, 2, 3, 4, 11, 12], [1, 2, 9, 10, 13, 14], [5, 6, 7, 8, 11, 12], [3, 4, 15, 16, 17, 18], [3, 4, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16], [1, 2, 5, 6, 17, 18], [9, 10, 11, 12, 17, 18], [1, 2, 7, 8, 15, 16], [#check_delete_all = True
#start_time  :  2022-12-19 18:33:39.365404
#finish_time :  2022-12-19 18:34:10.877638
#delta time  :  0:00:31.512234



#=================================================================
#Original = [19] 

#[19] + 6
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = random.randint(-5,4)  #單一演算法會有僵固性，故選擇多種方法，可有較好突破?
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#XYZ_RETRY_TIME_give_up_bet_number7_CONSTANT = 10000

#cycle_times =  2200
#return_list =  [[2, 3, 4, 11, 16, 17], [2, 4, 8, 12, 14, 18], [3, 4, 5, 8, 12, 16], [3, 4, 6, 15, 17, 19], [3, 8, 9, 13, 16, 18]
# , [5, 7, 9, 12, 17, 19], [5, 6, 7, 11, 14, 18], [2, 6, 9, 14, 16, 17], [1, 6, 11, 12, 13, 15], [4, 6, 7, 8, 10, 11]
# , [1, 2, 5, 11, 16, 19], [1, 10, 13, 14, 17, 19], [2, 5, 8, 10, 13, 15], [1, 7, 9, 10, 15, 16], [8, 9, 11, 14, 15, 19]
# , [1, 2, 7, 13, 17, 18], [1, 4, 5, 9, 10, 18], [2, 3, 6, 10, 12, 18], [1, 3, 6, 7, 8, 14], [4, 6, 7, 13, 16, 19]
# , [11, 12, 15, 16, 18, 19]]
#
#set6 =  21 [[2, 3, 4, 11, 16, 17], [2, 4, 8, 12, 14, 18], [3, 4, 5, 8, 12, 16], [3, 4, 6, 15, 17, 19], [3, 8, 9, 13, 16, 18]
# , [5, 7, 9, 12, 17, 19], [5, 6, 7, 11, 14, 18], [2, 6, 9, 14, 16, 17], [1, 6, 11, 12, 13, 15], [4, 6, 7, 8, 10, 11]
# , [1, 2, 5, 11, 16, 19], [1, 10, 13, 14, 17, 19], [2, 5, 8, 10, 13, 15], [1, 7, 9, 10, 15, 16], [8, 9, 11, 14, 15, 19]
# , [1, 2, 7, 13, 17, 18], [1, 4, 5, 9, 10, 18], [2, 3, 6, 10, 12, 18], [1, 3, 6, 7, 8, 14], [4, 6, 7, 13, 16, 19]
# , [11, 12, 15, 16, 18, 19]]
#check_delete_all = True
#start_time  :  2022-05-01 01:07:37.000432
#finish_time :  2022-05-01 04:41:25.549578
#delta time  :  3:33:48.549146

#圈選號碼 =  [[5, 6, 7, 23, 36, 40], [5, 7, 18, 26, 34, 41], [6, 7, 8, 18, 26, 36], [6, 7, 9, 35, 40, 42], [6, 18, 20, 29, 36, 41]
# , [8, 15, 20, 26, 40, 42], [8, 9, 15, 23, 34, 41], [5, 9, 20, 34, 36, 40], [4, 9, 23, 26, 29, 35], [7, 9, 15, 18, 22, 23]
# , [4, 5, 8, 23, 36, 42], [4, 22, 29, 34, 40, 42], [5, 8, 18, 22, 29, 35], [4, 15, 20, 22, 35, 36], [18, 20, 23, 34, 35, 42]
# , [4, 5, 15, 29, 40, 41], [4, 7, 8, 20, 22, 41], [5, 6, 9, 22, 26, 41], [4, 6, 9, 15, 18, 34], [7, 9, 15, 29, 36, 42]
# , [23, 26, 35, 36, 41, 42]]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[19] + 7

#for w in range( length5*10 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
# select_counter = random.randint(-5,4)
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#escape from dead loop = 1500
#select_counter = random.randint(-5,4)
#cycle_times =  750
#return_list =  [[3, 4, 5, 6, 8, 13], [6, 12, 13, 14, 16, 19], [2, 8, 10, 14, 16, 19], [1, 5, 11, 16, 18, 19], [1, 3, 4, 9, 13, 14]
#               , [1, 7, 8, 11, 15, 16], [2, 5, 7, 13, 17, 19], [1, 2, 8, 12, 17, 18], [2, 3, 11, 14, 15, 17], [2, 4, 6, 8, 9, 19]
#               , [3, 6, 7, 9, 11, 18], [1, 4, 10, 11, 16, 17], [3, 9, 10, 13, 18, 19], [3, 7, 9, 10, 12, 14], [5, 9, 12, 15, 16, 17]
#               , [1, 2, 6, 10, 13, 15], [4, 7, 12, 15, 18, 19], [5, 7, 8, 10, 15, 18], [1, 5, 6, 7, 14, 17], [2, 4, 5, 11, 12, 14]
#               , [6, 8, 10, 11, 12, 13], [2, 4, 6, 9, 10, 16]]
#check_delete_all = True
#start_time  :  2021-12-04 23:01:15.528789
#finish_time :  2021-12-05 00:32:21.359430
#delta time  :  1:31:05.830641


#=================================================================
#Original = [20] 
#[20] + 3
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
# select_counter = random.randint(-5,4)
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#escape from dead loop = 1500
#select_counter = random.randint(-5,4)
#cycle_times =  578
#return_list =  [[2, 10, 11, 17, 19, 20], [4, 7, 14, 16, 18, 19], [1, 5, 13, 14, 15, 20], [1, 3, 4, 10, 15, 18], [1, 4, 10, 12, 16, 20]
#               , [3, 6, 7, 8, 14, 19], [6, 11, 12, 13, 14, 16], [2, 5, 8, 12, 15, 19], [3, 5, 6, 7, 11, 18], [1, 6, 10, 13, 17, 19]
#               , [2, 7, 9, 10, 14, 18], [5, 9, 11, 14, 15, 17], [1, 7, 8, 9, 11, 13], [4, 5, 9, 13, 16, 19], [3, 6, 9, 12, 17, 20]
#               , [1, 2, 3, 11, 16, 17], [2, 4, 5, 6, 8, 20], [2, 7, 12, 13, 15, 17], [8, 13, 16, 17, 18, 20], [6, 9, 10, 15, 16, 18]
#               , [5, 7, 8, 10, 16, 17], [3, 5, 10, 12, 13, 14], [1, 11, 12, 15, 16, 18], [3, 4, 11, 13, 14, 20], [4, 8, 9, 12, 14, 17]
#               , [3, 4, 15, 18, 19, 20]]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[20] + 3
#cycle_times =  2
#check_delete_all = True
#start_time  :  2021-12-05 20:31:58.411675
#finish_time :  2021-12-05 22:37:22.429491
#delta time  :  2:05:24.017816
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[20] + 3
#by get_one_function()
#return_list =  [[3, 4, 5, 6, 17, 18], [7, 8, 11, 12, 13, 14], [1, 2, 9, 10, 15, 16], [5, 6, 11, 12, 19, 20], [3, 4, 13, 14, 19, 20], 
# [7, 8, 9, 10, 17, 18], [1, 2, 3, 4, 7, 8], [13, 14, 15, 16, 17, 18], [1, 2, 11, 12, 17, 18], [5, 6, 7, 8, 15, 16], 
# [3, 4, 9, 10, 11, 12], [5, 6, 9, 10, 13, 14], [1, 2, 15, 16, 19, 20], [9, 10, 15, 16, 19, 20], [1, 2, 9, 10, 19, 20], 
# [1, 2, 5, 6, 13, 14], [7, 8, 17, 18, 19, 20], [3, 4, 11, 12, 15, 16], [3, 4, 9, 10, 13, 14], [9, 10, 11, 12, 17, 18], 
# [5, 6, 7, 8, 9, 10]]
#check_delete_all = True
#start_time  :  2022-12-15 22:27:12.300208
#finish_time :  2022-12-15 22:31:14.765794
#delta time  :  0:04:02.465586
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[20] + 3
#by get_one_function()
#time usage:  0:03:17.829467
#max_remove_count 2036
#min_remove_count 1000
#remove_count 2036
#cycle_times =  2
#return_list =  [
    # [1, 2, 7, 8, 9, 10], [5, 6, 11, 12, 13, 14], [3, 4, 17, 18, 19, 20], [7, 8, 15, 16, 19, 20], [9, 10, 15, 16, 17, 18], 
    # [1, 2, 3, 4, 13, 14], [3, 4, 5, 6, 7, 8], [1, 2, 11, 12, 19, 20], [7, 8, 11, 12, 17, 18], [5, 6, 9, 10, 19, 20], 
    # [3, 4, 11, 12, 15, 16], [1, 2, 5, 6, 17, 18], [9, 10, 13, 14, 15, 16], [9, 10, 13, 14, 17, 18], [13, 14, 15, 16, 17, 18], 
    # [1, 2, 5, 6, 15, 16], [7, 8, 13, 14, 19, 20], [3, 4, 9, 10, 11, 12], [7, 8, 11, 12, 15, 16], [5, 6, 15, 16, 19, 20], 
    # [1, 2, 3, 4, 15, 16]]


#=================================================================
#Original = [21] 
#[21] + 9


#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
# select_counter = random.randint(-5,4)
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#escape from dead loop = 1500
#select_counter = random.randint(-5,4)
#cycle_times =  

#=================================================================
#Original = [22] 
#[22] + 15
# step = 4
#time usage:  0:08:25.895934
#return_list =  [[1, 2, 9, 10, 15, 16], [5, 6, 11, 12, 17, 18], [5, 6, 7, 8, 13, 14], [15, 16, 19, 20, 21, 22], [3, 4, 7, 8, 19, 20], [3, 4, 5, 6, 21, 22], [1, 2, 3, 4, 13, 14], [7, 8, 11, 12, 17, 18], [9, 10, 17, 18, 21, 22], [3, 4, 11, 12, 15, 16], [5, 6, 9, 10, 13, 14], [1, 2, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [1, 2, 17, 18, 21, 22], [7, 8, 9, 10, 11, 12], [11, 12, 13, 14, 21, 22], [5, 6, 15, 16, 19, 20], [3, 4, 9, 10, 19, 20], [7, 8, 9, 10, 15, 16], [1, 2, 7, 8, 11, 12], [3, 4, 11, 12, 19, 20], [1, 2, 7, 8, 19, 20], [3, 4, 5, 6, 9, 10], [1, 2, 3, 4, 17, 18], [11, 12, 13, 14, 15, 16], [1, 2, 3, 4, 15, 16], [7, 8, 13, 14, 21, 22], [1, 2, 19, 20, 21, 22], [9, 10, 13, 14, 17, 18], [1, 2, 7, 8, 9, 10], [5, 6, 15, 16, 21, 22], [5, 6, 9, 10, 17, 18], [5, 6, 7, 8, 21, 22], [3, 4, 17, 18, 21, 22], [1, 2, 13, 14, 19, 20], [3, 4, 9, 10, 13, 14], [5, 6, 15, 16, 17, 18], [5, 6, 19, 20, 21, 22], [11, 12, 17, 18, 19, 20], [3, 4, 5, 6, 13, 14]]
#[22] + 12
# step = 1
#cycle_times = 1
#time usage:  0:30:25.895934
#cycle_times =  4
#min_set6_length =  22
#select_counter =  0
#return_list =  [[7, 8, 9, 10, 11, 12], [1, 2, 17, 18, 19, 20], [3, 4, 5, 6, 21, 22], [11, 12, 13, 14, 15, 16], [9, 10, 13, 14, 21, 22], [1, 2, 5, 6, 7, 8], [3, 4, 15, 16, 19, 20], [3, 4, 7, 8, 17, 18], [5, 6, 9, 10, 15, 16], [11, 12, 17, 18, 21, 22], [5, 6, 13, 14, 19, 20], [1, 2, 15, 16, 21, 22], [1, 2, 3, 4, 11, 12], [9, 10, 17, 18, 19, 20], [7, 8, 13, 14, 15, 16], [7, 8, 19, 20, 21, 22], [1, 2, 9, 10, 17, 18], [5, 6, 11, 12, 17, 18], [3, 4, 9, 10, 13, 14], [1, 2, 11, 12, 19, 20], [13, 14, 17, 18, 21, 22], [7, 8, 11, 12, 13, 14], [5, 6, 15, 16, 17, 18], [3, 4, 9, 10, 15, 16], [5, 6, 11, 12, 21, 22], [1, 2, 9, 10, 19, 20], [7, 8, 11, 12, 15, 16], [3, 4, 11, 12, 19, 20], [1, 2, 3, 4, 13, 14], [7, 8, 9, 10, 17, 18], [3, 4, 7, 8, 9, 10], [11, 12, 15, 16, 21, 22], [1, 2, 5, 6, 9, 10], [9, 10, 11, 12, 13, 14]]
#check_delete_all = True
#start_time  :  2022-12-15 02:38:13.240481
#finish_time :  2022-12-15 06:39:35.299957
#delta time  :  4:01:22.059476
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
#[22] + 12
#print("***Combination_List_5element = ",len(Combination_List_5element),target_remove_count, remove_count, len(choosen_dict[0]) )
#Combination_List_5element 26334            
#***Combination_List_5element =  23688 2546 2646 1
#***Combination_List_5element =  21042 2545 2646 2
#***Combination_List_5element =  18396 2545 2646 3
#***Combination_List_5element =  16062 2334 2334 4
#***Combination_List_5element =  4918 716 716 13
#***Combination_List_5element =  4272 646 646 14
#***Combination_List_5element =  3776 496 496 15
#***Combination_List_5element =  3304 472 472 16
#***Combination_List_5element =  2880 424 424 17
#***Combination_List_5element =  2496 384 384 18
#***Combination_List_5element =  2144 352 352 19
#***Combination_List_5element =  1824 320 320 20
#***Combination_List_5element =  1600 224 224 21
#***Combination_List_5element =  1408 192 192 22
#***Combination_List_5element =  1216 192 192 23
#***Combination_List_5element =  1056 160 160 24
#***Combination_List_5element =  928 128 128 25
#***Combination_List_5element =  800 128 128 26
#***Combination_List_5element =  672 128 128 27
#***Combination_List_5element =  544 127 128 28
#***Combination_List_5element =  416 127 128 29
#***Combination_List_5element =  288 126 128 30
#***Combination_List_5element =  192 96 96 31
#***Combination_List_5element =  128 64 64 32
#***Combination_List_5element =  64 64 64 33
#=================================================================



bet_number7  = 20
extra_length = 3
list_pointer = []

    
cycle_times_display = 2
XYZ_RETRY_TIME_give_up_bet_number7_CONSTANT = 10000 #bet_number7 <= 16
#XYZ_RETRY_TIME_give_up_one_CONSTANT = 2000
#XYZ_RETRY_TIME_CONSTANT = 3000 #bet_number7 >= 17zsczscZZ 
cpus = os.cpu_count()
cpus -= 1
start_time = datetime.datetime.now()
dict = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0, 23:0, 24:0}
trial_dict =            {12:2,   13:5,    14:5,    15:8,    16:8,    17:11,    18:12,    19:15,    20:18,    21:21,   22:22,   23:26,    24:30, 25:36}
max_remove_count_dict = {12:396, 13:531,  14:686,  15:861,  16:1056, 17:1271,  18:1506,  19:1761,  20:2036,  21:2331, 22:2646, 23:2981,  24:3336}
min_remove_count_dict = {12:396, 13:531,  14:686,  15:861,  16:1056, 17:1271,  18:1506,  19:1761,  20:2036,  21:2331, 22:2646, 23:2981,  24:3336}
combination_size_dict = {12:792, 13:1287, 14:2002, 15:3003, 16:4368, 17:6188,  18:8568,  19:11628, 20:15504, 21:15504,22:26334,23:26334, 24:26334}
combination6_size_dict ={12:924, 13:1716, 14:3003, 15:5005, 16:8008, 17:12376, 18:18564, 19:27132, 20:38760, 21:54264,22:74613,23:100947,24:134596}
choosen_size_dict      ={12:20,  13:20,   14:35,   15:35,   16:56,   17:56,    18:84,    19:84,    20:120,   21:120,  22:165,  23:165,   24:220}

seed = [[1,2],[3,4],[5,6],[7,8],[9,10],
        [11,12],[13,14],[15,16],[17,18],[19,20],
        [21,22],[23,24],[25,26],[27,28],[29,30]]
seed = seed[:int(bet_number7/2)]
temp_cadidate = list(combinations(seed,3))
original_choosen_list = []
for i in temp_cadidate:
    k = i[0]+i[1]+i[2]
    original_choosen_list.append(k)
choosen_list = []
len_cadidate = 0
max_remove_count_number = max_remove_count_dict[bet_number7]
choosen_dict = {}

#for i in range(max_remove_count_number + 1):
#    list_pointer.append([]) # 令其轉為二維串列形式
#print(len(list_pointer))    
pointer_of_list_pointer = max_remove_count_number
#min_ending_section = 18

#9 : 75, 42, 9
#10: 95, 79, 30, 6
#11: 115, 46, 39, 14


global_close = mp.Value('i', 0)
lock_global_close = mp.Lock()

def check_delete_all( target_list ):
    Original = []
    remove_count = 0
    for i in range(bet_number7):
        Original.append(i+1)
    Combination_List_5element = list(combinations(Original ,5))
    for x in target_list:
        three = list(combinations(x ,3))
        for c in three:
            dup_Combination_List_5element = copy.deepcopy(Combination_List_5element)
            for d5 in dup_Combination_List_5element:
                if set(c) <= set(d5):
                    Combination_List_5element.remove(d5)
                    remove_count = remove_count + 1 
    print("remove_count", remove_count)
    print("Combination_List_5element", Combination_List_5element)
    if (len(Combination_List_5element) == 0):
        return True
    else:
        return False


def get_one_function( pointer_of_list_pointer, Combination_List_5element, target_remove_count, choosen_dict):
    new_list = []
    #length = len(choosen_list)-1
    #k = random.randint(0,len(choosen_list)-1)
    #new_list = choosen_list[k]
    pointer_of_list_pointer = target_remove_count
    found = False
    while found == False:

        if (pointer_of_list_pointer in choosen_dict) and (len(choosen_dict[pointer_of_list_pointer])>0):
            k_list = choosen_dict[pointer_of_list_pointer]
            #print("k_list", k_list)
            new_list = k_list[random.randint(0,len(k_list)-1)]
            k_list.remove(new_list)
            choosen_dict[pointer_of_list_pointer] = k_list
            #print(target_remove_count)                
            #print(list_pointer[0])
            #print("pointer_of_list_pointer",new_list, len(Combination_List_5element) )            
            found = True
        else:
            if (pointer_of_list_pointer != max_remove_count_number):
                pointer_of_list_pointer += 1    
                #print("pointer_of_list_pointer",new_list, len(Combination_List_5element) )
                #print(target_remove_count)                
            else:
                break    
    #print("pointer_of_list_pointer",new_list, len(Combination_List_5element) )
    #print(target_remove_count)
 
    return new_list
    
def section_matching_function( index_start, global_close, lock_global_close, return_list  ):
    #trial_dict = {9:3,   10:4,   11:5,   12:6,   13:9,   14:11,  15:14,  16:16,  17:20,  18:25,  19:31,  20:38, 21:0}
    #stop_others = False
    print("Process", index_start)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    Original = []
    min_length_Combination_List_5element = 2000
    max_remove_count = 0

        
    for i in range(bet_number7):
        Original.append(i+1)
    #print("Original : ", Original)
    try_set_number = trial_dict[bet_number7]
    #print("try_set_number : ", try_set_number)

    start_Combination_List_5element = list(combinations(Original ,5))


    #reverse_Combination_List_6element = copy.deepcopy(Combination_List_6element)
    #reverse_Combination_List_6element.reverse()

    #length = 0
    close = False
    #terminator = False
    cycle_times = 0
    set6_complete_times = 0
    set6 = []

    length5 = len(start_Combination_List_5element)
    #length6 = len(Combination_List_6element)
    #try_set_number = try_set_number + 5
    print("Combination_List_5element", length5 )
    #print("len(Combination_List_6element)",len(Combination_List_6element) )
    #while ((terminator == False) & (close == False)):
    hit_upper_number = len(start_Combination_List_5element) *4 / bet_number7 
    #print("hit_upper_number", hit_upper_number)
    remove_count = 0
    done_by_others = False

# added on 2022 0903, try to reduce computing time for "bet_number7 == 21"
    start_set6 = []

    while (close == False):
        #Combination_List_5element = list(combinations(Original ,5))
        #if (bet_number7 == 21) :
        #    Combination_List_5element = copy.deepcopy(start_Combination_List_5element)
        Combination_List_6element = list(combinations(Original ,6))
        #random.shuffle(Combination_List_5element)
        random.shuffle(Combination_List_6element)
        #print("############## restart Combination_List_5element = ", len(Combination_List_5element), "##########################")
        set6 = copy.deepcopy(start_set6)
        hit_treated_list = []
        remove_count = 0
        cycle_times += 1
        min_set6_length = trial_dict[bet_number7]

        #lock_global_close.acquire()
        if  (global_close.value >= 1):
            #lock_global_close.release()
            print("exit while = ", index_start)
            done_by_others = True
            break
        #lock_global_close.release()

        ending_section = False
        inner_counter = 0
        inner_exit = False

        for w in range( length5*10 ): 
            #if the range is too small, it will cause "if (try_set_number+6 == len(set6))" fail. the reason is no sufficient set6 elements to be generated in the for's cycle 
            #length5**2 is too big, sometimes the process can not escape from loop it will loop such a big number(length5**2= Mega grade number)
            #有些時候XYZ無法形成len == 6，這時候就會出不來，無法到"while (close == False):"這級迴圈重新"Combination_List_5element""

            if( close == True):
                print("exit for w = ", index_start)
                break
            if( inner_exit == True):
                break
            #lock_global_close.acquire()
            if  (global_close.value >= 1):
                #lock_global_close.release()             
                print("exit for w = ", index_start)
                done_by_others = True  
                break
            #lock_global_close.release()
            #print("**************** restart Combination_List_5element = ", index_start, len(Combination_List_5element), "**************** ")  
            min_remove_count = 1000
            #print("***length of Combination_List_5element = ",len(Combination_List_5element))
            select_counter = 0
            up_remove_count   = max_remove_count_dict[bet_number7]
            combination6_size = combination6_size_dict[bet_number7]
            ratio = int(combination6_size/up_remove_count)
            step = int(up_remove_count/200)

            choosen_list = copy.deepcopy(original_choosen_list)
            choosen_dict[max_remove_count_number-1] = choosen_list

            #Total6_list = copy.deepcopy(Combination_List_6element)
            #choosen_dict[max_remove_count_number] = Total6_list 
    
            choosen_dict[0] = []
            Combination_List_5element = list(combinations(Original ,5))
            #print(choosen_dict)


            #print(pointer_of_list_pointer)
            #print(len(list_pointer[len(list_pointer)-1]))
            for descend_cycle in range((up_remove_count-100)*ratio, 2, -1): #每一回圈取一組六個數的list
                target_remove_count = int(descend_cycle/ratio)
                #print("target_remove_count =", target_remove_count)
                #target_remove_count = 3 #不是好的選擇，會造成min_length過大
                #lock_global_close.acquire()
                if  (global_close.value >= 1):
                    #lock_global_close.release()
                    print("exit for descend_cycle = ", index_start)
                    done_by_others = True  
                    break
                #lock_global_close.release()

                if (inner_exit == True): #2021_1201
                    break

                inner_counter += 1
                set_Combination_List_5element = set()
 
                #print("set6 = ", set6)
                #find elements of remaining in  set_Combination_List_5element
                for p in Combination_List_5element:
                    set_Combination_List_5element = set_Combination_List_5element.union(p)

                list_t = []
                uni = []
                if (len(set_Combination_List_5element) <= 6):
                    ending_section = True
                
                elif (len(set_Combination_List_5element) == 7):
                    list_t = list(set_Combination_List_5element)
                    uni = list_t[0:6]
                    set6.append(uni)
                    uni = list_t[1:]
                    set6.append(uni)                   
                    set_Combination_List_5element= {}
                    ending_section = True   
                elif (len(set_Combination_List_5element) == 8):
                    list_t = list(set_Combination_List_5element)                    
                    uni = list_t[0:6]
                    set6.append(uni)
                    uni = list_t[2:]
                    set6.append(uni)                      
                    set_Combination_List_5element= {}                               
                    ending_section = True   
                elif (len(set_Combination_List_5element) == 9):
                    list_t = list(set_Combination_List_5element)                    
                    uni = list_t[0:6]
                    set6.append(uni)
                    uni = list_t[3:]
                    set6.append(uni)                      
                    set_Combination_List_5element= {}                                
                    ending_section = True                       
                elif (len(set_Combination_List_5element) == 10):
                    list_t = list(set_Combination_List_5element)                    
                    uni = list_t[0:6]
                    set6.append(uni)
                    uni = list_t[4:]
                    set6.append(uni)                      
                    set_Combination_List_5element= {}                          
                    ending_section = True                       
                elif (len(set_Combination_List_5element) == 11):
                    list_t = list(set_Combination_List_5element)                    
                    uni = list_t[0:6]
                    set6.append(uni)
                    uni = list_t[5:]
                    set6.append(uni)               
                    set_Combination_List_5element= {}                                 
                    ending_section = True                       
                elif (len(set_Combination_List_5element) == 12):
                    list_t = list(set_Combination_List_5element)                    
                    uni = list_t[0:6]
                    set6.append(uni)
                    uni = list_t[6:]
                    set6.append(uni)                 
                    set_Combination_List_5element= {}                          
                    ending_section = True                       
                else:
                    ending_section = False
                                                                                         
                if (ending_section == False):
                    select_counter = 0
                    if (select_counter == 0):
                        uni  = get_one_function( pointer_of_list_pointer,Combination_List_5element, target_remove_count, choosen_dict )
                        #uni = choosen_list[random.randint(0,len(choosen_list)-1)]
                        #choosen_list.remove(uni)
                        len_cadidate = len(choosen_list)


                    #uni.sort()
                    #print("***uni = ", uni)
                    remove_count = 0
                    remove_list = []
                    if (len(uni)==6):
                        three = list(combinations(uni ,3))
                        for c in three:
                            dup_Combination_List_5element = copy.deepcopy(Combination_List_5element)
                            for d5 in dup_Combination_List_5element:
                                if set(c) <= set(d5):
                                    Combination_List_5element.remove(d5)
                                    remove_list.append(d5) 
                                    remove_count = remove_count + 1
                                #print("c = ", c)
                        #print("remove_count = ", remove_count)

                        if remove_count < target_remove_count:    
                            if remove_count > 0 :
                                if remove_count not in choosen_dict:
                                    choosen_dict[remove_count] = []
                                k_list = choosen_dict[remove_count]
                                k_list.append(uni)
                                choosen_dict[remove_count] = k_list
                            for k in remove_list:
                                Combination_List_5element.append(k)
                        else:
                            #list_pointer[0].append(uni)
                            k_list = choosen_dict[0]
                            k_list.append(uni)
                            choosen_dict[0] = k_list
                            #list_pointer[max_remove_count_number-1].remove(uni)
                            #print("list_pointer", list_pointer[0])
                            set6.append(uni)    
                            ###########################################
                            #choosen_list.remove(uni) 
                            #print("choosen_list len = ", len(choosen_list))
                            #print("descend_cycle = ", descend_cycle )
                            ###########################################
                            for d6 in Combination_List_6element:
                                if set(uni) <= set(d6):
                                    Combination_List_6element.remove(d6)
                                    break
                            #print("***uni", uni)
                            #print("***remove_count", index_start, remove_count)
                            print("***Combination_List_5element = ",len(Combination_List_5element),target_remove_count, remove_count, len(choosen_dict[0]) )
                            #print("*set6 = ",len(set6), set6)
                            if (remove_count > max_remove_count):
                                max_remove_count = remove_count
                            if (remove_count < min_remove_count):
                                min_remove_count = remove_count
                else:
                    remove_count = len(Combination_List_5element)
                    print("***remove_count", index_start, remove_count, ", ending_section")
                    print("Combination_List_5element",Combination_List_5element)
                    Combination_List_5element = []
                    if (len(set_Combination_List_5element)>0):
                        uni =  list(set_Combination_List_5element)            
                        uni.sort()
                        print("uni", uni)
                        set6.append(uni)   

                if (len(Combination_List_5element)==0):  
                    return_list.append( set6 ) 
                    #return_list = copy.deepcopy(set6)
                    #list(set(return_list).union(set(set6))  )
                    close = True
                    lock_global_close.acquire()
                    global_close.value += 2
                    lock_global_close.release()
                    print("#global_close: ", global_close.value ) 
                    print("#target_remove_count = ", target_remove_count)       
                    print("###successful Process: ", index_start)
                    print("#Combination_List_5element = ",len(Combination_List_5element))
                    print("#set6 = ",len(set6), set6)
                    print("#max_remove_count", max_remove_count)
                    print("#cycle_times = ",  cycle_times )
                    print("min_set6_length = ", min_set6_length) 
                    break

                if (try_set_number + extra_length == len(set6)):
                    #print("oooooooooooooooooooooooooooo")
                    #print("inner_counter", inner_counter)
                    #print(">>> 6  set6 = ",len(set6))
                    set6_complete_times += 1
                    length_Combination_List_5element = len(Combination_List_5element)
                    #print(">>> Combination_List_5element = ",length_Combination_List_5element )
                    if (length_Combination_List_5element < min_length_Combination_List_5element):
                        min_length_Combination_List_5element = length_Combination_List_5element
                    #print(">>> min_length = ", min_length_Combination_List_5element)    
                    #print()
                    if ((set6_complete_times % 10000) == 0 ):
                        #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                        #print("Process: ", index_start)
                        #print("time : ", time.ctime())   
                        #print("Combination_List_5element = ",len(Combination_List_5element))
                        #print("set6 = ",len(set6))
                        #print("#max_remove_count", max_remove_count)                
                        #print("#min_remove_count", min_remove_count)      
                        #print("#remove_count", remove_count)
                        #print("#set6_complete_times", set6_complete_times)
                        #print(">>> min_length = ", min_length_Combination_List_5element, " <<<")   
                        #print("#cycle_times = ",  cycle_times )
                        #print("min_set6_length = ", min_set6_length) 
                        #print("set_Combination_List_5element = ", set_Combination_List_5element)
                        k = 10
                    inner_exit = True #set6 length limit is reached, no more 
                    break              
            if ( min_set6_length > len(set6)):
                min_set6_length =  len(set6)
            if (( cycle_times% cycle_times_display ) == 0): 
                print()
                print("**************************************************************")
                print("Process: ", index_start)
                #print("time : ", time.ctime())   
                now = datetime.datetime.now()
                print("time usage: ", now - start_time)   
                print("Combination_List_5element = ",len(Combination_List_5element))
                print("set6 = ",len(set6))
                print("#max_remove_count", max_remove_count)                
                print("#min_remove_count", min_remove_count)      
                print("#remove_count", remove_count)
                print(">>> min_length = ", min_length_Combination_List_5element, " <<<")   
                print("#cycle_times = ",  cycle_times )
                print("min_set6_length = ", min_set6_length) 
                print("select_counter = ", select_counter) 

#    if (done_by_others == False): 
#        print("===============Process: ", index_start)
#        print("===============Combination_List_5element = ",len(Combination_List_5element), Combination_List_5element)
#        print("===============set6 = ",len(set6), set6)
#        return_list.append ( set6)
    # uni = list(set(x).union(set(y)).union(set(z)))
    #uni = list(   set(x).union(set(y) )  )
    #print("dict", dict)
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

def generate_original_number(bet_number7):

    try_set_number = 0

    Original = []
    for i in range(bet_number7):
        Original.append(i+1)
    print("Original : ", Original)
    try_set_number = trial_dict[bet_number7]
    print("try_set_number : ", try_set_number)

    Exclusive = []
    inclusive = []

    #Exclusive = list(set(Exclusive))
    #include = [1,7,9,11,17,24,28]

    Exclusive = Exclusive + inclusive

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
    digit_limit = [10,10,10,10,10] #4,3,2,1,0
    digit_available = digit_limit
    print("digit_limit" , digit_limit )

    for i in range(5):
        digit_available[i] = digit_limit[i] - digit_used[i]
    print("digit_available" , digit_available )

    print("generate_number7" , generate_number7 )
    Appear3 = inclusive

    while len(Appear3) < bet_number7:  
        i = random.randint(1,49)
        if ( i not in Appear3 ) & ( i not in Exclusive ) :
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
    print("====================================================")            
    print("")       

    return Appear3

# end of generate_original_number
#P===========================================================
#global_close = False

def show():
    print("show")


if __name__=='__main__':
    original_number =  []
    original_number = generate_original_number(bet_number7)  


    #start_time = time.ctime()
    start_time = datetime.datetime.now()
    print("start_time: ", start_time)   
    print("cpus :", cpus)
    #pool = Process.Pool(4)
    print('main parent process:', os.getppid())
    print('main process id:', os.getpid())
    return_list = []
    mapped_list = []
    process_list = []
#if __name__=='__main__':

#    pool = mp.Pool(cpus)
#    for i in range (cpus):
#        return_list.append( pool.apply_async( section_matching_function, args = ( i,  ))    )       
#    pool.close()
#    pool.join()
#    for i in range (cpus):
#        mapped_list = mapper(len(return_list[i].get()), original_number, return_list[i].get())
#        print(">>>>>>> success mapped_list", mapped_list )
#    #print(len(mapped_list))
#    L = len(mapped_list)
#    Y = L*50

        
    
    manager = mp.Manager()
    return_list = manager.list([])

    #for i in range (cpus):
    #    return_list.append(manager.list())

    print("return_list",return_list)    

    global_close = mp.Value('i', 0)
    lock_global_close = mp.Lock()


    for i in range (cpus):
        process_list.append(  mp.Process( target=section_matching_function, args = ( i, global_close, lock_global_close, return_list ))      )

    for i in range (cpus):
        process_list[i].start()

    for i in range (cpus):
        process_list[i].join()

    print("#return_list = ",return_list[0])  

    if (check_delete_all(return_list[0]) == True):
        print("#check_delete_all = True")
    else:
        print("#check_delete_all = False")


    #finish_time = time.ctime()
    finish_time = datetime.datetime.now()

    print("#start_time  : ", start_time )
    print("#finish_time : ", finish_time )
    print("#delta time  : ", finish_time - start_time)
   # for i in range (cpus):
   #     print(">>>>>>> success return_list", return_list[i].get() )

   # print("")
#    for i in range (cpus):
    print(">>>>>>> len(return_list)", len(return_list[0]) )
    mapped_list = mapper(len(return_list[0]), original_number, return_list[0])
    print("圈選號碼 = ", mapped_list )
    print()
    #print("mapped_list", len(mapped_list))
    L = len(mapped_list)
    Y = L*50
    print("下注號碼 = ", original_number)

    print("P7大樂透中三保三 :", bet_number7, "個號碼，" , Y, "元", "4期共", Y*4, "元" )
    print("===========================================")
    print(choosen_dict)
