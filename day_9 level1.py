#prac-1
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('sleep'))
print(add_string('amazing'))
print(add_string('is'))

#PF-Prac-2
def bracket_pattern(input_str):
    length=len(input_str)
    if(length%2!=0):
        return False
    elif input_str[0]==')' or input_str[-1:]=='(':
        return False
    else:
        return True

print(bracket_pattern(')()((()())'))
print(bracket_pattern('()((())())'))

#PF-prac-3

def create_new_dictionary(prices):
    new_dict={}
    for key in prices:
        if(prices[key]>200):
            new_dict.__setitem__(key, prices[key])
     return new_dict
prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))

#PF-Prac-4
def find_nine(nums):
   for i in range(0,len(nums)):
        if(nums[i]==9 and i<4):
            return True
        return False
nums=[1,9,4,5,6]
print(find_nine(nums))

#PF-Prac-6
def list123(nums):
    nums=""
    for i in nums:
        nums+=str(i)
    if "123" in nums:
        return True
    else:
        return False
nums=[1,2,3,4,5]
print(list123(nums))

#PF-Prac-7
def seed_no(number,ref_no):
    t=number
    while(number!=0):
        rem=number%10
        t=t*rem
        number=number//10
    if(t==ref_no):
        return True
    else:
        return False
number=123
ref_no=738
print(seed_no(number,ref_no))


#PF-Prac-9
def generate_dict(number):
    new_dict={}
    for i in range(1,number+1):
        new_dict[i]=i**2
    return new_dict

number=20
print(generate_dict(number))

#PF-Prac-10
def string_both_ends(input_string):
    length=len(input_string)
    if(length<2):
        return -1
    else:
        str=" "
        str=input_string[0:2]+input_string[-2:]
        return str

input_string="w3w"
print(string_both_ends(input_string))

#PF-Prac-11
def find_upper_and_lower(sentence):
    upper=0
    lower=0
    for i in sentence:
        if(i>="a" and i<="z"):
            lower+=1
        if(i>="A" and i<="Z"):
            upper+=1
        result_list=[]
        result_list.append(upper)
        result_list.append(lower)
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))

#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    for i in subjects:
        for j in verbs:
            for k in verbs:
                sentence_list.append(i+" "+j+" "+k)

    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))


#PF-Tryout 14
def find_five_digit():
    num2=0
    num3=0
    num4=0
    num5=0
    for i in range(9,-1,-1):
        num2=int(i-2)
        num3=int(num2-2)
        num4=int(num3-2)
        num5=int(num3)
        if(num3+num4+num5==i and num2+num3+num4+num5+i==19):
            break
    s=str(i)+str(num2)+str(num3)+str(num4)+str(num5)
    print(s)

find_five_digit()

#PF-Prac-15
def check_22(num_list):
    for i in range(0,len(num_list)-1):
        if(num_list[i]==2 and num_list[i+1]==2):
            return True
         else:
            return False
        
print(check_22([3,2,5,1,2,1,2,2]))


#PF-Tryout 22
def diagonal_stars(number):
    for i in range (0,number):
        for j in range(i):
            print(".",end=" ")
        print("*")
 

number=5    
diagonal_stars(number)


#PF-Prac-23
def divisible_by_sum(number):
    temp=number
    sum=0
    while(number>0):
        rem=number%10
        number=number//10
        sum=sum+rem
    if(temp%sum==0):
        return True
    else:
        return False
number=42
print(divisible_by_sum(number))
