# import the necessary dependencies for our code 
import streamlit as st

# load transformers since we are using Pytorch as our machine learning framework we load AutoToknizer and Auto%odelSeuqenceClassification 
# for emotion detection
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import TextClassificationPipeline
from PIL import Image
# load transformers packages for summarization
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

# Page confing where we set up page title and icon
st.set_page_config(
   
   page_title= 'Here for you',
   page_icon='🧠'
)
 #Dipslay  title 
stri = """
       <h1 style= 'text-align:center;'>  Welcome To Here for you </h1>
"""

st.markdown( stri, unsafe_allow_html= True)

st.markdown("#")


# diplay images using  

c1,c2 = st.columns(2)

m = Image.open('images/grad.jpg')
m1 = Image.open('images/together.jpg')

c1.image(m )
c2.image(m1)

st.write('#')
# small introductory text 
text= """Hello in this website will help you in your studies or professional duties by allowing you to look formal and advance in your career"""
st.write(text) 
st.write("#")


# Generate function that detects emotions using transformers

def emotiondetection(opinion):
  
  # method one using transformer's pipeline 
   # classifier = pipeline(model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
    #result = classifier(opinion)
    
     checkpoint = "SamLowe/roberta-base-go_emotions"
     tokenizer = AutoTokenizer.from_pretrained( checkpoint)
     model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
     pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)
     output = pipe(opinion)
  
     return output

#  Generate function that summarize text using transformer
def generative(opinion):

     pipe = pipeline("summarization", model="Falconsai/text_summarization")
     output = pipe( opinion, max_length=150, min_length=30, do_sample=False) 
     return output


# Tabs division using streamlit
tab1,tab2= st.tabs([' Text Emotion Detection ', 'Summarize text'])


# Tab1 cotent 
with tab1 : 
 
  col1 ,col2 = st.columns([2,8])
  st.write("#")
  text = """  <h3  style='text-align:center ;'> 👂🏻 + 🙉 Check how your text sounds </h3>"""

  st.markdown( text, unsafe_allow_html= True)

  st.write('#')
  
  # introductory text 

  text1 = """The importance of the feelings conveyed by a text lies in its ability to create a meaningful and impactful experience for the reader, fostering connection, understanding, and resonance.
    Whether the goal is to inform, persuade, entertain, or express artistry, emotions are a powerful tool in the hands of skilled communicators."""

  st.write('**Important Notice:**')
  st.write(text1)

  st.write('You can write text see what kind of feelings the reader can sense in your texts')
  
  st.write('**Express yourself:**')
  text = st.text_area('')


  if text:

    result = emotiondetection(text)

    label = result[0]['label']
    
    st.info(f'Your text is giving of a feeling of {label}')


# tab 2 content 

with tab2:
    
    text = st.text_area('Put your text here')

    if text:
       result = generative(text)
       st.success(result[0]['summary_text'])
   