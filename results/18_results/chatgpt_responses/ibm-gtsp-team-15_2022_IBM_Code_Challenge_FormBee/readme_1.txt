REQUEST
Problem: This is a README file from a Rasa chatbot repository # React-based Chatroom Component for Rasa Stack

[![CircleCI](https://circleci.com/gh/scalableminds/chatroom.svg?style=svg)](https://circleci.com/gh/scalableminds/chatroom)

<a href="https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/demo.html"><img src="https://npm-scalableminds.s3.amazonaws.com/%40scalableminds/chatroom/demo.gif" alt="Demo" width="409" height="645" /></a>

**Note: This project is not maintained anymore. If you like to become a community maintainer get in touch with @hotzenklotz. It may still work for your project or serve as a point of reference for others.**

[Watch a demo of our Chatroom in action](https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/demo.html)

## Features

* React-based component
* Supports Text with Markdown formatting, Images, and Buttons
* Customizable with SASS variables
* Generates a unique session id and keeps it in `sessionStorage`
* Queues consecutive bot messages for better readability
* Speech input (only in Chrome for now)
* Text to Speech (only in Chrome for now)
* Demo mode included (ideal for scripted screencasts)
* Hosted on S3 for easy use
* Simple setup. Works with Rasa's [REST channel](https://rasa.com/docs/rasa/user-guide/connectors/your-own-website/#rest-channels)

## Usage
1. Embed the `chatroom.js` in the HTML of your website and configure it to connect to your Rasa bot. Either use the S3 hosted version or build it yourself. (see below)

```html
<head>
  <link rel="stylesheet" href="https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/dist/Chatroom.css" />
</head>
<body>
  <div class="chat-container"></div>

  <script src="https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/dist/Chatroom.js"/></script>
  <script type="text/javascript">
    var chatroom = new window.Chatroom({
      host: "http://localhost:5005",
      title: "Chat with Mike",
      container: document.querySelector(".chat-container"),
      welcomeMessage: "Hi, I am Mike. How may I help you?",
      speechRecognition: "en-US",
      voiceLang: "en-US"
    });
    chatroom.openChat();
  </script>
</body>
```


2. In your Rasa bot setup, make sure to include the Rasa [REST channel](https://rasa.com/docs/rasa/user-guide/connectors/your-own-website/#rest-channels) in your `credentials.yml` file:
```
rest:
  # pass
```

Restart your Rasa server. Depending on your setup you might need to add CORS headers, e.g. `--cors "*"`.

```
rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"
```

Note, the version of the Chatroom's Javascript file is encoded in the URL. `chatroom@master` is always the latest version from the GitHub master branch. Use e.g. `chatroom@0.10.0` to load a specific release. [All Releases can be found here.](https://github.com/scalableminds/chatroom/releases)


| Chatroom Version  | Compatible Rasa Core Version |
|-------------------|------------------------------|
| 0.10.x            | 1.0 - 2.x                    |
| 0.9.x (Deprecated)| 0.11.4+, 0.13.7              |
| 0.8.x (Deprecated)| 0.11.4+                      |
| 0.7.8 (Deprecated)| 0.10.4+                      |

Note, versions prior to `0.10.x` used a custom Python channel to connect the chatroom frontend with a Rasa bot backend. Upgrading, from version `0.9.x` or below will require you to modify the `credentials.yml` and include the Rasa REST channel. (see installation instructions above)


## Development

### Install dependencies

```
yarn install
```

### Continuously build the Chatroom component

```
yarn watch
yarn serve
```

Open `http://localhost:8080/demo.html` in your browser.

## Build

```
yarn build
```

Distributable files will be created in folder `dist`.

## License

AGPL v3

Made by [scalable minds](https://scalableminds.com)

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