# Example showing basic features of original Dick language
**Prints `4Dick`**

This example uses pretty much all the features in legacy Dick (not LongDick) language.

## Line-by-line

`DICK my_dong 8=D` - we create a variable my_dong with inital value of 1. In Dick, integers come in form of ASCII dicks, and its value is equal to number of `=` in the middle.

`GRAB my_dong` - we grab my_dong. This places value of my_dong into the hand. Hand is a kind of register. All arithmetic operations operate on th value in hand.

```
LONGDICK 8====D
SMALLDICK 8==D
HUGEDICK 8====D
```
These are arithmetic operations. We add 4 to the hand, subtract 2 and multiply by 4. As hand was 1, now it is 12. 

`DICK huge_cock 8=D` - we create another variable, huge_cock.

`RELEASE huge_cock` - we release into huge_cock. This sets huge_cock to hand's value and then resets hand to 0.

`GRAB huge_cock` - grab huge_cock.

`TINYDICK 8===D` - divide hand by 3. It's now 4. Note that huge_cock is still 12! We still need to release to put the result into a variable.

`PEE` - PEE prints numerical value on the hand. In this example it prints 4. P.S. no newline is printed.

`RELEASE my_dong` - we release into my_dong. my_dong is now 4 and huge_cock is now 12.

Let's print the language name. To do this we need ASCII values:
```
GRAB huge_cock
HUGEDICK 8=====D
LONGDICK my_dong
LONGDICK my_dong
```
We grab huge_cock (12) and multiply it by 5. We then add the value of my_dong (4) twice. Now we hold 68 in the hand. 68 is the ASCII value of D.

`WEE` - prints value in hand as an ASCII character.

Then we print the remaining letters:
```
LONGDICK 8=====================================D
WEE

SMALLDICK 8======D
WEE

LONGDICK 8========D
WEE
```

Output:
```
4Dick
```

Notice that this example uses variable names valid in LongDick, but you can disable this check with `-l` flag and use any variable names.
