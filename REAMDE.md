---
title: 'Large Language Model Prompt Engineering for Complex Summarization'
author: John Stewart
slug: gpt-summary-prompt-engineering
post_date: 2023-03-26 12:01:00
categories: GPT, LLM, Prompt-Engineering, Medical
tags: GPT, LLM, prompt-engineering, medical
# featured_image: assets/pair-programming-raccoons.png
summary: Learn how to use GPT / LLMs to create complex summaries such as for medical text
---

# Large Language Model Prompt Engineering for Complex Summarization 

The recent explosion in the popularity of Large language Models (LLM) such as ChatGPT has opened the floodgates to an enormous and ever-growing list of possible new applications in a lot of different fields. 
On a recent engagement, our team created a demo of how to use the [Azure OpenAI]() service to leverage LLM capabilities in generating summaries of medical documents for non-specialist readers.

## Background

Every day, hundreds of new medical specialist papers are published on sites such as [PubMed](). 
For patients or caregivers with a keen interest in new research impacting their condition, it can often be difficult to comphrehend the complex jargon and language.
Consequently, many journals are require submitters to produce a separate, short [Plain Language Summary]() for the non-specialist reader. 
Our customer asked that we prototype a way to use GPT to produce these lay-summaries using AI, freeing up 
time for researchers and editors to concentrate on their primary focus of publishing new medical research.

## Hypothesis

A model like OpenAI's Davinci-3, the original LLM that underpinned ChatGPT, could produce a passable Plain Language Summary of medical text describing a drug-study, which could then be refined by an author or editor in short time.  
We targed a complete summary, including important details from the source text like patient population, treatment outcomes, and how the research impacted disease treatment.  
The output needed to be ~250 words, omit specialist medical terms, and be informative enough for the reader to get a full understanding of the source paper.

## Setup

You can follow along with the example Jupyter Notebook prompt-engineering exercise from the [Github repo](https://github.com/microsoft/gpt-prompt-eng-blogpost).  
We are using the [LangChain](https://python.langchain.com/en/latest/index.html) python library as a harness for our use of Azure OpenAI and GPT3.  
Ensure you have a new virtual-environment setup and install the needed dependencies by running `pip install -r requirements.txt` from the root of the project.
We will use the [pdfminer](https://pypi.org/project/pdfminer/) library to convert the source paper PDF into plaintext for ingestion into Azure OpenAI GPT.
The prompt-engineering exercise uses a representative medical article from [PubMed](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10171157/pdf/41398_2023_Article_2435.pdf).  

## Caveats
### Length of paper
The Azure OpenAI Davinci-3 model has a [limit](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/models#model-summary-table-and-region-availability) of 4097 [tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) of combined input and output.  
Given that we want around 250 words of output and a token represents around three-quarters of a word, we will reserve 500 tokens for the completion response.  That leaves ~3600 tokens for input, or about 2700 words.
Any source text longer than 2700 words will need to be manually edited to fit.
### Graphs and Figures
The Davinci-3 model was trained on billions of words of text, including a lot of graphs and charts.  However we can only input plain-text into the OpenAI service.
For this experiment we will assume the input is only plain-text, and whatever unformatted table data that can be extracted automatically from the source PDF.
### Need for Human Review
It bears repeating that the goal of this experiment is to make a _draft_ summary, and any output produced must be reviewed, edited, and approved by a responsible human party.

## Initial Try

Initially we just ask it to summarize the input text, as someone might using the public ChatGPT website...

`
prompt_template = """
Write a Plain Language Summary of the medical study below:
{study_text}
"""
`

## Refinining As You Go

## Multi-Step Generation

## Matching the Desired Tone

## Lessons Learned

## Future Directions
- graphs and figures
- longer input text
- GPT4 and beyond
- chat based interface
- 

## Acknowledgements

Authored by [John Stewart](https://www.linkedin.com/in/john-ms/), Microsoft Commercial Software Engineering, with helpful editing and suggestions from ChatGPT.