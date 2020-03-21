import cv2
import numpy as np
class colshape:
    
 def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys
 def col(img2): 
   img =img2
   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   
   yellow_lower = np.array([20,158,158],np.uint8)
   yellow_upper = np.array([35,255,255],np.uint8)
   
   purple_lower = np.array([130,158,158],np.uint8)
   purple_upper = np.array([146,255,255],np.uint8)

   pink_lower = np.array([146,60,190],np.uint8)
   pink_upper = np.array([164,255,255],np.uint8)
    
   green_lower = np.array([36,158,158],np.uint8)
   green_upper = np.array([71,255,255],np.uint8)
   
   greend_lower = np.array([35,72,72],np.uint8)
   greend_upper = np.array([75,158,158],np.uint8)
   
   orange_lower = np.array([7,190,190],np.uint8)
   orange_upper = np.array([20,255,255],np.uint8)

   white_lower = np.array([0,0, 190],np.uint8)
   white_upper = np.array([180,63,255],np.uint8)
       
   red_lower = np.array([0,158,158],np.uint8)
   red_upper = np.array([7,255,255],np.uint8)
   
   red2_lower = np.array([164,158,158],np.uint8)
   red2_upper = np.array([180,255,255],np.uint8)

   bluedark_lower = np.array([98,158,158],np.uint8)
   bluedark_upper = np.array([130,255,255], np.uint8)

   blue_lower = np.array([71,158,158],np.uint8)
   blue_upper = np.array([98,255,255], np.uint8)
   
   blued_lower = np.array([75,72,72],np.uint8)
   blued_upper = np.array([119,158,158], np.uint8)

   black_lower = np.array([ 0,0, 0],np.uint8)
   black_upper = np.array([180,255,44],np.uint8)

   gray_lower = np.array([0,44, 0,],np.uint8)
   gray_upper = np.array([180,75, 44],np.uint8)
   
   gray2_lower = np.array([0,44, 0,],np.uint8)
   gray2_upper = np.array([180,75, 44],np.uint8)

   brown_lower = np.array([0,72,72],np.uint8)
   brown_upper = np.array([35,158,158],np.uint8)
   
   brown2_lower = np.array([ 157,72,72],np.uint8)
   brown2_upper = np.array([180,158,158],np.uint8)

   voilet_lower = np.array([119,72,72],np.uint8)
   voilet_upper = np.array([157,158,158],np.uint8)

   yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
   green = cv2.inRange(hsv, green_lower, green_upper)
   green2 = cv2.inRange(hsv, greend_lower, greend_upper)
   red = cv2.inRange(hsv, red_lower, red_upper)
   red2 = cv2.inRange(hsv, red2_lower, red2_upper)
   brown = cv2.inRange(hsv, brown_lower, brown_upper)
   brown2 = cv2.inRange(hsv, brown2_lower, brown2_upper)
   black = cv2.inRange(hsv, black_lower, black_upper)
   gray = cv2.inRange(hsv, gray_lower, gray_upper)
   gray2 = cv2.inRange(hsv, gray2_lower, gray2_upper)
   orange = cv2.inRange(hsv, orange_lower, orange_upper)
   white = cv2.inRange(hsv, white_lower, white_upper)
   blue = cv2.inRange(hsv, blue_lower, blue_upper)
   blued = cv2.inRange(hsv, blued_lower, blued_upper)
   bluedr = cv2.inRange(hsv, bluedark_lower, bluedark_upper)
   pink = cv2.inRange(hsv, pink_lower, pink_upper)
   purple = cv2.inRange(hsv, purple_lower,purple_upper)
   voilet = cv2.inRange(hsv, voilet_lower,voilet_upper)
     
   res_y = cv2.bitwise_and(img, img, mask = yellow)
   res_g = cv2.bitwise_and(img, img, mask =green)
   res_r = cv2.bitwise_and(img, img, mask = red)
   res_r2 = cv2.bitwise_and(img, img, mask = red2)
   res_br = cv2.bitwise_and(img, img, mask = brown)
   res_br2 = cv2.bitwise_and(img, img, mask = brown2)
   res_b = cv2.bitwise_not(img, img, mask = black)
   res_gr = cv2.bitwise_and(img, img, mask = gray)
   res_o = cv2.bitwise_and(img, img, mask = orange)
   res_w = cv2.bitwise_and(img, img, mask = white)
   res_bl = cv2.bitwise_and(img, img, mask = blue)
   res_bl2= cv2.bitwise_and(img, img, mask = bluedr)
   res_pu = cv2.bitwise_and(img, img, mask = purple)
   res_vo = cv2.bitwise_and(img, img, mask = voilet)
   res_pi = cv2.bitwise_and(img, img, mask = pink)
   
   (contours_y,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

   yellow_max=0.0
   for pic, contour in enumerate(contours_y):
      area_ytry = cv2.contourArea(contour)
      if(area_ytry > yellow_max):
          yellow_max = area_ytry
   #print("max yellow",yellow_max)
          
   (contours_g,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   green_max=0.0
   for pic, contour in enumerate(contours_g):
      area_g = cv2.contourArea(contour)
      if(area_g>green_max):
          green_max=area_g
   #print("green max",green_max)
              
   (contours_r,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   red_max=0.0
   for pic, contour in enumerate(contours_r):
      area_r = cv2.contourArea(contour)
      if(area_r>red_max):
          red_max=area_r
   #print("red max",red_max)
    
   (contours_r2 ,hierarchy)=cv2.findContours(red2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   red2_max=0.0
   for pic, contour in enumerate(contours_r2):
      area_r2 = cv2.contourArea(contour)
      if(area_r2 > red2_max):
         red2_max=area_r2
   #print("max red2",red2_max)
   
   (contours_br,hierarchy)=cv2.findContours(brown,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   brown_max=0.0
   for pic, contour in enumerate(contours_br):
      area_br = cv2.contourArea(contour)
      if(area_br> brown_max):
          brown_max =area_br
   #print("max brown",brown_max)
      
   (contours_br2,hierarchy)=cv2.findContours(brown2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   brown2_max=0.0
   for pic, contour in enumerate(contours_br2):
      area_br2 = cv2.contourArea(contour)
      if(area_br2>brown2_max):
          brown2_max=area_br2
   #print("max brown2",brown2_max)
   
   (contours_b,hierarchy)=cv2.findContours(black,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   black_max=0.0
   for pic, contour in enumerate(contours_b):
      area_b = cv2.contourArea(contour)
      if(area_b>black_max):
          black_max=area_b
   #print("max black",black_max)      
          
   (contours_gr,hierarchy)=cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   gray_max=0.0
   for pic, contour in enumerate(contours_gr):
      area_gr = cv2.contourArea(contour)
      if(area_gr>gray_max):
          gray_max =area_gr
   #print("max gray",gray_max) 
   
   (contours_o,hierarchy)=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   orange_max=0.0
   for pic, contour in enumerate(contours_o):
      area_o = cv2.contourArea(contour)
      if(area_o>orange_max):
          orange_max = area_o
   #print("max orange",orange_max)       
    
   (contours_w,hierarchy)=cv2.findContours(white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   white_max=0.0
   for pic, contour in enumerate(contours_w):
      area_w = cv2.contourArea(contour)
      if(area_w > white_max):
          white_max = area_w
   #print("white max",white_max)
    
   (contours_bl,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   blue_max=0.0
   for pic, contour in enumerate(contours_bl):
      area_bl = cv2.contourArea(contour)
      if(area_bl>blue_max):
          blue_max = area_bl
   #print("max blue",blue_max)
   
   (contours_bl2,hierarchy)=cv2.findContours(bluedr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   blue2_max=0.0
   for pic, contour in enumerate(contours_bl2):
      area_bl2 = cv2.contourArea(contour)
      if(area_bl2 > blue2_max):
          blue2_max = area_bl2
   #print("max blue",blue2_max)
    
   (contours_pu,hierarchy)=cv2.findContours(purple,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   purple_max=0.0
   for pic, contour in enumerate(contours_pu):
      area_pu = cv2.contourArea(contour)
      if(area_pu>purple_max):
          purple_max=area_pu
   #print("purple max",purple_max)      

   (contours_vo,hierarchy)=cv2.findContours(voilet,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   voilet_max=0.0
   for pic, contour in enumerate(contours_vo):
      area_vo = cv2.contourArea(contour)
      if(area_vo> voilet_max):
          voilet_max = area_vo
   #print("voilet max",voilet_max)
   
   (contours_g2,hierarchy)=cv2.findContours(green2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   green2_max=0.0
   for pic, contour in enumerate(contours_g2):
      area_g2 = cv2.contourArea(contour)
      if(area_g2> green2_max):
          green2_max = area_g2
   #print("green2 max",green2_max)
   
   (contours_gr2,hierarchy)=cv2.findContours(gray2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   gray2_max=0.0
   for pic, contour in enumerate(contours_gr2):
      area_gr2 = cv2.contourArea(contour)
      if(area_gr2> gray2_max):
          gray2_max = area_gr2
   #print("gray2 max",gray2_max)

   (contours_bld,hierarchy)=cv2.findContours(blued,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   blued_max=0.0
   for pic, contour in enumerate(contours_bld):
      area_bld = cv2.contourArea(contour)
      if(area_bld> blued_max):
          blued_max = area_bld
   #print("dirty blue max",blued_max)
   
   (contours_pi,hierarchy)=cv2.findContours(pink,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   pink_max=0.0
   for pic, contour in enumerate(contours_pi):
      area_pi = cv2.contourArea(contour)
      if(area_pi> pink_max):
          pink_max = area_pi


   li = {'blue':blue_max ,'pink':pink_max, 'green':green_max ,'light green':green2_max, 'red':red_max , 'yellow':yellow_max ,'dirty blue':blued_max, 'blue':blue2_max , 'purple':purple_max , 'voilet':voilet_max,'white':white_max, 'orange':orange_max ,'gray':gray2_max, 'gray':gray_max , 'black':black_max , 'brown':brown2_max , 'brown':brown_max , 'red':red2_max }
   ok1=(max(li, key=li.get))
  
   print(ok1)
   max2 = 0
   maxx = max(li.values())

   for v in li.values(): 
     if(v>max2 and v<maxx): 
            max2 = v 

   listOfKeys = colshape.getKeysByValue(li, max2)
   col2 =listOfKeys[0]

   print(listOfKeys[0])  

   return ok1,col2
    
 