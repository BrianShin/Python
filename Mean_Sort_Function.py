#SOPHIA INTRO TO CS MODULE 7 ASSIGNMENT 2
numbers = [3,9,7,4,0,2]

def Sort_and_Mean(list):
    #calculates mean
    mean =(list[0]+list[1]+list[2]+list[3]+list[4]+list[5])/6
    print("mean of the numbers: ", mean)

    #bubble sorting
    for i in range (0, len(list)-1):
        for j in range(0,len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j] 
    print("sorted numbers: ", list)

#this prints out the sorted numbers and mean
Sort_and_Mean(numbers)



