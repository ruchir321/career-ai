# Career-ai

A LLM app personalized to my job application history.

## Motivation

I have applied to more than 30 applications in the past 20 days.

The job tracker spreadsheet has job posting link, job tile, referral status and application status.

I believe a RAG application will be a helpful guide to get clarity with the types of job I have been applying.

The app will compare a new job description to old ones to find similarities, which is a good hint to reuse resume from a previous job application.

Job descriptions are available as web links or pdf print of the job posting webpage.

## data available

1. Job tracker spreadsheet
2. Job description pdf (almost all job apping folder have it)
3. Resume
4. Job posting webpage (if it is still live)

## RAG application

As a user I would like to:

1. input my job descriptions to find common job requirements
2. Find jobs which are relevant to a set of requirements

## Frontend

Streamlit app

UI will have dropbox for:

1. user resume draft
2. job tracker spreadsheet
3. job application folder

## Backend

An LLM will retrieve inferences from:

1. user resume draft
2. job description
3. common keywords

The expected output is a `text-generation` of resume improvement suggestions.

## Prompt

`Langchain Hub` has a collection prompts for community
