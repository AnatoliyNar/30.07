def datatime(date):
    a = date.replace('','')
    print(a[2:4],'.',a[0:2],'.',a[4:], sep="")


def file(**data):
    f = open ('C:/Users/Anatoliy/Desktop/file.txt', 'a')
    for key, value in data.items():
        f.write('{}:{}\n'.format(key, value))
    f.close()



def balance_p(spisok,balance):
    for el in spisok:
        if el > 0:
            balance +=el
            print(balance)
        elif el < 0:
            balance_n
    return balance

    
def balance_n(el,balance):
    for el in spisok:
        if el < 0:
            balance +=(el)**2
            
    
                
    


def main():
    while True:
        choice = int(input('1.Конвертер введённой даты в американский вариант.\n2.Файл с данными.\n3.Баланс.\n4.Выход из программы.\n---------------------------->'))
    
        if choice == 1:

            date = input('Введите дату(дд/мм/год):')
            datatime(date)

        elif choice == 2:

            second_name = input('Введите фамилию: ')
            name = input('Введите имя: ')
            imya_po_batky = input('Введите отчество: ')
            profession = input('Введите профессию: ')
            file(Фамилия = second_name, Имя = name, Отчество = imya_po_batky, Профессия = profession)

        elif choice == 3:

            spisok = [2,5,-12]
            balance = 0
            balance_p(spisok,balance)

        elif choice == 4:
            print('Завершение работы.')
            break
        else:
            print('Нет такого пункта в меню.')
            continue 
            
        
    


main()







