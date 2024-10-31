import re

def contains_bulgarian_cyrillic(text):
    # Match any Cyrillic character in the Bulgarian range
    cyrillic_pattern = r'[\u0400-\u04FF]'
    return bool(re.search(cyrillic_pattern, text))
  
