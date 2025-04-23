REQUEST
Problem: This is a README file from a Rasa chatbot repository # Generate Neural Network Diagrams

Build the docker image:

~~~bash
cd ${HOME}/Breast-Cancer-Segmentation/NeuralNetDiagrams
docker build -t cmpe258_proj:dev .
~~~

Put your python code in `pyexamples/` folder, then run the following commands:

~~~bash
# Clone repo
git clone git@github.com:HarisIqbal88/PlotNeuralNet.git

PATH_TO_NNP_DIR="${HOME}/Breast-Cancer-Segmentation/NeuralNetDiagrams/PlotNeuralNet"
cp $PATH_TO_NNP_DIR/pyexamples/msgrap.py .
~~~

Launch the docker container from `cmpe258_proj:dev` docker image with volume mount to our NeuralNetDiagrams:

~~~bash
cd $PATH_TO_NNP_DIR
docker run --name plotnn --privileged -it -v $PWD:/sjsu/PlotNeuralNet cmpe257_ml:dev

# assuming you just cloned the repo
cd PlotNeuralNet/pyexamples

# run an example: shell script runs your python script, test_simple
# then generates a neural network graph as pdf
bash ../tikzmake.sh test_simple

# ex: copy over your py nn diagram code to pyexamples/

bash ../tikzmake.sh msgrap

# You should see a msgrap.pdf and msgrap.tex be generated
~~~
        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    None
None
None
None
None
None
None
None
None
None
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
NO