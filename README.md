# UX-UI development
This is a repository about user interface development, 
and it contains several tasks that I did in my university classes

### Lab 1: merge files
Write a console application to combine two text files into a third

**Comment from me**: use my code running with this command

`python lab1.py <first_file.txt> <second_file.txt> <output_file.txt>`

### Lab 2: hash
Write a program that calculates the blf-crypt hash transmitted via pipe/standard input;
The program should run without standard input by displaying a message about how to use it.

**Comment from me**: launching via echo '<string>' | python lab2.py

### Lab 3: curses printing
Using the _curses_ library, implement a "running line" that stops working when you press any
(not any, but any "press any key") key.

If possible, please:
* use text written using ascii art.;
* use colors;
* work out the potential problems that arise when resizing the window.

You can rely at least on
https://docs.python.org/3/howto/curses.html
https://docs.python.org/3/library/curses.html

A few facts:

* the window sizes are determined by variables https://docs.python.org/3/library/curses.html#curses.COLS
* when working on windows, you must first install https://pypi.org/project/windows-curses / (nothing special is required when importing)

### Lab 4: design
1. Get inspired [Artiom Dasinsky - Solving Product Design Exercises](resources/Artiom_Dasinsky_-_Solving_Product_Design_Exercises.pdf) (the first 55 pages should be enough)
2. To develop a product design that allows conducting a student survey

### Lab 5: please, login
Choose TUI-framework and realise login window from the previous task

### Lab 6: mockup
Using _figma_ or similar drawing tools, "sketch" the layout of the graph drawing application.

* the object to be drawn (function, set, surface, ...) should be different for everyone; you should write them here
* the interface must contain at least three controls for the rendered content.

**About me:** I chose cubic functions

### Lab 7: planning + state
1. You have to select technology stack (programming language + graphics framework + rendering library)
to implement the invented program;
2. Draw diagram of program's operating conditions.

**About me:** Python + Matplotlib + Tkinter
### Lab 8: template
Based on the decisions made in the framework of tasks 6 and 7, implement the preparation of an application for drawing graphs.

The blank must:
* launch, show the main program window
* be accompanied by recommendations on the launch method
* have an implemented mechanism for changing and storing interface state parameters
(i.e. storing parameter values that determine the type of the object being rendered)

### Lab 9: "complexity" as common ingredien
During development, it is not uncommon for it to be necessary to add something unplanned to the program from the beginning.
A problem that was suddenly added to the solution after solution 8 task is proposed: when changing the parameters, the rendered object should change beautifully smoothly.
That is, it is necessary:

* refine solution 8 task to a working rendering in the program interface
* add smoothness to object changes when changing rendering parameters

### Lab 10: terms or reference
After reviewing the

* https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5
* https://habr.com/ru/post/300420/

try to compose in md format and submit a draft of the terms of reference for the preparation of a program similar to the one you got in task 9.

### Lab 11: go faster
Testing the solution of task 9 showed that, in some cases, the appearance of the rendered item does not change smoothly enough. In order to eliminate this problem, it was decided to test the capabilities of immediate mode graphical interfaces.
Implement the rendering of a 5-task object using imgui (see https://dearpygui.readthedocs.io and bindings for different languages https://github.com/ocornut/imgui/wiki/Bindings )

The program should:
* illustrate a smooth transition from task 9
* Show the operating frame rate (fps)

The program may not contain interface elements for parameter management (smooth transition can be set with hard-skinned parameters)

### Lab 12: what user wants?
There was a need to develop an application for X
Financing allows you to spend some time researching user needs. Since you work in a startup, interviews with a small number of unfamiliar people who are part of the target audience were chosen from the research methods (~guerrilla testing)

Choose X. (if it's hard, work with a questionnaire of 4 and mention it, but try to think not only from the point of view of the interviewees, but also from the point of view of those who use the survey results)

Guided by approximately [The_user_experience_team_of_one](resources/The_user_experience_team_of_one.pdf) (page 126, 8th method) make and submit one of two (optional):
* a list of questions that you plan to ask your interlocutors
* mind-map for making a list of questions

**About me:** I chose an app for planning and organizing mountain hikes and made mind-map.

### Lab 13: bits
When working with interfaces, there are quite a few small tasks for working out user interaction, the existing experience in solving which allows you to move faster.

Select an interaction option from the list below, name it here (you can add details if they are not enough in the formulation of the option):

* interception of drag and drop with subsequent display of file contents (text, images, ...)
* display of data/dataset in a hierarchical list (dataset from the network of your choice, at least 3 levels of hierarchy)
* create a context menu (cut-copy-paste for the text input field)

**About me:** I selected a context menu

### Lab 14: packaging

The part of the program that the user cannot help but notice is its packaging: the dependency installation system and/or the program itself.

* select the code from one of the past classes that you want to pack 
* select the platform for which you will produce the packaging

**About me:** I selected 13 task
