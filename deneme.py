with open("C:\\Users\\zeyne\\OneDrive\\Desktop\\ce 223\\Marvel.txt") as f:
    data=f.readlines()
    content="".join(data)
    print(content)

from tkinter import *




r=Tk()
r.title('Empty Example')



#first method
def function():
 f=open("C:\\Users\\zeyne\\OneDrive\\Desktop\\ce 223\\Marvel.txt")
 for x in f:
  print(x)
 f.write(ent1.get())
 f.close()

#second method
def calculate():
 file = open("C:\\Users\\zeyne\\OneDrive\\Desktop\\ce 223\\Marvel.txt", "r")
 content = []
 for line in file:
  for word in line.split():
   content.append(word)
 content2 = []
 content3 = []
 for word in content:
  if word in content2:
   continue
  else:
   content3.append(str(word) + " = " + str(content.count(word)))
   content2.append(word)
 print(content3)


ent1 = Entry(r)
ent1.grid(row=1, padx=10)

name =StringVar()


button1 = Button(r, text ='Hello',bg="white",fg="pink",font="Arial 20 bold",width=20, command =function)
button1.pack(side=LEFT)


button2=Button(r,text='Hello2',bg="white",fg="violet",font="Arial 20 bold",width=20,command=calculate)
button2.pack(side=LEFT)
ent1.pack()
r.mainloop()
''' Please design an interface which is a box with 2 buttons and a textBox
The first button is called READ and when clicked it will read everything inside the text file. 
Then, the contents will be printed inside textBox.
The second one is called CALCULATE and when clicked, it will calculate the frequency of the 
words in the text file. Then, the contents will be printed inside textBox. Of course, before 
printing the new data clear the textBox first
'''
