class Song(object):
    """This class print Jaadu teri nazar song."""

    def __init__(self):
        self.lyrics = ["Jaadu teri nazar."]

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def __str__(self):
        return "KKKKKiiiiirrrraaaaaannnn."


happy_bday = Song()
happy_bday.sidef hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    binx = bin(x)[2:]
    biny = bin(y)[2:]
    smaller = min(binx, biny)

    hamming_distance = 0
    for i in range(len(smaller)):
        if binx[-(i + 1)] == biny[-(i + 1)]:
            hamming_distance += 1
    return hamming_distanceng_me_a_song()
print(help(Song))
