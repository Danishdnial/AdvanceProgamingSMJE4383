a= input('How many inches of rain have fallen:')
b= float(a)
c= int(b)
volume1= (b/12)*43560
gallons1= volume1 * 7.48051945
volume2= (c/12)*43560
gallons2= volume2 * 7.48051945
print(a,'in float rain on 1 acre is',gallons1 , "gallons")
print(a,'in integer rain on 1 acre is',gallons2 , "gallons")