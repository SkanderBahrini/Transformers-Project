# Transformer in machine learning tasks

🎯 The goal of this project was to help users in their careers by providing simple guidance while writing professional or academic documents.

# 🐍 Streamlit Web app

To design this project we opted for a Python library named Streamlit that allows users to design their web application using Python.
The advantages of Streamlit are:

* 👌 Simplicity
* 📈 Integrated with data science libraries
* 🆕 Automatic updates


We decided to opt for specific types of deep learning models named transformers to achieve our aim. 
To achieve our goal we decided to opt for Hugging face transformers.

# 🤗 Hugging Face
First of all, let's define Hugging Face, It is a company based in Brooklyn that develops application programming interfaces (APIs) to download pre-trained models and use them for specific tasks such as:

* ✍️ NLP: Natural language processing
* 🖼️ Image recognition
* 📝 Text-generation
* 🎧 Audio tasks

Now after introducing the company and the field of use of its transformers. 

* Let's discuss the models:

Transformer architectures  are divided into three types:

* Encoders: It converts each word of a sequence into a sequence of numbers named (tensor features). Each vector is defined by the context it is surrounded by thanks to a bi-directional self-attention mechanism.
  They are used for text classification, masked world, and question answering. Used for NLU: Natural language understanding (Bert)
  
* Decoders: It has the same characteristics as Encoders. Nevertheless, it uses a one-direction self-attention mechanism (right or left). It is mainly used in text-generation tasks NLG: Natural language generation (GPT).
  
* Encoders and Decoders: A models that mix between the two previous types of architectures

