# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.






if __name__ == '__main__':
    ###############################
    my_list = [1,2000,3000,4,5]
    for num in my_list:
        if num > 100:
            print(num)
    ###############################
    my_result = []
    for num in my_list:
        if num > 100:
            my_result.append(num)
    print(my_result)
    ###############################
    if len(my_list) < 2 :
        my_list.append(0)
    elif len(my_list) >= 2:
        my_list.append(my_list[len(my_list)-2]+my_list[len(my_list)-1])
    print(my_list)
    ###############################
    my_string1 = '0123456789'
    my_List = []
    for symbol in my_string1 :
        for num in my_List:
            num = int(symbol)
            num.append(my_List)
    print(my_List)







