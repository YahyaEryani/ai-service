from transformers import AutoTokenizer, AutoModelForCausalLM

class HuggingFaceModel:
    def __init__(self):
        self.model_name = "gpt2-large"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        self.model.resize_token_embeddings(len(self.tokenizer))  

    def encode_input(self, input_text: str):
        return self.tokenizer.encode_plus(
            input_text, 
            return_tensors='pt',
            padding='max_length',  # This ensures padding if required
            max_length=1024  #
        )

    def generate_response(self, prompt: str) -> str:
        encoded_input = self.encode_input(prompt)
        input_ids = encoded_input['input_ids']

        # Make sure you're also providing attention_mask
        attention_mask = encoded_input['attention_mask']

        output = self.model.generate(
            input_ids, 
            attention_mask=attention_mask,  # Add this line
            max_length=800,
            temperature=0.3,
            top_k=80,
            top_p=0.95,
            eos_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=2
        )

        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

    def decode_output(self, response_ids):
        return self.tokenizer.decode(response_ids[0], skip_special_tokens=True)