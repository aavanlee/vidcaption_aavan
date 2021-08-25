import json
import os
import pandas as pd
import sys
from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap

vidname = str(sys.argv[1])
file = vidname + '-OUTPUT.json'
path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.split(path_to_current_file)[0]
path_to_file = os.path.join(current_directory, file)
with open(path_to_file) as mydata:
    data = json.load(mydata)
df = pd.DataFrame(data[0:],columns=data[0])
df.drop('stime', axis=1, inplace=True)
df.drop('dur(s)', axis=1, inplace=True)
df.columns = ['image_id', 'caption']
print(df)
out = df.to_json(orient='records')
outputfile = 'coco-OUTPUT.json'
with open(outputfile, 'w') as f:
    f.write(out)
   
#annotation_file = 'captions_val2014.json' ###FOR COCO VAL2014 SET
annotation_file = 'cocomaked.json' ###FOR TEST SET DEST

results_file = 'coco-OUTPUT.json'

# create coco object and coco_result object
coco = COCO(annotation_file)
coco_result = coco.loadRes(results_file)

# create coco_eval object by taking coco and coco_result
coco_eval = COCOEvalCap(coco, coco_result)

# evaluate on a subset of images by setting
# coco_eval.params['image_id'] = coco_result.getImgIds()
# please remove this line when evaluating the full validation set
coco_eval.params['image_id'] = coco_result.getImgIds()

# evaluate results
# SPICE will take a few minutes the first time, but speeds up due to caching
coco_eval.evaluate()

# print output evaluation scores
for metric, score in coco_eval.eval.items():
    print(f'{metric}: {score:.3f}')
