#CONDITIONAL STATEMENTS IN PYTHON
msg='New line'
print(msg)

def control_flow(value):
    if value :
        print('yep!')
    else:
        print('Nope!!')  
        
def age_value():
    age=20
    if age < 3:
        person="BABY"
    elif age > 4 :
        person='TODDLER'  
    elif age < 13:
        person="PRE-TEEN"
    else :
        age >18
        person="Adult"     
age_value()


control_flow(False)
print(msg)
control_flow(True)
print(msg)
control_flow(0)
print(msg)
control_flow('0')
  
#SYNTAX FOR IF/ELSE STATEMENT IN PYTHON


dog ='Cuddly'
if dog =='hungry':
    owner='Refill food bowl'
elif dog =='thirsty':
    owner='thirsty' 
elif dog=='playful':
    owner='Play again'   
else:
    owner='Reading newspaper'    
print(dog)       
print(owner) 

      
age = 4
if age < 2:
    is_baby= 'baby'
else:
    is_baby='not a baby'    
print(is_baby)  
Tal ={}
print(Tal)  

age=9
is_baby='baby' if age < 2 else 'not a babe'
print(is_baby)

# TRY/EXCEPT STATEMENTS
def divide(num1,num2):
    try:
        quotient=num1 /num2
        print(quotient)
    except:
        print("ERROR")
divide(10,0)


def divide(num1,num2):
    try:
        quotient= num1/num2
        print(quotient)
        
    except ZeroDivisionError:
        print('Error: num2 cannot be equal to 0' )
    except TypeError:
        print('Error:input must be of type int or float')
    finally:
        print('Division possible')
divide(40,0) 



def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
hows_the_weather(75)