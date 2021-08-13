# Python_code_indenter
Python Program for adjusting the indentation of your Python code given a line range (start, finish).

Command format: python3 adjust_columnar_code.py <i/u> <file_name> S F <optional>
where i/u are indent or unindent, file_name is the name of the Python file to be adjusted, 
S and F correspond to the range of lines you would like to indent/unindent (1 to number of lines in your code).
In addition, you can add an optional parameter like "safe" as in "safe mode" that would, instead of overwriting the target file,
save the edited code to a text file from which you can select the entire code and copy it back to the targeted file. \
e.g., if you are using a line numbered editor like Sublime, then you just need to specify
the line numbers you see: "python3 adjust_columnar_code.py calculator.py i 1 10" will indent lines 1 through 10 inclusive.

Also, if there is an indentation command line error and you are using Sublime, you can select all, go to View, then Indentation,
and "Convert Indentation to Spaces".
