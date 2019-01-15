


def diamond(n):
    lower_space = ''
    top_space =  '' 
    parameter = n    
    lower_pyramid = ''
    top_pyramid = ''
    
   
    for z in range(1,n,2):
        for q in range(1,parameter,2):
            top_space += ' '

        parameter-=2 
        top_pyramid += '{}{}\n'.format(top_space , '*'*z )
        top_space = ''

    for p in range(n,0,-2):
        if p == n :
            lower_pyramid = '{}\n'.format('*'*p )
        else:
            lower_space += ' '
            
            lower_pyramid += '{}{}\n'.format(lower_space , '*'*p )
           

    diamante = top_pyramid + lower_pyramid

    return None if  n < 0 or n % 2 == 0 else diamante


print(diamond(1))
print(diamond(0))
print(diamond(5))
print(diamond(15))
print(diamond(26))