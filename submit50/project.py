import os

def main():
   quit = False
   while not quit:
        results = []
        print('Simple Calculator in Python!')
        print('Enter \'a\' for addition')
        print('Enter \'s\' for substraction')
        print('Enter \'m\' for multiplication')
        print('Enter \'d\' for division')
        print('Enter \'q\' to quit')

        choice = input('Selection: ')

        if choice == 'q':
           quit = True
           continue

        num_1 = float(input('Enter a number: '))
        num_2 = float(input('Enter another number: '))
        if choice == 'a':
            results = addition(num_1 , num_2)
            results=continue_add(results)
            print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 's':
           results = subtraction(num_1,num_2)
           results=continue_sub(results)
           print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 'm':
           results = multiplication(num_1,num_2)
           results=continue_mult(results)
           print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 'd':
           results = division(num_1,num_2)
           results=continue_div(results)
           print('Ans = ', results[0], ' total inputs: ', results[1])
        else:
           print('Sorry, invalid character')

def addition(num_1 : float,num_2: float):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')

    ans = num_1 + num_2
    print(f'Current result: {ans}')
    return ans

def continue_add(ans):
    continue_calc = 'y'
    values_entered = 2

    while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       ans += num
       print(f'Current result: {ans}')
       values_entered += 1
    return [ans, values_entered]

def subtraction(num_1:float,num_2:float):
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Subtraction')
   ans = num_1 - num_2
   print(f'Current result: {ans}')
   return ans

def continue_sub(ans):
   values_entered = 2
   continue_calc = 'y'
   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       ans -= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]

def multiplication(num_1:float,num_2:float):
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Multiplication')
   ans = num_1 * num_2
   print(f'Current result: {ans}')
   return ans

def continue_mult(ans):
   continue_calc = 'y'
   values_entered = 2
   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       ans *= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]

def division(num_1:float,num_2:float):
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Division')
   while num_2 == 0.0:
       print('Please enter a second number > 0')
       num_2 = float(input('Enter another number: '))

   ans = num_1 / num_2
   print(f'Current result: {ans}')
   return ans

def continue_div(ans):
   continue_calc = 'y'
   values_entered = 2
   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       while num == 0.0:
           print('Please enter a number > 0')
           num = float(input('Enter another number: '))
       ans /= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]


if __name__=="__main__":
    main()