from langchain_community.llms import openai
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI as gai
from langchain.prompts import PromptTemplate
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
import os
import json
import re
import markdown

md = markdown.Markdown()

def generate_brand_name(industry: str, niche: str):
    llm = gai(temperature=0.8, model="gemini-pro", google_api_key=os.getenv('GOOGLE_AI_API_KEY'))
    prompt_template_name = PromptTemplate(
        template="I have a business with the niche being {niche}, and I want a cool name for it, it is operating in the {industry} industry.suggest me 3 short but fancy names for my company",
        input_variables = ["industry", "niche"],
    )

    name_chain = LLMChain(llm=llm, prompt= prompt_template_name, output_key="brand name")
    response = name_chain({"industry": industry, "niche": niche})


    final_res = response['brand name'].split('\n')
    return [re.sub(r'[^a-zA-Z ]', '', i) for i in final_res if i != '']

def generate_brand_color(industry: str, niche: str):
    llm = gai(temperature=0.8, model="gemini-pro", google_api_key=os.getenv('GOOGLE_AI_API_KEY'))
    prompt_template_name = PromptTemplate(
        template="I have a business with the niche being {niche}, and it is operating in the {industry} industry.Give me 3 sets of complete set of brand colors in HEX codes for a brand in {industry} industry, put it is a array format",
        input_variables = ["industry", "niche"],
    )

    name_chain = LLMChain(llm=llm, prompt= prompt_template_name, output_key="brand colors")
    response = name_chain({"industry": industry, "niche": niche})

    s= response['brand colors']
    #return s
    html_str = md.convert(s)
    # return html_str
    json_str = html_str.split("<code>")[1].split("</code>")[0]
    json_str = re.sub(r'//.*', '', json_str)
    color_sets = json.loads(json_str)
    return color_sets


def generate_brand_messaging(industry: str, niche: str):
    llm = gai(temperature=0.8, model="gemini-pro", google_api_key=os.getenv('GOOGLE_AI_API_KEY'))
    prompt_template_name = PromptTemplate(
        template="I have a business with the niche being {niche}, and I want a cool brand messaging for it, it is operating in the {industry} industry.suggest me 3 short but fancy brand messaging for my company",
        input_variables = ["industry", "niche"],
    )

    name_chain = LLMChain(llm=llm, prompt= prompt_template_name, output_key="brand messaging")
    response = name_chain({"industry": industry, "niche": niche})

    final_res = response['brand messaging'].split('\n')
    return [re.sub(r'[^a-zA-Z ]', '', i) for i in final_res if i != '']

def generate_business_strategy(industry: str, niche: str, country: str = "Nigeria"):
    llm = gai(temperature=0.8, model="gemini-pro", google_api_key=os.getenv('GOOGLE_AI_API_KEY'))
    prompt_template_name = PromptTemplate(
        template="I have a business with the niche being {niche}, and I want a superb brand strategy for it, it is operating in the {industry} industry.Give me a well detailed business strategy for a company operating in {industry} for {niche} living in {country}, using the Odyssey 3.14 approach of Value Architecture, Value Proposition and Profit Equation",
        input_variables = ["industry", "niche", "country"],
    )

    name_chain = LLMChain(llm=llm, prompt= prompt_template_name, output_key="brand strategy")
    response = name_chain({"industry": industry, "niche": niche, "country": country})

    s= response['brand strategy']
    #return s
    html_str = md.convert(s)
    return html_str


def generate_logo(industry: str, niche: str):
    llm = openai.OpenAI(temperature=0.8, api_key=os.getenv("OPENAI_API_KEY"))
    prompt_template_name = PromptTemplate(
        template="give me one minimalist logo only with for {niche}, which operates in {industry} industry.",
        input_variables = ["industry", "niche"],
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="brand logos")
    response = DallEAPIWrapper(
        model="dall-e-3",
        quality="standard",
    ).run(name_chain.run({"industry": industry, "niche" : niche }))
    return response

def generate_pattern(industry: str):
    llm = openai.OpenAI(temperature=0.8, api_key=os.getenv("OPENAI_API_KEY"))
    prompt_template_name = PromptTemplate(
        template="give me a svg repeated pattern that can be used for background color or image in {industry} company website or flier",
        input_variables=["industry"]
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = DallEAPIWrapper(
model="dall-e-3",
        quality="standard",
        ).run(name_chain.run({"industry": industry}))
    ans = response.split("\n")
    return ans

def generate_pics(industry: str):
    llm = openai.OpenAI(temperature=0.8, api_key=os.getenv("OPENAI_API_KEY"))
    prompt_template_name = PromptTemplate(
        template="give me realistic image that can be used to define a company in {industry} company website or flier",
        input_variables=["industry"]
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = DallEAPIWrapper(
model="dall-e-3",
        quality="standard",
                        ).run(name_chain.run({"industry": industry}))
    ans = response.split("\n")
    return ans
