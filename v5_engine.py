import json
import os

class PhoneticEngineV5:
    def __init__(self, glossary_file='glossary.json'):
        self.version = "5.1"
        self.glossary_file = glossary_file
        self.v5_library = self.load_glossary()

    def load_glossary(self):
        """Loads the phonetic dictionary from the JSON file."""
        if os.path.exists(self.glossary_file):
            with open(self.glossary_file, 'r') as f:
                data = json.load(f)
                return data.get("v5_data", {})
        else:
            print("Error: glossary.json not found.")
            return {}

    def translate(self, text, to_phonetic=True):
        """
        BIDIRECTIONAL LOGIC: 
        True = Standard to Phonetic
        False = Phonetic back to Standard
        """
        words = text.lower().split()
        result = []

        if to_phonetic:
            for word in words:
                result.append(self.v5_library.get(word, word))
        else:
            # Reverse Lookup for corrections
            reverse_lib = {v: k for k, v in self.v5_library.items()}
            for word in words:
                result.append(reverse_lib.get(word, word))

        return " ".join(result)

# --- INSTRUCTIONS FOR USE ---
if __name__ == "__main__":
    engine = PhoneticEngineV5()
    
    # Example: User is trying to fix a mispronounced word
    print(f"V5 Engine Status: {engine.version} Active")
    user_input = "faith power forgiveness"
    print(f"Standard Input: {user_input}")
    print(f"AI Code Output: {engine.translate(user_input, to_phonetic=True)}")
