IDA2Sym
=======
IDAScript to create pseudos symbol file which can be loaded in WinDbg via IDebug->AddSyntheticSymbol. This script was inspired by this [forum](http://www.woodmann.com/forum/archive/index.php/t-15503.html) post.
The addsym.dll is the precompiled version of this post. The
difference to the original IDC script is that IdaSym.py is focused only
on function names which contain a specific token and their internal call-ret addresses. 
This keeps the symbol file small and though the creation and load time
faster.


Installation
---
Copy the IdaSym.py file to your favorite IDAPython folder.

Copy the addsym.dll to the binary path of your windbg installation.

Usage
---


License
---
