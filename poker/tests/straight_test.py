import pokerhand as ph
import playingcards as pc

a = ['AH', 'KS', 'QH', 'JH', 'TH']
#b = [pc.Card(name) for name in a]
c = ph.Hand()
c.add(*a)
print c
print "c.ranks", c.ranks
print "c.is_straight():", c.is_straight()
