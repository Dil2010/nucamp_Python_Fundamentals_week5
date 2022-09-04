import random

def guess_random_number(tries, start,stop):
    rand_num=random.randint(start,stop)
    while tries!=0:
        print("Number of tries left:",tries)        
        guess_str=input("Guess a number between "+str(start)+" and "+ str(stop)+":")
        guess_int=int(guess_str)
        if guess_int>stop:
            print("The number you have entered higher than upper bound")
            guess_str=input("Guess a number between "+str(start)+" and "+ str(stop)+":")
            guess_int=int(guess_str)
        elif guess_int<start:
            print("The number you have entered lower than lower bound")
            guess_str=input("Guess a number between "+str(start)+" and "+ str(stop)+":")
            guess_int=int(guess_str)
        else:
            if guess_int==rand_num:
                print("You guessed the correct number")
                return
            elif guess_int>rand_num:
                print("Guess higher")
            elif guess_int<rand_num:
                print("Guess lower")
            tries=tries-1

guess_random_number(5,1,10)

def guess_random_num_linear(tries, start,stop):
    rand_num1=random.randint(start,stop)
    print("The number for the program to guess is:",str(rand_num1))
    # print("Number of tries left",tries)
    for x in range(tries):
        rand_num2=random.randint(start,stop)
        if rand_num2==rand_num1:
            print("The program is guessing...",str(rand_num2))
            print("The program has guessed the correct number!")
            return
        else:
            tries_left=tries-x
            print("Number of tries left",tries_left)
            print("The program is guessing...",str(rand_num2))
    print("The program has failed to guess the correct number!")

# guess_random_num_linear(10,0,10)

def guess_random_num_binary(tries, start,stop):
    rand_num=random.randint(start,stop)
    print("The number for the program to guess is:",str(rand_num))    
    while start<=stop:
        guess=(start+stop)//2        

        if guess==rand_num:
            print("Found it",str(guess))
            return 
        if guess>rand_num:
            stop=guess-1
            print("Guessing higher",str(guess))            
        else:
            start=guess+1
            print("Guessing lower",str(guess))  
        
        tries =tries-1
        if tries==0:
            print("Your failed to find")
            return 

# guess_random_num_binary(10,0,100)
