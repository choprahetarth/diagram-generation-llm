import os 
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = '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'


# Prompt templates
context_for_generation = PromptTemplate(
    input_variables = ['question', 'answer'], 
    template="""Given the question that a person is asking here -  </> {question} </> with the answer provided by the user here </> {answer}. Given this, you need to provide the thorough description of how will you make the diagram. Make sure that it is a simplistic one. """
)

code_generator = PromptTemplate(
    input_variables = ['context_for_generation'], 
    template='GIven the description of the diagram, generate the code in a{resume_scorer}, '
)

message_generator = PromptTemplate(
    input_variables = ['name_of_referrer','resume', 'job_description', 'resume_evaluator'], 
    template="""Act as a Job Seeker requesting {name_of_referrer} a personalized referral for a job posting in the form of a LinkedIn DM.
            Make sure that the DM is precise and aligns your resume (given here {resume}) with the job description ({job_description}) according to alignment information given here {resume_evaluator}, in maximum 150 words.
            DO NOT MENTION ANYTHING IN THE DM THAT IS MISALIGNED WITH THE RESUME, ESPECIALLY THE YEARS OF EXPERIENCE, OR THE USER WILL DIE!"""
)

# Llms
llm = ChatOpenAI(temperature=0) 
# llm2 = OpenAI(temperature=0.1) 
evaluator_chain = LLMChain(llm=llm, prompt=resume_evaluator, verbose=False, output_key='evaluation')
resume_scorer_chain = LLMChain(llm=llm, prompt=resume_scorer, verbose=False, output_key='script')
generator_chain = LLMChain(llm=llm, prompt=message_generator, verbose=False, output_key='message')


# Show stuff to the screen if there's a prompt
 
print("Running GPT-3.5-Turbo Agent.......")
print("--------------- EVALUATING RESUME WITH THE JOB DESCRIPTION ------------------------------")
evaluation = evaluator_chain.run({'resume':resume,'job_description':job_description})
print("--------------- EVALUATING RESULT -------------------------------------------------------")
print(evaluation)
resume_score = resume_scorer_chain.run({'resume_scorer':evaluation})
print("-------------- THE LABEL IS FOUND OUT AS ------------------------------------------------")
print(resume_score)
message = generator_chain.run({'resume':resume,'job_description':job_description, 'name_of_referrer': name_of_referrer, 'resume_evaluator':evaluation})
print("-------------- GENERATING THE DM GIVEN THE EVALUATION RESULTS ---------------------------")
print(message)