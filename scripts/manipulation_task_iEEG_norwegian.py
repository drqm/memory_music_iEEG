# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:28:26 2020

@author: David Quiroga-Martinez
"""
#################### Load libraries and set directories #######################
from random import shuffle
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
#prefs.hardware['audioLib'] = ['pyo']
from psychopy import visual, core, sound, event, gui, logging
import itertools as it
import os
import numpy as np
from sys import argv

from triggers import setParallelData
setParallelData(0)

# set project directory:
my_path = os.path.abspath(os.path.dirname(__file__))
os.chdir(my_path)
os.chdir('..')
#os.chdir('C:/Users/au571303/Documents/projects/memory_music_iEEG')
stim_dir = 'stimuli/manipulation_normalized'
log_dir = 'logs'

# Uncomment this seed to reproduce the randomization:
#rgnSeed = np.random.randint(900509) 
col = 'white' # text color
###############################################################################

######### Prepare block-specific texts to display in the experiment ##########

instructions = [['Du skal nå høre en melodi.\n\n'
                 'Når den er ferdig vil du se ordene “IMAGINE” (FORESTILL DEG) på skjermen. \n'
                 'Når dette skjer, prøv å forestille deg melodien i hodet ditt så livlig som du kan.\n\n'
                 'Etter litt tid vil du høre en annen melodi. Indiker om den andre '
                 'melodien er NØYAKTIG DEN SAMME som den første melodien, '
                 'eller ikke, ved å trykke på knappene:\n\n'
                 '1: samme, 2: forskjellig\n\n'],

                ['Du skal nå høre en melodi.\n\n'
                 'Når den er ferdig vil du se ordene “IMAGINE” (FORESTILL DEG) på skjermen. \n'
                 'Når dette skjer, prøv å forestille deg en OMVENDT versjon så livlig som mulig i '
                 'hodet ditt. For eksempel, C B A er det omvendte av A B C. \n\n'
                 'Etter litt vil du høre en annen melodi. Venligst indiker om den andre '
                 'melodien er en OMVENDT versjon av den første melodien, '
                 'eller ikke, ved å trykke:\n\n'
                 '1: omvendt, 2: annet\n\n']]

rehearse_texts = [["IMAGINE \n\n"
                   "Ta den tiden du trenger for å forestille deg den originale melodien i hode ditt.\n\n"
                   "Vennligst IKKE lag selve lyden eller beveg munnen din imens du forestiller deg melodien.\n\n"
                   "Når du er klar, trykk på en knapp for å høre den andre melodien "
                   "og gi et svar."],

                  ["IMAGINE \n\n"
                   "Ta deg tid til å forestille deg hvordan en OMVENDT versjon av denne melodien lyder. \n\n"
                   "Vennligst IKKE lag selve lyden eller beveg munnen din imens du forestiller deg melodien.\n\n"
                   "Husk: A B C omvendt blir C B A. \n\n"
                   "Når du er klar, trykk en knapp for å høre den andre melodien, "
                   "og avgi et svar."]]

continue_texts = [["Det var alle melodieksemplene.Vi er nå klar for å begynne det ordentlige forsøket. "
                  "Melodiene vil spilles av automatisk. Hver runde vil gå rsakere enn i eksempelene. "
                   "Husk at du må svare: \n\n 1: samme, 2: forskjellig\n\n"
                   "Prøv å forestille deg melodien så livlig som mulig i hodet ditt, "
                   "nøyaktig når ordene “IMAGINE” (FORESTILL DEG) vises på skjermen.\n"
                   "Trykk en tast for å starte forsøket.\n"],
                  
                  ["Det var alle melodieksemplene.Vi er nå klar for å begynne det ordentlige forsøket. "
                  "Melodiene vil spilles av automatisk. Hver runde vil gå raskere enn i eksempelmelodiene. "
                  "Husk at du må svare: \n\n 1: omvendt, 2: annet\n\n"
                  "Prøv å forestille den omvendte melodien så livlig som mulig "
                  "i hodet ditt, nøyaktig når ordene “IMAGINE” (FORESTILL DEG) vises på skjermen.\n"
                  "Trykk en tast for å starte forsøket.\n"]]

feedback_same_texts = [["Svarte du riktig?\n\n"
                        "Den andre melodien var NØYAKTIG DEN SAMME som den første melodien.\n"
                        "Trykk en knapp for å høre et annet eksempel."],

                       ["Svarte du riktig?\n\n"
                        "Den andre melodien var en OMVENDT versjon av den første melodien. \n"
                        "Trykk en knapp for å høre et annet eksempel."]]

feedback_diff_texts = [["Svarte du riktig?\n\n"
                        "Den andre melodien var helt forskjellige fra den første melodien.\n"
                        "Trykk en knapp for å fortsette."],
                       
                       ["Svarte du riktig?\n\n"
                        "Forsiktig! Denne melodien hørtes lignende ut som den første, "
                        "men den er IKKE en omvendt versjon. Derfor vil det riktige svaret være 2, i dette tilfellet.\n"
                        "Trykk en knapp for å fortsette."]]

orders_same = [[0,1,2],[2,1,0]] # for practice trials
orders_diff = [[0,2,1],[0,1,2]] # for practice trials
##############################################################################

############# create stimulus list for each experimental block ###############

blocks = {'recognize': [],'invert': []}
blocknames = ['recognize','invert']
stim = [1,2,3]
for bidx,b in enumerate(blocknames):
    blocks[b] = {'stim': [], 'primes': [], 'targets': [], 'melID': [],
                 'trialID': [],'type': [], 'melodies': [],'rehearse': [],
                 'instructions': [],'continue': [], 'feedback_same': [],
                 'feedback_diff': [], 'order_same': [], 'order_diff': []}

    # create prime melodies (12 repetitions of the two melodies)
    primes = [[1,2,3],[3,2,1]]*12 # 48 melodies per block
    
    # create targets:
    if b == 'recognize':
       same = primes.copy()
       diff1 = [[l[a] for a in [2,1,0]] for l in primes[0:12]]
       diff2 = [[l[a] for a in [0,2,1]] for l in primes[12:25]]
       diff = list(it.chain(diff1,diff2))

    elif b == 'invert':
       same = [[l[a] for a in [2,1,0]] for l in primes]
       diff1 = [[l[a] for a in [2,0,1]] for l in primes[0:12]]
       diff2 = [[l[a] for a in [0,1,2]] for l in primes[12:25]]
       diff = list(it.chain(diff1,diff2))
    
    # lists of trial information
    primes = list(it.chain(primes,primes))
    targets = list(it.chain(same,diff))    
    trialID = list(range(len(primes)))   # trial number (before scrambling)

    # random trial order
    rand = trialID.copy()
    shuffle(rand)   

    trialID = [id + 1 for id in trialID] # record trial identity
    melID = list(range(2))*24
    melID = [id + 1 for id in melID] # record melody identity

    # store randomized versions in corresponding block dictionary:
    blocks[b]['primes'] = [primes[p] for p in rand]
    blocks[b]['targets'] = [targets[t] for t in rand]
    blocks[b]['melID'] = [melID[m] for m in rand]
    blocks[b]['trialID'] = [trialID[t] for t in rand]
    blocks[b]['type'] = [1 if x < 24 else 2 for x in rand]
    blocks[b]['melodies'] = [list(l) for l in list(it.permutations(stim))]
    blocks[b]['stim'] = ['{}/{}.wav'.format(stim_dir,s) for s in stim]
    blocks[b]['instructions'] = instructions[bidx]
    blocks[b]['rehearse'] = rehearse_texts[bidx]
    blocks[b]['continue'] = continue_texts[bidx]
    blocks[b]['feedback_same'] = feedback_same_texts[bidx]
    blocks[b]['feedback_diff'] = feedback_diff_texts[bidx]
    blocks[b]['order_same'] = orders_same[bidx]
    blocks[b]['order_diff'] = orders_diff[bidx]
    
##############################################################################

####################### prepare Psychopy task ################################

#### Prepare relevant keys:
    
#keyNext = 'space' # key to advance

#### function to quit the experiment and save log file:
def quit_and_save():
    win.close()
    if logfile:
       logfile.close()
    logging.flush()
    core.quit()
    
event.globalKeys.add(key='escape', func=quit_and_save, name='shutdown')

#### Collect participant identity:
csid = ''
if len(argv)>1:
    csid = argv[1]

ID_box = gui.Dlg(title = 'Subject identity')
ID_box.addField('ID: (change if subject ID is incorrect) ', csid)
ID_box.addField('block order (random order: leave blank; maintenance first: 1; manipulation first: 2): ')
ID_box.addField('Photodiode? (yes/no): ', 'no')

sub_id = ID_box.show()

block_order = [0,1]
shuffle(block_order)

pcolor = 'black'
if sub_id[1] == '1':
   block_order = [0,1]
if sub_id[1] == '2':
   block_order = [1,0]
if sub_id[2] == 'yes':
   pcolor = col

##### create window to display text:
win = visual.Window(fullscr=True, color='black')

# Set frame rate
frate = np.round(win.getActualFrameRate())
prd = 1000 / frate
print('screen fps = {} - cycle duration = {}'.format(frate, prd))

##### create other text ojects to display during the experiment:
    
nextText = visual.TextStim(win, text='(Trykk en tast for å fortsette.)',
                           color=col, pos=(0, -0.8))

endText = visual.TextStim(win, text='Det var slutten på forsøket.\n\nTakk for at du deltok!',
                          color=col, height=0.2, wrapWidth=2)

practice_txt = visual.TextStim(win, text = "Før du gjør oppgaven skal vi høre noen eksempler.\n\n"
                                           "Trykk en tast for å høre og prøv å huske den første melodien.\n\n Klar?",
                                         wrapWidth=1.8, color = col)

pause_txt = visual.TextStim(win, text = "Tid for en litt pause.\n\n"
                                        "Ta den tiden du trenger.\n"
                                        "Trykk en tast for å fortsette.",
                                         wrapWidth=1.8, color = col)

vividness_txt = visual.TextStim(win, text = "I den forrige delen, hvor livlig "
                                            "klarte du å forestille deg lydene? \n\n"
                                            "Trykk en av disse nummerene på tastaturet:\n\n "
                                            "Ikke livlig i det hele tatt  <  1  2  3  4  5  > "
                                            "Ekstremt livlig",
                                         wrapWidth=1.8, color = col)

fixationCross = visual.TextStim(win, text='+', color=col, height=0.3)
listen_txt =  visual.TextStim(win, text='Listen', color=col, height=0.2)
imagine_txt = visual.TextStim(win, text='Imagine', color=col, height=0.2)
pdiode = visual.Rect(win, size = (.3,.35), pos = (-1,-1),fillColor=pcolor)

# set default log file
log_fn_def = log_dir + '/' + sub_id[0] +  '_iEEG_default_norwegian.log'
lastLog = logging.LogFile(log_fn_def, level=logging.INFO, filemode='a')

## create a silent sound to prevent buffer issues
silentDur = .5
silent = sound.Sound('C', secs=silentDur, volume=0, sampleRate = 44100, stereo = False)

# set relevant clocks:
RT = core.Clock()
block_time = core.Clock()

##############################################################################

############## Now run the experimental blocks ###############################

#### select blocks to include:         
           
bnames = ['recognize','invert'] # block names to loop over
bnames = [bnames[b] for b in block_order] # counterbalance

for bidx, b in enumerate(bnames): # loop over blocks
    
    ################### prepare block-specific variables #####################
    block = blocks[b]
    if bidx == (len(bnames) - 1):
        blockendText = visual.TextStim(win, text= "Det var slutten på oppgaven. \n\n"
                                                "Trykk en tast for å avslutte denne delen av forsøket.",
                               color=col, wrapWidth=1.8)
    else:
        blockendText = visual.TextStim(win, text= "Det var slutten på denne delen.\n "
                                                  "Nå kan du ta en liten pause.\n\n"
                                                  "Trykk en tast for å fortsette, når du er klar.\n",
                               color=col,wrapWidth=1.8)
        
    instr = visual.TextStim(win, text=block['instructions'][0],
                            color=col, wrapWidth=1.8)
 
    continue_txt = visual.TextStim(win, text = block['continue'][0],
                                   wrapWidth=1.8, color = col)
        
    rehearse_txt = visual.TextStim(win, text = block['rehearse'][0],
                                wrapWidth=1.8, color = col)
   
    #### initialize custom log file:
    filename = log_dir + '/' + sub_id[0] + '_' + b + '_iEEG_norwegian.csv'
    logfile = open(filename,'w')
    logfile.write("subject,block,time,melID,trialID,prime,"
                  "target,type,response,rt\n")
    
    #### preload sounds:
    sounds = []
    sounds = [sound.Sound('{}'.format(bb)) for bb in block['stim']]       

    #################### Start experiment ####################################
    ## display instructions:
    for i in range(5):
        pdiode.draw()
        win.flip()
        core.wait(0.05)
        win.flip()
        core.wait(0.05)

    instr.draw()
    nextText.draw()
    win.flip()
    event.waitKeys()
    
    ##################### Run example trials #################################

    practice_txt.draw()
    nextText.draw()
    win.flip()
    event.waitKeys()
    
    # We will present a "same" (or "invert") and a "different" (or "other") trial.
    cases = ['same','diff'] 
    
    for tt in cases:
        
        ########## Prepare condition-specific variables #######################
        feedback_txt = visual.TextStim(win, text = block['feedback_' + tt][0],
                                               wrapWidth=1.8, color = col)
        order = block['order_' + tt]
                       
        ################### begin stimulus presentation #######################
        
        #prime melody:
            
        listen_txt.draw(win)
        win.flip()
        silent.play()  # to prevent omission/cut of the first stimulus
        core.wait(1)
        for s in [0,1,2]:  
            sounds[s].play()
            core.wait(0.5)     
                          
        rehearse_txt.draw(win)
        nextText.draw()    
        win.flip()
        event.waitKeys()
        
        # target melody:
            
        listen_txt.draw(win)
        win.flip()
        silent.play()  # to prevent omission/cut of the first stimulus
                   
        for s in order:  
            sounds[s].play()
            core.wait(0.5)    
            
        core.wait(2)       
        feedback_txt.draw()
        nextText.draw()    
        win.flip()
        event.waitKeys()
        
    continue_txt.draw()
    win.flip()
    event.waitKeys()
        
    ###################### Now we begin the real task ########################
    
    block_time.reset()
    
    silent.play()  # to prevent omission/cut of the first stimulus
    core.wait(silentDur)

    for tidx, t in enumerate(block['primes']):     # loop over trials:
        trialtxt = visual.TextStim(win, text='Runde {} / 48'.format(tidx + 1),
                                   color=col, height = 0.2)
        trialtxt.draw()
        win.flip()
        ttime = block_time.getTime() #  track trial onset
        core.wait(2.5)

        pmel = block['primes'][tidx] #prime melody
        tmel = block['targets'][tidx] # target melody
        # present prime (loop over sounds):
        nextFlip = win.getFutureFlipTime(clock='ptb')
        for p,ps in enumerate(pmel):
            trigger = str(p + 1) + str(ps)
            win.callOnFlip(setParallelData, int(trigger))
            sounds[ps-1].play(when = nextFlip)
            for frs in range(int(np.round(50/prd))): # 6 frames = 50 ms
                listen_txt.draw()
                if (p == 0) and (frs == 0):
                    pdiode.draw()
                win.flip()

            win.callOnFlip(setParallelData, 0)
            for frs in range(int(np.round(450/prd))): # 30 frames = 450 ms
                listen_txt.draw()
                win.flip()
            nextFlip = win.getFutureFlipTime(clock='ptb')
        
        for frs in range(int(np.round(500/prd))): # 30 frames = 450 ms
            listen_txt.draw()
            win.flip()
            
        #delay period:
        for frs in range(int(np.round(2000/prd))): # 30 frames = 450 ms
            imagine_txt.draw()
            win.flip()
       
        #present target (loop over sounds)
        for midx, ts in enumerate(tmel):
            trigger = str(block['type'][tidx]) + str(midx + 1) + str(ts) 
            win.callOnFlip(setParallelData, int(trigger))           
            sounds[ts-1].play(when = nextFlip)
            #clear events and reset the clock for RT
            if midx == 0:
                event.clearEvents(eventType='keyboard')
                RT.reset()
            for frs in range(int(np.round(50/prd))): # 6 frames = 50 ms
                listen_txt.draw()
                win.flip()  
            win.callOnFlip(setParallelData, 0)
            for frs in range(int(np.round(450/prd))): # 30 frames = 450 ms
                listen_txt.draw()
                win.flip()
            nextFlip = win.getFutureFlipTime(clock='ptb')
        
        # if there is a response record keys and RT. Else record 0 and time limit:
           
        resp = None 
        while resp == None: 
           key = event.getKeys(timeStamped = RT)
           if len(key) > 0:
                resp = key[0][0] 
                rt = key[0][1]
           elif RT.getTime() > 3.5:
                resp = 0
                rt = RT.getTime()

        ## gather log info and add to logfile:
        lrow = '{},{},{},{},{},{};{};{},{};{};{},{},{},{}\n'
        lrow = lrow.format(sub_id[0],b,ttime,block['melID'][tidx],block['trialID'][tidx],
                           pmel[0],pmel[1],pmel[2], tmel[0],tmel[1],tmel[2],
                           block['type'][tidx], resp,rt*1000)
        logfile.write(lrow)            
        core.wait(0.1)  # 100 ms after response, to start new trial
        
        # now we introduce a small pause in trial 30 so that participants can rest
        if tidx == 23:
            pause_txt.draw()
            win.flip()
            event.waitKeys()
    vividness_txt.draw()
    win.flip()
    event.waitKeys(keyList = ['1','2','3','4','5'])
    logfile.close() # save log file

    blockendText.draw()
    win.flip()
    event.waitKeys()

core.wait(2)
for i in range(5):
    pdiode.draw()
    win.flip()
    core.wait(0.05)
    win.flip()
    core.wait(0.05)
core.quit()