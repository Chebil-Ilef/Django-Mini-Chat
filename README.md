# 🐍 Django Real-Time Chat System

A real-time chat application built using Django Channels, providing WebSocket-based communication for instant messaging.

## Features

- **WebSocket Integration**: Utilizes Django Channels for handling WebSocket connections.
- **Real-Time Messaging**: Enables users to send and receive messages instantly without refreshing the page.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Chebil-Ilef/Django-RealTime-Chat-System.git
   cd Django-RealTime-Chat-System
   ```

2. Create your virtual environment:

   ```bash
   python -m venv env
   ```

    ```bash
   source activate env/Scripts/activate
   ```

     ```bash
     pip install requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the chat application in your web browser at `http://localhost:8000/`.

## Sneak Peak

![Chat Demo](/demo.png)

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.
