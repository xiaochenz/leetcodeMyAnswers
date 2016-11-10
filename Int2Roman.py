def intToRoman(num):
    if num == None:
        return None
    if num == 0:
        return ''
    first_digit = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
    second_digit = {1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
    third_digit = {1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}
    romanStr = ''
    #-------------------------find the part over 1000, [1000,3999]
    q = num/1000
    num = num%1000
    if q > 0:
        for i in range(q):
            romanStr += 'M'
    #-------------------------find the part in [100,1000)
    q = num/100
    num = num%100
    if q > 0:
        romanStr += third_digit[q]
    #------------------------find the part in [10,100)
    q = num/10
    num = num%10
    if q > 0:
        romanStr += second_digit[q]
    #------------------------find the part in [1,10)
    q = num
    if q > 0:
        romanStr += first_digit[q]
    return romanStr

test1 = 1
test2 = 1234
test3 = 3999
test4 = 1954
test5 = 1990
test6 = 2014
print intToRoman(test1),intToRoman(test2),intToRoman(test3),intToRoman(test4),intToRoman(test5),intToRoman(test6)