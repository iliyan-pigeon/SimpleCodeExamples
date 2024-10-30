from deep_translator import GoogleTranslator

# Initialize the translator for Bulgarian
translator = GoogleTranslator(source='auto', target='bg')

# Text to translate
text = "revolut payments"

# Translate text to Bulgarian
translated_text = translator.translate(text)

print("Translated text:", translated_text)
