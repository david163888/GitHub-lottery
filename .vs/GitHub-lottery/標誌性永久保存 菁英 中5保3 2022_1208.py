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
bet_number = 18
exclusive = []
inclusive = []
digit_limit = [4,4,4,4,4] #0,1,2,3,4
        
#Original = [12] OK
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = -1
# remove Combination_List_6element if dick[i] == 0
#xyz
#escape from dead loop = 1500
#cycle_times =  1
if (bet_number == 12):
    #return_list =  [[2, 5, 6, 7, 10, 11], [1, 3, 4, 8, 9, 12]]
    return_list = [[1,2,3,4,5,6],[7,8,9,10,11,12]]
#check_delete_all = True
#start_time  :  2021-12-04 11:22:11.113351
#finish_time :  2021-12-04 11:22:11.928107
#delta time  :  0:00:00.814756


#=================================================================
#Original = [13] OK
#[13]
# [[1,2,3],[4,5,6],
#  [1,4,7],[2,5,7],[3,6,7]]
if (bet_number == 13):
    return_list = [[1,2,3,4,5,6],[7,8,9,10,11,12],
               [1,2,7,8,13,4],[3,4,9,10,13,5],[5,6,11,12,13,2] ]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[13]
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
#return_list = [[1,2,3,4,5,6],[7,8,9,10,11,12],[1,2,7,8,13,14],[3,4,9,10,13,14],[5,6,11,12,13,14 ]]
#return_list = [[1,2,3,4,5,6],[1,2,7,8,11,12],[3,4,7,8,13,14],[5,6,9,10,11,12],[1, 2, 9, 10, 13, 14]]  #auto
if (bet_number == 14):
    return_list = [
        [1,2,9,10,13,14],[3,4,11,12,13,14],[3,4,5,6,9,10],[5, 6, 7, 8, 11, 12],[1, 2, 3, 4, 7, 8]]
    return_list =  [{3, 4, 7, 8, 9, 10}, {1, 2, 5, 6, 9, 10}, {1, 2, 3, 4, 11, 12}, {7, 8, 11, 12, 13, 14}, {3, 4, 5, 6, 13, 14}]
    return_list =  [{5, 6, 9, 10, 13, 14}, {1, 2, 7, 8, 9, 10}, {3, 4, 11, 12, 13, 14}, {1, 2, 3, 4, 5, 6}, {5, 6, 7, 8, 11, 12}]
#check_delete_all = True
#start_time  :  2021-12-04 11:28:56.095119
#finish_time :  2021-12-04 11:29:18.487585
#delta time  :  0:00:22.392466

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++



#=================================================================
#Original = [15] 

# [15] 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#[15]  
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = -1
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#escape from dead loop = 1500
#cycle_times =  1
if (bet_number == 15):
    return_list =  [[2, 4, 7, 8, 10, 14], [1, 2, 3, 6, 7, 11], [3, 5, 6, 10, 13, 14], [3, 9, 10, 11, 12, 15], [1, 2, 7, 9, 13, 14]
               , [4, 5, 6, 8, 9, 11], [1, 4, 8, 12, 13, 15], [2, 5, 7, 12, 14, 15]]
#check_delete_all = True
#start_time  :  2021-12-04 11:47:13.550689
#finish_time :  2021-12-04 11:47:15.547304
#delta time  :  0:00:01.996615

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#=================================================================
#Original = [16] 

#[16] 
#graph
#   1,2,3
#   4,5,6
#   7,8

