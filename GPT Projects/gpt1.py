import openai

openai.api_key = "api-key-here"

def translate_text(text, source_language, target_language):
    prompt = f"Translate this ' {source_language} ' text to' {target_language}': {text}"

    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that translates text."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    translation = response.choices[0].message.content.strip()
    
    return translation


def test(text):
    source_language = "English"
    target_language = "Italian"

    translated_text = translate_text(text, source_language, target_language)
    return translated_text

