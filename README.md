# [Mechanical Linkages in Python](https://x.st/linkages/)
![animated Penrose linkage](https://x.st/images/linkages.gif)

Provides a graphical interface for simulating mechanical linkages, and describes the rigidity theory used to implement the simulator.

<h1>Mac/Linux Setup</h1>

The following is code to set up a virtual environment, download the linkages simulator's required libraries, and run a basic program on a Mac or Linux operating system.
<pre>
<code>
git clone https://github.com/alexliu22/linkages.git
cd linkages/python
python3 -m venv .
. bin/activate    (or activate.fish if you use fish shell)
pip install -r requirements.txt
python main.py peaucellier.txt
</code>
</pre>

<h1>Windows Setup</h1>

Windows machines use the same commands as Mac/Linux for setup, but they require an additional modification.

The PyOpenGL library has issues when running 'main.py', and you will have to uninstall and reinstall a Windows-specific version. Details can be found in this Stack Overflow post: https://stackoverflow.com/a/68258293/2556682.
