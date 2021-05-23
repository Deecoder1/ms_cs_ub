def zeropad(padded_string, numzeros, leftpointer=True):
    '''Function for padding the number with zeros'''
    try:
        i = 0
        while i < numzeros:
            i = i+1
            if leftpointer == True:
                padded_string= '0'+padded_string
            else:
                padded_string=padded_string+'0'
        return padded_string
    except Exception as e:
        return (e)
            
def karatsuba_multiplication(integer_1,integer_2):
    '''Function that computes the karatsuba multiplication recursively'''
    try:
        integer_1, integer_2=str(integer_1), str(integer_2)
        if len(integer_1)==1 and len(integer_2)==1:
            return int(integer_1)*int(integer_2)
        if len(integer_2)<len(integer_1):
            integer_2=zeropad(integer_2,len(integer_1)-len(integer_2))
        elif len(integer_1)<len(integer_2):
            integer_1=zeropad(integer_1,len(integer_2)-len(integer_1))
    
        length=len(integer_1)
        l=length//2
        if length%2!=0:
            l = l+1
        p, q, r, s = int(integer_1[:l]), int(integer_1[l:]),int(integer_2[:l]), int(integer_2[l:])
        '''We use the same function to calculate the individual products'''
        pr = karatsuba_multiplication(p, r)
        qs = karatsuba_multiplication(q, s)
        k = karatsuba_multiplication(p + q, r + s)
        A = int(zeropad(str(pr), (length-l)*2, False))
        B = int(zeropad(str(k - pr - qs), (length-l), False))
        return A + B + qs
    except Exception as e:
        return (e)

integer_1 = input()
integer_2 = input()
print(karatsuba_multiplication(integer_1,integer_2))