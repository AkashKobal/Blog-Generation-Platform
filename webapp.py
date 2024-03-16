from langchain.llms import CTransformers
import streamlit as st
# from langchain_community import CTransformers
from langchain_community.llms import CTransformers

# creating a function to get a response from LLama 2 model
def get_response(input_text, no_of_words, blog_style):

    # llm = CTransformers(model="model\llama-2-7b-chat.ggmlv3.q8_0.bin", model_type="llama")

    # calling LLama model which we downloaded from Hugging Face using CTransformers
    llm = CTransformers(model="model\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type="llama",
                        config={"max_new_tokens": 256,"temperature": 0.9})

    # creating a prompt template
    template = '''
            Write a blog about {blog_style} on {input_text} with {no_of_words} words.
            '''
    
    # creating a prompt template
    prompt_template = PromptTemplate(input_variables=["blog_style", "input_text", "no_of_words"],
                                     template=template)
    
    # generate a response from LLama model
    response=llm(prompt_template.format(blog_style=blog_style,input_text=input_text,no_of_words=no_of_words))
    print(response)
    return response

# setting the Streamlit or Flask API
st.set_page_config(page_title="Generate Blogs with LLama 2", 
                   page_icon=":rocket:", 
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs with LLama 2 :rocket:")

input_text = st.text_area("Enter the blog topic")

## creating to more columns for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    no_of_words = st.text_input("No of words")

with col2:
    blog_style = st.selectbox("Writing the blog for",
                              ("Research", "Creative","Technical"), index=0)
    
submit = st.button("Generate")

## final response from the model
if submit:
    st.write(get_response(input_text, no_of_words, blog_style))



