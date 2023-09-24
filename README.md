# diagram-generation-llm
LLM Diagram Generation

## Description

This project is a web application that generates diagrams and corresponding code based on a given question and answer. It utilizes the OpenAI GPT-4 language model to generate a description of the diagram, and then uses the description to generate Python code using the graphviz and langchain library. The generated code can be executed to produce the diagram.

## Installation

To install and use the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Install the required Python libraries by running the following command in the project directory:

   ```bash
   pip install -r requirements.txt
   ```

3. Install the required Linux packages by running the following command in the project directory:

   ```bash
   sudo apt-get install -y $(cat packages.txt)
   ```

4. Generate an OpenAI API key by following the instructions provided in the [OpenAI documentation](https://openai.com/docs/authentication/).

5. Set the OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY=<your_api_key>
   ```

## Usage

1. Run the Streamlit application by executing the following command in the project directory:

   ```bash
   streamlit run streamlit_app.py
   ```

2. Access the application in your web browser at `http://localhost:8501`.

3. Enter the question and answer in the respective input fields.

4. Adjust the temperature slider to control the creativity of the generated output.

5. Click the "Compute!" button to generate the diagram and code.

6. Wait for the diagram to be generated and displayed on the web page.

## Video Tutorial

For a video tutorial on how to use the project, please refer to the following link: [Project Demo](https://www.youtube.com/watch?v=jvYLPBmxqFg)