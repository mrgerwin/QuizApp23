from guizero import App, Text, PushButton, ButtonGroup, Picture, TextBox
import random

def nameChanged():
    pass

def shuffleChoices():
    pass

def nextPressed():
    pass
    
def updateQuestion():
    pass

def checkAnswer():
    pass
    
def submitPressed():
    pass
    

questionList = []
question1 = "Select the word that means an object from some class."
question2 = "Variables that are used to describe data of objects are called _______________."
question3 = "Functions that are used to describe the behavior of objects are called _______________."
question4 = "What is a string when referred to in computer programming?"
question5 = "In computer programming, is a list a type of function?"

questionList.append(question1)
questionList.append(question2)
questionList.append(question3)
questionList.append(question4)
questionList.append(question5)


answerList = ["Instance", "Properties", "Methods", "Text", "No"]
choicesList = [["Creation", "Instance", "Establishment", "Definition"], ["Properties","Numbers", "Files", "Descripters"], ["Regulators", "Events", "Elaborators", "Methods"],["Yarn", "Guitars", "Text", "Functions"], ["Yes", "No"]]

ImageList = ["ImageQuestion1.png", "ImageQuestion2.png", "ImageQuestion3.png", "ImageQuestion4.png", "ImageQuestion5.png"]
index = 0

app = App(title="Quiz App", height = 800, width = 1200)
nameLabel = Text(app, text="Your Name: ")
nameTextBox = TextBox(app)
picture = Picture(app, image = "ImageQuestion1.png")
question = Text(app, text = question1)
submitButton = PushButton(app, text = "Submit Answer", command = submitPressed)
nextButton = PushButton(app, text = "Next Question", command = nextPressed)
answerChoices = ButtonGroup(app, options = ["Creation", "Instance", "Establishment", "Definition"], selected = None)


app.display()