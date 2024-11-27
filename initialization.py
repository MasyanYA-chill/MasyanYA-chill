# for test you can use test base
#  user_pass = {'Log In': 'password', Max123': '123456'}
# ///////////////////////////////////////////////////////




import time

# user_base is a file with logins and Passwords
from users_base import user_pass



mode = 'out'


print('Hi! Put here your Log In name')
while mode == 'out':
    inputed_username = input('=> ')
    if inputed_username in user_pass:
        while mode == 'out':
            print('Nice! Let you put here your password')
            print('You have 5 attempts')
            attempts = 5
            while attempts > 0 and mode == 'out':
                inputed_pass = input('=> ')
                check_pass = user_pass.get(inputed_username)
                if inputed_pass == check_pass:
                    print(f'Welcome, {inputed_username}!')
                    mode = 'in'
                else: 
                    print('Wrong Log In or pass')
                attempts -= 1
                
            
            if mode != 'in':
                print('Available to system is blocked for 1 minute')
                time.sleep(60)
    else:
        print('You have no profile in this system')





