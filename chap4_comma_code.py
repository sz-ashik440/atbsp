def commaToString(arr):
    str = arr[0]
    for i in range(1, len(arr)):
        if i == len(arr)-1:
            str = str + ' and ' + arr[i]
        else:
            str = str + ', ' + arr[i]
        
    return str

spam = ['apple' , 'bannanas', 'tofu', 'cats']
print(commaToString(spam))
