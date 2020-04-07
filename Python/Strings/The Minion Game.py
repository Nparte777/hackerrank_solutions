def minion_game(s):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    ln = len(s)
    '''ln-1 is used instead of game rules because if for examlpe if BANANA and s[0]=consonant then:
    BANANA
    and following sequences are valid:
    BANAN
    BANA
    BAN
    BA
    B
    which is n-1
    Hence for B kevin score (6-0) ~ (ln - i) as given in code below'''
    for i in range(ln):
        if s[i] in vowels:
            kevsc += (ln-i)
        else:
            stusc += (ln-i)

    if kevsc > stusc:
        print ("Kevin "+str(kevsc))
    elif kevsc < stusc:
        print ("Stuart "+str(stusc))
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
