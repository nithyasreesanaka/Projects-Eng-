from transformers import pipeline

# Load summarization pipeline with free Hugging Face model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Limit text length for demo
    max_input = 1024
    text = text.strip().replace("\n", " ")
    if len(text) > max_input:
        text = text[:max_input]
    
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    # Test text
    input_text = """
    Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems.
    These processes include learning, reasoning, and self-correction. Applications of AI include expert systems, natural
    language processing, speech recognition, and machine vision.
    """
    result = summarize_text(input_text)
    print("Summary:")
    print(result)
