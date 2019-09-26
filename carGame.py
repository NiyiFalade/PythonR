message = ""
car_Started = False
while True:
    message = input("> ").lower()
    if message == 'help':
      print('''
start - to start 
stop - to stop car
quit - to exit
    ''')
    elif message == 'start':
        if car_Started:
            print("car already started")
        else:
            print('car started')
            car_Started = True;
    elif message == 'quit':
        print('quit program')
    else:
        print("dont understand")




