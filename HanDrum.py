#!/usr/bin/env python

# 
# HanDrum is an electronic hand drum for use with a TUIO
# compatible physical interface. It is intended to reproduce
# the natural playing characteristics of an acoustic
# drum such as a conga or djembe.
#
# @author John Cook
# @version 0.3
#

from touch import *
import os.path, sys
import pygame.mixer, pygame.time
import event

mixer = pygame.mixer
time = pygame.time

main_dir = os.path.split(os.path.abspath(__file__))[0]

def main(file_path=None):

   if file_path is None:
      file_path = os.path.join(main_dir,
                      'beep.wav')
      mixer.init(frequency=22050, size=-16, channels=8, buffer=512) # sets buffer lower than default for
                                                                    # rhythmic accuracy

if __name__ == '__main__':
   if len(sys.argv) > 1:
      main(sys.argv[1])
   else:
      main()

class Observer(object):
   def __init__(self, subject):
      subject.push_handlers(self)

class touch_down(Observer):
   def TOUCH_DOWN(self,blobID):
      x = t.blobs[blobID].xpos
      y = t.blobs[blobID].ypos
      print 'TOUCH LOCATION: ' +str(x) + ',' +str(y)
       
      global bList
      bList.append(t.blobs[blobID]) #adds +1 to bList for each fiducial added to the surface
      mixer.set_reserved(5)                   #reserves channels 0-5 so that each sound can be 
      reserved_channel_0 = mixer.Channel(0)   #assigned to a specific channel
      reserved_channel_1 = mixer.Channel(1)
      reserved_channel_2 = mixer.Channel(2)
      reserved_channel_3 = mixer.Channel(3)
       
      if len(bList) == 1 and 0.4 < x < 0.6 and 0.4 < y < 0.6:
         file_path = os.path.join(main_dir,
                    'CenterOne.wav')       #Placeholder sound recording; "Center One"
         sound = mixer.Sound(file_path)
         reserved_channel_0.play(sound)
         print 'CENTER ZONE ONE BLOB'
      
      elif len(bList) == 1 and 0.35 < x < 0.65 and 0.35 < y < 0.65:
         file_path = os.path.join(main_dir,
                    'ThreeOne.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_0.play(sound)
         print 'ZONE THREE ONE BLOB'
      
      elif len(bList) == 1 and 0.15 < x < 0.75 and 0.15 < y < 0.75:
      
         file_path = os.path.join(main_dir,
                    'TwoOne.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_0.play(sound)
         print 'ZONE TWO ONE BLOB'
      
      elif len(bList) == 1 and 0 < x < 1 and 0 < y < 1:
         file_path = os.path.join(main_dir,
                    'OneOne.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_0.play(sound)
         print 'ZONE ONE ONE BLOB'
   
      if len(bList) == 2 and 0.4 < x < 0.6 and 0.4 < y < 0.6:
         reserved_channel_1 = mixer.Channel(1)
         reserved_channel_0.stop()             #Stopping the channels correlated to sounds
                                               #triggered a lower bList value assures that
         file_path = os.path.join(main_dir,    #only the sound for the maximum number of 
                    'CenterTwo.wav')           #fiducials in contact will sound.
         sound = mixer.Sound(file_path)
         reserved_channel_1.play(sound)
         print 'CENTER ZONE TWO BLOBS'
      
      elif len(bList) == 2 and 0.35 < x < 0.65 and 0.35 < y < 0.65:
         reserved_channel_1 = mixer.Channel(1)
         reserved_channel_0.stop()                                                 
         file_path = os.path.join(main_dir,     
                    'ThreeTwo.wav')             
         sound = mixer.Sound(file_path)
         reserved_channel_1.play(sound)
         print 'ZONE THREE TWO BLOBS'
      
      elif len(bList) == 2 and 0.15 < x < 0.75 and 0.15 < y < 0.75:
         reserved_channel_1 = mixer.Channel(1)
         reserved_channel_0.stop()                                                   
         file_path = os.path.join(main_dir,     
                    'TwoTwo.wav')             
         sound = mixer.Sound(file_path)
         reserved_channel_1.play(sound)
         print 'ZONE TWO TWO BLOBS'
      
      elif len(bList) == 2 and 0 < x < 1 and 0 < y < 1:
         reserved_channel_1 = mixer.Channel(1)
         reserved_channel_0.stop()                                                   
         file_path = os.path.join(main_dir,     
                    'OneTwo.wav')             
         sound = mixer.Sound(file_path)
         reserved_channel_1.play(sound)
         print 'ZONE ONE TWO BLOBS'
   
      if len(bList) == 3 and 0.4 < x < 0.6 and 0.4 < y < 0.6:
         reserved_channel_2 = mixer.Channel(2)
         reserved_channel_1.stop()
         file_path = os.path.join(main_dir,
                    'CenterThree.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_2.play(sound)
         print 'CENTER ZONE THREE BLOBS'
      
      elif len(bList) == 3 and 0.35 < x < 0.65 and 0.35 < y < 0.65:
         reserved_channel_2 = mixer.Channel(2)
         reserved_channel_1.stop()
         file_path = os.path.join(main_dir,
                    'ThreeThree.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_2.play(sound)
         print 'ZONE THREE THREE BLOBS'
      
      elif len(bList) == 3 and 0.15 < x < 0.75 and 0.15 < y < 0.75:
         reserved_channel_2 = mixer.Channel(2)
         reserved_channel_1.stop()
         file_path = os.path.join(main_dir,
                    'TwoThree.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_2.play(sound)
         print 'ZONE TWO THREE BLOBS'
      
      elif len(bList) == 3 and 0 < x < 1 and 0 < y < 1: #Rimshot
         reserved_channel_2 = mixer.Channel(2)
         reserved_channel_1.stop()
         file_path = os.path.join(main_dir,
                    'Shot.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_2.play(sound)
         print 'Rimshot'
   
      if len(bList) == 4 and 0.4 < x < 0.6 and 0.4 < y < 0.6:
         reserved_channel_3 = mixer.Channel(3)
         reserved_channel_2.stop()
         file_path = os.path.join(main_dir,
                    'CenterFour.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_3.play(sound)
         print 'CENTER ZONE FOUR BLOBS'
      
      elif len(bList) == 4 and 0.35 < x < 0.65 and 0.35 < y < 0.65:
         reserved_channel_3 = mixer.Channel(3)
         reserved_channel_2.stop()
         file_path = os.path.join(main_dir,
                    'ThreeFour.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_3.play(sound)
         print 'ZONE THREE FOUR BLOBS'
      
      elif len(bList) == 4 and 0.15 < x < 0.75 and 0.15 < y < 0.75:
         reserved_channel_3 = mixer.Channel(3)
         reserved_channel_2.stop()
         file_path = os.path.join(main_dir,
                    'TwoFour.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_3.play(sound)
         print 'ZONE TWO FOUR BLOBS'
      
      elif len(bList) == 4 and 0 < x < 1 and 0 < y < 1: #Rimshot
         reserved_channel_3 = mixer.Channel(3)
         reserved_channel_2.stop()
         file_path = os.path.join(main_dir,
                    'Shot.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_3.play(sound)
         print 'Rimshot'
           
      if len(bList) == 5 and 0.4 < x < 0.6 and 0.4 < y < 0.6: #5 or more; 4 finger slap will also trigger due to 5+ points of contact
                                                              #5 or more anywhere on surface plays slap.wav, but prints zone location
         reserved_channel_4 = mixer.Channel(4)               
         reserved_channel_3.stop()
         file_path = os.path.join(main_dir,
                    'Slap.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_4.play(sound)
         print 'CENTER ZONE FIVE OR MORE BLOBS'
      
      elif len(bList) == 5 and 0.35 < x < 0.65 and 0.35 < y < 0.65:
         reserved_channel_4 = mixer.Channel(4)
         reserved_channel_3.stop()
         file_path = os.path.join(main_dir,
                    'Slap.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_4.play(sound)
         print 'ZONE THREE FIVE OR MORE BLOBS'
      
      elif len(bList) == 5 and 0.15 < x < 0.75 and 0.15 < y < 0.75:
         reserved_channel_4 = mixer.Channel(4)
         reserved_channel_3.stop()
         file_path = os.path.join(main_dir,
                    'Slap.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_4.play(sound)
         print 'ZONE TWO FIVE OR MORE BLOBS'
      
      elif len(bList) == 5 and 0 < x < 1 and 0 < y < 1:
         reserved_channel_4 = mixer.Channel(4)
         reserved_channel_3.stop()
         file_path = os.path.join(main_dir,
                    'Slap.wav')
         sound = mixer.Sound(file_path)
         reserved_channel_4.play(sound)
         print 'ZONE ONE OR MORE BLOBS'


class touch_up(Observer):
   def TOUCH_UP(self,blobID, xpos, ypos):
      global bList
      bList.remove(t.blobs[blobID]) #adds -1 to bList for each fiducial removed from the surface                    
                                          
#class touch_move(Observer):         <-- Not currently needed.
#def TOUCH_MOVE(self,blobID):
       #print 'Move'

t = touchpy()
tu = touch_up(t)
td = touch_down(t)
#tm = touch_move(t)      Not currently needed, see above
bList = [] #stores number of fiducials currently in contact with the surface

try:
   while True:
      t.update() #keeps pytouch constantly looking for blobs
	
except (KeyboardInterrupt, SystemExit):
   del t
