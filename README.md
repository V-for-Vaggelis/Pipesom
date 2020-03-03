# Pipesom
Pipesom is a web-app destined to make data-preprocessing easier. The target audience is scientists of several fields. The user uploads a csv file containing data of several variables of interest. By submitting the file, some graphs are displayed, to provide a basic understanding of the dataset.

## Code dependencies

<em>Python:</em>
<ul>
  <li><a href="https://github.com/JustGlowing/minisom">minisom</a></li>
  <li><a href="https://flask.palletsprojects.com/en/1.1.x/">flask</a></li>
  <li><a href="https://pandas.pydata.org/">pandas</a></li>
  <li><a href="https://numpy.org/">numpy</a></li>
  <li><a href="https://matplotlib.org/">matplotlib</a></li>
  <li><a href="https://seaborn.pydata.org/">seaborn</a></li>
  <li><a href="https://scikit-learn.org/stable/">scikit-learn</a></li>
</ul>

## How to run
At the moment, the app is only available in developer mode, so some steps are required to use the app:
<ol>
  <li><em>Install python</em> in your system. If you're just getting started, <a href="https://www.anaconda.com/">anaconda</a> is recommended.</li>
  <li><em>Open a terminal</em> that can run python, and install all the dependencies by running:  
  <code>pip install "dependency-name" </code> for each one of them. </li>
  <li><em>Clone this repository</em>: <code>git clone https://github.com/V-for-Vaggelis/Pipesom.git</code>, or download and unzip it if you're not familiar with git.</li>
  <li> On your terminal, navigate to the project's directory and run <code>python app.py</code>, then <em>wait until a status of running indicating the host's port appears on the terminal</em>.
  <img src="/images/host.png" alt="Hosting example"></li>
  <li>Open your favorite browser and navigate to the hosting port, for example: <code>localhost: 5000</code>, the app should instantly appear. <img src="/images/browser.png" alt="Browser example"</img></li>

</ol>

## How to use
_Upload a csv file_ and submit it. After a few minutes you should get some plots back.

_**Warning:** The app is very sensitive to to the input file's format_, follow the examples in the "input-examples" directory to create a valid file. The file should follow the rules below:
1. First row should be the names of the variables seperated by commas
1. All the other rows should contain _**numeric values**_ of those variables seperated by commas
1. All the variables must have equal number of data, meaning that all columns for each row should be filled
1. All _**missing values should be filled with naN**_

## Interpret the results
There are two plots displayed:
1. _A <a href="https://www.displayr.com/what-is-a-correlation-matrix/">correlation matrix</a>_, which just shows the linear relationships between the variables.
1. _The feature planes of each variable_, after a _<a href="http://www.ai-junkie.com/ann/som/som1.html">self organizing map</a>_ has been trained and adjusted to the data, where the values are normalized around the mean. Variables that exhibit similar behavior here (similar colors in same regions of the grids) can have strong non-linear relationships. **If a variable has more than 70% of missing values it is not added in the analysis**.

## Ideas for improvement
1. Make the app more _user-friendly_ by improving the GUI.
1. Give _feature selection_ capability to the user via the trained SOM  network.
1. Give the user the ability to tune the SOM network's parameters (with proper guidance) to achieve better results.
