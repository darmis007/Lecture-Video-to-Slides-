#This script should be run on Google Colab preferably after mounting your drive

from os import listdir
from os.path import isfile, join

mypath='/content/gdrive/MyDrive/Chemical Engineering BITS Pilani/HT Vids/'
onlyfiles2 = [str(f) for f in listdir(mypath) if isfile(join(mypath, f))] #(Where a copy of all the lectures is assembled)

import cv2
for i in onlyfiles2: #onlyfiles2 is collection of a copy of lectures shared on drive)
  vidcap = cv2.VideoCapture(str("/content/gdrive/MyDrive/Chemical Engineering BITS Pilani/HT Vids/"+i)) #feed the lectures through a loop
  count = 0
  success = True
  fps = int(vidcap.get(cv2.CAP_PROP_FPS))

  print(fps)

  while success:
      success,image = vidcap.read()
  #     print('read a new frame:',success)
      if count%(60*fps) == 0 : #60 corresponds to 60seconds of video footage, you can vary this as per your choice of slide frequency
           cv2.imwrite('/content/HT/{}/frame{}.jpg'.format(i,count),image)
           print('successfully written 60th sec')
      count+=1
  print(i)
  
from PIL import Image

for i in onlyfiles2:
  mypath="/content/HT/"+i #path of where lecture screenshot have been saved
  onlyfiles = [str('/content/HT/'+i+'/'+f) for f in listdir(mypath) if isfile(join(mypath, f))]
  im_list = []
  im1 = Image.open(onlyfiles[0])
  for j in onlyfiles[0:]:
    im = Image.open(j)
    im_list.append(im)
  pdf1_filename = "/content/21-01/{}.pdf".format(i) #21-01 corresponds to the folder name where you want to save the pdf file

  im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
  print(i)
