def palindrom(object):
    object = object.replace(' ','').lower()
    if object == object[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'


def main():

    print("!!!ПАЛИДРОМАЙЗЕР!!!")
    while True:
        word = input("Введите слово: ")
        print(palindrom(word))
        


main()
