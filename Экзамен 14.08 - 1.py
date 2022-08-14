def kartochka(object):
    return '*' * (len(object)-4) + object[-4:]



def main():
    print(kartochka('4250458748578745'))

main()
