#presets
coloumn = 0
row = 0
table = ""
height=0
width=0
current_pixel=0
state=0



#states
on="[]"
off="--"



#sizes
width=int(input("enter desired width: "))
height=int(input("enter desired height: "))
print(width,"x",height)



#single pixels
pixel=[0,0,1,1,5,2,7,9,6,4]
#print(pixelx[0],pixely[1])



#screen creator
while (coloumn<height):
    while (row<width):
        while (current_pixel<len(pixel)):
            if(row==pixel[(current_pixel)] and coloumn==pixel[(current_pixel+1)]):
                state=True
            current_pixel=current_pixel+2
        current_pixel=0



        if(state==True):
            table=(table+on)
        else:
            table=(table+off)
        if (row>(width-2)):
            table=(table+"\n")
        


        state=False



        row=row + 1
    row=0
    coloumn=coloumn + 1
#putting the screen into terminal
print (table)