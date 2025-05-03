from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .chunkers import fixsize

# Create; your views here.
def home(request):
    return HttpResponse("Hello from the Chunking Home!")

def fixSize(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            size = data.get("size")
            input_text = data.get("text", "")
            chunk_data = fixsize.chunk_fixSize(size,input_text)
            if not input_text:
                return JsonResponse({"error": "No text provided"}, status=400)
            
            # Example processing (just return length)
            return JsonResponse({"chunk data": chunk_data, "size": size})
        
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


