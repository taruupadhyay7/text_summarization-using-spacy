import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extractive_summarize(text, num_sentences=5):

    # Extra stopwords
    extra_words = set(STOP_WORDS) | set(punctuation) | {"\n", " "}

    # Process text with spaCy
    docx = nlp(text)

    # ── Word Frequency ──
    all_words = [
        word.text.lower()
        for word in docx
        if word.text.lower() not in extra_words and word.is_alpha
    ]

    freq_word = {}
    for word in all_words:
        freq_word[word] = freq_word.get(word, 0) + 1

    # ── Normalize Frequencies ──
    if not freq_word:
        return "Could not generate summary. Please provide more text."
    
    max_freq = max(freq_word.values())
    for word in freq_word:
        freq_word[word] = freq_word[word] / max_freq

    # ── Score Each Sentence ──
    sent_strength = {}
    for sent in docx.sents:
        for word in sent:
            word_lower = word.text.lower()
            if word_lower in freq_word:
                sent_strength[sent] = sent_strength.get(sent, 0) + freq_word[word_lower]

    # ── Pick Top N Sentences ──
    top_sentences = sorted(sent_strength, key=sent_strength.get, reverse=True)
    top_n = top_sentences[:num_sentences]

    # ── Return in Original Order ──
    summary = [sent.text.strip() for sent in docx.sents if sent in top_n]
    return " ".join(summary)


def get_topic_keywords(text, top_n=5):
    extra_words = set(STOP_WORDS) | set(punctuation) | {"\n", " "}
    docx = nlp(text)

    freq_word = {}
    for word in docx:
        w = word.text.lower()
        if w not in extra_words and word.is_alpha:
            freq_word[w] = freq_word.get(w, 0) + 1

    # Return top N keywords
    sorted_words = sorted(freq_word, key=freq_word.get, reverse=True)
    return sorted_words[:top_n]