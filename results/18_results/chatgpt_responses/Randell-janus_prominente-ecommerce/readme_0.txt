REQUEST
Problem: This is a README file from a Rasa chatbot repository # Prominente E-commerce

This is a three-part project consisting of an e-commerce website, content management system (CMS), and an AI chatbot assistant.

## Technology Stack

- The e-commerce website and CMS is built with NextJS, TailwindCSS, and Firebase (v9)
- The chatbot is built using Rasa, a framework for developing AI chatbots that utilizes natural language understanding (NLU)

## System Features

### E-commerce Website

- Authentication
  - Signup with name, email, password
  - Login with email and password
  - Forgot password
  - Protected pages with private routes
  - Re-authentication on email update
- Manage profile
  - Update personal information (name, address, contact)
  - Update account settings (email, password)
- Add items to cart
  - Add/remove items
  - Update item quantity
- Checkout items
  - Checkout restriction with incomplete account info
  - Categorized orders (pending, to receive, received, cancelled)
- Notification system
  - Notify on account info update
  - Notify on order status update
  - Mark notifications as read
- AI chatbot assistant
  - Computes glass pricing base on user input
  - Recommends appropriate materials base on user input
  - Answers basic questions about the business

### Content Management System

- Add and manage products being shown in the ecommerce website
  - Includes easy toggling of product availability/visibility
- Display account information and orders of each registered user
- Search, filter, and sort orders received from the ecommerce website
- Update status of orders (pending, confirmed, unapproved, delivered)
- Daily total income and product sales tracking

## Snapshots

### E-commerce Website

- Home page
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-ecommerce/public/snapshots/home.png)
- Auth page
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-ecommerce/public/snapshots/auth.png)
- Cart page
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-ecommerce/public/snapshots/cart.png)
- Profile page
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-ecommerce/public/snapshots/profile.png)
- Notifications
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-ecommerce/public/snapshots/notifications.png)
- Orders
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-ecommerce/public/snapshots/received.png)
- Chatbot basic chat
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/rasa-chatbot/public/snapshots/rasa-basic-chat.png)
- Chatbot compute glass price
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/rasa-chatbot/public/snapshots/rasa-compute-price.png)
- Chatbot recommend materials
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/rasa-chatbot/public/snapshots/rasa-recommend-materials.png)

### Content Management System

- Users page
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-cms/public/snapshots/cms-users.png)
- Orders page
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-cms/public/snapshots/cms-orders.png)
- Order modal
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-cms/public/snapshots/cms-order.png)
- Products/inventory management
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-cms/public/snapshots/cms-products.png)
- Sales/income tracking
  - ![](https://github.com/Randell-janus/prominente-ecommerce/blob/main/prominente-cms/public/snapshots/cms-sales.png)

        Does the chatbot use any database (local or external) or any external service? Answer with a list of these databases and services (only names on a single line, no further explanation, no numeration). 
        
    For this problem I received these answers, each with a list of services:
    Firebase,,##
Firebase,,##
Firebase,,##
None
None
None
None
Firebase,,##
Firebase,,##
Firebase,,##
    Basing on these answers and on the action file written in the problem, write one complete and correct list of the external services used in this action file. Keep in mind that some answers may have incorrect terms which are not external services or databases (like libraries that are not external services, or services that do not exist) and you have to remove them. 
    Different answers may refer to the same service with different names, and there could be missing services that you have to add.
    Write this list of service names on a single line, with no introduction, further explanation or numeration, so like this:
    Service1, Service2, Service3 
    In a new section titled "Purpose of external services" explain the purpose of each service.
    If the file doesn't use any external service nor database, answer only with "NO" and nothing else

RESPONSE
Firebase

## Purpose of external services

### Firebase
Firebase is used for authentication, database management, and hosting services for the e-commerce website and CMS. It provides functionalities such as user signup, login, password management, and data storage for user profiles, orders, and product information.