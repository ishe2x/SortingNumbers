import time
import random

def listNumbers(size):
    original = []
    for value in range(size):
        original.append(value)
    random.shuffle(original)
    return original

def listNumTemp(original):
    temp = []
    for value in range(len(original)):
        temp.append(original[value])
    return temp 

def bubbleSort(alist):
    cbs = 0
    ebs = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            cbs += 1
            if alist[i] > alist[i+1]:
                ebs += 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    print("\nNumber of comaparisons for bubble sort: "+"{:,}".format(cbs))
    print("Number of exchanges for bubble sort: "+"{:,}".format(ebs))

def selectionSort(alist):
    css2 = 0
    ess2 = 0
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            css2 += 1
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        ess2 += 1
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    print("\nNumber of comaparisons for selection sort: "+"{:,}".format(css2))
    print("Number of exchanges for selection sort: "+"{:,}".format(ess2))

def insertionSort(alist):
    cis3 = 0
    eis3 = 0
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentValue:
            cis3 += 1
            alist[position] = alist[position - 1]
            position = position - 1
        eis3 += 1
        alist[position] = currentValue
    print("\nNumber of comaparisons for insertion sort: "+"{:,}".format(cis3))
    print("Number of exchanges for insertion sort: "+"{:,}".format(eis3))
            
def shellSort(alist):
    csh4 = 0
    esh4 = 0
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            csh4, esh4 = gapInsertionSort(alist, startPosition, sublistCount,
                                          csh4, esh4)
            sublistCount = sublistCount // 2
    print("\nNumber of comaparisons for shell sort: "+"{:,}".format(csh4))
    print("Number of exchanges for shell sort: "+"{:,}".format(esh4))
            
def gapInsertionSort(alist, start, gap, csh4, esh4):
    for i in range(gap, len(alist), start + gap):
        currentValue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentValue:
            csh4 += 1
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentValue
        esh4 += 1
    return csh4, esh4

def main():
    ####### FOR LIST SIZE 100 #######
    print("For list size 100: ")
    original = listNumbers(100)
    
    temp = listNumTemp(original)
    start = time.time()
    bubbleSort(temp)
    end = time.time()
    
    temp = listNumTemp(original)
    start_2 = time.time()
    selectionSort(temp)
    end_2 = time.time()

    temp = listNumTemp(original)
    start_3 = time.time()
    insertionSort(temp)
    end_3 = time.time()

    temp = listNumTemp(original)
    start_4 = time.time()
    shellSort(temp)
    end_4 = time.time()
        
    print("\nThe bubble sort took:", end - start, "seconds.")
    print("The selection sort took:", end_2 - start_2, "seconds.")
    print("The insertion sort took:", end_3 - start_3, "seconds.")
    print("The shell sort took:", end_4 - start_4, "seconds.")

    ####### FOR LIST SIZE 1,000 #######
    print("\nFor list size 1,000: ")
    original = listNumbers(1000)
        
    temp = listNumTemp(original)
    start1 = time.time()
    bubbleSort(temp)
    end1 = time.time()
        
    temp = listNumTemp(original)
    start_21 = time.time()
    selectionSort(temp)
    end_21 = time.time()
        
    temp = listNumTemp(original)
    start_31 = time.time()
    insertionSort(temp)
    end_31 = time.time()

    temp = listNumTemp(original)
    start_41 = time.time()
    shellSort(temp)
    end_41 = time.time()
        
    print("\nThe bubble sort took:", end1 - start1, "seconds.")
    print("The selection sort took:", end_21 - start_21, "seconds.")
    print("The insertion sort took:", end_31 - start_31, "seconds.")
    print("The shell sort took:", end_41 - start_41, "seconds.")

      #######  FOR LIST SIZE 10,000 #######
    print("\nFor list size 10,000: ")
    original = listNumbers(10000)
        
    temp = listNumTemp(original)
    start2 = time.time()
    bubbleSort(temp)
    end2 = time.time()
        
    temp = listNumTemp(original)
    start_22 = time.time()
    selectionSort(temp)
    end_22 = time.time()
        
    temp = listNumTemp(original)
    start_32 = time.time()
    insertionSort(temp)
    end_32 = time.time()

    temp = listNumTemp(original)
    start_42 = time.time()
    shellSort(temp)
    end_42 = time.time()
        
    print("\nThe bubble sort took:", end2 - start2, "seconds.")
    print("The selection sort took:", end_22 - start_22, "seconds.")
    print("The insertion sort took:", end_32 - start_32, "seconds.")
    print("The shell sort took:", end_42 - start_42, "seconds.")
        
main()
