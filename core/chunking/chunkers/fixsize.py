from langchain.text_splitter import CharacterTextSplitter

def chunk_fixSize(size,input_text):
    
    textsprit = CharacterTextSplitter(
        separator=" ",
        chunk_size = size,
    )
        
    chunk  = textsprit.split_text(input_text)

    return chunk