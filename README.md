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

## Scalability and Caveats
In order to make the current app more scaleable, and stable, we can make the following design changes -

1. Instead of using Streamlit, which is a a free service, a proper REST-API can be developed with the help of Flask, and a front-end UI can be designed with the help of ReactJS.

2. It can be deployed on Serverless infra such as Vercel or an AWS Lambda. It can help us scale the system horizontally, and since we are using GPT-4 we don't need to worry about vertical scaling. If needed to use an internal LLM such as a fine-tuned version of LLaMA-2, we have to take care of vertical scaling as well. 

3. Since the system uses langchain, we can swap and experiment with multiple LLM's all at once. However, the prompts will have to be fine-tuned accordingly.

Some other caveats include -

1. The biggest caveat is that the dependence on GraphViz, which might not be the best method to generate diagrams. It is good in plotting graphs that show relationships between each other, however it might not be able to generate diagrams that have no inter dependencies. 

2. If one uses the system with temperature setting = 0, the prompt will work and the generated code will run. However, the system will be less and less deterministic if the temperature settings are increased, and there can be a chance that the diagram generation code might not run at all. 

3. How to avoid such scenarios? - Using sophisticated prompt chaining such as Chain of Thought (Wei et al. https://arxiv.org/abs/2201.11903). I have not used the technique here, as it is currently experimental, and a little expensive to implement.

4. Also, a google search button can be added if a user is not happy with the results.

Given more time, we can integrate these changes for a more robust experience. 