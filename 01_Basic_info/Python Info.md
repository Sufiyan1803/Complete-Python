                   PYTHON INFO

Python inner working:

Python IDE
     --->Chai.py   ---->   Byte Code  ---->  Python Virtual Machine
                       (Mostly hidden)



  
  1. Compile to Byte code         #byte code is low level & platform independent


----->  Byte code runs faster
    .pyc ---> Compiled python  (frozen binaries)
 
     __pychache__


     Source change & Python version

       hello_chai.cpython-311.pyc

---->  Works only for imported files
----> NOt for top level files

------------------------------------------------------------------------------------

--------> PYTHON VIRTUAL MACHINE (PVM)
 ---> Code loop to iterate byte code
 ---> Run time Engine
 ---> Also known as python interpreter

#Byte code is NOT machine code

------------------------------------------------------------------------------------
---> Python specific interpretation
---> cpython (standard implememtation)

MORE---> jython , Ironpython , Stackless , PyPy


------------------------------------------------------------------------------------

    PYTHON SHELL

--->import os
    os.getcwd()

--->import sys
    sys.platform


---->from importlib import reload
  -->reload(what you to reload)

------------------------------------------------------------------------------------

    COMMON PYTHON ERRORS

NameError : name is not defined

IndentationError : tab, space, etc error

AttributeError : mentioned module has no attribute






NOTE:- In python variable has no datatype
      -----> memory has datatypes and assigned inside the memory 










































