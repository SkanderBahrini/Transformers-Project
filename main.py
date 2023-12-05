import streamlit as st

import PIL 

from PIL import Image

st.set_page_config(
   
   page_title= 'Here for you',
   page_icon='🧠'
)

stri = """
       <h1 style= 'text-align:center;'>  Welcome To Here for you </h1>
"""

st.markdown( stri, unsafe_allow_html= True)

st.markdown("#")


# images of food 

c1,c2 = st.columns(2)

m = Image.open('images/grad.jpg')
m1 = Image.open('images/together.jpg')

c1.image(m )
c2.image(m1)


st.write('#')
# small introductory text 
text= """Hello in this website will help you in your studies or professional duties by allowing you to look formal and advance in your career"""

st.write(text) 
# input space

st.write("#")


# instantiate tranformer using tensorflow:
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import TextClassificationPipeline
def nlp(opinion):

   # classifier = pipeline(model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
    #result = classifier(opinion)
    
     checkpoint = "SamLowe/roberta-base-go_emotions"
     tokenizer = AutoTokenizer.from_pretrained( checkpoint)
     model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
     pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)
     output = pipe(opinion)
  
     return output

from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
def generative(opinion):


  pipe = pipeline("question-answering", model="deepset/tinyroberta-squad2")
  output = pipe(opinion)

  return opinion

tab1,tab2,tab3= st.tabs([' Text Emotion Detection ', 'e', 'r'])



with tab1 : 
 
  col1 ,col2 = st.columns([2,8])
 

  st.write("#")
  text = """  <h3  style='text-align:center ;'> 👂🏻 + 🙉 Check how your text sounds </h3>"""

  st.markdown( text, unsafe_allow_html= True)

  st.write('#')

  text1 = """The importance of the feelings conveyed by a text lies in its ability to create a meaningful and impactful experience for the reader, fostering connection, understanding, and resonance.
    Whether the goal is to inform, persuade, entertain, or express artistry, emotions are a powerful tool in the hands of skilled communicators."""

  st.write('**Important Notice:**')
  st.write(text1)

  st.write('You can write text see what kind of feelings the reader can sense in your texts')
  
  st.write('**Express yourself:**')
  text = st.text_area('')


  if text:

    result =nlp(text) 

    label = result[0]['label']
    
    st.info(f'Your text is giving of a feeling of {label}')



with tab2:
    
    text = st.text_input('write')
    result = generative(text)
    result 