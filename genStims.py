from random import randint
import numpy as np
import pandas as pd
img_dict = {2: 'image_folder/stim_2.png', 3: 'image_folder/stim_3.png', 4: 'image_folder/stim_4.png', 5: 'image_folder/stim_5.png'}

length = 256 # number of trials within a  block should be 256
dfStims = pd.DataFrame()
block_ids = [1, 1, 2, 2, 2, 1, 2] #1 is random #2 is sequence

#Generate Pseudo-Random Stimuli Ordering
def genRandom(length):
    random_stims = []
    random_img_ids = []
    for x in range(0,length):
        if len(random_stims) == 0:
            random_stims.append(randint(2,5))
        elif len(random_stims) > 0:
            val = randint(2,5)
            while val == random_stims[x-1]:
                val = randint(2,5)
            random_stims.append(val)
        random_img_ids.append(img_dict[random_stims[x]])
    random_img_ids = np.asarray(random_img_ids)
    random_ans= np.asarray(random_stims)
    return (random_img_ids, random_ans)

#Generate Sequence Ordering --.
def genSequence(length):
    #Generate Sequence Stimuli Ordering.
    sequence_stims = [4,5,3,4,2,5,3,2,4,5,4,5,2,4,5,3,2,3,5,3,4,2,3,2,3,5,4,2,4,2,3,5]
    rota_ind = randint(1,31)
    sequence_stims = sequence_stims[rota_ind:]  + sequence_stims[:rota_ind]
    sequence_img_ids = []
    sequence_stims= np.tile(sequence_stims,8)
    for x in range(0,length):
        sequence_img_ids.append(img_dict[sequence_stims[x]])
    return (sequence_img_ids, sequence_stims)

for type in range(0,len(block_ids)):
    if block_ids[type] == 1:
        img_ids, cor_ans = genRandom(length)
        dfStims['block_'+str(type+1)+'_img'] = img_ids
        dfStims['block_'+str(type+1)+'_ans'] = cor_ans
    elif block_ids[type] == 2:
        img_ids, cor_ans = genSequence(length)
        dfStims['block_'+str(type+1)+'_img'] = img_ids
        dfStims['block_'+str(type+1)+'_ans'] = cor_ans

dfStims.to_csv('stimuli.csv', index= False)
