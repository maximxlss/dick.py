# Example showing LongDick's variable name restrictions
**This example raises an exception on purpose**

LongDick by default does not allow variable names without at least one occurrence anywhere in the variable name of any word from the list, case-insensitive: Johnson, Dick, Cock, Schlong, Penis, Dong

Example shows, how you can create a variable fine_dong, but not fine_dog

You can disable this restriction (for compatability with older Dick) with `--legacy-vars` or `-l` flags
