def binary_search(number, lo, hi):
    trial = 1

if __name__ == "__main__":
lo = 1
hi = 100
number = int(input('what number is in your mind?'))

result, trial = binary_search(number, lo, hi)
    while(lo<=hi):

     guess = int((hi+lo)/2)
     if guess == number:
        return(guess, trial)
     elif (guess < number):
        lo=guess+1
     else:
        hi=guess-1
        trial=trial+1  
    return (-1, trial)  #that's how many times


    if result == -1:
        print('congrats! Your number is',(guess), " , I have used",(trial),"times to get it.")



