#!/usr/bin/env python
# coding: utf-8

# In[2]:


import turtle
shelly=turtle.Turtle()
shelly.shape('turtle')
shelly.color('light blue')
shelly.shapesize(1,0.5)
shelly.forward(100)
shelly.left(60)
shelly.right(10)


# In[1]:


for shelly in range(8):
    print(shelly)


# In[4]:


#Repeat 6 times the following:   
#        repeat 4 times the following:
#                 move 100 steps forward
#                 turn 90 degrees to the left
#       turn 60 degrees to the right.
import turtle
shelly=turtle.Turtle()
shelly.shape('turtle')
shelly.color('purple')
shelly.shapesize(1,0.2)
i=1
y=1
for i in range(6):
    for y in range(4):
        shelly.forward(100)
        shelly.left(90)
    shelly.right(60)
    


# In[1]:


#repeat 36 times the following:
#        repeat 6 times the followings:
#                   move 100 steps foward
#                   turn 60 degrees to the left 
#       turn at 10 degrees to the right.
import turtle
shelly=turtle.Turtle()
shelly.shape('turtle')
shelly.color('light blue')
shelly.shapesize(1,0.5)
z=1
x=1
for z in range(36):
    for x in range(6):
        shelly.forward(100)
        shelly.left(60)
    shelly.right(10)


# In[ ]:




