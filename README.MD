# Python Computer Exercise Assessment 1

## Introduction and description

The purpose of this programme is to make a communication between agents and environment. Running an animation model to display and get results.

## Installation Environment

Install Spyder (Python 3.7) from Anaconda Navigator 3 in the computer.

## Usage

Open the software Anaconda Navigator and select the 'Spyder (Python 3.7)'. Open two python files called 'agentframework.py' and 'model.py'. 'model.py' is the main programme.

The following steps illustrate the functions of python files and the usage to run Python codes.

Firstly, a python file called 'agentframework.py'. The functions of this python file which included:

1. Initilize each agent.
2. Define two agents' distance.
3. Make a connection between agents and environment.
4. Make agents move randomly.
5. Make agents communicate with each other.

Secondly, import file 'agentframework' into 'model.py'. The file 'model.py' have many functions which are

1. Get the agents information from the web.
2. Initialize animation.
3. Get the environment from the flie 'in.txt'.
4. Initialize the solid variable.
5. Make the agents from the web data.
6. Shuffle the agents list.
7. Animation the model.
8. Define and implements the agents' action.
9. Plot the agents and the environment. 
10. Do a GUI model. 

Thirdly, holding 'Shift' button, right click in the file, open the 'windows Powershell'. Input the code 'python model.py', run the model and get results.

The result: many agents in the environment move randomly in the 100x100 units, move left/right/up/down in a loop that picks randomly the way and it will go like this code:

```python
	        def move(self):
	         	      if random.random() < 0.5:
			                    self.y = (self.y + 1) % 100
	              	else:
			                    self.y = (self.y - 1) % 100
		
	              	if random.random() < 0.5:
			                    self.x = (self.x + 1) % 100
	              	else:
			                    self.x = (self.x - 1) % 100
```

## A Result

This is like 'the sheep eating grass', agents represent sheeps and black trajectories demonstrate the trace where sheeps have eaten grass. Once the agents move, there are many trajectories would be illustrated.

## License

This project is under the MIT License, please see the 'LICENSE.txt' to check details.
