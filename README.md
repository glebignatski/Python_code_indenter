# Python_Code_Indenter
Python Program for adjusting the indentation of your Python code given a line range (start, finish). <br/>

Command format: <i> python3 adjust_columnar_code.py <file_name> <i/u> S F </i> <optional>
where file_name is the name of the Python file to be adjusted, i/u are indent or unindent,
S and F correspond to the range of lines you would like to indent/unindent (1 to number of lines in your code). <br/> <br/>
In addition, you can add an optional parameter like "safe" as in "safe mode" that would, instead of overwriting the target file,
save the edited code to a text file from which you can select the entire code and copy it back to the targeted file. <br/> <br/>
e.g., if you are using a line numbered editor like Sublime, then you just need to specify
the line numbers you see: <br/> <br/>
"python3 adjust_columnar_code.py calculator.py i 1 10" will indent lines 1 through 10 inclusive. <br/> <br/>
"python3 adjust_columnar_code.py calculator.py i 1 10 safe" will create a new file and put the updated code there that is indented/unindented <br/>

Also, if there is an indentation command line error and you are using Sublime, you can select all, go to View, then Indentation,
and "Convert Indentation to Spaces".
