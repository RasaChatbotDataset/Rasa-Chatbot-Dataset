REQUEST
Problem: This is a README file from a Rasa chatbot repository # Rasa Chatbot for Rhodes College 


This Rasa-based chatbot is designed to provide information about the various department, answering queries related to faculty specialization, course requirements, and more.


## Features

- **Faculty Specialization Inquiries**: Find out which faculty member specializes in a particular area.
- **Major Requirement Details**: Get detailed information about major requirements in Computer Science.
- **Course Guidance**: Guidance on what courses to take for a CS major.

## Installation

To run this chatbot, you need to install Rasa Open Source. Follow these steps:

1. **Install Rasa**: 
   ```bash
   pip install rasa
2. **Clone the Repository: **
    ```bash
    git clone <repository-url>
    cd <repository-directory>

4. **Train the Model**:
    ```bash
    rasa train
5. **Run the Actions Server (In a separate terminal):**:
    ```bash
    rasa run actions

6. **Start Talking to Your Bot:**:
   ```bash
   rasa shell
## Project Structure

- `data/`
  - `nlu.yml`: NLU training data for the Rasa model.
  - `stories.yml`: Sample stories representing conversation flows.
  - `rules.yml`: Rules to define deterministic behavior of the bot.
- `actions/`
  - `actions.py`: Custom actions for dynamic responses.
- `tests/`
  - `test_stories.yml`: Test stories for evaluating the bot.
- `domain.yml`: Defines the chatbot's universe, including intents, entities, actions, and responses.
- `config.yml`: Configuration for the NLU pipeline and policies.
- `endpoints.yml`: Configures external services like action server.

## Usage

- Start a conversation with a greeting like "Hello".
- Ask about faculty specializations, e.g., "Who specializes in machine learning?"
- Inquire about major requirements, e.g., "What are the CS major requirements?"

## Customization

You can customize and extend the chatbot by:

- Adding more intents and examples in `data/nlu.yml`.
- Creating new stories in `data/stories.yml`.
- Defining additional rules in `data/rules.yml`.
- Implementing more custom actions in `actions/actions.py`.

## Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

MIT License









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