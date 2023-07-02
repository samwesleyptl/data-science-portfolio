import pandas as pd
import cv2
import statistics
import matplotlib.pyplot as plt
def snoring_predict():
    # Save image in set directory
    # Read RGB image
    img = cv2.imread(r'C:\Users\samwe\OneDrive\Desktop\Sam\snoring\images\snoring1.png')
    #print(img)
    '''
    meannomov=statistics.mean(img)
    stddevnomov=statistics.stdev(img)
    '''
    # Output img with window name as 'image'
    cv2.imshow('image', img) 
    # Maintain output window utill
    # user presses a key
    cv2.waitKey(0)        
      
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    img = cv2.imread(r'C:\Users\samwe\OneDrive\Desktop\Sam\snoring\images\snoring2.png')
    '''
    meanmov=statistics.mean(img)
    stddevmov=statistics.stdev(img)
    '''
    print("Image")
    print(img[120:560,360:505].mean)
    # Output img with window name as 'image'
    cv2.imshow('image', img[120:560,360:505]) 
      
    # Maintain output window utill
    # user presses a key
    cv2.waitKey(0)        
      
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    cv2.imshow('image', img[120:560,705:850]) 
      
    # Maintain output window utill
    # user presses a key
    cv2.waitKey(0)        
      
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    cv2.imshow('image', img[120:560,1028:1180]) 
      
    # Maintain output window utill
    # user presses a key
    cv2.waitKey(0)
    
      
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    s=[]
    s=r'C:\Users\samwe\OneDrive\Desktop\Sam\snoring\test_data\test0.csv'
    s1='snoringresult0.csv'
    check=0
    snore=[]
    for i in range(5):
        snore=[]
        df = pd.read_csv(s.replace('0',str(i+1)))
        print(df)
        l=len(df.iloc[:,0])
        plt.plot(list(range(l)),df.iloc[:,0])
        plt.savefig('mnm.png')
        plt.close()
        img = cv2.imread(r'mnm.png')
        cv2.imshow('image',img) 
        vibrations=[]
        # Maintain output window utill
        # user presses a key
        cv2.waitKey(0)        
              
        # Destroying present windows on screen
        cv2.destroyAllWindows()
        check=df.iloc[0,0]
        for j in range(0,l,600):
            vibrations=[]
            sum1=0
            c=600
            if j+599>l:
                c=l-j
            for k in range(c):
                if k==0:
                    vibrations.append(0)
                if k>0:
                    if df.iloc[j+k,0]==check:
                        vibrations.append(1)
                    else:
                        vibrations.append(1)
                        check=df.iloc[j+k,0]
            for k in range(c):
                if vibrations[k]==1:
                    sum1+=1
            if sum1 > 5:
                for k in range(c):
                    snore.append("Yes")
            else:
                for k in range(c):
                    snore.append("No")
        '''
        if statistics.stddev(df)>=stddevmov:
            print("Movement")
        else:
            print("No Movement")
        '''
        dict = {'Vibrations': df.iloc[:,0], 'Snoring': snore}
        df1 = pd.DataFrame(dict)
        # saving the dataframe
        df1.to_csv(s1.replace('0',str(i+1)))
if __name__ == "__main__":
    snoring_predict()
