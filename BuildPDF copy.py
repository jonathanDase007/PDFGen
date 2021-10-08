from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import inch, cm
from PyPDF2 import PdfFileMerger, PdfFileReader

import random


PAGEWIDTH = 8.5 * inch
PAGEHEIGHT = 11*inch

#list of Students

names = []
for x in range(100):
    names.append(str(x))
TITLE = "Addition Practice"

difficulty = 4
#1: single digits
#2: two digits and no carry over
#3: two digits carry over
#4: three digits carry over

sign = '+'


#Centers String
def CenterStirng(canvas, words, font, fontsize, y):
    canvas.drawString(((PAGEWIDTH - stringWidth(words, font, fontsize))/2), y * inch, words)


def GenerateProb(canvas, yVal, xVal, x1, y1, sign, font, fontsize, space, width):
    canvas.setFont(font, fontsize)
    yVal = (5 - len(str(yVal)))*' ' + str(yVal)
    xVal = sign + (5 - len(str(xVal)))*' ' + str(xVal)
    canvas.drawString(x1 * inch + stringWidth(xVal, font, fontsize) - stringWidth(yVal, font, fontsize), y1*inch, yVal)
    canvas.drawString(x1 * inch, (y1-space) * inch, xVal)
    canvas.drawString(x1 * inch, (y1-space) * inch, round(len(xVal) * width)*"_")
    print()

for name in names:
    canvas = Canvas(name + ".pdf", pagesize=(PAGEWIDTH, PAGEHEIGHT))
    answers = Canvas(name + "-Answers.pdf", pagesize=(PAGEWIDTH, PAGEHEIGHT))

    #Set Title
    canvas.setFont("Times-Bold", 25)
    answers.setFont("Times-Bold", 25)
    CenterStirng(canvas, TITLE, "Times-Bold", 25, 10.3)
    CenterStirng(answers, TITLE, "Times-Bold", 25, 10.3)


    #Sets Font
    canvas.setFont("Times-Bold", 14)
    answers.setFont("Times-Bold", 14)

    #Sets Name
    canvas.drawString(1*inch, 9.7*inch, "Name:  ")
    canvas.drawString(.99*inch, 9.7*inch, "            " + 12*"_")
    #canvas.drawString(.99*inch, 9.7*inch, "            " + round(len(names)* 1.78)*"_")


    answers.drawString(1*inch, 9.7*inch, "Name:  ")
    answers.drawString(.99*inch, 9.7*inch, "            " + 12*"_")
    #answers.drawString(.99*inch, 9.7*inch, "            " + round(len(names)* 1.78)*"_")



    #Other Text boxes
    CenterStirng(canvas, "Date:  ______________", "Times-Bold", 14, 9.7)
    CenterStirng(answers, "Date:  ______________", "Times-Bold", 14, 9.7)
    canvas.drawString(6.5*inch, 9.7*inch, "Score:__/30")
    answers.drawString(6.5*inch, 9.7*inch, "Score:__/30")

    #Generates problems
    n = 8.7
    number = 1
    for b in range(5):
        c = .9
        for i  in range(6):
            sum = 0

            #Difficulty level 1: only single digit number
            if(difficulty == 1):
                #addition or Mult
                if(sign == '+' or sign == "x"):
                    x = random.randint(0, 10)
                    y = random.randint(0, 10)
                #Subtraction
                elif(sign == '-'):
                    x = random.randint(0, 10)
                    y = random.randint(0, x)


            elif(difficulty == 2):
                #addition or Mult
                if(sign == '+' or sign == "x"):
                    x = random.randint(0, 30)
                    y = random.randint(0, 30)
                #subtraction
                elif(sign  == '-'):
                    x = random.randint(0, 30)
                    y = random.randint(0, x)

                    print("Here")
                    while(str(y)[-1] > str(x)[-1]):
                        x = random.randint(0, 30)
                        y = random.randint(0, x)
                    
            
            elif(difficulty == 3):

                #addition or Mult
                if(sign == "+" or sign == "x"):
                    x = random.randint(0, 100)
                    y = random.randint(0, 100)
                
                #subtraction
                elif(sign == "-"):
                    x = random.randint(0, 30)
                    y = random.randint(0, x)

            elif(difficulty == 4):
                #addition or Mult
                if(sign == "+" or sign == "x"):
                    x = random.randint(0, 200)
                    y = random.randint(0, 200)
            
                elif(sign == "-"):
                    y = random.randint(0, 100)
                    x = random.randint(0, 100)

            if(sign == "+"):
                sum = x + y
            elif(sign == "-"):
                sum = x - y
            elif(sign == "x"):
                sum = x * y

            GenerateProb(answers, x, y, c, n, sign, "Times-Bold", 20, .3, .8)
            GenerateProb(canvas, x, y, c, n, sign, "Times-Bold", 20, .3, .8)


            answers.setFont("Times-Bold", 20)
            answers.drawString((c+.25) * inch, (n-.7)* inch, str(sum))
            
            c += 1.2
            number += 1
        n -= 1.7
    answers.setFont("Times-Bold", 15)
    canvas.setFont("Times-Bold", 15)

    answers.drawString((7.2) * inch, (.2)* inch, "NextsMath")
    canvas.drawString((7.2) * inch, (.2)* inch, "NextsMath")


    canvas.save()
    answers.save()

