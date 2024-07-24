# Numbers in Python

## Operator Precendence (Highest to Lowest)
- Parenthesis (grouping): ```()```
- Exponentiation: ``` ** ```
- Unary Positive, Unary Negative, Bitwise Negotion : ```+x, -x, ~x```
- Arithmetic ``` * ,  / , %, +, -  ```
- Left Shift , Right Shift : ``` <<, >> ```
- Bitwise AND : ```&```
- Bitwise XOR : ```^```
- Bitwise OR : ```|```
- Comparison : ``` == , !=, < , > , <=, >=```
- Identity : ```is, is not ```
- Membership : ```in, in not ```
- Boolean NOT : ``` not ```
- Boolean AND : ``` and ```
- Boolean OR : ``` or ```

## Precision Example
```
x = 2
y = 5
z = 7

x + y --> 7
x + z --> 9 

x + y * z --> 37 # Here Multiplication has higher precision

(x+y) * z --> 49 # Here Paranthesis has higher precision
```
## Different DT issues

- Add integer with Floating decimal ``` 10 + 2.5  = 12.5```, Works But Not Good Practice!
- Optimized Solution : ``` 10 + int(2.5) = 12``` OR ``` float(10) + 2.5 = 12.5```.
- Add strig with integer ``` 'sohail' + 2  = Error```, Not Works
- Optimized Solution : ``` 'sohail' + 'shaikh' -> sohailshaikh```

## Output is in Tuple if we call ek sath
- ``` x , y , z --> (2, 5, 7) ```
- ``` x + 1, y * 2 --> (3, 10)```

## Python Powerful Number Handling Capability
- ``` 100 ** 2 --> 10000```
- ``` 2 ** 100 --> 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376```