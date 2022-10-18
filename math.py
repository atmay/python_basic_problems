# Дано натуральное число. Выведите его последнюю цифру.

def get_last_number(number):
  ...

# Дано натуральное число. Найдите число десятков в его десятичной записи.

def get_dec(number):
  ...
  
if __name__ == '__main__':
  test_data = [128, 32, 57, 93]
  for data in test_data:
    print(f'Последняя цифра {data} - {get_last_number(data)}') 
    print(f'Число десятков в {data} - {get_dec(data)}') 
    
    
