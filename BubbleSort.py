#SOPHIA INTRO TO CS MODULE 8 ASSIGNMENT 2
numbers = ''
sort_list = []
def bubble(sort_list):
    counter = 0
    list = sort_list
    #bubble sorting
    for i in range(0, len(list)-1):
        for j in range(0,len(list)-1-i):
            if list[j]>list[j+1]:
                #a counter on how many passes
                counter = counter + 1
                list[j],list[j+1]=list[j+1],list[j]
                print('Pass',counter,':', list)
    print('Original List: ',sort_list)
    print("Sorted List: ", list)
    print("Number of Passes: ",counter)

#loops until the user finishes placing numbers
while numbers != 'n':
    #input of the numbers
    numbers = input("type a number. if finished type 'n': ")

    #if the input are numbers turn them into int
    #put them into a list so the bubble sort can sort them
    if numbers.isnumeric():
        numbers = int(numbers)
        sort_list.append(numbers)
        print('numbers so far: ',sort_list,'\n')

    #if its not a number or 'n'
    else: 
        if numbers.lower() == 'n':
            bubble(sort_list)
        else:
            print('numbers only')
