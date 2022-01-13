# Memory_music_iEEG

In this repository you will find the implementation of experimental paradigms investigating musical memory and imagery with intracranial EEG and MEG. The experiment consists of three tasks:

1- A recognition memory task in which participants listen to a short musical excerpt (from a J.S. Bach work) and afterwards are presented with short melodies which could belong or not to the musical excerpt. Participants decide whether each melody is "old" or "new".

2- A localizer block in which participants are presented each of the three tones used in task 3 in random order (avoiding consecutive repetitions). After each sound, participants are asked to imagine it very vividly in their minds.

3- A working memory and imagery task (maintenance) in which participants are presented with a short three-note melody, then are asked to imagine it vividly on cue, and finally are required to decide if the second melody is the same or different from the first. In this task, there is a second block (manipulation) in which participants need to mentally invert the melody in their minds (e.g. ABC becomes CBA) and judge whether the second melody is an inverted version of the first or not. The two blocks (maintenance and manipulation) are counterbalanced across subjects.


For tasks 2 and 3 we have both MEG and iEEG versions. These are the correspoinding implementations of each task, for different Psychopy versions and different languages:

Implementations in English using Psychopy 3.1.2:

- task 1 [scripts/LerningBach_iEEG_3.1.2.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/LearningBachShort_iEEG_3.1.2.py)

- task 2 [scripts/localizer_iEEG_3.1.2.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/localizer_iEEG_3.1.2.py)

- task 3 [scripts/manipulation_task_iEEG_3.1.2.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/manipulation_task_iEEG_3.1.2.py)


Implementations in English using Psychopy 2021.2.3

- task 1 [scripts/LerningBach_iEEG_spanish.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/LearningBachShort_iEEG.py)

- task 2 [scripts/localizer_iEEG_spanish.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/localizer_iEEG.py) (for iEEG) and [scripts/localizer_MEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/localizer_MEG.py) (for MEG)

- task 3 [scripts/manipulation_task_iEEG_spanish.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/manipulation_task_iEEG.py) (for iEEG) and [scripts/manipulation_task_MEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/localizer_MEG.py) (for MEG)


Implementations in Spanish using Psychopy 2021.2.3

- task 1 [scripts/LerningBach_iEEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/LearningBachShort_iEEG.py)

- task 2 [scripts/localizer_iEEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/localizer_iEEG.py)

- task 3 [scripts/manipulation_task_iEEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/manipulation_task_iEEG.py)


The three tasks should be presented in this order: 1, 2, 3 or this order: 2, 3, 1; so that the localizer always preceds the maintenance/manipulation task. These two orders may be counterbalanced across participants.

To facilitate running the tasks, master scripts have been created in which the order is predetermined. However, if desired, blocks can be run individualy and / or in a custom order as specified in a prompt dialogue at the beginning:

Task run in English using psychopy 3.1.2

[scripts/task_run_iEEG.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/task_run_iEEG.py)


Task run in English using psychopy 2021.2.3

[scripts/task_run_iEEG_3.1.2.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/task_run_iEEG_3.1.2.py)


Task run in Spanish using psychopy 2021.2.3

[scripts/task_run_iEEG_spanish.py](https://github.com/drqm/memory_music_iEEG/blob/master/scripts/task_run_iEEG_spanish.py)


These are the approximate durations and number of trials in each task:

For iEEG

- Task 1: 42 trials (21 old, 21 new) (5 minutes)

- task 2: 120 trials (40 for each tone) (5 minutes)

- task 3: 96 trials (48 maintenance: 24 same, 24 different; 48 manipulation: 24 inverted, 24 not inverted/other) (17 minutes)

for MEG:

- task 2: 180 trials (60 for each tone) (8 minutes)

- task 3: 120 trials (60 maintenance: 30 same, 30 different; 60 manipulation: 30 inverted, 30 not inverted/other) (21 minutes)

Stimuli found under the "stimuli" folder. Log files stored in the "logs" folder.


