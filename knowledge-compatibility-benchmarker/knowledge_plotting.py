# for plotting knowledge

import matplotlib.pyplot as plt
import csv
import numpy as np
from knowledge_loader import load_cooccurence_knowledge
from knowledge_loader import load_spatial_knowledge

def cooccurence_knowledge_plotting():
  knowledge = load_cooccurence_knowledge('cooccurence_knowledge.xml')
  #print knowledge['car']['person'] == knowledge['person']['car']
  ordered_class_list = ['motorbike', 'bicycle', 'person', 'boat', 'cat', 'horse', 'bottle', 'car', 'dog', 'sofa', 'bird', 'chair', 'diningtable', 'tvmonitor', 'sheep', 'train', 'bus', 'aeroplane', 'cow', 'pottedplant']
  
  shape = (len(ordered_class_list), len(ordered_class_list))
  conf_arr = np.zeros(shape)
  
  for i in range(len(ordered_class_list)):
    for j in range(len(ordered_class_list)):
        conf_arr[i][j] = round(knowledge[ordered_class_list[i]][ordered_class_list[j]],2)
  
  #sanity check
  #for row in range(conf_arr.shape[0]):
    #total = sum(conf_arr[row,:])
    #print total
    #assert total==1.0
    
  #plotting
  fig = plt.figure()
  plt.clf()
  ax = fig.add_subplot(111)
  ax.set_aspect(1)
  res = ax.imshow(np.array(conf_arr), cmap=plt.cm.jet, 
                  interpolation='nearest')

  width = len(conf_arr)
  height = len(conf_arr[0])

  for x in xrange(width):
      for y in xrange(height):
          ax.annotate(str(conf_arr[x][y]), xy=(y, x), size = 7, 
                      horizontalalignment='center',
                      verticalalignment='center')

  cb = fig.colorbar(res)
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  plt.xticks(range(width), alphabet[:width])
  plt.yticks(range(height), alphabet[:height])

  plt.savefig('cooccurence_knowledge.png', format='png')


def spatial_knowledge_plotting():
  knowledge = load_spatial_knowledge('spatial_knowledge.xml')
  ordered_class_list = ['motorbike', 'bicycle', 'person', 'boat', 'cat', 'horse', 'bottle', 'car', 'dog', 'sofa', 'bird', 'chair', 'diningtable', 'tvmonitor', 'sheep', 'train', 'bus', 'aeroplane', 'cow', 'pottedplant']
  #ordered_pos_list = ['bottom', 'center', 'top']
  
  print knowledge['motorbike']['bottom']
  print knowledge['motorbike']['center']
  print knowledge['motorbike']['top']
  
  
  bottom_pos = []
  center_pos = []
  top_pos = []
  bottom_plus_center_pos = []
  
  for i in range(len(ordered_class_list)):
    bottom_pos.append(knowledge[ordered_class_list[i]]['bottom'])
    center_pos.append(knowledge[ordered_class_list[i]]['center'])
    top_pos.append(knowledge[ordered_class_list[i]]['top'])
    
    bottom_plus_center_pos.append(bottom_pos[i]+center_pos[i])  
  
  print top_pos[0]
  
  N = 20
  
  ind = np.arange(N)    # the x locations for the groups
  width = 0.35       # the width of the bars: can also be len(x) sequence

  plt.figure()
  p1 = plt.bar(ind, bottom_pos,   width, color='r')
  p2 = plt.bar(ind, center_pos, width, color='y',
               bottom=bottom_pos)
                 
  p3 = plt.bar(ind, top_pos, width, color='b',
               bottom=bottom_plus_center_pos)
               

  plt.ylabel('Scores')
  plt.title('Scores by group and gender')
  plt.xticks(ind+width/2., ('A', 'B', 'C', 'D', 'E', 'F ', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ) )
  plt.yticks(np.arange(0,1.1,0.1))
  plt.legend( (p1[0], p2[0], p3[0]), ('Bottom', 'Center', 'Top') )
  
  plt.savefig('spatial_knowledge.png', format='png')
  #plt.show()
  
def main():
  cooccurence_knowledge_plotting()
  spatial_knowledge_plotting()

if __name__ == '__main__':
  main()

