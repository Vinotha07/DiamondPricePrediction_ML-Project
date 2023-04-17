# Housing_ML-Project
This project helps us to understand the Regression 

Initially create a repository in the git hub and clone it to the local machine by adding the github link 
to the gitclone cmd in the cmd prompt by changing the directory in the local machine

......

cd <path of the local machine directory>
git clone <path from the git hub link>

code
.........

To open vs code


Step 1: Create an environment

''''
conda create -p venv python==3.8
conda activate venv\

''''

Step2: Create the requirement.txt file and include all the necessary libraries which required to perform the project
list out the libraries which need to be installed and include -e. to trigger the setup file
...........
pip install -r requirements.txt
..........

Step3: Create a setup.py file so that we can use the overall project as the package.
.........
python setup.py install
.........

Step 4:Create source folder and include all the required files and the folders for the whole project.

Step 5: Create notebook folder to perform the Jupyter notes operation

Step 6: Create components and the pipeline folders under src folder.

Step 7: Add __init__.py file(module) in the folder so that we can import that folder as the package.

Step8: Get the dataset and store it in the Data folder under the notebook folder to perform EDA and the model training

Step 9: create EDA.ipynb file to perform the EDA

step 10: Create model training.ipynb file to perform Model training

Step 11: Write code for logging and custom exception .

Step 12: Write code for utils if we have any common function

Step 13: Write code for data ingestion , for that we require what are the input and output from this step and saved that into artifacts.

Step 14: Write code for data transformation where we can apply pipeline and transform the columns by applying feature scaling and convert that into pickle file

Step 15: Write a code for the saving pickle file in the utils file since it can use commonly

step 16: Write code for model training where we can split the dataset into dependent and independent feature and perform the model training and convert them into pickle file.

step 17: write a function in utils file to perform the evaluation of the model

step 18: write a code for the steps to be followed to execute in the training pipeline file

step 19: write a code for prediction pipeline by adding the load file function for unpack the pickle file in the utils.

step 20: write code to get the custom data and convert that into dataframe in the pipeline module

step 21: Create app.py under the main folder to define the flask 

step22:create the folder template where we can create the html files for index, form and result.