# [[1,2,3],[4,5,6],
#  [1,4,7],[2,5,8],
#  [3,5,7],[1,6,8],
#  [2,6,7],[3,4,8]
if (bet_number == 16):
    return_list = [[1,2,3,4,5,6],[7,8,9,10,11,12],
              [1,2,7,8,13,14],[3,4,9,10,15,16],
              [5,6,9,10,13,14],[1,2,11,12,15,16],
              [3,4,11,12,13,14],[5,6,7,8,15,16]]

    return_list =  [
    {16, 7, 8, 11, 12, 15}, {5, 6, 11, 12, 13, 14}, {16, 5, 6, 9, 10, 15}, {1, 2, 7, 8, 9, 10}, {16, 1, 2, 13, 14, 15}
        , {3, 4, 7, 8, 13, 14}, {1, 2, 3, 4, 5, 6}, {3, 4, 9, 10, 11, 12}]  
    return_list =  [
    {1, 2, 7, 8, 13, 14}, {16, 5, 6, 13, 14, 15}, {3, 4, 5, 6, 11, 12}, {3, 4, 7, 8, 9, 10}, {16, 1, 2, 3, 4, 15}
    , {1, 2, 5, 6, 9, 10}, {9, 10, 11, 12, 13, 14}, {16, 7, 8, 11, 12, 15}]     
    
    return_list =  [[1, 5, 6, 9, 11, 15], [2, 8, 11, 12, 13, 14], [2, 3, 5, 9, 12, 16], [4, 5, 7, 8, 15, 16], [1, 4, 7, 10, 12, 14], 
                    [3, 4, 7, 8, 10, 11], [1, 3, 6, 13, 14, 15], [6, 9, 10, 13, 14, 16], [2, 4, 6, 7, 9, 13], [1, 2, 5, 8, 10, 15], 
                    [1, 2, 4, 6, 7, 8], [10, 11, 12, 13, 15, 16]]
    return_list =  [[3, 4, 5, 6, 13, 14], [1, 2, 3, 4, 15, 16], [1, 2, 3, 4, 11, 12], [9, 10, 11, 12, 15, 16], [7, 8, 9, 10, 13, 14], [5, 6, 7, 8, 9, 10], [1, 2, 5, 6, 13, 14], [7, 8, 11, 12, 15, 16]]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++



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
if (bet_number == 17):
    return_list =  [[2, 9, 10, 12, 14, 15], [1, 2, 3, 6, 14, 16], [4, 6, 8, 9, 10, 13], [5, 6, 11, 12, 13, 14], [1, 7, 8, 11, 15, 16]
               , [1, 3, 9, 13, 15, 17], [2, 3, 5, 8, 12, 17], [1, 4, 5, 7, 8, 14], [3, 4, 7, 12, 15, 16], [3, 5, 9, 10, 11, 17]
               , [2, 5, 7, 13, 16, 17], [1, 2, 4, 6, 11, 17], [6, 7, 10, 15, 16, 17], [7, 9, 10, 12, 14, 16]]
#check_delete_all = True
#start_time  :  2021-12-05 16:27:48.703694
#finish_time :  2021-12-05 19:05:56.259616
#delta time  :  2:38:07.555922
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#=================================================================
#Original = [18] 
if (bet_number == 18):
    return_list =  [
    {16, 3, 4, 5, 6, 15}, {5, 6, 9, 10, 11, 12}, {17, 18, 9, 10, 13, 14}, {1, 2, 5, 6, 13, 14}, {17, 18, 5, 6, 7, 8}
    , {16, 7, 8, 9, 10, 15}, {17, 18, 3, 4, 11, 12}, {16, 1, 2, 17, 18, 15}, {1, 2, 7, 8, 11, 12}, {1, 2, 3, 4, 9, 10}
    , {3, 4, 7, 8, 13, 14}, {16, 11, 12, 13, 14, 15}]
    return_list =  [
    {16, 17, 18, 7, 8, 15}, {1, 2, 18, 17, 9, 10}, {1, 2, 5, 6, 7, 8}, {5, 6, 9, 10, 13, 14}, {16, 3, 4, 5, 6, 15}
    , {7, 8, 11, 12, 13, 14}, {1, 2, 3, 4, 11, 12}, {16, 9, 10, 11, 12, 15}, {3, 4, 7, 8, 9, 10}, {17, 18, 3, 4, 13, 14}
    , {16, 1, 2, 13, 14, 15}, {17, 18, 5, 6, 11, 12}]
    return_list =  [
    {16, 1, 2, 13, 14, 15}, {16, 3, 4, 5, 6, 15}, {7, 8, 9, 10, 13, 14}, {16, 9, 10, 11, 12, 15}, {1, 2, 17, 18, 11, 12}
    , {17, 18, 3, 4, 9, 10}, {16, 17, 18, 7, 8, 15}, {1, 2, 3, 4, 7, 8}, {17, 18, 5, 6, 13, 14}, {5, 6, 7, 8, 11, 12}
    , {1, 2, 5, 6, 9, 10}, {3, 4, 11, 12, 13, 14}]

