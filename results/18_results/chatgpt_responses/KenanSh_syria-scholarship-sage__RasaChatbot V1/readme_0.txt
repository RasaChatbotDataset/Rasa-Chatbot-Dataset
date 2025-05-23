REQUEST
Problem: This is a README file from a Rasa chatbot repository # Syria-Scholarship-Sage
This project focuses on developing an **Arabic** AI Assistant integrated into a website, specifically designed for accessing information about Scholarships and Internships worldwide. It is worth noting that the initial version of the assistant was in English.

The primary objective of this assistant is to assist visitors in navigating the website to discover relevant Scholarships or Internships. Additionally, it aids students by addressing questions related to their academic life.

The implementation utilizes the **Rasa Framework**, a leading open-source conversational AI platform that emphasizes Natural Language Understanding (NLU).

## Dataset

### Manually Gathered Dataset

For the navigation task, the NLU is trained on nine general-purpose Arabic sentences collected from four different individuals. For the **Academic Assisting** aspect, data was gathered through a questionnaire distributed to university students. The collected data was then analyzed to identify 14 distinct academic problems faced by students. Responses to these problems were sourced from academic assistants across various faculties and integrated into the chatbot's domain file.

## Why Rasa Framework?

1. Open-Source Framework.
2. Suitable for interactive assistance, providing a more dynamic experience compared to static question-answering or expert systems.
3. Rasa's robust NLU capabilities enable effective training with minimal examples, ensuring accurate user input recognition in the desired dialect.
4. Integration capabilities with various external systems and APIs.
5. Customizability to tailor the chatbot's behavior according to the unique requirements of the application.

Some Testing Scenarios:


1. ![image](https://github.com/KenanSh/syria-scholarship-sage/assets/101220492/970298ae-ff45-41fb-987b-cfd512d7fda0)
2. ![image](https://github.com/KenanSh/syria-scholarship-sage/assets/101220492/791127d3-bbf5-44f9-8611-e92670442676)


**Note: First version was in English**

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    None
None
None
None
None
None
None
Databases and services: Rasa Framework,,##
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