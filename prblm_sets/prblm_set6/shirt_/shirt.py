#implementing a programme that accepts two command line arg
#1st- name or path of jpeg or png to read and other to write
#overlay the png on input after resizing the input to the same size
#save the result as output 
#%%
import sys
from PIL import Image,ImageOps
#checking file for conditions of validity
#%%

def main():
    old_img,new_img=arg_check()
    output_maker(old_img,new_img)

#checking file for conditions of validity    
def arg_check():

    try:#taking CLA
        old_img = sys.argv[1]
        new_img = sys.argv[2]

    except IndexError:
        sys.exit("Too few command-line arguments")

    if len(sys.argv)>3: # for >2 CLA
        sys.exit("Too many command-line arguments")
    #checking for file type
    elif old_img[-4:] in [".jpg",".png"] or old_img[-5:].endswith(".jpeg"): 
        if old_img[-4:] in [".jpg",".png"] or old_img[-5:].endswith(".jpeg"):       
            if new_img[-4:]==old_img[-4:] or new_img[-5:]==old_img[-5:]:
                return old_img,new_img
            sys.exit("Input and output have different extensions")
        sys.exit("Invalid output")
    sys.exit("Invalid input")   

def output_maker(o,n):
    
    try:
       #%%
        #getting size of shirt img
        with Image.open("shirt.png") as shirt:
            shirt_size = shirt.size  
            #%%
            print(shirt_size)
            #no () as it is not a fn just returns a tuple 
            with Image.open(o) as o_img:
                # o_crop = o_img.resize(shirt_size) 
                #NOT use as it not preserves the aspect ratio of img,distorts it to fit
               
                # o_crop = ImageOps.pad(o_img,shirt_size)
               #.pad tries to show whole image by adding balck bars if needed
               
                o_crop = ImageOps.fit(o_img,size=shirt_size)
               #this just crops the image while preserving aspect ratio.
                print(o_crop.size)
                #inside ImageOps
                #prsrvs aspect ratio not distorts it

                #overlaying both images
                o_crop.paste(shirt, shirt) #returns none,thus no assignment to variabe
                #directly edits orignial img
                
                o_crop.save(n)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    
# %%

if __name__=="__main__":
    main()