#[18] 
# [[1,2,3],[4,5,6],[7,8,9],
#  [1,4,7],[2,5,8],[3,6,9],
#  [1,5,9],[2,6,7],[3,4,8],
#  [2,4,9],[3,5,7],[1,6,8]]
       
#return_list = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],
#               [1,2,7,8,13,14],[3,4,9,10,15,16],[5,6,11,12,17,18],
#               [1,2,9,10,17,18],[3,4,11,12,13,14],[5,6,7,8,15,16],
#               [3,4,7,8,17,18],[5,6,9,10,13,14],[1,2,11,12,15,16]]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#=================================================================
#Original = [19] 

#[19] + 6
#for w in range( length5*2 ): 
#for descend_cycle in range(up_remove_count, 2, -6): #每一回圈取一組六個數的list
#target_remove_count = descend_cycle
#select_counter = random.randint(-5,4)  #單一演算法會有僵固性，故選擇多種方法，可有較好突破?
# remove Combination_List_6element if dick[i] == 0
#xy (XYZ太難)
#XYZ_RETRY_TIME_give_up_bet_number_CONSTANT = 10000

#cycle_times =  750
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
#for w in range( length5*2 ): 
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

#>>>>>>> success mapped_list [[6, 7, 9, 10, 14, 25], [10, 24, 25, 28, 38, 48], [2, 14, 18, 28, 38, 48], [1, 9, 23, 38, 41, 48], [1, 6, 7, 17, 25, 28]
#                           , [1, 11, 14, 23, 34, 38], [2, 9, 11, 25, 40, 48], [1, 2, 14, 24, 40, 41], [2, 6, 23, 28, 34, 40], [2, 7, 10, 14, 17, 48]
#                           , [6, 10, 11, 17, 23, 41], [1, 7, 18, 23, 38, 40], [6, 17, 18, 25, 41, 48], [6, 11, 17, 18, 24, 28], [9, 17, 24, 34, 38, 40]
#                           , [1, 2, 10, 18, 25, 34], [7, 11, 24, 34, 41, 48], [9, 11, 14, 18, 34, 41], [1, 9, 10, 11, 28, 40], [2, 7, 9, 23, 24, 28]
#                           , [10, 14, 18, 23, 24, 25], [2, 7, 10, 17, 18, 38]]
#Answer number =  [1, 2, 6, 7, 9, 10, 11, 14, 17, 18, 23, 24, 25, 28, 34, 38, 40, 41, 48]

#>>>>>>> success mapped_list [[15, 16, 17, 18, 24, 34], [18, 33, 34, 39, 43, 49], [7, 24, 28, 39, 43, 49], [1, 17, 30, 43, 47, 49], [1, 15, 16, 26, 34, 39]
#                             , [1, 19, 24, 30, 42, 43], [7, 17, 19, 34, 45, 49], [1, 7, 24, 33, 45, 47], [7, 15, 30, 39, 42, 45], [7, 16, 18, 24, 26, 49]
#                             , [15, 18, 19, 26, 30, 47], [1, 16, 28, 30, 43, 45], [15, 26, 28, 34, 47, 49], [15, 19, 26, 28, 33, 39], [17, 26, 33, 42, 43, 45]
#                             , [1, 7, 18, 28, 34, 42], [16, 19, 33, 42, 47, 49], [17, 19, 24, 28, 42, 47], [1, 17, 18, 19, 39, 45], [7, 16, 17, 30, 33, 39]
#                             , [18, 24, 28, 30, 33, 34], [7, 16, 18, 26, 28, 43]]
#Answer number =  [1, 7, 15, 16, 17, 18, 19, 24, 26, 28, 30, 33, 34, 39, 42, 43, 45, 47, 49]


