from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

class Summarizer:
    def __init__(self, model_name="t5-base"):
        # Load pre-trained model and tokenizer
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, no_repeat_ngram_size=2):
        """
        Summarize the input text using T5 model.
        """
        # Preprocess the input text for T5
        input_ids = self.tokenizer.encode(f"summarize: {text}", return_tensors="pt", max_length=512, truncation=True)
        
        # Generate the summary (Greedy or Beam search depending on parameters)
        summary_ids = self.model.generate(
            input_ids, 
            max_length=max_length, 
            min_length=min_length, 
            length_penalty=length_penalty, 
            num_beams=num_beams, 
            no_repeat_ngram_size=no_repeat_ngram_size, 
            early_stopping=True
        )
        
        # Decode the summary output
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    
def main():
    # Example text
    text = """
    Your long input text here...
    """

    summarizer = Summarizer()
    summary = summarizer.summarize(text)
    print("Summary: ", summary)

if __name__ == "__main__":
    main()