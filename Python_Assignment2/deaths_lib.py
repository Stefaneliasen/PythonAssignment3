import numpy as np

def cutArray(arrayOfLines, year, cause):
    lineArrayof2016 = []
# If 2016 is in the line. We add it to a new array. We make sure we use the first four places in the strings of line
    for line in arrayOfLines:
        if year not in line[0:4]:
            continue
        else:
            if cause not in line:
                continue
            else:
                # Get all states and append them to a new array
                lineArrayof2016.append(line.split(',')[-3: -1])
    return lineArrayof2016

def countDeaths(arrayOfLines, year, cause, prio=None):

    lineArrayof2016 = cutArray(arrayOfLines, year, cause)
    lineArrayOfAllDeathsCount = []
    for line in lineArrayof2016:
        lineArrayOfAllDeathsCount.append(int(line[1]))
    
    if prio == "Lowest":
        for line in lineArrayof2016:
            if int(line[1]) == min(lineArrayOfAllDeathsCount):
                result = line
    elif prio == "All":
        return lineArrayof2016
    else:
        lineArrayOfAllDeathsCount.remove(max(lineArrayOfAllDeathsCount))
        for line in lineArrayof2016:
            if int(line[1]) == max(lineArrayOfAllDeathsCount):
                 result = line
    return result

def countList(list1999, list2016):
    counter = 0
    listOfIncrease = []

    # Get all percentages
    for line in list1999:
        percentage = (int(list2016[counter][1]) - int(line[1])) / int(line[1]) * 100
        listOfIncrease.append({"state": line[0], "percentage": percentage})
        counter += 1
    
    listOfPositiveIncrease = []

    # Get all positive percentages
    for lineObject in listOfIncrease:
        if lineObject['percentage'] > 0:
            listOfPositiveIncrease.append(lineObject)
        else:
            continue
    
    listOfAllIncreases = []

    # Validate between min and all objects
    for line in listOfPositiveIncrease:
        listOfAllIncreases.append(line['percentage'])
    
    for lineObject in listOfIncrease:
        if lineObject['percentage'] == min(listOfAllIncreases):
            result = lineObject['state'] + ": " + str(lineObject['percentage'])
    print(result)

