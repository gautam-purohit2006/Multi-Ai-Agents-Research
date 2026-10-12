from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Thinking-2507",   
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional research writer.

Your task is to create a clear, accurate, and well-structured research report
using the information provided by the research agents.

Follow these rules:
- Use only the information provided in the research data.
- Do not invent facts.
- Organize the answer with clear headings.
- Explain important points in simple language.
- Include important source URLs when available.
- Remove duplicate or irrelevant information.
- Mention uncertainty when the information is incomplete.
- Keep the final report concise but informative.

Output format:

# Research Report

## Overview
Brief introduction.

## Key Findings
- Important finding 1
- Important finding 2
- Important finding 3

## Detailed Analysis
Explain the findings clearly.

## Sources
- Title: URL
- Title: URL
"""
    ),
    (
        "human",
        """
Research topic:
{topic}

Research data:
{research_data}

Write the final research report.
"""
    )
])


writer_chain = writer_prompt | model | parser

critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional research critic.

Your job is to review the research report and give a short,
clear, user-friendly critique.

IMPORTANT RULES:
- Do NOT explain your reasoning.
- Do NOT mention what you are thinking or analyzing.
- Do NOT write a long paragraph.
- Do NOT rewrite the complete research report.
- Use only the information available in the report.
- If something cannot be verified from the report, say "Needs verification".
- Be concise and professional.

Return ONLY this exact format:

# Research Critique

## Accuracy
[Briefly state whether the main information appears accurate.
Mention incorrect or unsupported claims if any.]

## Completeness
[Mention important missing information, or write "No major missing information."]

## Relevance
[Mention irrelevant information, or write "The report is relevant to the topic."]

## Clarity
[Mention clarity problems, or write "The report is clear and easy to understand."]

## Sources
[Mention source problems, or write "Sources are sufficient based on the report."]

## Suggestions
- [Suggestion 1]
- [Suggestion 2]

## Final Status
[APPROVED or NEEDS_REVISION]

Do not add anything before or after this format.
"""
    ),
    (
        "human",
        """
Research Report:

{research_report}

Review this report and return ONLY the required critique format.
"""
    )
])
critic_chain = critic_prompt | model | parser



