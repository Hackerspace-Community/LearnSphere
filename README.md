# LearnSphere ⦡

<img src="https://i.imgur.com/r88JjEV.png">

LearnSphere utilizes the power of OpenAI's Chat-GPT model for creating personalized learning roadmaps.

## Setup Instructions

Follow these steps to set up the project:

1. Clone the repository
```bash
git clone git@github.com:HarshitRV/LearnSphere.git
```

2. Create a virtual environment for the project. If you're not familiar with creating virtual environments, you can refer to this guide: [How to Setup Virtual Environments in Python](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

3. Activate the virtual environment.

4. Install the project dependencies by running the following command in the project root directory:
```bash
pip install -r requirements.txt

```
5. Create a .env file in the root of the project folder and add the following line, replacing `YOUR_OPEN_AI_API_KEY` with your actual OpenAI API key:
```makefile
API_KEY=YOUR_OPEN_AI_API_KEY
```
6. Obtain your OpenAI API key from the official OpenAI website: [OpenAI API](https://platform.openai.com/)
7. Start the server by running the following command:
```bash
python main.py
```
8. Open your web browser and navigate to http://localhost:3000 to see the LearnSphere server in action.

### [See Demo (click here) 🎥](https://www.youtube.com/watch?v=cpgLHeSlJuE)