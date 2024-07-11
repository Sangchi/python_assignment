# def febonacci(n):
#     if n in[0,1]:
#         return n
#     else:
#         return febonacci(n-1)+febonacci(n-2)
# print(febonacci(6))


# def factorial(n):
#     if n in [0,1]:
#      return n
#     else:
#         return n*factorial(n-1)
# print(factorial(4))
         

        # how to find the sum of a possitive intiger number using recursion?

# def sum_positive_num(n):
    # assert n>=0 and int(n)==n,'the sum of possitive intiger!'
    # if n ==0:
    #   return 0
    # else:
    #   return int(n%10)+sum_positive_num(int(n/10))
# print(sum_positive_num(10))


#find the power of the possitive number
# def power(x,n): # x is base and n is exponent(x*xn-1)
    # if n==0:
        # return 1
    # if n==1:
        # return x
    # return x * power(x,n-1)
# print(power(2,4))

# find greatest common divider
# def gcd(a,b):            #eclerian role ( gcd(a,0) and gcd (b,a%b))
    # if b==0:
        # return a
    # else:
        # return gcd(b,a%b)
# print(gcd(48,18))


#  how to convert a number from decimal to binary number
# def binary(n):
    # if n==0:               #f(n)=n%2+10*f(n/2)
        # return 1
    # else:
        # return  int(n%2) +10*binary(int(n/2))
# print(binary(100))


# def febonacci(n):
    # if n in [0,1]:
        # return n
    # else:
        # return febonacci(n-1)+febonacci(n-2)
# print(febonacci(8))


# find recursive range


# def recursive(num):
    # if num<=0:
        # return 0
    # else:
        #  return num + recursive(num-1)
# print(recursive(5))

# def palindrome(num):
    # if len(num)==0:
    #    return True
    # if num[0]!=num[len(num)-1]:
        # return False
    # return palindrome(num[1:-1])




    
