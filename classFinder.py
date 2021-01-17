from tkinter import *
import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl = "http://registrar.indiana.edu/browser/soc4172/index.shtml"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")




class Application (Frame):

    def __init__ (self, master):
        Frame.__init__ (self, master)
        self.grid()
        self.create_widget()

    def create_widget (self):

        self.label1 = Label (self, text = 'Graduate or Undergraduate:')
        self.label1.grid (row = 0, column = 0, sticky = W)
        
        self.label2 = Label (self, text = 'Department:')
        self.label2.grid (row = 1, column = 0, sticky = W)

        self.label3 = Label (self, text = 'Subject:')
        self.label3.grid (row = 2, column = 0, sticky = W)
        
        self.radioVar1 = StringVar()
        self.radioVar1.set('under')
        
        self.radio1 = Radiobutton (self, text = 'Graduate', value = 'grad', variable = self.radioVar1)
        self.radio1.grid (row = 0, column = 1, sticky = E)        

        self.radio2 = Radiobutton (self, text = 'Undergraduate', value = 'under', variable = self.radioVar1)
        self.radio2.grid (row = 0, column = 2)
        
        x = self.radioVar1.get()

        self.entry1 = Entry (self, width = 10)
        self.entry1.grid (row = 1, column = 1, sticky = E)

        self.entry2 = Entry (self, width = 10)
        self.entry2.grid (row = 2, column = 1, sticky = E)

        self.submit = Button(self, text='Select', command=self.run)
        self.submit.grid(row = 2, column = 2, columnspan = 1)

    def run(self):

        dept = ''
        dept = str(self.entry1.get())

        subject = ''
        subject = self.entry2.get()

        theurl2 = "http://registrar.indiana.edu/browser/soc4172/" + dept + "/index.shtml"
        thepage2 = urllib.request.urlopen(theurl2)
        soup2 = BeautifulSoup(thepage2, "html.parser")
        
        if self.radioVar1.get() == 'grad':
            for link in soup2.findAll('a'):
                if link.text[:3] == str(dept[:3]):
                    if link.text[-3] in (str('5'),str('6'),str('7'),str('8'),str('9')):
                        if link.text[-5] == str(subject):
                            rowList = []
                            for td in soup2.findAll('td'):
                                rowList += td.text.split()
                                linkList = link.text.split()
                            for item in range(0,len(rowList)):
                                if rowList[item] == linkList[0]:
                                    if rowList[item + 1] == linkList[1]:
                                        string = ''
                                        string = string + rowList[item] + ' '
                                        string = string + rowList[item + 1] + ' '
                                        dept = dept + '-'
                                        if str(rowList[item + 2][:5]) != str(dept[:5]):
                                            try:
                                                int(rowList[item + 2])
                                            except:
                                                string = string + rowList[item + 2] + ' '     
                                        if str(rowList[item + 3][:5]) != str(dept[:5]):
                                            try:
                                                int(rowList[item + 3])
                                            except:
                                                string = string + rowList[item + 3] + ' '
                                        if str(rowList[item + 4][:5]) != str(dept[:5]):
                                            try:
                                                int(rowList[item + 4])
                                            except:
                                                string = string + rowList[item + 4] + ' '
                                        if str(rowList[item + 5][:5]) != str(dept[:5]):
                                            try:
                                                int(rowList[item + 5])
                                            except:
                                                string = string + rowList[item + 5] + ' '
                                        print (string)
    
        if self.radioVar1.get() == 'under':
            for link in soup2.findAll('a'):
                if link.text[:3] == str(dept[:3]):
                    if link.text[-3] in (str('1'),str('2'),str('3'),str('4')):
                        if link.text[-5] == str(subject):
                            rowList = []
                            for td in soup2.findAll('td'):
                                rowList += td.text.split()
                                linkList = link.text.split()
                            for item in range(0,len(rowList)):
                                if rowList[item] == linkList[0]:
                                    if rowList[item + 1] == linkList[1]:
                                        string = ''
                                        string = string + rowList[item] + ' '
                                        string = string + rowList[item + 1] + ' '
                                        dept = dept + '-'
                                        if str(rowList[item + 2][:5]) != str(dept[:5]):
                                            try:
                                                int(rowList[item + 2])
                                            except:
                                                string = string + rowList[item + 2] + ' '     
                                        if str(rowList[item + 3][:5]) != str(dept[:5]):
                                            try:
                                                int(rowList[item + 3])
                                            except:
                                                string = string + rowList[item + 3] + ' '
                                        if str(rowList[item + 4][:5]) != str(dept[:5]):
                                            try:
                                                int(rowList[item + 4])
                                            except:
                                                string = string + rowList[item + 4] + ' '
                                        if str(rowList[item + 5][:5]) != str(dept[:5]):
                                            try:
                                                int(rowList[item + 5])
                                            except:
                                                string = string + rowList[item + 5] + ' '
                                        print (string)
                            

                
root = Tk()
root.title ('Course Finder')
root.geometry ('500x150')
root.resizable (width = TRUE, height = TRUE)

app = Application (root)
root.mainloop()
