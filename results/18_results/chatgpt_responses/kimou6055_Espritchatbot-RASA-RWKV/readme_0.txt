REQUEST
Problem: This is a README file from a Rasa chatbot repository <img  width='805' src="https://miro.medium.com/v2/resize:fit:1400/1*iGdFJTHMIG79N2HChWaooQ.gif" alt="kimou6055" /></a> 
<img   width='400' src="./assets/esprit.png" alt="kimou6055" /></a> 
<img   width='400' src="./assets/INNOVISION.png" alt="kimou6055" /></a> 

## Espritchatbot V1.2
This is a chatbot designed to answer questions about Esprit University. It was created by a group of Esprit's Students called INNOVISION using the [Rasa](https://rasa.com/) framework.

The unindexed intents are generated using the [RWKV-4-Raven](https://github.com/BlinkDL/RWKV-LM) Model

## Prerequirments
Python 3.4+
Virtualenv
pip

## Installation
To open the chatbot, clone the repository to your local machine:

```
git clone https://github.com/kimou6055/Espritchatbot.git
```
All of the following will be built into a virtualenv

open the cmd in the root folder
do : 
```
cd ../

```

Then do the follow:

```
python -m venv myenv
```

Then activate the environnement

windows : 
```
myenv\Scripts\activate
```


linux : 
```
source myenv/bin/activate
```
Make sure you have Python 3.x installed on your machine. You can install the required Python libraries by running:

```
pip install rasa
pip install langdetect
pip install translate
pip install pynvml
pip install rwkv
pip install ninja 
```
You need to install torch with CUDA 
```
pip3 install torch(version)+cu(CUDA version) torchvision(version)+cu(CUDA version) torchaudio --index-url https://download.pytorch.org/whl/cu117
```
Updgrade the RWKV-4 package : 
```
pip install rwkv --upgrade

```

open the RWKV folder and drop the [RWKV-4-Raven-7B-V10 model](https://cdn-lfs.huggingface.co/repos/41/55/4155c7aaff64e0f4b926df1a8fff201f8ee3653c39ba67b31e4973ae97828633/5c50ad861a16267ec45853bad106b6f6975c49f66e27fe2b01d555834be88492?response-content-disposition=attachment%3B+filename*%3DUTF-8%27%27RWKV-4-Raven-7B-v10-Eng99%2525-Other1%2525-20230418-ctx8192.pth%3B+filename%3D%22RWKV-4-Raven-7B-v10-Eng99%25-Other1%25-20230418-ctx8192.pth%22%3B&Expires=1682535932&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZG4tbGZzLmh1Z2dpbmdmYWNlLmNvL3JlcG9zLzQxLzU1LzQxNTVjN2FhZmY2NGUwZjRiOTI2ZGYxYThmZmYyMDFmOGVlMzY1M2MzOWJhNjdiMzFlNDk3M2FlOTc4Mjg2MzMvNWM1MGFkODYxYTE2MjY3ZWM0NTg1M2JhZDEwNmI2ZjY5NzVjNDlmNjZlMjdmZTJiMDFkNTU1ODM0YmU4ODQ5Mj9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2ODI1MzU5MzJ9fX1dfQ__&Signature=BD4PrRn6wRLcbqCG4gOpsygpna~nDeCTxn8WjDGHn30sidsC6T59AkmX6U3hPlQgBQchOoPLn5WThOp-6-t2yk1SlFnlf6Q1YXIn5BDH6-vcgvAQJ-DU2nxjJO3E92WxwGsE1LjRZ39Pn~ma-VXjLwdij0WsdNAyNEcOvjVumhfVAJgZOsRvTM4Q0IqCfVLHgK1dSOYr9AG5YtbuPZWJrMWRf3Xr5MFWj4BNn8-1G-B~PlaO99I1YFPvL0RtrYnsdrFEvL~jViisgMLRnNYNudphOaI4d22xb~dKlNfTpRMIdT0ljpHjEPz74MJMFw77qWMkaVF1YppckkTxf0N7Lg__&Key-Pair-Id=KVTP0A1DKRTAX)

click on it to download

Here we used the V11X 99% English 1% other 8192 ctx (V11+LaMini instructions)

you can download and use any other version found [HERE](https://huggingface.co/BlinkDL/rwkv-4-raven/tree/main)

Make sure to install CUDA : 
 [Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/)
 [Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/)


## Usage
To use the chatbot, navigate to the Espritchatbot directory and run these following commands:

1- if you are using the chatbot for the first time you will need to train it :

```
rasa train
```

2- Run the chatbot :

```
rasa shell
```
3- You will need to  run the actions

Open another cmd access the root then run :
```
rasa run actions --port 5055
```
PS : choose the proper strategy for your own hardware configuration while loading the RWKV model in the actions.py file

Here we tested it with a custom cuda fp16 *12 -> cuda fp16i8 *1 -> cpu fp32 

you can see other options [HERE](https://github.com/BlinkDL/ChatRWKV/blob/main/ChatRWKV-strategy.png)

RWKV python implementation can be found [HERE](https://pypi.org/project/rwkv/)

Hyperparameters of RWKV can be found in the actions.py file

4- Run the chatbot with nlu accuracy:

```
rasa shell nlu
```



## Credits

 Credits for the RWKV-4-Raven model goes to [BlinkDL](RWKV-4-Raven)

 Credits for Rasa project structure and implementation goes to INNOVISION
 
 INNOVISION Team Members: 
 - Med Karim Akkari
 - Nadia Bedhiafi
 - Sarra Gharsallah
 - Karim Aloulou
 - Yosr Abbassi
 - Med Hedi Souissi
 - Aziz Jebabli

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