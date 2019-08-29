# Coding Challenge 02

## Explanation
The file sales.json contains a list of dictionaries, each dictionary contains these keys:
* date
* amount (pennies)
* agent

A table showing the total value of each agent's sales per month must be printed, using only the python standard library like this:
<pre>
Agent   Jan Sales  Jan Total    Feb Sales  Feb Total    Mar Sales  Mar Total
Andy         30     4,100.00         25     5,199.25         32       250.32
Belinda      50    10,125.33         15       100.00         27     1.250.67
</pre>

## Platform Recommendation
* This program has been run on Windows 10.0.15063 build 15063 and Mac OS X, developed using Python version 3.7, Other systems have not been tested, and it is advised to have caution with untested OS.

## To Start
* Open a command line window and navigate to the folder holding the program's *.py* file.
* Then type: python sales_reader.py, which should run the program.

## Example Runtime
<pre>
C\...\sales_reader_py>python sales_reader.py

Agent       Jan Sales   Jan Total   Feb Sales   Feb Total   Mar Sales   Mar Total
Anna        35          19258.59    45          23418.60    38          19876.48
Bill        43          20134.33    37          18368.95    33          16368.39
Caroline    48          26058.12    43          23389.25    38          20366.71
David       41          23925.14    46          20930.59    40          18900.08
Ella        29          12765.33    61          25924.73
Fred        40          21124.50    37          18819.21    41          22787.11
Gina        45          22073.52    38          20682.71    53          25221.64
Henry       35          21450.80    49          23939.57    39          22642.50
</pre>
