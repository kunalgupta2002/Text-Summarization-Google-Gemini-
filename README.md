# Text Summarizer and Key Points Highlighter
Overview:
This project leverages LangChain, Google Gemini, and Streamlit to create a web application that takes text input from the user, summarizes the content, and highlights the key points within the text. The main goal is to provide users with a concise summary while emphasizing the most important information from the provided text.

Features:
Text Summarization: Automatically generates a concise summary of the input text.
Key Points Highlighting: Highlights key points within the text to emphasize the most important information.
User-Friendly Interface: Streamlit-based interface for easy interaction and input.
Technologies Used
LangChain: Used for handling natural language processing tasks and text manipulation.
Google Gemini: Employed for advanced text analysis and summarization capabilities.
Streamlit: Provides a simple and interactive web interface for user input and output display.
Installation
To get started with the project, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/kunalgupta2002/text-summarizer-key-points-highlighter.git
cd text-summarizer-key-points-highlighter
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Usage
Open the web browser and go to the local URL provided by Streamlit (usually http://localhost:8501).

Enter the text you want to summarize in the input box.

Click the "Summarize" button.

The application will display the summarized text and highlight the key points.

Project Structure
app.py: Main application file that sets up the Streamlit interface and handles user input.
summarizer.py: Contains the functions for text summarization and key points highlighting using LangChain and Google Gemini.
requirements.txt: Lists all the dependencies required for the project.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
LangChain
Google Gemini
Streamlit
