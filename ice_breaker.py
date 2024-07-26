import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI  # Assuming this is the correct import
from langchain.chains import LLMChain


if __name__ == "__main__":
    print("hello langchain!")

summary_template = """
Given the information {information} about a person, create:
1. A short summary
2. Two interesting facts about them
"""

summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyB3S-OLnzz_qT6CXsrPbfWuU2H6WmfzEhU")

chain = LLMChain(prompt=summary_prompt_template, llm=llm)

def generate_summary(information):
    return chain.run(information=information)


def main():
    st.title('Person Summary Generator')
    input_information = st.text_area('Enter information about a person:', height=250)

    if st.button('Generate Summary') and input_information:
        summary = generate_summary(input_information)
        st.subheader('Generated Summary:')
        st.write(summary)


if __name__ == "__main__":
    main()
