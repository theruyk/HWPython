# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 4. Выход по требованию пользователя

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных


def all_contacts():
  with open ('phone_number.txt', 'r', encoding='utf8') as data:
    for line in data:
      print (line)

# all contacts ( )
def find_contact(name):
  with open ('phone_number.txt', 'r', encoding='utf8') as data:
    for line in data:
      if name in line:
        print(line)

def add_contact (new_contact):
  with open ('phone_number.txt', 'a', encoding='utf8') as data:
    data.write('\n'+ new_contact)

def del_contact(name):
  with open ('phone_number.txt', 'r', encoding='utf8') as data:  
      list1 = data.readlines()
      list1 = [line.rstrip('\n') for line in list1]
      for i in list1: 
        if name in list1:
          list1.remove(name)
  with open ('phone_number.txt', 'w', encoding='utf8') as data:
    for i in list1:
      data.write(i + '\n')
    data.close()

def replace_nata(name):
  del_contact(name)
  with open ('phone_number.txt', 'a', encoding='utf8') as data:
    data.write(input ('Введите новый контакт: ')) 

def main_menu (numb):
  if numb == 1:
    all_contacts ()
  elif numb == 2:
    name = input ('Введите искомое имя: ')
    find_contact (name)
  elif numb == 3:
    data = input ('Введите новый контакт: ')
    add_contact (data)
  elif numb == 4:
    data = input ('Введите Имя Фамилию и телефон чтобы удалить контакт: ')
    del_contact (data)
  elif numb == 5:
    name = input ('Введите Имя Фамилию и телефон чтобы перезаписать контакт: ')
    replace_nata(name)
while True:
  numb = int(input('Введите 1 - для печати всего справочника; 2 - для поиска контакта;''3 - для записи контакта; 4 - для удаления контакта; 5 - для перезаписи контакта; 6 - для выхода из программы: '))
  if numb == 6:
    break 
  main_menu (numb)

# Иван Попов +7345543534
# Ирина Крылова +75347892906
# Александр Карякин +7208053502
# Даниил Горинов +7038459935
# Владимир Овчинников +734095830945
