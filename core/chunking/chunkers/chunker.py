from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter , HTMLHeaderTextSplitter
from langchain_text_splitters import HTMLSectionSplitter
import tiktoken
import logging

logger = logging.getLogger(__name__)

class MyTextSplitter:
    def __init__(self, chunk_size=100):
        self.chunk_size = chunk_size

    def split_text(self, text):
        return [text[i:i + self.chunk_size] for i in range(0, len(text), self.chunk_size)]

def chunk_fixSize(size,input_text):
    
    textsplit = MyTextSplitter(
        chunk_size = size,
    )
        
    chunks  = textsplit.split_text(input_text)
    return chunks

def Sliding(size,input_text,overlap, separators):
    
    sentenceTextsplit =  RecursiveCharacterTextSplitter(
        chunk_size=size,    
        chunk_overlap=overlap,
        separators=separators
    )
    logger.info("provided chunk separators : "+separators)

    
    chunks = sentenceTextsplit.split_text(input_text)
    return chunks

# def token(size,input_text):
    enc = tiktoken.get_encoding("gpt2")
    tokens = enc.encode(input_text)
    logger.info("All tokens len : "+str(len(tokens)))
    
    chunks = [tokens[i:i+size] for i in range(0, len(tokens), size)]
    chunks_text = [enc.decode(chunk) for chunk in chunks]
    
    logger.info("provided chunk size : "+str(size))
    logger.info("First chunk : "+chunks_text[0])
    return chunks_text    