#>>>>>>> success mapped_list 
# [[9, 11, 12, 16, 23, 33], [16, 30, 33, 35, 38, 48], [7, 23, 28, 35, 38, 48], [4, 12, 29, 38, 41, 48], [4, 9, 11, 27, 33, 35]
# , [4, 20, 23, 29, 37, 38], [7, 12, 20, 33, 40, 48], [4, 7, 23, 30, 40, 41], [7, 9, 29, 35, 37, 40], [7, 11, 16, 23, 27, 48]
# , [9, 16, 20, 27, 29, 41], [4, 11, 28, 29, 38, 40], [9, 27, 28, 33, 41, 48], [9, 20, 27, 28, 30, 35], [12, 27, 30, 37, 38, 40]
# , [4, 7, 16, 28, 33, 37], [11, 20, 30, 37, 41, 48], [12, 20, 23, 28, 37, 41], [4, 12, 16, 20, 35, 40], [7, 11, 12, 29, 30, 35]
# , [16, 23, 28, 29, 30, 33], [7, 11, 16, 27, 28, 38]]
#Answer number =  [4, 7, 9, 11, 12, 16, 20, 23, 27, 28, 29, 30, 33, 35, 37, 38, 40, 41, 48]




#=================================================================
#Original = [20] 
if (bet_number == 20):
#[20] + 3
# [[1,2,3],[4,5,6],[7,8,9],
#  [1,4,7],[2,5,8],[3,6,9],
#  [1,5,9],[2,6,7],[3,4,8],
#  [2,4,9],[3,5,7],[1,6,8],

#  [1,4,10],[2,5,10],[3,6,10],
#  [4,7,10],[5,8,10],[6,9,10],
#  [1,7,10],[2,8,10],[3,9,10]]
      
    return_list = [
                [1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],
                [1,2,7,8,13,14],[3,4,9,10,15,16],[5,6,11,12,17,18],
                [1,2,9,10,17,18],[3,4,11,12,13,14],[5,6,7,8,15,16],
                [3,4,7,8,17,18],[5,6,9,10,13,14],[1,2,11,12,15,16],

               [1,2,7,8,19,20],[3,4,9,10,19,20],[5,6,11,12,19,20],
               [7,8,13,14,19,20],[9,10,15,16,19,20],[11,12,17,18,19,20],
               [1,2,13,14,19,20],[3,4,15,16,19,20],[5,6,17,18,19,20]]




  
#=================================================================
#Original = [21] 
if (bet_number == 21):
    return_list = [
    [1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],
    
    [1,2,9,10,17,18],[7,8,15,16,23,24],[5,6,13,14,21,22],[3,4,11,12,19,20],
    [1,2,17,18,21,22],[3,4,7,8,23,24],[5,6,9,10,13,14],[11,12,15,16,19,20],
    
    [1,2,11,12,15,16],[7,8,17,18,21,22],[3,4,13,14,23,24],[5,6,9,10,19,20],
    [5,6,7,8,15,16],[11,12,13,14,21,22],[3,4,17,18,19,20],[1,2,9,10,23,24],

    [1,2,7,8,13,14],[3,4,9,10,15,16],[5,6,11,12,17,18],
    [1,2,7,8,19,20],[3,4,9,10,21,22],[5,6,11,12,23,24],
    [7,8,13,14,19,20],[9,10,15,16,21,22],[11,12,17,18,23,24],
    [1,2,13,14,19,20],[3,4,15,16,21,22],[5,6,17,18,23,24]]

#=================================================================
#Original = [22] 
if (bet_number == 22):
#[22] + n
# [[1,2,3],[4,5,6],[7,8,9],[10,11,12]

#  [1,5,9],[4,8,12],[3,7,11],[2,6,10]
#  [1,9,11],[2,4,12],[3,5,7],[6,8,10]

#  [1,6,8],[4,9,11],[2,7,12],[3,5,10]
#  [3,4,8],[6,7,11],[2,9,10],[1,5,12]

