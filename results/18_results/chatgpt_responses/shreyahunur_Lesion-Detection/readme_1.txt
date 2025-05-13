REQUEST
Problem: This is a README file from a Rasa chatbot repository # Deploy CMPE257 ML LD Docker Container

1\. Create proj/ and go to Lesion Detection folder:

~~~bash
# Create proj/ folder
mkdir -p $HOME/Documents/GitHub/
cd $HOME/Documents/GitHub/

# Clone cmpe257 Lesion Detection project repo to GitHub folder
git clone git@github.com:shreyahunur/Lesion-Detection.git
cd Lesion-Detection
~~~

## Approach 1: Build a Docker GPU Container for LD

2\. Build GPU Docker image from Dockerfile:

~~~bash
# copy over GPU Dockerfile
cp Docker_GPU/Dockerfile .

# Build cmpe257_ld docker image with Anaconda3, TensorFlow Jupyter Notebook, 
# if on linux, prepend sudo
docker build -t cmpe257_ld_gpu:dev .
~~~

## Deploy a Docker GPU Container for LD

2\. Deploy cmpe257 Lesion Detection GPU Docker container:

~~~bash
# volume mount created from dev host curr proj $PWD to /sjsu/cmpe257 in container
# if on linux, prepend sudo
docker run --name cmpe257_ld_dev --gpus all -p 8888:8888 -it -v $PWD:/sjsu/cmpe257_ld cmpe257_ld:dev
~~~

## Approach 2: Build a Docker CPU Container for LD

3\. Build CPU Docker image from Dockerfile:

~~~bash
# copy over CPU Dockerfile
cp Docker_CPU/Dockerfile .

# Build cmpe257_ld docker image with Anaconda3, TensorFlow Jupyter Notebook, 
# if on linux, prepend sudo
docker build -t cmpe257_ld_cpu:dev .
~~~

## Deploy a Docker CPU Container for LD

2\. Deploy cmpe257 Lesion Detection CPU Docker container:

~~~bash
# volume mount created from dev host curr proj $PWD to /sjsu/cmpe257 in container
# if on linux, prepend sudo
docker run --name cmpe257_ld_dev -p 8888:8888 -it -v $PWD:/sjsu/cmpe257_ld cmpe257_ld:dev
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