#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. In the below elements which of them are values or an expression? 
eg:- values can be integer or string and expressions will be mathematical operators.
    
*   is expression or variable operator according to the given data
A=10    a1=A*3	=30
A="Hi"	a2=A*3	=HiHiHi
'hello'	= value
-87.8	=value
- =expression
(=expression)
+ =expression
6 =value


# In[ ]:


get_ipython().run_line_magic('pinfo', 'variable')
String is a data type in python. Variable is a storage container, which stores the assigned data type either be integer, 
float or string or Boolean.  

Name= ”Shivaprrasad”   #Here Name is string data type
Value=5	 #Value is variable which stores any value	


# In[ ]:


3. Describe three different data types.
In python there are several data types like 

Integers =to  represent integers to represent integer values
Float	= to represent with decimal values
Strings	= to represent text values
Lists= to represent set of integer , float or strings
Other data types also like tuple, dictionary, sets  etc..


# In[ ]:


get_ipython().run_line_magic('pinfo', 'do')
An expression is used to operate some set of calculations or a code to produce an output value .
it can be used to perform the some set of operations and new value be assigned to new variable


# In[ ]:


get_ipython().run_line_magic('pinfo', 'statement')
Here we are assigning the value 10 to a variable spam. 

Spam =10  # expression
Spam=spam *3 #Expression
Print(spam)	# Statement
Expressions produce a value where as statement to perform an action, it may not produce value


# In[ ]:


get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1
print(bacon) = 22 only. Because after adding 1 to bacon i.e   22+1=23 is not reassigned to bacon. hence output will be 22
bacon = bacon +1 or  
bacon += 1


# In[ ]:


get_ipython().run_line_magic('pinfo', 'be')

'spam' + 'spamspam'
'spam' * 3
Answer1 = spamspamspam
Answer2= spamspamspam
Here *  can be used as an expression sometimes or can be used as an statement


# In[ ]:


get_ipython().run_line_magic('pinfo', 'invalid')
Variables can not start or assigned with numeric values like

Eggs = 10  right
 100=10  wrong  ..in python variable cannot start with numeric
Like wise variable cant be eg..My Eggs=10  wrong.no space
10Eggs	=100 is  wrong.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'value')
Int()   = int(10.2)= 10
Float()	= Float(12)	=12.0
Str()	=str(10)	='10'


# In[ ]:


get_ipython().run_line_magic('pinfo', 'it')

'I have eaten ' + 99 + 'burritos'
It can concatenate string only. 
To overcome this error we can use this expression.
'I have eaten'+'99'+'burritos'
'Ihaveeaten'+str(99)+'burritos'