#  [1,4,7],[2,5,8],[3,6,9],
#  [1,4,10],[2,5,11],[3,6,12],
#  [4,7,10],[5,8,11],[6,9,12],
#  [1,7,10],[2,8,11],[3,9,12]]
      
    return_list =  [
        [1, 2, 9, 10, 15, 16], [5, 6, 11, 12, 17, 18], [5, 6, 7, 8, 13, 14], [15, 16, 19, 20, 21, 22], [3, 4, 7, 8, 19, 20], 
        [3, 4, 5, 6, 21, 22], [1, 2, 3, 4, 13, 14], [7, 8, 11, 12, 17, 18], [9, 10, 17, 18, 21, 22], [3, 4, 11, 12, 15, 16], 
        [5, 6, 9, 10, 13, 14], [1, 2, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [1, 2, 17, 18, 21, 22], [7, 8, 9, 10, 11, 12], 
        [11, 12, 13, 14, 21, 22], [5, 6, 15, 16, 19, 20], [3, 4, 9, 10, 19, 20], [7, 8, 9, 10, 15, 16], [1, 2, 7, 8, 11, 12], 
        [3, 4, 11, 12, 19, 20], [1, 2, 7, 8, 19, 20], [3, 4, 5, 6, 9, 10], [1, 2, 3, 4, 17, 18], [11, 12, 13, 14, 15, 16], 
        [1, 2, 3, 4, 15, 16], [7, 8, 13, 14, 21, 22], [1, 2, 19, 20, 21, 22], [9, 10, 13, 14, 17, 18], [1, 2, 7, 8, 9, 10], 
        [5, 6, 15, 16, 21, 22], [5, 6, 9, 10, 17, 18], [5, 6, 7, 8, 21, 22], [3, 4, 17, 18, 21, 22], [1, 2, 13, 14, 19, 20], 
        [3, 4, 9, 10, 13, 14], [5, 6, 15, 16, 17, 18], [5, 6, 19, 20, 21, 22], [11, 12, 17, 18, 19, 20], [3, 4, 5, 6, 13, 14]]
    
    return_list =  [
        [5, 6, 9, 10, 17, 18], [11, 12, 15, 16, 19, 20], [3, 4, 7, 8, 13, 14], [1, 2, 5, 6, 21, 22], [1, 2, 17, 18, 19, 20], 
        [7, 8, 11, 12, 21, 22], [3, 4, 9, 10, 15, 16], [13, 14, 19, 20, 21, 22], [9, 10, 11, 12, 13, 14], [5, 6, 7, 8, 15, 16], 
        [3, 4, 17, 18, 21, 22], [1, 2, 3, 4, 11, 12], [1, 2, 7, 8, 9, 10], [3, 4, 5, 6, 19, 20], [1, 2, 13, 14, 15, 16], 
        [7, 8, 15, 16, 17, 18], [5, 6, 11, 12, 17, 18], [9, 10, 19, 20, 21, 22], [13, 14, 17, 18, 21, 22], [7, 8, 9, 10, 19, 20], 
        [3, 4, 5, 6, 13, 14], [5, 6, 7, 8, 13, 14], [9, 10, 11, 12, 21, 22], [3, 4, 15, 16, 21, 22], [13, 14, 17, 18, 19, 20], 
        [1, 2, 7, 8, 19, 20], [3, 4, 11, 12, 17, 18], [5, 6, 9, 10, 19, 20], [15, 16, 17, 18, 21, 22], [1, 2, 3, 4, 9, 10], 
        [3, 4, 5, 6, 17, 18], [5, 6, 7, 8, 9, 10], [1, 2, 11, 12, 13, 14], [9, 10, 13, 14, 21, 22], [9, 10, 11, 12, 15, 16], 
        [5, 6, 7, 8, 21, 22], [5, 6, 11, 12, 13, 14]]
    
    return_list =  [
        [3, 4, 5, 6, 15, 16], [7, 8, 9, 10, 19, 20], [13, 14, 17, 18, 21, 22], [1, 2, 3, 4, 11, 12], [1, 2, 15, 16, 19, 20], 
        [5, 6, 9, 10, 21, 22], [7, 8, 11, 12, 13, 14], [9, 10, 15, 16, 17, 18], [1, 2, 5, 6, 17, 18], [11, 12, 17, 18, 19, 20], 
        [7, 8, 15, 16, 21, 22], [3, 4, 13, 14, 19, 20], [5, 6, 9, 10, 13, 14], [3, 4, 7, 8, 21, 22], [1, 2, 9, 10, 21, 22], 
        [5, 6, 11, 12, 19, 20], [11, 12, 13, 14, 15, 16], [3, 4, 9, 10, 17, 18], [1, 2, 5, 6, 7, 8], [1, 2, 7, 8, 17, 18], 
        [3, 4, 9, 10, 15, 16], [5, 6, 13, 14, 21, 22], [5, 6, 17, 18, 19, 20], [3, 4, 15, 16, 17, 18], [11, 12, 19, 20, 21, 22], 
        [5, 6, 11, 12, 15, 16], [7, 8, 13, 14, 15, 16], [1, 2, 9, 10, 13, 14], [3, 4, 5, 6, 17, 18], [7, 8, 9, 10, 11, 12], 
        [1, 2, 3, 4, 19, 20], [11, 12, 17, 18, 21, 22], [3, 4, 15, 16, 19, 20], [3, 4, 11, 12, 13, 14], [1, 2, 13, 14, 21, 22], 
        [9, 10, 13, 14, 15, 16], [15, 16, 19, 20, 21, 22]]

#=================================================================

#Original = [24] 
if (bet_number == 24):
#[22] + n
# [[1,2,3],[4,5,6],[7,8,9],[10,11,12]

#  [1,5,9],[4,8,12],[3,7,11],[2,6,10]
#  [1,9,11],[2,4,12],[3,5,7],[6,8,10]

###############################################  [1,6,8],[4,9,11],[2,7,12],[3,5,10]
#  [1,6,11],[2,4,9],[5,7,12],[3,8,10]
###############################################  [3,4,8],[6,7,11],[2,9,10],[1,5,12]
#  [3,4,11],[2,6,7],[5,9,10],[1,8,12]


#  [1,4,7],[2,5,8],[3,6,9],
#  [1,4,10],[2,5,11],[3,6,12],
#  [4,7,10],[5,8,11],[6,9,12],
#  [1,7,10],[2,8,11],[3,9,12]]
      
    return_list = [
    [1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],
    
    [1,2,9,10,17,18],[7,8,15,16,23,24],[5,6,13,14,21,22],[3,4,11,12,19,20],
    [1,2,17,18,21,22],[3,4,7,8,23,24],[5,6,9,10,13,14],[11,12,15,16,19,20],
    
    [1,2,11,12,21,22],[3,4,7,8,17,18],[9,10,13,14,23,24],[5,6,15,16,19,20],
    [5,6,7,8,21,22],[3,4,11,12,13,14],[9,10,17,18,19,20],[1,2,15,16,23,24],

    [1,2,7,8,13,14],[3,4,9,10,15,16],[5,6,11,12,17,18],
    [1,2,7,8,19,20],[3,4,9,10,21,22],[5,6,11,12,23,24],
    [7,8,13,14,19,20],[9,10,15,16,21,22],[11,12,17,18,23,24],
    [1,2,13,14,19,20],[3,4,15,16,21,22],[5,6,17,18,23,24]]

#=================================================================



cpus = os.cpu_count()
cpus = 1



dict = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0}
trial_dict =            {12:2, 13:5, 14:5, 15:8, 16:8, 17:11, 18:12, 19:15, 20:18, 21:21, 22:22, 23:26, 24:30}
max_remove_count_dict = {12:135, 13:155, 14:175, 15:195, 16:215, 17:235, 18:255, 19:275, 20:295,21:300}
min_remove_count_dict = {12:13,  13:4,   14:4,   15:4,   16:4,   17:4,   18:4, 19:4,  20:4, 21:0}
combination_size_dict = {12:495, 13:715, 14:1001, 15:1365, 16:1820, 17:2380, 18:3060, 19:3876, 20:4845, 21:0}
min_ending_section = 18


