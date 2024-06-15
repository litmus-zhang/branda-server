import json
import os
import re

import markdown
from langchain_community.llms import openai
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI as gai
from langchain_google_vertexai.vision_models import VertexAIImageGeneratorChat
from langchain_openai import OpenAI


md = markdown.Markdown()
generator = VertexAIImageGeneratorChat(number_of_results=2, quality="standard")



def generate_brand_name(industry: str, niche: str):
    llm = gai(
        temperature=0.8,
        model="gemini-pro",
        google_api_key=os.getenv("GOOGLE_AI_API_KEY"),
    )
    prompt_template_name = PromptTemplate(
        template="I have a business with the niche being {niche}, and I want a cool name for it, it is operating in the {industry} industry.suggest me 3 short but fancy names for my company",
        input_variables=["industry", "niche"],
    )

    name_chain = prompt_template_name | llm
    response = name_chain.invoke({"industry": industry, "niche": niche})

    final_res = response.split("\n")
    return [re.sub(r"[^a-zA-Z ]", "", i) for i in final_res if i != ""]


def generate_brand_color(industry: str, niche: str):
    llm = gai(
        temperature=0.8,
        model="gemini-pro",
        google_api_key=os.getenv("GOOGLE_AI_API_KEY"),
    )
    prompt_template_name = PromptTemplate(
        template="I have a business with the niche being {niche}, and it is operating in the {industry} industry.Give me 3 sets of complete set of brand colors in HEX codes for a brand in {industry} industry, put it is a array format",
        input_variables=["industry", "niche"],
    )

    name_chain = prompt_template_name | llm
    response = name_chain.invoke({"industry": industry, "niche": niche})
    array_str = response.strip("`\n")
    array = json.loads(array_str)
    return array


def generate_brand_messaging(industry: str, niche: str):
    llm = gai(
        temperature=0.8,
        model="gemini-pro",
        google_api_key=os.getenv("GOOGLE_AI_API_KEY"),
    )
    prompt_template_name = PromptTemplate(
        template="I have a business with the niche being {niche}, and I want a cool brand messaging for it, it is operating in the {industry} industry.suggest me 3 short but fancy brand messaging for my company",
        input_variables=["industry", "niche"],
    )
    name_chain = prompt_template_name | llm
    response = name_chain.invoke({"industry": industry, "niche": niche})

    final_res = response.split("\n")
    return [re.sub(r"[^a-zA-Z ]", "", i) for i in final_res if i != ""]


def generate_business_strategy(industry: str, niche: str, country: str = "Nigeria"):
    llm = gai(
        temperature=0.8,
        model="gemini-pro",
        google_api_key=os.getenv("GOOGLE_AI_API_KEY"),
    )
    prompt_template_name = PromptTemplate(
        template="I have a business with the niche being {niche}, and I want a superb brand strategy for it, it is operating in the {industry} industry. Give me 2 well detailed business strategies for a company operating in {industry} for {niche} living in {country}, using the Odyssey 3.14 approach of Value Architecture, Value Proposition and Profit Equation. i want the strategy should be written in markdown format like Strategy 1: Description of the strategy. Strategy 2: Description of the strategy.",
        input_variables=["industry", "niche", "country"],

    )

    name_chain = prompt_template_name | llm
    response = name_chain.invoke(
        {"industry": industry, "niche": niche, "country": country}
    )
    final = format_strategies(response)
    return final


def format_strategies(markdown_text):
    strategies = markdown_text.split("**Strategy")
    if strategies[0] == "":
        strategies.pop(0)

    formatted_strategies = []

    for strategy in strategies:
        title_end_index = strategy.find("\n")
        title = strategy[1:title_end_index].strip()
        content = strategy[title_end_index:].strip()

        strategy_dict = {f"Strategy {title}": content}

        formatted_strategies.append(strategy_dict)
    return formatted_strategies


def generate_logo(industry: str, niche: str):
    llm = OpenAI(temperature=0.9, n=2, api_key=os.getenv("OPENAI_API_KEY"))
    prompt_template_name = PromptTemplate(
        template="give me 3 minimalist logo only with for {niche}, which operates in {industry} industry.",
        input_variables=["industry", "niche"],
    )
    name_chain = prompt_template_name | llm
    # message = "give me some minimalist logo only with for Defi Startup, which operates in blockchain industry."
    # messages = [HumanMessage(content=[message])]
    # response = generator.invoke(messages)
    # generated_image = response.content[0]
    # print(generated_image)
    image_url = DallEAPIWrapper(n=2).run(
        name_chain.invoke({"industry": industry, "niche": niche})
    )
    response = image_url.split("\n")

    return response


def generate_pattern(industry: str):
    llm = openai.OpenAI(temperature=0.8, api_key=os.getenv("OPENAI_API_KEY"))
    prompt_template_name = PromptTemplate(
        template="give me a svg repeated pattern that can be used for background color or image in {industry} company website or flier",
        input_variables=["industry"],
    )
    # name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    name_chain = prompt_template_name | llm
    # response = DallEAPIWrapper(
    #     model="dall-e-3",
    #     quality="standard",
    # ).run(name_chain.run({"industry": industry}))
    # ans = response.split("\n")
    image_url = DallEAPIWrapper(n=2).run(name_chain.invoke({"industry": industry}))
    response = image_url.split("\n")
    return response


def generate_pics(industry: str):
    llm = openai.OpenAI(temperature=0.8, api_key=os.getenv("OPENAI_API_KEY"))
    prompt_template_name = PromptTemplate(
        template="give me realistic image that can be used to define a company in {industry} company website or flier",
        input_variables=["industry"],
    )
    name_chain = prompt_template_name | llm
    # response = DallEAPIWrapper(
    #     model="dall-e-3",
    #     quality="standard",
    # ).run(name_chain.run({"industry": industry}))
    # ans = response.split("\n")
    image_url = DallEAPIWrapper(n=2).run(name_chain.invoke({"industry": industry}))
    response = image_url.split("\n")

    return response