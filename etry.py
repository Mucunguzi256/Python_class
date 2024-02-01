while True:
    try:
        age = int(input('What is your age?'))
        print(age)
    except:
        print('Please enter a whole number')
    else:
        print('Thank you')
        break
