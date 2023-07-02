import pandas as pd
import cv2
import statistics
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import math
def movement_predict():
    # Save image in set directory
    # Read RGB image
    img = cv2.imread(r'C:\Users\samwe\OneDrive\Desktop\Sam\movement\images\mov1.png')
    #print(img)
    # Output img with window name as 'image'
    cv2.imshow('image', img) 
    # Maintain output window utill
    # user presses a key
    cv2.waitKey(0)        
      
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    img = cv2.imread(r'C:\Users\samwe\OneDrive\Desktop\Sam\movement\images\mov2.png')
    # Output img with window name as 'image'
    cv2.imshow('image', img) 
      
    # Maintain output window utill
    # user presses a key
    cv2.waitKey(0)        
      
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    #without movement-Mean-50,Standard deviation-10
    #with movement-Mean-50,Standard deviation-41.23
    check=0
    s=[]
    s=r'C:\Users\samwe\OneDrive\Desktop\Sam\movement\test_data\test0.csv'
    s1='movementresult0.csv'
    mean=50
    sdmovup=23
    sdmovdown=50
    sdnonmov=13
    for i in range(5):
        movement=[]
        df = pd.read_csv(s.replace('0',str(i+1)))
        print(df)
        l=len(df.iloc[:,0])
        sec=l//240
        plt.plot(list(range(l)),df.iloc[:,0])
        plt.savefig('mnm.png')
        plt.close()
        img = cv2.imread(r'mnm.png')
        cv2.imshow('image',img) 
          
        # Maintain output window utill
        # user presses a key
        cv2.waitKey(0)        
          
        # Destroying present windows on screen
        cv2.destroyAllWindows()
        for j in range(0,l,sec):
            c=sec
            if j+sec>l:
                c=l-j
            for k in range(c):
                if df.iloc[j+k,0]>mean:
                    if (1.0 / (sdmovup * math.sqrt(2*math.pi))) * math.exp(-0.5*((df.iloc[j+k,0] - mean) / sdmovup) ** 2)>(1.0 / (sdnonmov * math.sqrt(2*math.pi))) * math.exp(-0.5*((df.iloc[j+k,0] - mean) / sdnonmov) ** 2):
                        check=1
                        break
                else:
                    if (1.0 / (sdmovdown * math.sqrt(2*math.pi))) * math.exp(-0.5*((df.iloc[j+k,0] - mean) / sdmovdown) ** 2)>(1.0 / (sdnonmov * math.sqrt(2*math.pi))) * math.exp(-0.5*((df.iloc[j+k,0] - mean) / sdnonmov) ** 2):
                        check=1
                        break
            if check==0:
                for k in range(c):
                    movement.append("No")
            else:
                for k in range(c):
                    movement.append("Yes")
            check=0
        dict = {'Vibrations': df.iloc[:,0], 'Movement': movement}
        df1 = pd.DataFrame(dict)
        # saving the dataframe
        df1.to_csv(s1.replace('0',str(i+1)))
if __name__ == "__main__":
    movement_predict()
