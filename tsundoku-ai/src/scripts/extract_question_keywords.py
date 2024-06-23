import json

from openai import chat


def classify_question_and_extract_keywords(question):
    response = chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates search queries based on user question.",
            },
            {"role": "user", "content": "Python で形態素解析を実装する方法を教えてください。"},
            {
                "role": "assistant",
                "content": json.dumps({"keywords": ["Python", "形態素解析"]}),
            },
            {"role": "user", "content": question},
        ],
    )

    search_query = response.choices[0].message.content
    return search_query
