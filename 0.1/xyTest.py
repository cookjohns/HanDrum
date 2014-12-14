#!/usr/bin/env python


from touch import *
import os.path, sys
import pygame.mixer, pygame.time
mixer = pygame.mixer
time = pygame.time
import event


main_dir = os.path.split(os.path.abspath(__file__))[0]


def main(file_path=None):

    if file_path is None:
        file_path = os.path.join(main_dir,
                                 'beep.wav')
        
        mixer.init(frequency=22050, size=-16, channels=8, buffer=512) #sets buffer lower than default for
                                                                      #rhythmic accuracy

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
                
 
                if len(bList) == 1:

                    file_path = os.path.join(main_dir,
                                 'beep.wav')
                    sound = mixer.Sound(file_path)
                    reserved_channel_0.play(sound)


                if len(bList) == 2:

                    reserved_channel_1 = mixer.Channel(1)

                    reserved_channel_0.stop()             #Stopping the channels correlated to sounds
                                                          #triggered a lower bList value assures that
                    file_path = os.path.join(main_dir,    #only the sound for the maximum number of 
                                 'blip1.wav')             #fiducials in contact will sound.
                    sound = mixer.Sound(file_path)
                    reserved_channel_1.play(sound)


                if len(bList) == 3:

                    reserved_channel_2 = mixer.Channel(2)

                    reserved_channel_1.stop()

                    file_path = os.path.join(main_dir,
                                 'squiggle.wav')
                    sound = mixer.Sound(file_path)
                    reserved_channel_2.play(sound)


                if len(bList) == 4:

                    reserved_channel_3 = mixer.Channel(3)

                    reserved_channel_2.stop()

                    file_path = os.path.join(main_dir,
                                 'scratch.wav')
                    sound = mixer.Sound(file_path)
                    reserved_channel_3.play(sound)

                    
                if len(bList) == 5: #5 or more; 4 finger slap will also trigger due to 5+ points of contact

                    reserved_channel_4 = mixer.Channel(4)

                    reserved_channel_3.stop()

                    file_path = os.path.join(main_dir,
                                 'buzz.wav')
                    sound = mixer.Sound(file_path)
                    reserved_channel_4.play(sound)


class touch_up(Observer):
	def TOUCH_UP(self,blobID, xpos, ypos):

		global bList
		bList.remove(t.blobs[blobID]) #adds -1 to bList for each fiducial removed from the surface                    
                   
                                       
#class touch_move(Observer):               Not currently needed.
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


