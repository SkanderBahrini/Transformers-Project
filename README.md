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

In this project, we used different models from Hugging Face Hub [Click Here] (https://huggingface.co/models)

Hugging Face offers a set of pre-trained models (since training a transformer model consumes a lot of energy is very harmful to the environment and requires a lot of hardware resources) as Bert and Bert uncased.

Users take those models and fine-tune them ( re-train them on specific tasks) example: fine-tune a model as Bert ( trained on English corpus) for specific tasks such as making it detect toxic speech ( Homophobic, Racist). Once the model is ready coders push it on their repo in Hugging Face Hub.

This project uses different models:

* First model: Aim to help the user understand what kind of feeling is transferred to the reader from his text.
  
  The checkpoint used : [Click Here] (https://huggingface.co/SamLowe/roberta-base-go_emotions) this model was created by fine-tuning Bert (bi-directional encoder representation transformer)

  A checkpoint is a specific file that contains model architecture and model-initialized weights.
  We used **Pytorch** to load the model, a machine learning framework that allows you to train and use machine learning and deep learning models. 
  To use it we have two methods:
  
  * Using Transformer pipeline ( Commented code)
  * Import Tokenizer and model separately
    
  ![oo](https://github.com/SkanderBahrini/Hate-speech-detection--Transformer/assets/74383561/e054f91a-c2f6-4817-a469-8cc3418c8ca1)

  * Tokenizer: The tokenizer will divide the sequence into words and then convert them into numbers ( input IDs and give attention mask)
    **Attention Mask**: Tell the model which words to focus on in a specific sequence
    **Input IDs**: A digit representation of a world in a sequence

  * Model: Contains the model that is already pre-trained by Huggigng face

  Once we downloaded our model and tokenizer from the Hugging Face hub we started using it in our web app as follows:
  
![text](https://github.com/SkanderBahrini/Hate-speech-detection--Transformer/assets/74383561/d343f33a-f922-448d-9d48-35ce68aab29b)

* Second model: Aim to help the user summarize a text:

  The checkpoint used: [Click here] (Falconsai/text_summarization): This model was created by fine_tuning the text to text transformer T5 developed by Google:
  We used **Pytorch** as a machine learning framework to load our model and tokenizer:
  For this transformer we opted for the first method by importing it directly using pipeline processing with the aim of 'Summarization' and the checkpoint: Falconsai/text_summarization
  You need also to have precise max_length and minimum_length of generated text
  
![pipeline](https://github.com/SkanderBahrini/Transformers-Project/assets/74383561/18722b80-fc0a-4cde-8e82-090e4913ade0)

* Once we loaded the model we can start using it:

![sum](https://github.com/SkanderBahrini/Transformers-Project/assets/74383561/65a60627-3cb4-429c-9a3a-e80bf55fcb3d)


Happy coding 😊


  


