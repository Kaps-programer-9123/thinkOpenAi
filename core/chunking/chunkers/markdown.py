from langchain.text_splitter import HTMLHeaderTextSplitter
from langchain_text_splitters import HTMLSectionSplitter
import logging

logger = logging.getLogger(__name__)

def markdown_header(input_text):
    
    headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
    ]

    html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    html_header_splits = html_splitter.split_text(input_text)
    return headers_to_split_on, html_header_splits
    
    
def markdown_section(input_text):
    
    headers_to_split_on = [("h1", "Header 1"), ("h2", "Header 2")]

    html_splitter = HTMLSectionSplitter(headers_to_split_on=headers_to_split_on)
    html_section_splits = html_splitter.split_text(input_text)
    logger.info(html_section_splits[0])
    
    return headers_to_split_on, html_section_splits