"""Normalize questions with Spacy."""
from argparse import ArgumentParser
from spacy import load
from re import search
from re import sub


# Spacy English Model
en_model = load('en_core_web_lg')
# Number Pattern
number_pattern = '\d+\.\d+|\d+'


def read_lines_from_file(file_path):
    """Read lines from a file."""
    with open(file_path, 'r', encoding='utf-8') as file_read:
        return [line.strip() for line in file_read.readlines() if line.strip()]


def write_lines_to_file(lines, file_path):
    """Write lines into a file."""
    with open(file_path, 'w', encoding='utf-8') as file_write:
        file_write.write('\n'.join(lines))


def normalize_questions(questions):
    """Normalize questions where you replace person names and numbers with a normalized tag."""
    normalized_questions = []
    for question in questions:
        parsed = en_model(question)
        normalized_question = []
        updated_flag = False
        for index, sent in enumerate(parsed.sents):
            updated_sentence = sent.text
            for ent in sent.ents:
                if ent.label_ == 'PERSON':
                    updated_sentence = sub(ent.text, 'PERSON', updated_sentence)
                    updated_flag = True
                elif search(number_pattern, ent.text):
                    updated_sentence = sub(number_pattern, 'NUMBER', updated_sentence)
                    updated_flag = True
            if not updated_flag:
                updated_sentence = sent.text
            normalized_question.append(updated_sentence)
            updated_flag = False
        normalized_question_text = ' '.join(normalized_question)
        normalized_question_text = sub(number_pattern, 'NUMBER', normalized_question_text)
        normalized_questions.append(normalized_question_text)
    return normalized_questions


def main():
    """Pass arguments and call functions here."""
    parser = ArgumentParser()
    parser.add_argument('--input', dest='inp', help='Enter the path of the input question file')
    parser.add_argument('--output', dest='out', help='Enter the path for the normalized question file')
    args = parser.parse_args()
    question_file = args.inp
    normalized_question_file = args.out
    questions = read_lines_from_file(question_file)
    normalized_questions = normalize_questions(questions)
    write_lines_to_file(normalized_questions, normalized_question_file)


if __name__ == '__main__':
    main()
