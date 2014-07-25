IDA2Sym
=======
IDAScript to create pseudos symbol file which can be loaded in WinDbg via IDebug->AddSyntheticSymbol. This script was inspired by this [forum](http://www.woodmann.com/forum/archive/index.php/t-15503.html) post.
The addsym.dll is the precompiled version of this post. The
difference to the original IDC script is that IdaSym.py is focused only
on function names which contain a specific token and their internal call-ret addresses. 
This keeps the symbol file small and speeds up the creation and load time.


Installation
---
Copy the IdaSym.py file to your favorite IDAPython folder.

Copy the addsym.dll to the binary path of your windbg installation.

Usage
---
The python script creates sym-entries only for functions which name ends with '_SYM'.
So you have to rename the functions you want symbol entries for, e.g. DEADBEEF_sub_fffff**_SYM**.

To create a symbol file ues the following command (**be sure to run the script IdaSym.py before**):
```
Python>SaveSyms(AllSyms())
>> 131 syms written to G:\IDAs\YourBin\YourBin.sym
```
If you don't give a filename the default location of the symbols file will be created in your binary location.

To use the symbols in WinDbg use these commands:
```
.load addsym
!addsym <modname> <path-of-file> 
```

License
---
MIT (see LICENSE file)
