# Automatic Chatbot for WhatsApp
This project is a fully automatic WhatsApp Chatbot that detects new messages, opens them, and replies without any manual interaction. The bot is designed to streamline the process of responding to messages, making communication hands-free.

## Features
- Automatic Detection: The bot detects new messages based on specific indicators on the WhatsApp interface (e.g., green dot).
- Message Replying: Automatically opens the new message and sends a reply based on pre-defined responses.
- Customizable Responses: You can modify or add responses by adjusting the code in whatsapprespo.py.

## Folder Structure
- Demo Folder: Contains a demo video showing how the bot works. This will give you a visual understanding of the bot's functionality.
- Images Folder: Contains images used to detect new messages and interact with the WhatsApp interface.
green_dot.jpeg is used to identify a new message notification.
clip.jpeg is used to find the location of the text box where the message is typed and sent.
- Note: If you're not using dark mode or using an iOS device, you may need to replace these images with updated screenshots from your version of WhatsApp.

## Main Files
- chatbot.py:
This file contains the main code for the WhatsApp Chatbot.
If you want to run this bot on your system, you will need to adjust some coordinates, as they may differ depending on your screen size and resolution.
All the coordinates that need to be adjusted are clearly mentioned in the comments within the script.
- whatsapprespo.py:
This file contains the logic for generating responses to messages.
You can easily modify or add new responses to match your needs.

## Setup Instructions
Ensure you have all the required dependencies installed.
Update the green_dot.jpeg and clip.jpeg images if needed (especially if you're not using dark mode).
Open the chatbot.py file and update the coordinates based on your screen resolution.
Run the chatbot.py script, and the bot will start detecting and responding to messages automatically.


## Notes
Screen Resolution: The bot uses image recognition and coordinate-based actions, so the coordinates in the script may vary based on your screen resolution.

Custom Responses: Feel free to modify whatsapprespo.py to customize the responses sent by the bot.
