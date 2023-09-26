'''Implement a class called player that represent a cricket player. The player class should have and
method called play() which prints" The player is playing cricket. derive two classes, batsman and
bowler, from the player class. override the play() method in each derive class to print "the batsman
is batting"and " the bowler is bowling", respectively. write a program to create objects of both The
batsman and bowler classes and call the play () method for each object. '''


#Define the base class player
class player:
  def play(self):
    print ("The player is playing cricket. ")

#Define the driver class batsman
class batsman(player):
￼  def play(self):
     print (" The batsman is batting. ")

#Define the derived class bowler
class bowler (player):
  def play(self):
￼    print (" The bowler is bowling. ")

#create objects of batsman and bowler classes
batsman=batsman()
bowler=bowler()

#call the play() method for each objects
batsman.play()
bowler. play()