def check_delete_all( target_list ):
    Original = []
    remove_count = 0
    for i in range(bet_number):
        Original.append(i+1)
    Combination_List_5element = list(combinations(Original ,5))
    print("len Combination_List_5element = ", len(Combination_List_5element))
    for x in target_list:
        three = list(combinations(x ,3))
        for c in three:
            dup_Combination_List_5element = copy.deepcopy(Combination_List_5element)
            for d5 in dup_Combination_List_5element:
                if set(c) <= set(d5):
                    Combination_List_5element.remove(d5)
                    remove_count = remove_count + 1
    print("remove_count", remove_count)
    print("Combination_List_5element = ", Combination_List_5element)
    if (len(Combination_List_5element) == 0):
        return True
    else:
        return False

def result_check_delete_all( target_list, original_number ):

    remove_count = 0
    Original = original_number
    
    Combination_List_5element = list(combinations(Original ,5))
    print("len Combination_List_5element", len(Combination_List_5element))
    for x in target_list:
        three = list(combinations(x ,3))
        for c in three:
            dup_Combination_List_5element = copy.deepcopy(Combination_List_5element)
            for d5 in dup_Combination_List_5element:
                if set(c) <= set(d5):
                    Combination_List_5element.remove(d5)
                    remove_count = remove_count + 1
    print("remove_count", remove_count)
    print("Combination_List_5element", len(Combination_List_5element))
    if (len(Combination_List_5element) == 0):
        return True
    else:
        return False

