import argparse
import turtle
from collections import Counter

ROUND_DEGREES = 360
types = {}
colors = [
    'red', 'blue', 'green', 'orange', 'yellow', 'aquamarine', 'azure', 'bisque', 'burlywood', 'chartreuse'
    ]

window = turtle.Screen()
pen = turtle.Turtle()

def word_counter(sentence):
    word_dict = Counter(sentence.split())
    return word_dict

def frequencies_dict(word_dict):
    all = 0
    freq_dict = {}
    for elem in word_dict:
        all = all + word_dict[elem]
    for elem in word_dict:
        freq_dict[elem] = word_dict[elem]/all
    return freq_dict

def add_to_dict(func):
    types[func.__name__] = func
    return func

@add_to_dict
def sectors(sentence):
    words = frequencies_dict(word_counter(sentence))
    titles = {}
    kantor = 0
    old_pos = (0, 0)
    old_heading = 0

    #drawing sectors
    for elem in words:
        pen.fillcolor(colors[kantor])
        pen.begin_fill()
       
        pen.circle(100, words[elem]*ROUND_DEGREES)
        pen.goto(0,100)
        pen.goto(old_pos)
        pen.end_fill()

        pen.seth(old_heading)
        pen.circle(100, words[elem]*ROUND_DEGREES)
        old_heading = pen.heading()
        old_pos = pen.pos()

        titles[elem] = kantor
        kantor = kantor + 1

    #drawing titles
    kantor = 0
    pen.up()
    pen.goto(200,200)
    for elem in titles:
        pen.goto(200,200-kantor*20)
        pen.down()
        #color identification
        pen.fillcolor(colors[titles[elem]])
        pen.begin_fill()
        pen.circle(5)
        pen.end_fill()
        pen.up()
        pen.goto(pen.xcor(), pen.ycor()-3)
        #title
        pen.goto(pen.xcor()+15, pen.ycor())
        pen.write(elem, font=("Arial", 11, "normal"))
        kantor = kantor + 1
    window.exitonclick()

@add_to_dict
def rays(sentence):
    words = word_counter(sentence)
    kantor = 0
    step = 50
    gap = ROUND_DEGREES/len(words)

    for elem in words:
        pen.color(colors[kantor])
        pen.setheading(kantor*gap)
        pen.down()

        for _ in range(0,words[elem]):
            pen.fd(step)
            pen.circle(1)
        
        pen.up()
        pen.fd(20)
        pen.write(elem, font=("Arial", 11, "normal"))
        pen.home()
        kantor = kantor + 1

    window.exitonclick()

def paint_diagram(sentence, dtype):
    types[dtype](sentence)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Constructing diagram of word frequencies in a sentence")
    parser.add_argument('-dtype', help = 'diagram type')
    parser.add_argument('-sentence', help = 'sentence to construct diagram from')
    args = parser.parse_args()
    paint_diagram(args.sentence, args.dtype)