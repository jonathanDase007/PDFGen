from fpdf import FPDF
import fpdf
import datetime


c = FPDF()


c.add_page()

def genTop(pdf, name, probs):

    date = datetime.datetime.now()
    day = str(date.month) +'/' + str(date.day) + '/' + str(date.year)

    pdf.set_font("Times", style = 'B', size = 15)



    pdf.cell(pdf.get_string_width("         Name:  " + name), 10, txt = "         Name:  " + name, ln = 0, align = 'L')
    pdf.set_font("Times", size = 12)
    pdf.cell(130, 10, txt = day, align = 'R')
    print(pdf.get_string_width('1234'))

    pdf.ln(' ')
    pdf.set_font("Times", style = 'B', size = 20)
    pdf.cell(200, 10, txt = probs, align = 'C')


    #pdf.line(0, 35, 200, 35)
    pdf.rect(x = 10, y = 32, w = 190, h = 1, style = 'F')

def ProbGen(pdf, x, y, part1, part2, size):
    pdf.set_font("Times", size = size)

    pdf.cell(x, y, txt = str(part1), align = 'C')
    #pdf.ln(' ')
    pdf.cell(x, y+30, txt = str(part2), align = 'C')
    

    





genTop(c, "Jonny", "Addition Practice")
ProbGen(c, -370, 55, 100, 20, 20)
c.output("GFG.pdf")

