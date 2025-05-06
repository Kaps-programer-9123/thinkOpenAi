from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .chunkers import chunker
from .chunkers import markdown as md
import logging

logger = logging.getLogger(__name__)
# Create; your views here.
def home(request):
    return HttpResponse("Hello from the Chunking Home!")

def fixSize(request):
    result, input_text, size, overlap, separators = validator(request)
    if result == "No_error":
        chunk_data = chunker.chunk_fixSize(size,input_text)
        return JsonResponse({"chunk data": chunk_data, "size": size})


def Sliding(request):
    result, input_text, size, overlap, separators = validator(request)
    logger.info(result,input_text,size,overlap)
    if result == "No_error":
        chunk_data = chunker.Sliding(size,input_text,overlap, separators)
        return JsonResponse({"chunk data": chunk_data, "size": size,  "overlap": overlap, "separators": separators})

def token(request):
    result, input_text, size, overlap, separators = validator(request)
    logger.info(result)
    if result == "No_error":
        chunk_data = chunker.token(size,input_text)
        return JsonResponse({"chunk data": chunk_data, "size": size})

def markdown(request):
    response = """use markdown/header or markdown/section for better split of text
    sample request : 
                     1 http://127.0.0.1:8000/chunking/markdown/header
                     2. http://127.0.0.1:8000/chunking/markdown/section
    """
    return HttpResponse(response)

def markdown_header(request):
    result, input_text, size, overlap, separators = validator(request)
    logger.info(result)
    logger.info(input_text)
    
    if result == "No_error":
        headers_to_split_on, chunk_data = md.markdown_header(input_text)
        logger.info(headers_to_split_on)
        logger.info(chunk_data)
        serializable_data = [
            {
                "page_content": doc.page_content,
                "metadata": doc.metadata
            }
            for doc in chunk_data
        ]

        return JsonResponse({"chunk data": serializable_data})
    
def markdown_section(request):
    result, input_text, size, overlap, separators = validator(request)
    logger.info(result)
    logger.info(input_text)
    
    if result == "No_error":
        headers_to_split_on, chunk_data = md.markdown_section(input_text)
        logger.info(headers_to_split_on)
        logger.info(chunk_data)
        serializable_chunk = [
            {
                "page_content": doc.page_content,
                "metadata": doc.metadata
            }
            for doc in chunk_data
        ]
        
        headers_to_split_on = {
        "h1": "Header 1",
        "h2": "Header 2"
        }

        return JsonResponse({"chunk data": serializable_chunk,"section split on :": headers_to_split_on})

def validator(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            input_text = data.get("text", "")
            size = data.get("size", 100)
            overlap = data.get("overlap",size/10)
            separators = data.get("separators","")
            if not input_text:
                return JsonResponse({"error": "No text provided"}, status=400)
            else:
                return "No_error" , input_text, size, overlap, separators   
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method allowed"}, status=405)
    
    
def example(request):
    sample = """
    ########################################
    --- Chunk 1 ---
    One day, an old man was walking along a beach that was littered with thousands of starfish that had been washed ashore by the tide.
    As he walked, he saw a young boy in the distance, picking something up and gently throwing it into the ocean.
    
    ########################################
    --- Chunk 2 ---
    As the man approached, he called out, “Good morning! May I ask what you are doing?”

    ########################################
    --- Chunk 3 ---
    The boy paused, looked up, and replied, “I’m throwing starfish back into the ocean.
    The tide has washed them up and they can’t return to the sea by themselves. If I don’t throw them back, they’ll die.”
    """
    return HttpResponse(f"<pre>{sample}</pre>")