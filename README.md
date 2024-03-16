# Blog-Generation-Platform-With-LLAMA

## Description:
### This repository contains code for generating blog content using the LLama 2 language model. It integrates with Streamlit for easy user interaction. Simply input your blog topic, desired word count, and writing style to generate engaging blog content.

### This GitHub code demonstrates the use of the LLama 2 model for generating blog content using Streamlit. It imports the CTransformers module from langchain.llms and langchain_community.llms for language model integration. The get_response function prompts the user to input a blog topic, number of words, and style, then generates a response using the LLama 2 model. Streamlit is used to create a user-friendly interface for input and output.

### The LLama 2 model is specified with its model file and type, along with configuration parameters such as max_new_tokens and temperature for text generation.

### Streamlit is configured to create a centered layout with collapsed initial sidebar state. Users can input the blog topic, number of words, and select the style of writing (Research, Creative, Technical) before generating the response.

### Finally, upon clicking the "Generate" button, the model generates a response based on the provided inputs and displays it using Streamlit.

## 🚀 Features:
### - Easy-to-use interface with Streamlit
### - Integration with LLama 2 model for generating diverse and context-aware blog content
### - Customize writing style for Research, Creative, or Technical topics



## _Example_
![alt text](https://github.com/AkashKobal/Blog-Generation-Platform/blob/main/Screenshot%20(324).png)

## Download requirements:
`sentence-transformers`
`uvicorn`
`ctransformers`
`langchain`
`python-box`
`streamlit`

### Download model from [Hugging Face](https://huggingface.co/localmodels/Llama-2-7B-Chat-ggml/tree/main) 👈

![alt text](https://github.com/AkashKobal/Blog-Generation-Platform/blob/main/hg.png)

### Steps to run

1. **Import Statements**:
   - You import the `CTransformers` module from both `langchain.llms` and `langchain_community.llms`. Ensure that you need both imports and that they are correctly referencing the desired functionality.
```python !
pip install langchain
```
```python
pip install langchain_community
```  
```python 
pip install CTransformers
```
```python 
pip install streamlit
```




2. **Function Definition (`get_response`)**:
   - This function is designed to retrieve a response from the LLama 2 model based on user inputs such as the blog topic, number of words, and writing style.
   - It initializes the LLama 2 model with the specified parameters, including the model file, model type, and configuration options such as `max_new_tokens` and `temperature`.
   - You define a prompt template to guide the model in generating the blog content based on the provided inputs.
   - The function then generates a response from the LLama 2 model using the prompt template and returns it.

3. **Streamlit Setup**:
   - You configure the Streamlit page with a title and layout settings.
   - The user is presented with input fields to enter the blog topic, number of words, and select the writing style (e.g., Research, Creative, Technical).
   - Upon clicking the "Generate" button, the function `get_response` is called with the provided inputs, and the generated response is displayed on the Streamlit interface.

4. **Final Response**:
   - The generated response from the LLama 2 model is displayed in the Streamlit interface for the user to review.
   - Run the command in terminal
   - ```txt
      streamlit run webapp.py
      ```

  

