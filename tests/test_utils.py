from utils.llm_ops import evaluate_prompt_performance
from utils.prompt_engineering import generate_prompt

def test_evaluate_prompt():
    performance = evaluate_prompt_performance("Sample prompt", "Sample response")
    assert "score" in performance

def test_generate_prompt():
    prompt = generate_prompt({"key": "value"})
    assert "value" in prompt
