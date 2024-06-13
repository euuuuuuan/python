input_id = input('id: ')
id = 'egoing'
input_password = input('password: ')
password = '111111'
if input_id == id:
    if input_password == password:
        print("Welcome")
    else:
        print("Wrong Password")
else:
    print("Wrong Id")

# Logical operator (논리 연산자)
    #if input_id == 'egoing' and input_password == '111111':
    #   print('Welcome')

    #if input_id == 'egoing' or input_id == 'basta':
    #   print("Welcome")
