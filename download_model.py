from transformers import WhisperProcessor, WhisperForConditionalGeneration

# processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
# model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")
processor = WhisperProcessor.from_pretrained("openai/whisper-medium")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-medium")
