#calc 2.py
#txtbk p. 392
from graphics import *
#following line of code is asked for in textbook but outputs error:
from button import Button
class Calculator:
#impliments simple GUI
    def __init__(self):
        #create window for calc
        win = graphWin("Calculator")
        win.setCoords(0,0,6,7)
        win.setBackground("blue")
        self.win = win
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):
        #create list of buttons, starting w standard
        bSpecs= [(2,1,'0'), (3,1,'.'),
                 (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                 (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                 (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'), (5,4,'C')]
        self.buttons = []
        for (cx,cy,label) in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),
                                       .75,.75,label))                           
        #make EQUAL button larger
            self.buttons.append(Button(self.win, Point(4,5,1),
                                       1.75, .75, "="))
        #activate buttons
            for b in self.buttons:
                b.activate()
    def __createDisplay(self):
        bg = Rectangle(Point(.5,5.5), Point(5.5,6.5))
        bg.setFill('blue')
        bg.draw(self.Win)
        text = Text(Point(3,6), "")
        text.draw(self.Win)
        text.setFace("courier")
        text.setstyle("bold")
        text.setsize(16)
        self.display = text

    def getButton(self):
        #waits for button to be clicked and returns label
        while True:
            p= self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()
                
    def processButton(self,key):
    #updates calc display
        text = self.disply.getText()
        if key == 'C':
            self.display.setText("")
        elif key =='<-':
            self.display.setText(text[:-1])
        elif key == '=':
            try:
                result = eval(text)
            except: result = 'ERROR'
            self.display.setText(str(result))
        else:
            self.display.setText(text+key)

    def run(self):
        while True:
            key = self.getButton()
            self.processbutton(key)

    if __name__ == '__main__':
        #'create a calculator object'
        theCalc = Calculator()
        #call run method
        theCalc.run()

#first program supposed to be used for calculations
        #def main():
#take user input for equation
    #equation=input("Input an equation: ")
    #Split equation to do operations
    #list = equation.split(' ')
    #while len(list)>1:
        #for i in range (1, len(list), 2):
            #Mult and Div
            #if '*' in list or '/' in list:
                #Mult
                #if list[i]=='*':
                    #result = float(list[i-1])*float(list[i+1])
                    #del list [i-1:1+2]
                    #list.insert (i-1, result)
                    #break
                #Div
                #elif list[i] == '/':
                    #result = float(list[i-1])/float(list[i+1])
                    #del list [i-1:1+2]
                    #list.insert (i-1, result)
                    #break
                #Add and Sub
            #if '+' in list or '-' in list:
                #Add
                #if list[i] == '+':
                    #result = float(list[i-1])+float(list[i+1])
                    #del list [i-1:1+2]
                    #list.insert (i-1, result)
                    #break
            #Sub
           #elif list[i] == '-':
                #result = float(list[i-1])-float(list[i+1])
                #del list [i-1:1+2]
                #list.insert (i-1, result)
                #break
            #else option
            #else:
                #print("error")

#output answer
  #?????
  #return result ?
  #print result ?
