1. To make sure that you can interact with the Python interpreter, try the following steps on your computer:
- Start the Python interpreter in interactive mode.
- At the prompt, type the following statement then press Enter:
  
> `print('This is a test of the Python interpreter.')` **Enter**
> 
- After pressing the Enter key, the interpreter will execute the statement. If you typed everything correctly, your session should look like this:

> `This is a test of the Python interpreter.`

- If you see an error message, enter the statement again, and make sure you type it exactly as shown.
  
- Exit the Python interpreter. (In Windows, press Ctrl-Z followed by Enter. On other systems, press Ctrl-D.)


2. To make sure that you can interact with IDLE, try the following steps on your computer:

- Start IDLE. To do this in Windows, type IDLE in the Windows search box. Click the IDLE desktop app, which will be displayed in the search results.
- When IDLE starts, it should appear similar to the window previously shown At the prompt, type the following statement then press Enter:


> `print('This is a test of IDLE.') **Enter**`

- After pressing the Enter key, the Python interpreter will execute the statement. If you typed everything correctly, your session should look like this:


> `This is a test of IDLE.`

- If you see an error message, enter the statement again and make sure you type it
exactly as shown.
- Exit IDLE by clicking File, then Exit (or pressing Ctrl-Q on the keyboard).


3. Use what you’ve learned about the binary numbering system in this chapter to convert the following decimal numbers to binary:
  
```
14

87

128

254
```

> Answer

---
14 = 8 + 4 + 2 = 

2<sup>3</sup> + 2<sup>2</sup> + 2<sup>1</sup> 

0x2<sup>7</sup> + 0x2<sup>6</sup> + 0x2<sup>5</sup> + 0x2<sup>4</sup> + 1x2<sup>3</sup> + 1x2<sup>2</sup> + 1x2<sup>1</sup> + 0x2<sup>0</sup>

This means the second, third, and fourth digits of the byte digit is turned on ( are 1).
00001110 = 14

---

87 = 64 + 16 + 4 + 2 + 1 

0x2<sup>7</sup> + 1x2<sup>6</sup> + 0x2<sup>5</sup> + 1x2<sup>4</sup> + 0x2<sup>3</sup> + 1x2<sup>2</sup> + 1x2<sup>1</sup> + 1x2<sup>0</sup>

01010111 = 87

---

128 = 1x2<sup>7</sup> + 0x2<sup>6</sup> + 0x2<sup>5</sup> + 0x2<sup>4</sup> + 0x2<sup>3</sup> + 0x2<sup>2</sup> + 0x2<sup>1</sup> + 0x2<sup>0</sup>

10000000 = 128

---

254 = 1x2<sup>7</sup> + 1x2<sup>6</sup> + 1x2<sup>5</sup> + 1x2<sup>4</sup> + 1x2<sup>3</sup> + 1x2<sup>2</sup> + 1x2<sup>1</sup> + 0x2<sup>0</sup>

11111110 = 254

---

<br>

4. Use what you’ve learned about the binary numbering system in this chapter to convert the following binary numbers to decimal:

```
101

1111

110010
```


> Answer

101 = 00000101


0x2<sup>7</sup> + 0x2<sup>6</sup> + 0x2<sup>5</sup> + 0x2<sup>4</sup> + 0x2<sup>3</sup> + 1x2<sup>2</sup> + 0x2<sup>1</sup> + 1x2<sup>0</sup>

0+0+0+0+0+4+0+1 = 5

---

1111 = 00001111 

 0x2<sup>7</sup> + 0x2<sup>6</sup> + 0x2<sup>5</sup> + 0x2<sup>4</sup> + 1x2<sup>3</sup> + 1x2<sup>2</sup> + 1x2<sup>1</sup> + 1x2<sup>0</sup>

  0+0+0+0+8+4+2+1 = 15

---

110010 = 00110010 

0x2<sup>7</sup> + 0x2<sup>6</sup> + 1x2<sup>5</sup> + 1x2<sup>4</sup> + 0x2<sup>3</sup> + 0x2<sup>2</sup> + 1x2<sup>1</sup> + 0x2<sup>0</sup>

0+0+32+16+8+0+2+0 = 50

---


5. Look at the ASCII chart in Appendix C and determine the code of the first printable
character (a space), the “A” character, and the “a” character.

According to ASCII "A" has value of 65 and "a" has a value of 97.

65 = 64 + 1 

0x2<sup>7</sup> + 1x2<sup>6</sup> + 0x2<sup>5</sup> + 0x2<sup>4</sup> + 0x2<sup>3</sup> + 0x2<sup>2</sup> + 0x2<sup>1</sup> + 1x2<sup>0</sup> 

01000001 = A

97 = 64 + 32 + 1 

0x2<sup>7</sup> + 1x2<sup>6</sup> + 1x2<sup>5</sup> + 0x2<sup>4</sup> + 0x2<sup>3</sup> + 0x2<sup>2</sup> + 0x2<sup>1</sup> + 1x2<sup>0</sup> 

01100001 = a


6. Use the Internet to research the history of the Python programming language, and answer the following questions:
   
- Who was the creator of Python, and what does his title of “BDFL” mean?
- What is “The Zen of Python”?
- In which year was the first version of Python 3 released, and in which year was the final version of Python 2 released?

`Answer`

> Guido Van Rossum is the creator of python. he is given the name BDFL which means Benevolent Dictator For Life because it is a title given for a small number of open source software development leaders who retain the final say in disputes or arguments within the community.

> [Zen of Python](https://peps.python.org/pep-0020/#the-zen-of-python) is a collection of 19 guiding principles used for writing computer programs that influenced the design of python programming language.

> Python3 was released on december, 3 2008

> Python 2.7.18, released in 2020, was the last release of Python 2.
