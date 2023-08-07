def validate_output(response: str) -> str:
    """
    Validate and sanitize the model's output using Guardrails or any other criteria.
    For now, it just checks the word count, you might want to extend this.
    """
    if len(response.split()) > 500: 
        return response[:500] + '...'  # truncate to 500 words
    return response
