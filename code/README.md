#### For installing the required libraries, type the following command
pip -r requirements.txt
#### Code to calculate Corpus Lexicon Diversity (CLD) for a set of word problems. We implemented a code as given in the paper [A Diverse Corpus for Evaluating and Developing
English Math Word Problem Solvers](https://aclanthology.org/2020.acl-main.92.pdf).
#### Requires 2 steps
- Normalize text where person names and numbers will be replaced by a common symbol or tag. PERSON is used for person names and NUMBER for numbers.
python use_spacy_to_find_named_entities_and_normalize_text.py --input sample_input.txt --output sample_input_normalized.txt
- Use Bleu scores to compute Corpus Lexicon Diversity (CLD) for a normalized corpus. Gives the CLD score on the screen.
python use_bleu_score_to_compute_lexicon_usage_diversity.py --input sample_input_normalized.txt
