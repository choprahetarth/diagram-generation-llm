import os 
import subprocess
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def runner_code(question, answer, temperature=0):
    """
    This function generates a diagram and code based on a given question and answer.

    Args:
        question (str): The question provided by the user.
        answer (str): The answer provided by the user.
        temperature (float, optional): The temperature parameter for the language model. Defaults to 0.

    Returns:
        None
    """

    # Prompt templates
    context_for_generation = PromptTemplate(
        input_variables = ['question', 'answer'], 
        template="""Given the question that a person is asking here -  </> {question} </> with the answer provided by the user here </> {answer}. Given this, you need to provide the thorough description of how will you make the diagram. Make sure that it is a simplistic one, which can be drawn by the python library of graphviz. Do not provide any other context."""
    )

    code_generator = PromptTemplate(
        input_variables = ['context_generated'], 
        template="""Given the description of the diagram - {context_generated}, generate a python code using the graphviz library. MAKE SURE THAT YOU JUST OUTPUT THE CODE, AND NOTHING ELSE. DO NOT INCLUDE THE CODE WITHIN THE '''python''' TAG, as the output code should be ready to run AS IS. The code should start like this - from graphviz import Digraph dot = Digraph(comment='image', format='png')'. The code should make sure that the output of the code should be "image.gv". The last line of the code should be dot.render('image.gv')."""
    )

    # Initialize language models
    llm = ChatOpenAI(temperature=temperature, model_name="gpt-4") 
    context_generation = LLMChain(llm=llm, prompt=context_for_generation, verbose=False, output_key='evaluation')
    code_generated_chain = LLMChain(llm=llm, prompt=code_generator, verbose=False, output_key='script')

    # Generate description of the diagram
    print("Running GPT-4 Agent.......")
    print("--------------- GENERATING DESCRIPTION ---------------------------------")
    context_generated = context_generation.run({'question':question,'answer':answer})
    print("--------------- DESCRIPTION IS GENERATED AS ----------------------------")
    print(context_generated)

    # Generate code based on the description
    generated_code = code_generated_chain.run({'context_generated':context_generated})
    print("-------------- THE CODE GENERATED IS -----------------------------------")
    print(generated_code)

    # Save the generated code to a file
    with open('generated_code.py', 'w') as file:
        file.write(generated_code)

    # Execute the generated code
    subprocess.run(["python", "generated_code.py"])