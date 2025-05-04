# from django.test import TestCase
# from .chunkers.chunker import MyTextSplitter
# # Create your tests here.


# class TestMyTextSplitter(TestCase):
    
#     def testing1(self):
#         text = "Lena was a curious girl who loved exploring the woods behind her house every afternoon she would pack a small bag with snacks a notebook and her favorite compass one day she discovered a trail she had never seen before it led her to a hidden pond with crystal clear water and colorful fish swimming near the surface excited she began sketching what she saw in her notebook suddenly a small turtle climbed out of the water and looked at her as if it wanted to say something she laughed and said hello little one this became her secret spot a magical place she would return to again and again."
#         testsplitter = MyTextSplitter(10)
        
#         chunks = testsplitter.split_text(text)
#         self.assertEqual(10,len(chunks[0]))
     
import pytest   
from .chunkers.chunker import MyTextSplitter
from .chunkers import chunker 

@pytest.fixture
def text():
    return "Lena was a curious girl who loved exploring the woods behind her house every afternoon she would pack a small bag with snacks a notebook and her favorite compass one day she discovered a trail she had never seen before it led her to a hidden pond with crystal clear water and colorful fish swimming near the surface excited she began sketching what she saw in her notebook suddenly a small turtle climbed out of the water and looked at her as if it wanted to say something she laughed and said hello little one this became her secret spot a magical place she would return to again and again."


def test_split_text_exact_chunks(text):
    splitter = MyTextSplitter(chunk_size=10)
    chunks = splitter.split_text(text)
    assert len(chunks[0]) == 10

def test_chunk_fixSize(text):
    chunks = chunker.chunk_fixSize(20,text)
    assert chunks is not None