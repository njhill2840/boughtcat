# Quick module to print lyrics to a repetitive song without redundant calls/typing


# set each verse to print when function is called
def get_verse_1():
    print('Bought me a cat and the cat pleased me,')
    print('I fed my cat under yonder tree.')


def get_verse_2():
    print('Bought me a hen and the hen pleased me,')
    print('I fed my hen under yonder tree.')


def get_verse_3():
    print('Bought me a duck and the duck pleased me,')
    print('I fed my duck under yonder tree.')


def get_verse_4():
    print('Bought me a goose and the goose pleased me,')
    print('I fed my goose under yonder tree.')


def get_verse_5():
    print('Bought me a sheep and the sheep pleased me,')
    print('I fed my sheep under yonder tree.')


def get_verse_6():
    print('Bought me a pig and the pig pleased me,')
    print('I fed my pig under yonder tree.')


# creating each animal sound to print when called, add blank line to separate verses
def get_cat_sound():
    print('Cat goes fiddle-i-fee.')
    print()


def get_hen_sound():
    print('Hen goes chimmy-chuck, chimmy-chuck,')
    get_cat_sound()


def get_duck_sound():
    print('Duck goes quack, quack,')
    get_hen_sound()


def get_goose_sound():
    print('Goose goes hissy, hissy,')
    get_duck_sound()


def get_sheep_sound():
    print('Sheep goes baa, baa,')
    get_goose_sound()


def get_pig_sound():
    print('Pig goes oink, oink,')
    get_sheep_sound()


def main():
    get_verse_1()
    get_cat_sound()
    get_verse_2()
    get_hen_sound()
    get_verse_3()
    get_duck_sound()
    get_verse_4()
    get_goose_sound()
    get_verse_5()
    get_sheep_sound()
    get_verse_6()
    get_pig_sound()


if __name__ == '__main__':
    main()



