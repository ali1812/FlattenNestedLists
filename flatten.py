#!/usr/bin/env python
# Copyright (c) 2106 Ali Al-Habsi

def flattenArray(nestedArray):
    newflatArray = []
    def loop(nestedIndex):
        for i in nestedIndex:
            if(isinstance(i,(list,tuple))):
                #loop through the nested index until it's no longer nested.
                loop(i)
            else:
                newflatArray.append(i)
    loop(nestedArray)
    return newflatArray            

#Test 
test = [1,2,[3],[[4]], [[[5]]]]
print flattenArray(test)

           

   
