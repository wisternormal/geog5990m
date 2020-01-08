import random
import operator


import agentframework
import csv

import matplotlib.pyplot
import matplotlib.animation


# using this to do GUI
import tkinter
import matplotlib
matplotlib.use('TkAgg') 


# using this to get agents form the web
import requests
import bs4

# get the agents information from the web
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


# initialize animination
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# get the environment from flie
# f = open('in.txt', newline='')
f = open('in.txt')
environment = []
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    rowlist = []
    for value in row:				# A list of value
    	rowlist.append(value)
    environment.append(rowlist)
f.close()
# Don't close until you are done with the reader;
# the data is read on request.

# initialize the solid variable
num_of_agents = 10
num_of_iterations = 1000
neighbourhood = 20
agents = []

# Make the agents from the web data.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents,x,y))


# shuffle the agents list
random.shuffle(agents)


# animanation the model
def update(frame_number):
    
    fig.clear()   

# deifne and implements the agents' action
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

# plot the agents and the environment
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment)        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)


# do a GUI mdoel
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False, interval=300)
    canvas.draw()


root = tkinter.Tk()

# this is title which can modify
root.wm_title("Agents Model")

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()