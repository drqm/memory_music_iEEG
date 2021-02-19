# Memory_music_iEEG

In this repository you will find the implementation of experimental paradigms investigating musical memory and imagery with intracranial EEG and MEG. The experiment consists of three tasks:

1- A recognition memory task in which participants listen to a short musical excerpt (from a J.S. Bach work) and afterwards are presented with short melodies which could belong or not to the musical excerpt. Participants decide whether each melody is "old" or "new".

2- A working memory and imagery task in which participants are presented with a short three-note melody, then are asked to imagine it vividly on cue, and finally are required to decide if the second melody is the same or different from the first. In this task, there is a second block in which participants need to mentally invert the melody in their minds (e.g. ABC becomes CBA) and judge whether the second melody is an iverted version of the first or not. The two blocks (maintanance and manipulation) are counterbalanced across subjects.

3- A localizer block in which participants are presented each of the three tones used in task 2 in random order (avoiding consecutive repetitions). After each sound, participants are asked to imagine it very vividly in their minds.

For tasks 2 and 3 we have both MEG and iEEG versions. These are the correspoinding implementations of each task:

1- [scripts/LerningBach_iEEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/LearningBachShort_iEEG.py)

2- [scripts/manipulation_task_iEEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/manipulation_task_iEEG.py) (for iEEG) and [scripts/manipulation_task_MEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/localizer_MEG.py) (for MEG)

3- [scripts/localizer_iEEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/localizer_iEEG.py) (for iEEG) and [scripts/localizer_MEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/localizer_MEG.py) (for MEG)

The three tasks should be presented in this order: 3, 2, 1 or this order: 1, 3, 2; so that the localizer always preceds the maintenance/manipulation task. These two orders may be counterbalanced across participants.

These are the approximate durations and number of trials in each task:

For iEEG

Task 1: 42 trials (21 old, 21 new) (5 minutes)
task 2: 96 trials (48 maintenance: 24 same, 24 different; 48 manipulation: 24 inverted, 24 not inverted/other) (17 minutes)
task 3: 120 trials (40 for each tone) (5 minutes)

for MEG:

task 2: 120 trials (60 maintenance: 30 same, 30 different; 60 manipulation: 30 inverted, 30 not inverted/other) (21 minutes)
task 3: 180 trials (60 for each tone) (8 minutes)

Simuli found under the "stimuli" folder. Log files stored in the "logs" folder.



