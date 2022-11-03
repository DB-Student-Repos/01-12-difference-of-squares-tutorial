def square_of_sum(number):
    x= (number*(number+1))/2
    return x*x
    


def sum_of_squares(number):
    x= (number*(number+1)*(2*number+1))/6
    return x
    


def difference_of_squares(number):
    x= (square_of_sum(number)-sum_of_squares(number))
    return x
    
