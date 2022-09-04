def linear_search_dictionary(dic, target):
    for x,y in dic.items():
        if target==y:
            print("Found at key",x)
            return x
        
    print("Target is not in Dictionary") 
    
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)