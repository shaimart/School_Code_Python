def sortNumbers(data:list[int], condition:str) -> list[int]:
    
    if condition == "ASC":
        for j in range(len(data)):
            for i in range(len(data)-1 -j):   
                if data[i] > data[i+1]:
                    data[i],data[i+1]=data[i+1],data[i]
    
    elif condition == "DESC":
            for j in range(len(data)):
                for i in range(len(data)-1 -j):   
                    if data[i] < data[i+1]:
                        data[i],data[i+1]=data[i+1],data[i]
    return data

                
       


    

def sortData(weights:list[int], data:list[int], condition:str) -> list[int]:
    
    if len(weights) == len(data):
        if condition == "ASC":
            for j in range(len(weights)):
                for i in range(len(weights)-1 -j):   
                    if weights[i] > weights[i+1]:
                        weights[i],weights[i+1]=weights[i+1],weights[i]
                        data[i],data[i+1]=data[i+1],data[i]
    
        elif condition == "DESC":
                for j in range(len(weights)):
                    for i in range(len(weights)-1 -j):   
                        if weights[i] < weights[i+1]:
                            weights[i],weights[i+1]=weights[i+1],weights[i]
                            data[i],data[i+1]=data[i+1],data[i]
    else: raise ValueError('Invalid input data')
    return data

