word = input()

a1 = word.count('A') + word.count('B') + word.count('C')
a2 = word.count('D') + word.count('E') + word.count('F')
a3 = word.count('G') + word.count('H') + word.count('I')
a4 = word.count('J') + word.count('K') + word.count('L')
a5 = word.count('M') + word.count('N') + word.count('O')
a6 = word.count('P') + word.count('Q') + word.count('R')
a7 = word.count('S') + word.count('T') + word.count('U')
a8 = word.count('V') + word.count('W') + word.count('X')
a9 = word.count('Y') + word.count('Z')

print(a1+2*a2+3*a3+a4*4+a5*5+a6*6+a7*7+a8*8+a9*9)