# Blog-Generation-Platform
## _Example_
![alt text](https://github.com/AkashKobal/Blog-Generation-Platform/blob/main/Screenshot%20(324).png)
1. **Import Statements**:
   - You import the `CTransformers` module from both `langchain.llms` and `langchain_community.llms`. Ensure that you need both imports and that they are correctly referencing the desired functionality.

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
  

