
"""
Created on Fri Jul 17 16:59:51 2020

@author: Leonardo Bonetti, Francesco Carlomagno

leonardo.bonetti@clin.au.dk

"""

#To use this script please do the following:
#-place the provided stimuli folders in your favorite directory
#-assign to the variable 'stimidr' (few lines below) such directory
#-define your log directory
#Please note that the csv file with the crucial stimuli presentation IDs and 
# behavioural responses is created within the log directory
 

#################### YOUR DIRECTORY TO BE UPDATED BEFORE RUNNING THE SCRIPT ####################
#THIS IS YOUR DIRECTORY WHERE YOU PUT THE PROVIDED FOLDERS, PLEASE UPDATE THIS, THANKS
logdir = ('C:/Users/au571303/Documents/projects/memory_music_iEEG/logs') 
stimdir = ('C:/Users/au571303/Documents/projects/memory_music_iEEG/stimuli')
#################### Load libraries and set directories ####################
from random import shuffle
from psychopy import prefs
#prefs.hardware['audioLib'] = ['pyo']
prefs.hardware['audioLib'] = ['PTB']
from psychopy import visual, core, sound, event, gui, monitors, logging
import itertools as it
import os
import numpy as np

#monitor settings
#mon = monitors.Monitor('SonyG55')#fetch the most recent calib for this monitor
#mon.setDistance(50)#further away than normal?
#win = visual.Window(size=[1920,1080], monitor=mon)

#################### Actual codes ####################

##TEST

# quit key
def quitpd():
    if logfile:
       logfile.close()
    core.quit()
event.globalKeys.add(key='escape',func=quitpd,name='shutdown')

#GUI for subject ID
ID = gui.Dlg(title = 'subj ID')
ID.addField('ID: ')
subID = ID.show()

#create csv file for log
filename = logdir + '/' + subID[0] + '_learning_bach_iEEG_custom.csv'
logfile = open(filename,'w')
logfile.write("subj;trial;response;RT;time \n")

#create log file
block_time = core.Clock()
logging.setDefaultClock(block_time)
filename2 = logdir + '/' + subID[0] + '_learning_bach_iEEG_default.log'
lastLog = logging.LogFile(filename2, level=logging.INFO, filemode='a')

#getting file for learning phase
os.chdir(stimdir + '/learningdef')
Bachminor = sound.Sound('Bachminorprelude.wav')

#getting files for recognition phase
os.chdir(stimdir + '/recogdef')
pathwave = stimdir + '/recogdef'
wavefilesd = []
wavenamesd = []
for file in sorted(os.listdir(pathwave)):
    if file.endswith(".wav"):
        wavenamesd.append(file)
        wavefilesd.append(sound.Sound(file))

#reproducing several times (here 7 times) the 3 Old excerpts
wnd = wavenamesd[21:] #extracting Old excerpts
wnd = wnd * 7 #multiplying them by 7
wfd = wavefilesd[21:]
wfd = wfd * 7
wavenames = wavenamesd[0:21] + wnd #getting the final list name
wavefiles = wavefilesd[0:21] + wfd #getting the final list files
wavezip = list(zip(wavenames,wavefiles))
shuffle(wavezip)

#initializing RT variable to get RTs
RT = core.Clock()
block_time = core.Clock() #this should not be useful anymore..

#this is a bit redundant.. anyway..
SPAAAAACE = 'space'

#preparing window for the screen
color_txt = 'white'
win = visual.Window(fullscr = True, color = 'black')#[.9,.9,.9])
pd = visual.TextStim(win,text = 'First, you will listen to a complete musical piece '
                                '(Learning phase). \n\n Please try to remember it as ' 
                                'much as possible. \n\n Second, you will listen to 42 '
                                'short musical excerpts (Recognition phase). \n\n For '
                                'each of them you will be asked to indicate whether '
                                'they were extracted from the musical piece of the '
                                'learning phase or not. \n\n Press space to continue',
                                color = color_txt, height = 0.1)
instr = visual.TextStim(win,text = 'Learning phase \n\n Now you are going to listen '
                                   'to a complete musical piece \n\n Please try to '
                                   'remember it as much as possible \n\n Press space '
                                   'to continue',color = color_txt)
instrrec = visual.TextStim(win,text = 'recognition part..',color = color_txt)
fix_c = visual.TextStim(win,text = '+', color = color_txt,height = 0.2)
block_time.reset() #this should not be useful anymore..

#actual experiment (learning phase)
pd.draw()
win.flip()
event.waitKeys(keyList = [SPAAAAACE])
instr.draw()
win.flip()
event.waitKeys(keyList = [SPAAAAACE])
ttime = block_time.getTime() #this should not be useful anymore..
#playing the whole musical piece 2 times
for ll in range(2):
    dumm = 'Repetition ' + str(ll+1) + '\n Press space to continue'
    playlear = visual.TextStim(win,text = dumm, color = color_txt)
    playlear.draw()
    win.flip()
    event.waitKeys(keyList = [SPAAAAACE])
    fix_c.draw()
    win.flip()
    core.wait(0.5)
    Bachminor.play() #open again this line later
    event.clearEvents(eventType='keyboard')
    core.wait(26) #open again this line later

#actual experiment (recognition phase)
playrec = visual.TextStim(win,text = 'Recognition phase \n\n Now you are going to '
                                     'listen to 42 short musical excerpts. \n\n For '
                                     'each of them please indicate with the keyboard '
                                     'whether they were extracted from the musical '
                                     'piece that you have just listened to (press 1) '
                                     'or not (press 2). \n\n Press space to continue',
                                     color = color_txt)
playrec.draw()
win.flip()
event.waitKeys(keyList = [SPAAAAACE])
#over musical excerpts (trials)
for wavve in range(len(wavefiles)):
    #displaying the progressive trial number for participants' comfort
    jes = 'trial number ' + str((wavve + 1)) + ' / ' + str(len(wavefiles))
    instrrectr = visual.TextStim(win,text = jes,color = color_txt)
    instrrectr.draw()
    win.flip()
    core.wait(1)
    fix_c.draw()
    win.flip()
    core.wait(0.5)
    ttime = block_time.getTime() #this should not be useful anymore..
    wavezip[wavve][1].play()
    event.clearEvents(eventType='keyboard')
    RT.reset()
    resp = None
    while resp == None:
        key = event.getKeys(keyList = ['1','2'])
        if len(key) > 0:
            rt = RT.getTime()
            resp = key[0][0]
        elif RT.getTime() > 3: #3 seconds of maximum wait if subject does not reply
            resp = 0
            rt = RT.getTime()
    core.wait(1)
    #writing RT, trial ID, subject's response
    lrow = '{};{};{};{};{} \n'
    lrow = lrow.format(subID[0],wavezip[wavve][0], resp, round(rt*1000),str(ttime))
    logfile.write(lrow)

logging.flush()
logfile.close()

#final message
playlear = visual.TextStim(win,text = 'That was the end. \n'
                                      'Thank you very much! \n\n '
                                      'Press space to end this part of the experiment',
                            color = color_txt)
playlear.draw()
win.flip()
event.waitKeys(keyList = [SPAAAAACE])

####################
