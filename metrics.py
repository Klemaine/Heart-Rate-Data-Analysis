def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    
    
    average = 0
    total = 0
    count = 0

    for num in data:
        total += num
        count += 1
    if count == 0:
        return []

    average = total / count

            
        
    return (round(average, 2))
    ...


def maximum(data: list) -> float:
    """
    This code reads the list and determines the maximum number in the list

    Args:
        data: list, a list of characters

    Returns
        float: the maximum float in the list
    
    """
    if not data:
        return []
    maximum = 0
    for number in data:
        if number > maximum:
            maximum = number
        
    return float(maximum)






def variance(data: list) -> float:
    """
    This code calculates the population variance of the data.

    Args:
        Data:list, a list of numbers

    Returns
        float: the population variance of the data rounded to 2 decimal points
    
    (calculate population variance)
    """
    mean = sum(data) / len(data)
    total = 0
    for num in data:
        total += (num - mean) ** 2
    var_a = total / len(data)
    return round(var_a, 2)

#result = variance
#print (result)

    #for variance in data:
     #   variance **= 
    


def standard_deviation(data: list) -> float:
    """
    This code calculates the popular standard deviation of the data

    Args:
        data:list, a list of values
    Returns
        float: the popular standard deviation of the data rounded to 2 decimal points

    (calculate population standard deviation)
    """
    if not data:
        return []
    return round(variance(data)**.5,2)
        
    

#result = standard_deviation
#print (result)
