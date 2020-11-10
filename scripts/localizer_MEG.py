# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:11:11 2020

@author: au571303
"""
from random import shuffle
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
#prefs.hardware['audioLib'] = ['pyo']
from psychopy import visual, core, sound, event, gui, logging
import os
import numpy as np
#from triggers import setParallelData
#setParallelData(0)

os.chdir('C:/Users/au571303/Documents/projects/memory_music_iEEG')
stim_dir = 'stimuli/manipulation'
log_dir = 'logs'
rgnSeed = np.random.randint(900509)
col = 'white'
n_tones = 150
n_targets = 40
frate = 60 #120
prd = 1000/frate
######################## create stimulus sequence ############################
seq = np.zeros(n_tones*3 + n_targets)
pattern = [1,2,3]

tidx = np.random.choice(range(n_tones),n_targets, replace = False)
tcount = 0
end = 0
p = 0
for n in range(n_tones):
    start = end
    end = start + 3
    if n > 0:
        p = None
    while p == None:
        shuffle(pattern)
        if pattern[0] != seq[start-1]:
            p = 0
    seq[start:end] = pattern 
    if np.isin(n,tidx):
        seq[end] = 4
        end = end + 1 

###################### Prepare psychopy task #################################

####preload stimuli:
sounds = [sound.Sound('{}/{}.wav'.format(stim_dir,int(s))) for s in np.unique(seq)]

#### Prepare relevant keys:
    
keyNext = 'space' # key to advance

#### function to quit the experiment and save log file:
def quit_and_save():
    logging.flush()
    core.quit()
    
event.globalKeys.add(key='escape', func=quit_and_save, name='shutdown')

#### Collect participant identity:
ID_box = gui.Dlg(title = 'Subject identity')
ID_box.addField('ID: ')
sub_id = ID_box.show()

win = visual.Window(fullscr=True, color=[.0, .0, .0])

##### create text oBjects to display during the experiment:

instructions = visual.TextStim(win, text = "In the following, you will hear "
                                           "a sequence of sounds. Please listen "
                                           "attentively to them.\n\n "
                                           "Ready?",
                                         wrapWidth=1.8, color = col)
   
endText = visual.TextStim(win, text='That is the end of the first task. \n'
                                    'We will continue in a moment',
                          wrapWidth=1.8, color = col)

fixationCross = visual.TextStim(win, text='+', color=col, height=0.2)

## create a silent sound to prevent buffer issues
silentDur = .5
silent = sound.Sound('C', secs=silentDur, volume=0, sampleRate = 44100, stereo = True)

# start log file:
filename = log_dir + '/' + sub_id[0] + '_localizer.log'
lastLog = logging.LogFile(filename, level=logging.INFO, filemode='w')
##############################################################################

############################# Start the task #################################
instructions.draw()
win.flip()
event.waitKeys(keyList=[keyNext])

fixationCross.draw()
win.flip()
silent.play()
core.wait(0.5)
nextFlip = win.getFutureFlipTime(clock='ptb')

for s in seq:
#   win.callOnFlip(setParallelData, int(s)) 
    win.callOnFlip(print, int(s))            
    sounds[int(s)-1].play(when = nextFlip)
    for frs in range(int(np.round(50/prd))): # 6 frames = 50 ms
        fixationCross.draw()
        win.flip()  
#            win.callOnFlip(setParallelData, 0)
    win.callOnFlip(print, 0)
    for frs in range(int(np.round(450/prd))): # 30 frames = 450 ms
        fixationCross.draw()
        win.flip()
    nextFlip = win.getFutureFlipTime(clock='ptb')
#    logging.flush()

endText.draw()
win.flip()
event.waitKeys(keyList=[keyNext])
win.close()
core.quit() 
