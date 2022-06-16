from tkinter import *
r=Tk()
r.title("LAB10")


def buttonRead():
    textBox.delete("1.0",END)
    with open("C:\\Users\\zeyne\\OneDrive\\Desktop\\ce 223\\Marvel.txt") as f:
     text = f.read()
    textBox.insert("end", text)
    print(textBox)

def calculateFreq():
    textBox.delete('1.0', END)
    with open("C:\\Users\\zeyne\\OneDrive\\Desktop\\ce 223\\Marvel.txt") as f:
        string = f.read()
    stringList = []
    for word in string.split():
        stringList.append(word)

    for word in stringList:
        x=str("Frequency of "+ str(word)+ " = "+ str(stringList.count(word))+ "\n")
        textBox.insert('1.0', (x))

    textBox.pack(side=LEFT, expand=True)


    r.pack(expand=True)

l1=Label(r,text="If you click READ, it will read everything in Marvel.txt file.\n If you click CALCULATE, it will calculate frequency of the words in text file.")
l1.pack()



textBox = Text(r,bg='pink',height=50,width=50)
textBox.pack()

b1=Button(r,text ='Read',bg="white",fg="pink",font="Arial 20 bold",width=20, command =buttonRead)
b1.pack(side=LEFT)

b2=Button(r,text='Calculate',bg="white",fg="violet",font="Arial 20 bold",width=20,command=calculateFreq)
b2.pack(side=LEFT)

r.mainloop()