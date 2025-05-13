from transformers import BartTokenizer, BartForConditionalGeneration

class FastSum:
    def __init__(self, model_name='facebook/bart-large-cnn'):
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text, max_length=300, min_length=50, do_sample=False):
        inputs = self.tokenizer(text, return_tensors='pt', max_length=1024, truncation=True)
        summary_ids = self.model.generate(inputs['input_ids'], max_length=max_length, min_length=min_length, do_sample=do_sample)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary