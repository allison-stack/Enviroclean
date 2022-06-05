# ML Model Manual

In order for our model to run locally in our application, the TensorFlow model (.tf) must be saved after it has been initially trained and then the saved model can then be imported in the main application code file to determine if a given item is Organic or Recycle. 

To make changes to the TensorFlow model (i.e. more epochs, optimization method, different dataset, etc.), the following instructions need to be followed:

1.	Locate the ```createdMLmodel.py``` file in the ML Model folder in the repo 
2.	Copy and paste each section of the code file into Google Colab document or Jupyter notebook
3.	Import the dataset.zip into the notebook. This dataset should be unzipped first.
4.	Make any necessary edits to the model or the database 
5.	Run each code snippet
6.	A new model will now be downloaded along with all its labels!

