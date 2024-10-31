import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    try:
        with codecs.open(html_file, 'r', 'utf-8') as file:
            html = file.read()
        cleaned_text = re.sub(r'<.*?>', '', html)
        cleaned_text_lines = cleaned_text.splitlines()
        cleaned_text_lines = [line for line in cleaned_text_lines if line.strip() != '']
        cleaned_text = '\n'.join(cleaned_text_lines)
        with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write(cleaned_text)

        print(f"Очищений текст записано у файл '{result_file}'")

    except Exception as e:
        print(f"Сталася помилка: {e}")

delete_html_tags('draft.html', 'cleaned.txt')