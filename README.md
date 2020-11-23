# Implementation-of-Decision-Tree-Classifer-Algorithm

<h3> Tools Used - Python, Terminal and MS Excel </h3>

<img align="left" alt="Python" width="26px" src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-512.png"/>
<img align="left" alt="Terminal" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png" />
<img align="left" alt="Excel" width="29px" src="https://img.icons8.com/fluent/48/000000/microsoft-excel-2019.png"/>

<br> </br>

Decision tree is a type of supervised algorithm that starts with a root node and traverse the tree based on a greedy approach in which all the possible traversing nodes are checked and the best one is selected. The best attribute is usually used as the root node and then the data is split into two parts, one for the training and testing the accuracy of the algorithm. These steps are repeated until the entire tree has been traversed. The core principle of decision trees is to identify those features which have the most "information" on the objective feature and then divide the dataset over the values of these features so that their target value is as pure as possible for the resulting sub datasets.

The dataset chosen is the zoo dataset available here at http://archive.ics.uci.edu/ml/datasets/Zoo

Each year hundreds of animal species is discovered and scientists look for various features in these animals to distinguish them from others in order to classify them in different animal categories. There are seven categories that these newly discovered animal species can fit in and to do that scientists look for factors such as how many legs does it has or does it have hairs, etc. This algorithm introduces a decision tree algorithm that can classify these new discovered species into their respective category. 

The training data is ran through the decision tree algorithm and the output is a tree which is then ran though the test module along with the training data. The final accuracy of the algorithm was 97%. More detailed information is available in the Report.pdf which is hosted on this repository.
