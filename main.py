import os 
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = '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'


question = "How does photosynthesis work?"
answer =  " Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll pigments."

# Prompt templates
context_for_generation = PromptTemplate(
    input_variables = ['question', 'answer'], 
    template="""Given the question that a person is asking here -  </> {question} </> with the answer provided by the user here </> {answer}. Given this, you need to provide the thorough description of how will you make the diagram. Make sure that it is a simplistic one. Do not provide any other context."""
)

code_generator = PromptTemplate(
    input_variables = ['context_generated'], 
    template="""Given the description of the diagram - {context_generated}, generate a python code using the graphviz library. The code should start like this - from graphviz import Digraph dot = Digraph(comment='image', format='png')'. The code should make sure that the output of the code should be "image.gv". """
)

# Llms
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo") 
# llm2 = OpenAI(temperature=0.1) 
context_generation = LLMChain(llm=llm, prompt=context_for_generation, verbose=False, output_key='evaluation')
code_generated_chain = LLMChain(llm=llm, prompt=code_generator, verbose=False, output_key='script')


# Show stuff to the screen if there's a prompt
 
print("Running GPT-3.5-Turbo Agent.......")
print("--------------- EVALUATING RESUME WITH THE JOB DESCRIPTION ------------------------------")
context_generated = context_generation.run({'question':question,'answer':answer})
print("--------------- EVALUATING RESULT -------------------------------------------------------")
print(context_generated)
generated_code = code_generated_chain.run({'context_generated':context_generated})
print("-------------- THE LABEL IS FOUND OUT AS ------------------------------------------------")
print(generated_code)


# Open a file in write mode
with open('generated_code.txt', 'w') as file:
    # Write the variable's value into the file
    file.write(generated_code)

print("Code Saved Successfully")