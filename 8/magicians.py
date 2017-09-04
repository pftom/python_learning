def show_magicians(magicians_list):
    """8-9 show all the magicians"""
    for magician in magicians_list:
        print(magician)


magicians = ['huangdaxia', 'tom', 'pftom']
show_magicians(magicians)


def make_great(magicians_list):
    """8-10 add 'great' word in the magician name"""
    a = 0
    for magician in magicians_list:
        magicians_list[a] = "The Great " + magician
        a += 1


# make_great(magicians)
# show_magicians(magicians)

make_great(magicians[:])
show_magicians(magicians)

make_great(magicians)
show_magicians(magicians)
