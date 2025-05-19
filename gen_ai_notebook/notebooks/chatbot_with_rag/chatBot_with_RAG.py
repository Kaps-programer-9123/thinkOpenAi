from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
import datetime

# New imports for RAG
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader  # Simple text file loader
from langchain.text_splitter import CharacterTextSplitter # Split text
from typing import List, Callable


# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

def create_chatbot(features: List[str] = None, knowledge_base_path: str = None) -> ConversationChain:
    """Creates a chatbot using LangChain with optional features and RAG."""
    llm = OpenAI(model_name="gpt-3.5-turbo")
    memory = ConversationBufferMemory()
    prompt = PromptTemplate(
        input_variables=["input", "history"],
        template="""You are a helpful chatbot.
        {history}
        User: {input}
        Chatbot:"""
    )
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt,
        verbose=True
    )

    if features:
        if "date_time" in features:
            conversation.predict = add_date_time(conversation.predict)
        if "summarize" in features:
            conversation.predict = add_summarization(conversation.predict, memory)

    if knowledge_base_path:
        # Set up RAG if knowledge base path is provided
        qa_chain = setup_rag(knowledge_base_path, llm)
        conversation.predict = add_rag(conversation.predict, qa_chain)

    return conversation


def add_date_time(predict_func: Callable[[str], str]) -> Callable[[str], str]:
    """Decorator to add current date and time to the chatbot's response."""
    def wrapper(input_str: str) -> str:
        now = datetime.datetime.now()
        formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        response = predict_func(input_str)
        return f"{response} (Current date and time: {formatted_date_time})"
    return wrapper


def add_summarization(predict_func: Callable[[str], str], memory: ConversationBufferMemory) -> Callable[[str], str]:
    """Decorator to summarize the conversation every 3 turns."""
    turn_count = 0
    summary_chain = LLMChain(llm=OpenAI(temperature=0), template="Summarize the following conversation:\n{conversation}")

    def wrapper(input_str: str) -> str:
        nonlocal turn_count
        turn_count += 1
        response = predict_func(input_str)
        if turn_count % 3 == 0:
            conversation_text = memory.load_memory_variables({})['history']
            summary = summary_chain.run(conversation=conversation_text)
            memory.chat_memory.add_message(f"Chatbot: (Summary of last 3 turns: {summary})")
        return response
    return wrapper

def add_rag(predict_func: Callable[[str], str], qa_chain: RetrievalQA) -> Callable[[str], str]:
    """Decorator to integrate RAG into the chatbot's response generation."""
    def wrapper(input_str: str) -> str:
        # Check if the input is a question
        if is_question(input_str):
            rag_response = qa_chain.run(input_str)
            return rag_response
        else:
            return predict_func(input_str)
    return wrapper

def is_question(text: str) -> bool:
    """Simple heuristic to determine if a text is a question."""
    return text.strip().endswith("?")

def setup_rag(knowledge_base_path: str, llm: OpenAI) -> RetrievalQA:
    """
    Sets up the Retrieval Augmented Generation (RAG) component.

    Args:
        knowledge_base_path (str): Path to the directory containing the knowledge base text files.
        llm (OpenAI): The language model.

    Returns:
        RetrievalQA: A LangChain RetrievalQA chain.
    """
    documents = []
    for filename in os.listdir(knowledge_base_path):
        if filename.endswith(".txt"):  # Only process text files.  Add other file types if you want.
            filepath = os.path.join(knowledge_base_path, filename)
            loader = TextLoader(filepath)
            documents.extend(loader.load())

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()  # Use OpenAI for embeddings
    db = FAISS.from_documents(texts, embeddings)  # FAISS for efficient similarity search
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
    return qa



def main():
    """Main function to run the chatbot."""
    print("Welcome to the RAG-Enabled Chatbot! Type 'exit' to end.")
    print("Available features: 'date_time', 'summarize'.  Type 'enable <feature>' or 'disable <feature>' to control them.")

    enabled_features = []
    # Specify the path to your knowledge base directory
    knowledge_base_path = "./knowledge_base"  # Create a folder named knowledge_base and put your .txt files there
    if not os.path.exists(knowledge_base_path):
        os.makedirs(knowledge_base_path)
        print(f"Created knowledge base directory at {knowledge_base_path}.  Please add .txt files to this directory.")

    chatbot = create_chatbot(features=enabled_features, knowledge_base_path=knowledge_base_path)
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        if user_input.startswith("enable "):
            feature_name = user_input.split(" ")[1]
            if feature_name in ["date_time", "summarize"]:
                enabled_features.append(feature_name)
                chatbot = create_chatbot(features=enabled_features, knowledge_base_path=knowledge_base_path)
                print(f"Feature '{feature_name}' enabled.")
            else:
                print(f"Feature '{feature_name}' not recognized.")
            continue

        elif user_input.startswith("disable "):
            feature_name = user_input.split(" ")[1]
            if feature_name in ["date_time", "summarize"]:
                enabled_features.remove(feature_name)
                chatbot = create_chatbot(features=enabled_features, knowledge_base_path=knowledge_base_path)
                print(f"Feature '{feature_name}' disabled.")
            else:
                print(f"Feature '{feature_name}' not recognized.")
            continue

        response = chatbot.predict(input=user_input)
        print("Chatbot:", response)



if __name__ == "__main__":
    main()
