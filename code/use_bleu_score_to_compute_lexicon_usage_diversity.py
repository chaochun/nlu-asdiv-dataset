"""Compute Corpus Lexicon Diversity on normalized text."""
from argparse import ArgumentParser
from sacrebleu.metrics import BLEU
import numpy as np


def read_lines_from_file(file_path):
    """Read lines from a file."""
    with open(file_path, 'r', encoding='utf-8') as file_read:
        return [line.strip() for line in file_read.readlines() if line.strip()]


def find_lexicon_usage_diversity_for_questions(questions):
    """Find lexicon usage diversity for questions."""
    bleu = BLEU()
    diversity_scores = np.zeros((len(questions), len(questions)))
    computed = np.zeros((len(questions), len(questions)))
    for i in range(len(questions)):
        for j in range(len(questions)):
            if i != j and diversity_scores[i][j] == 0. and computed[i][j] == 0.:
                question_i = questions[i]
                question_j = questions[j]
                bleu_forward = bleu.corpus_score([question_i], [[question_j]]).score
                if bleu_forward > 100.:
                    bleu_forward = 100.
                bleu_backward = bleu.corpus_score([question_j], [[question_i]]).score
                if bleu_backward > 100.:
                    bleu_backward = 100.
                average_bleu_norm = (1 / 200.) * (bleu_forward + bleu_backward)
                diversity_scores[i][j] = average_bleu_norm
                diversity_scores[j][i] = diversity_scores[i][j]
                computed[i][j] = 1.
                computed[j][i] = 1.
    return diversity_scores


def main():
    """Pass arguments and call functions here."""
    parser = ArgumentParser()
    parser.add_argument('--input', dest='inp', help='Enter the input file')
    args = parser.parse_args()
    questions = read_lines_from_file(args.inp)
    diversity_scores = find_lexicon_usage_diversity_for_questions(questions)
    max_scores = 1 - np.max(diversity_scores, axis=1)
    average_score = np.mean(max_scores)
    print(average_score)


if __name__ == '__main__':
    main()
