REQUEST
Problem: This is a README file from a Rasa chatbot repository # CoArgue: Fostering Lurkers’ Contribution to Collective Arguments in Community-based QA Platforms
This is the source code for the prototype system CoArgue, a tool that supports lurkers on Community-based QA (CQA) Platforms in making contributions. The system is part of a research paperwork with the above name, which is accepted by CHI 2023.

You are welcome to [cite](#cite) the paper if you find it insightful.

## Abstract
In Community-Based Question Answering (CQA) platforms, people
can participate in discussions about non-factoid topics by mark-
ing their stances, providing premises, or arguing for the opinions
they support, which forms “collective arguments”. The sustainable
development of collective arguments relies on a big contributor
base, yet most of the frequent CQA users are lurkers who seldom
speak out. With a formative study, we identified detailed obstacles
preventing lurkers from contributing to collective arguments. We
consequently designed a processing pipeline for extracting and
summarizing augmentative elements from question threads. Based
on this we built CoArgue, a tool with navigation and chatbot fea-
tures to support CQA lurkers’ motivation and ability in making
contributions. Through a within-subject study (N=24), we found
that, compared to a Quora-like baseline, participants perceived
CoArgue as significantly more useful in enhancing their motivation
and ability to join collective arguments and found the experience
to be more engaging and productive.

## Run

### Contribution Evaluation
The contribution after submitting the post is evaluated by serveral NLP models. Refer to this [link](https://github.com/pytorch/serve/blob/master/README.md) to create the evaluation APIs with your own model and update the API URLs at the very beginning of `main.js` in the "frontend" folder.

### Chatbot Widget
The essential code and settings are contained in the "chatbot" folder. 

To train and run a chatbot model, refer to the official Rasa documentation [here](https://rasa.com/docs/rasa/command-line-interface).

To connect the running chatbot model to the frontend chatbot widget, follow the instructions in this [link](https://rasa.com/docs/rasa/connectors/your-own-website/).

### Website
Simply open the `index.html` in the "frontend" folder to run the website.

It contains the augmented information for two question threads. To switch between the two threads, provide the URL param `question=bitcoin` or `question=car`. The system defaults to `bitcoin` if not provided.

It also contains the baseline version, which is no more than a port of plain Quora website, with UI element aligned. To switch to the baseline version, do `git switch baseline`.
## Cite
```bibtex
@inproceedings{10.1145/3544548.3580932,
    author = {Liu, Chengzhong and Zhou, Shixu and Liu, Dingdong and Li, Junze and Huang, Zeyu and Ma, Xiaojuan},
    title = {CoArgue : Fostering Lurkers’ Contribution to Collective Arguments in Community-Based QA Platforms},
    year = {2023},
    isbn = {9781450394215},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3544548.3580932},
    doi = {10.1145/3544548.3580932},
    abstract = {In Community-Based Question Answering (CQA) platforms, people can participate in discussions about non-factoid topics by marking their stances, providing premises, or arguing for the opinions they support, which forms “collective arguments”. The sustainable development of collective arguments relies on a big contributor base, yet most of the frequent CQA users are lurkers who seldom speak out. With a formative study, we identified detailed obstacles preventing lurkers from contributing to collective arguments. We consequently designed a processing pipeline for extracting and summarizing augmentative elements from question threads. Based on this we built CoArgue, a tool with navigation and chatbot features to support CQA lurkers’ motivation and ability in making contributions. Through a within-subject study (N=24), we found that, compared to a Quora-like baseline, participants perceived CoArgue as significantly more useful in enhancing their motivation and ability to join collective arguments and found the experience to be more engaging and productive.},
    booktitle = {Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems},
    articleno = {271},
    numpages = {17},
    keywords = {Collective Arguments, Lurker Support, CQA Platforms},
    location = {Hamburg, Germany},
    series = {CHI '23}
}
```

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    - pytorch/serve,- Rasa,,###
Databases and services:,- pytorch/serve,- Rasa
None
NLP models, Rasa,,###
Databases and services:,- pytorch/serve,- Rasa
Databases and services:,- PyTorch Serve,- Rasa
Databases and services:,- pytorch/serve,- Rasa
- pytorch/serve,- Rasa,,###
- pytorch/serve,- Rasa,,###
Databases and services:,- pytorch/serve,- Rasa
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
pytorch/serve, Rasa

## Purpose of external services
- **pytorch/serve**: Used to create evaluation APIs for assessing the contributions made by users after submitting their posts.
- **Rasa**: Used to train and run the chatbot model that interacts with users on the frontend chatbot widget.