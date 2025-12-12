from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI

#OpenAI LLM Setup
def main():
    llm = OpenAI(temperature=0.7)

    #prompt template
    prompt_template = PromptTemplate(
        input_variables=["question"], 
        template="You are a detailed and precise assistant. Answer the following question: {question}"
    )


    #LLM Chain
    chain = LLMChain(llm=llm, prompt=prompt_template)

    print("Hello! I am Mother A\n's AI chatbot. Ask me anything or type 'exit to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")

    # Generates the AI response
        response = chain.run(question=user_input)
        print(f"Chatbot: {response}")

    if __name__ == "__main__":
        main()
