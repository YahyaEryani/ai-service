from transformers import AutoTokenizer, AutoModelForCausalLM

class HuggingFaceModel:
    def __init__(self):
        # Specifying the model's name
        self.model_name = "gpt2-large"
        
        # Initializing tokenizer and model from the Hugging Face library
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        
        # Adding padding token for cases where padding might be required
        self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        
        # Adjusting the model's token embedding size according to the new tokenizer's vocabulary size
        self.model.resize_token_embeddings(len(self.tokenizer))  

    def encode_input(self, input_text: str):
        """
        Encode the given input text to be suitable for the model's input.

        Parameters:
        - input_text (str): The text to be encoded.

        Returns:
        - dict: Dictionary containing input IDs and attention masks.
        """
        return self.tokenizer.encode_plus(
            input_text, 
            return_tensors='pt',
            padding='max_length',  # This ensures padding if required
            max_length=1024  # Define a max length for the encoded input
        )

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response for the given prompt using the model.

        Parameters:
        - prompt (str): The prompt to which a response should be generated.

        Returns:
        - str: The generated response.
        """
        # Encoding the provided prompt
        encoded_input = self.encode_input(prompt)
        input_ids = encoded_input['input_ids']
        
        # Also extracting the attention mask which will be used during the generation process
        attention_mask = encoded_input['attention_mask']

        # Using the model to generate a response
        output = self.model.generate(
            input_ids, 
            attention_mask=attention_mask,  # Providing attention_mask for better results
            max_length=800,  # Defining a max length for the response
            temperature=0.3,  # Temperature affects the randomness in the output
            top_k=80,  # Top k sampling
            top_p=0.95,  # Top p sampling
            eos_token_id=self.tokenizer.eos_token_id,  # Token indicating the end of the sequence
            no_repeat_ngram_size=2  # Prevents the model from repeating ngrams of size 2
        )

        # Decoding the model's output to obtain the response text
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

    def decode_output(self, response_ids):
        """
        Decode the response IDs to obtain the text.

        Parameters:
        - response_ids (list): List of token IDs representing the response.

        Returns:
        - str: The decoded text.
        """
        return self.tokenizer.decode(response_ids[0], skip_special_tokens=True)