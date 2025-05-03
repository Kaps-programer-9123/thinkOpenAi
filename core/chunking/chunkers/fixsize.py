from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter 

def chunk_fixSize(size,input_text):
    
    textsplit = CharacterTextSplitter(
        separator=" ",
        chunk_size = size,
        chunk_overlap = (size / 10)
    )
        
    chunks  = textsplit.split_text(input_text)
    return chunks

def Sliding(size,input_text,overlap, separators):
    
    sentenceTextsplit =  RecursiveCharacterTextSplitter(
        chunk_size=size,    
        chunk_overlap=overlap,
        separators=separators
    )
    
    chunks = sentenceTextsplit.split_text(input_text)
    return chunks
    
    