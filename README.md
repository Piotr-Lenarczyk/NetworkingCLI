# NetworkingCLI
A collection of networking tools in a form of Command Line Interface written in Python.
# Status
The following project is <i>in-progress</i>, therefore any code as well as information in this README file is subject to change.
## Functionalities
* Subnet calculator
* Ping Sweep
* Port Scanner
## Requirements
After creating a local copy of the files, in the root folder of the project, run the following command in a terminal of your choice:
<pre>pip install -r requirements.txt</pre>
This will install necessary dependencies.
## Usage
Run:
<pre>python main.py &lt command &gt &lt options &gt</pre>
for example
<pre>python main.py subnet 192.168.1.0/24</pre>
in order to execute one of the scripts.
At any point you may use <i>-h</i> switch to find out how to complete the command:
<pre>python main.py -h</pre>
