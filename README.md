🐾 Moscow Zoo Totem Bot
A Telegram bot designed for the Moscow Zoo concept. The main goal is to help users discover their "totem animal" through a quiz and encouraging them to participate 
in the guardianship program.
Note: This is an educational project. I am not affiliated with the Moscow Zoo. All images and brand assets are used for demonstration purposes only.

What it does
The Quiz – a 8-question survey using a Finite State Machine (FSM) to determine the user's animal match. It’s built to be smooth – no crashes if you click the wrong button.
After the quiz, you get a custom result with a photo and a description of your animal. It's designed to be shareable and fun.
I've added a feature that helps you send result to a staff member of the zoo to ask about how to become a "Guardian" for that specific animal.
Privacy and Safety: Added a /privacy command so people know exactly what's happening with their data.
Built on the aiogram 3.25.0 framework, ensuring high performance through asynchronous request handling. That mean that the bot stays fast even if multiple people are using it 
at the same time.
Integrated logging and performance monitoring to track errors and response times.

The Tech Side
Language: Python 3.14
Framework: Aiogram 3.25.0 
State Management: Aiogram FSM 
Formatting: HTML & aiogram.utils.formatting
Environment Variables: All secret variables like the Bot Token are kept in a Token file.
I integrated a monitoring system that logs errors and response times to a file, so I can fix bugs quickly.

How to use it
Type /start to see the welcome message.
Use /survey to start the totem quiz.
Check /privacy if you're curious about data handling.
Use /contact for official zoo links.
