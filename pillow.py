from PIL import Image
import numpy as np
import random
import string 
import secrets 


# this piece of code will convert the seed into key for PRNG 
def seed(key):
    seed=" "
    for char in key:
        if char.isdigit():
            seed+=char
        elif char.isalpha():
            seed+=str(ord(char))
        else:
            print("your seed was incorrect kindly insert the correct seed")
    #print(seed)
    return int(seed)

# it will generate a list of indexes in order the pixels get shuffle
# those indices will determine by PRNG (pseudorandom number generator) and PRNG will determined by key/seed 
def pseudoRandomnumber(array,key = None):
    if not key:
        alphabet = string.ascii_letters + string.digits 
        key = ''.join(secrets.choice(alphabet) for i in range(16)) 
        print("remember this key to decrypt your image= ", key)
    
    random.seed(seed(key)) #PRNG generator
    random_list=[]
    for i in range (len(array)-1,-1,-1):
        pick=random.randint(0,i)
        random_list.insert(0,pick)
    return random_list



# this will shuffle the pixels using FISHER YATES shuffling algorithm
def knuth_shuffles(array,key = None):
    PRNG = pseudoRandomnumber(array,key)
    #print(PRNG)
    #print(len(PRNG))

    for i in range(len(array)-1,-1,-1):
        j=PRNG[i]
        array[i],array[j]=array[j],array[i]
    return array

#this will reverse the algorithm to get the original image back
def reverse_shuffle(Shuffled_array,key = None):
    PRNG = pseudoRandomnumber(Shuffled_array,key)
    for i in range(0,len(Shuffled_array),+1):
                j=PRNG[i]
                Shuffled_array[j],Shuffled_array[i]=Shuffled_array[i],Shuffled_array[j]
    return Shuffled_array


#main code 
def main():
    
    #seed_value = 9337994969 
  
    filename = "D:\Image scrambling\scrambled_image.png"
    img = Image.open(filename)
    print(img.size)
    width,height=img.size
    pixel_list = list(img.getdata())
    print(len(pixel_list))
    Array=np.array(pixel_list,dtype=int)
    
    operation = input("""enter what operation you wanna perform 
                      A. Scramble the image ( original image to scrambled image )
                      B. Rescramble the image ( scrambled image to original image, you must have a key with you to decrypt the image ) \nYour choice:  """)

    if operation == "A" or operation == "a":
        shuffled = knuth_shuffles(Array)
        print("extracting the pixels from the image......")
        #print("shuffled list= ", shuffled)
        pixels = [tuple(row) for row in shuffled]
        #print(len(pixel_list))
        scrambled_image = Image.new("RGB", (width, height))
        scrambled_image.putdata(pixels)
        scrambled_image.save("scrambled_image.png")
        scrambled_image.show()

    elif operation == "B" or operation == "b":
        Key=input("kindly insert the key here: ")
        original_array = reverse_shuffle(Array,Key)
        #print("original_Array= ", original_array)
        pixels = [tuple(row) for row in original_array]
        original_image=Image.new("RGB",(width,height))
        original_image.putdata(pixels)
        original_image.save("original_image.jpg")
        original_image.show()
    else:
        print("your entered choice is not available, kindly enter the available choices only")


if __name__ == "__main__":
    main()



