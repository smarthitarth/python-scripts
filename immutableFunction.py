"""Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)

Inputs

- Original list of strings

- List of strings to be added

- List of strings to be removed

Return

- List shall only contain unique values

- List shall be ordered as follows

--- Most character count to least character count

--- In the event of a tie, reverse alphabetical

Other Notes

- You can use any programming language you like

- The function you submit shall be runnable

For example:

Original List = ['one', 'two', 'three',]

Add List = ['one', 'two', 'five', 'six]

Delete List = ['two', 'five']

Result List = ['three', 'six', 'one']*"""
import numpy as np
def function(main_list,add_list,remove_list):
    new_main_list = main_list.copy()
    for a in add_list:
        new_main_list.append(a)
    #print(new_main_list)
    for b in remove_list:
         new_main_list = [value for value in new_main_list if value != b]
    #print(new_main_list)
    new_main_list = np.unique(new_main_list)
    sortList(new_main_list)
    return new_main_list
    
    
def sortList(lis):
    for i in range(len(lis)-1):
        for j in range(i+1, len(lis)):
            if(len(lis[i])<len(lis[j])):
                lis[i], lis[j] = lis[j], lis[i]
            elif(len(lis[i])==len(lis[j])):  
                if(lis[i]<lis[j]):
                    lis[i], lis[j] = lis[j], lis[i]

if __name__ == "__main__":
    main_list = ['one', 'two', 'three']
    add_list = ['one', 'two', 'five', 'six']
    remove_list = ['two','five']
    print(function(main_list, add_list, remove_list))
    

            
            
