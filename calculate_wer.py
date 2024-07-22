import Levenshtein as lev


def calculate_wer(reference_text, hypothesis_text):
    # Tokenize the texts (splitting by spaces)
    reference_tokens = reference_text.strip().split()
    hypothesis_tokens = hypothesis_text.strip().split()

    # Calculate the Word Error Rate (WER)
    wer = lev.distance(' '.join(reference_tokens), ' '.join(hypothesis_tokens)) / float(len(reference_tokens))
    return wer


def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    reference_file = 'transcripts/8842-304647-0013.txt'
    hypothesis_file = 'transcription.txt'

    # Load reference and hypothesis texts
    reference_text = load_text(reference_file)
    hypothesis_text = load_text(hypothesis_file)
    import re
    import Levenshtein as lev

    def preprocess_text(text):
        # Küçük harfe çevir
        text = text.lower()
        # Noktalama işaretlerini kaldır
        text = re.sub(r'[^\w\s]', '', text)
        # Fazla boşlukları kaldır
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def calculate_wer(reference, hypothesis):
        # Metinleri ön işleme tabi tut
        reference = preprocess_text(reference)
        hypothesis = preprocess_text(hypothesis)

        # WER hesaplamak için Levenshtein mesafesini kullan
        # Levenshtein mesafesi, ekleme, silme ve değişiklik sayısını verir
        ref_words = reference.split()
        hyp_words = hypothesis.split()

        # Levenshtein mesafesini hesapla
        distance = lev.distance(' '.join(ref_words), ' '.join(hyp_words))

        # WER hesapla
        wer = distance / len(ref_words) if ref_words else 0
        return wer

    # Örnek kullanım
    reference_text = "THOU LIKE ARCTURUS STEADFAST IN THE SKIES WITH TARDY SENSE GUIDEST THY KINGDOM FAIR BEARING ALONE THE LOAD OF LIBERTY"
    hypothesis_text = "Val like arc steadfast in the skies, with tar scents guide by kingdom fair, bearing alone the load of liberty."

    wer = calculate_wer(reference_text, hypothesis_text)
    print(f"Word Error Rate (WER): {wer:.2f}")

    # Calculate WER
    wer = calculate_wer(reference_text, hypothesis_text)

    print(f"Word Error Rate (WER): {wer:.2f}")


if __name__ == "__main__":
    main()
