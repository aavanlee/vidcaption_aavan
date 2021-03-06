import json
import os
import pandas as pd

path_to_current_file = os.path.realpath(__file__)
current_directory = os.path.split(path_to_current_file)[0]
path_to_file = os.path.join(current_directory, "captions.json")
with open(path_to_file) as mydata:
    captionsraw_list = json.load(mydata)
captionsraw_df = pd.DataFrame(captionsraw_list[0:],columns=captionsraw_list[0])

print(captionsraw_df)

    
data = {}

#image captioning COCO format
info={}
licenses=[]
images=[]
annotations=[]

####
x = 8
# x is filename part to be removed eg: "DATASET_"

##INFO
info['description'] = 'SAMPLE COCO FORMAT DATASET'
info['url'] = 'http://123.com'
info['version'] = "1.0"
info['year'] = 2021
info["contributor"] = "aavan"
info["date_created"] = "25/8/2021"

##LICENSES
#empty

##IMAGES
for index, row in captionsraw_df.iterrows():
    images.append({
        'license': 12345,
        'filename': row['filename'],
        'id': int(row['filename'][x:-4])
    })

##ANNOTATIONS(IMAGE CAPTIONING)
#for (filename, caption1, caption2, caption3, caption4) in captionsraw_df.iteritems():
for index, row in captionsraw_df.iterrows():
    annotations.append({
        'image_id': int(row['filename'][x:-4]),
        'id': int(row['filename'][x:-4]),
        'caption': row['caption1']
    })
    annotations.append({
        'image_id': int(row['filename'][x:-4]),
        'id': int(row['filename'][x:-4]),
        'caption': row['caption2']
    })
    annotations.append({
        'image_id': int(row['filename'][x:-4]),
        'id': int(row['filename'][x:-4]),
        'caption': row['caption3']
    })
    annotations.append({
        'image_id': int(row['filename'][x:-4]),
        'id': int(row['filename'][x:-4]),
        'caption': row['caption4']
    })





data['info'] = info
data['licenses'] = licenses
data['images'] = images
data['annotations'] = annotations
print(json.dumps(data, indent=4))

with open('captions_coco_format.json', 'w') as outfile:
    json.dump(data, outfile)
