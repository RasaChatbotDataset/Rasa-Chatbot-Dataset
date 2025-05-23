REQUEST
Problem: This is a README file from a Rasa chatbot repository # 2022_IBM_Code_Challenge_FormBee

<h1> Problem Statement</h1>
<p>
    Digitization of government services directly leads to a significant increase in quantity of digital data and data entry tasks, especially considering current situations. the average layman finds it difficult to manage and fill the various forms and surveys of the government. even tech-savvy people may find it difficult to fill a form instantaneously and may resort to googling for jargons which wastes time.
</p>

<h1>Personas of the system</h1>

<p>
    Consider a normal citizen , they can interact with this chatbot to fill government forms they don't have to go anywhere else.
</p>

<h5> Usecases</h5>
<ol>   
    <li> Form filling </li>
    <li> printing and exporting filled forms</li>
    <li>viewing and managing forms</li>  
   </ol>
  

<h1>Architecture</h1>
<img src="architecture.png"></img>

<h1>Technical stack</h1>
<h5>Frontend</h5>
<ol>
    <li>Bootstrap : Landing page creation</li>
    <li>React Webapp : Chatroom creation</li>
    </ol>
    
<h5>Middlewarre</h5>
<ol>
    <li>Rasa : For chatbot creation </li>
</ol>

<h5>Backend </h5>
<ol>
    <li> Nodejs with Firebase as storage</li>
    </ol>
  

<h1>Working Demo Video</h1>

[![Working Demo Video](https://img.youtube.com/vi/1GOBrDdNPEQ/0.jpg)](https://www.youtube.com/watch?v=1GOBrDdNPEQ)

## ![Presentation Slide](https://github.com/ibm-gtsp-team-15/2022_IBM_Code_Challenge_FormBee/blob/ace8bf42d13fdb036ad27935f07e45f20278fbb7/FormBee%20Slides.pptx)

<h2>Explanation videos</h2>
> Frontend and ActionSelectTemplate

[![Frontend and ActionSelectTemplate](https://img.youtube.com/vi/-jTI6Py_hKo/0.jpg)](https://www.youtube.com/watch?v=-jTI6Py_hKo)

> ActionFillFormSlot and Search function

[![ActionFillFormSlot and Search function](https://img.youtube.com/vi/cwBFQc8Qz78/0.jpg)](https://www.youtube.com/watch?v=cwBFQc8Qz78)

> Backend

[![Backend](https://img.youtube.com/vi/XjhjORGLTfQ/0.jpg)](https://www.youtube.com/watch?v=XjhjORGLTfQ)

<h1>List of Contributors</h1>
<ol>
  <li>Adharsh S</li>
  <li>Allen B Abraham</li>
  <li>Dennis Thomas</li>
  <li>Jeril Monzi Jacob</li>
</ol>

<h1>License &amp acknowledgement</h1>

<P>
    <b>GNU General Public License v3.0</b>
    </P>
<p>
    We would like to thank our mentors <b>Manoj Jain</b> and <b>Ayush Utkarsh</b> for helping us throughout this hackathon.They have helped us to clear our doubts reagrding the stacks in which we worked.Once again thanking their guidance in this hackathon.
    </p>
    

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Firebase,,##
Firebase,,<h1>
Firebase,,##
Firebase,,##
Firebase,,<h1>
Firebase,,##
Firebase,,###
Firebase,,##
Firebase,,<h1>
Firebase,,###
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Firebase

<h1>Purpose of external services</h1>
<p>
    <b>Firebase:</b> Firebase is used as a backend service to store and manage data for the chatbot. It provides real-time database capabilities, authentication, and cloud storage, which are essential for handling user interactions and storing form data securely.
</p>