def section_matching_function( index_start ):
    #stop_others = False
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    Original = []
    for i in range(bet_number):
        Original.append(i+1)
    #print("Original : ", Original)
    try_set_number = trial_dict[bet_number]
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

def generate_original_number(bet_number, exclusive):


    try_set_number = 0

    Original = []
    for i in range(bet_number):
        Original.append(i+1)
    print("Original : ", Original)
    try_set_number = trial_dict[bet_number]
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

    generate_number7 = bet_number - len(inclusive)
    #digit_limit = [10,10,10,10,10] #0,1,2,3,4
    digit_available = digit_limit
    print("digit_limit" , digit_limit )

    for i in range(5):
        digit_available[i] = digit_limit[i] - digit_used[i]
    print("digit_available" , digit_available )

    print("generate_number7" , generate_number7 )
    Appear3 = inclusive

    while len(Appear3) < bet_number:  
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
    random.shuffle(Appear3)
    random.shuffle(Appear3)
    #Appear3 = [1,2,3,4,5,6,7,8]
    print( Appear3)
    print("=====generate_original_number===============================================")            
    print("")       

    return Appear3

# end of generate_original_number
#P===========================================================



if __name__=='__main__':
    
    original_number =  []
    original_number = generate_original_number(bet_number, exclusive)  


    #cpus = os.cpu_count()
    #cpus = 1
    print("cpus :", cpus)
    #pool = Process.Pool(4)
    print('main parent process:', os.getppid())
    print('main process id:', os.getpid())
    #return_list = []
    mapped_list = []
    pool = mp.Pool(cpus)

    random.shuffle(return_list)
    random.shuffle(return_list)
    if (check_delete_all(return_list) == True):
        print("check_delete_all = True")
    else:
        print("check_delete_all = False")
    print("")
    #print(">>>>>>> success return_list", return_list )      
    #       

    mapped_list = mapper(len(return_list), original_number, return_list)

    for i in mapped_list:
        i.sort()

    if (result_check_delete_all(mapped_list, original_number) == True):
        print("result_check_delete_all = True")
    else:
        print("result_check_delete_all = False")

    print("=============================================")
    print(">>>>>>> success mapped_list", mapped_list )
    #print(len(mapped_list))
    L = len(mapped_list)
    Y = L*50
    original_number.sort()
    print("Answer number = ", original_number)
    print()
    print("大樂透中5保3 :", bet_number, "個號碼，" , Y, "元", "4期共", Y*4, "元" )
    print("===========================================")
