import json
import os

class PhoneticEngineV5:
    """
    Phonetic Translation Engine V5.1
    A specialized utility for optimizing AI music generation (Suno/Udio).
    Developed by: AI Recording Specialist
    Principle: Philippians 3:13 - Pressing Forward
    """

    def __init__(self, glossary_file='glossary.json'):
        self.version = "5.1"
        self.quality_standard = "Golden Apple"
        self.glossary_file = glossary_file
        self.v5_library = self.load_glossary()

    def load_glossary(self):
        """Loads the phonetic dictionary from the JSON database."""
        if os.path.exists(self.glossary_file):
            try:
                with open(self.glossary_file, 'r') as f:
                    data = json.load(f)
                    return data.get("v5_data", {})
            except Exception as e:
                print(f"Error loading database: {e}")
                return {}
        else:
            print("Status: Glossary file not found. Please add glossary.json.")
            return {}

    def translate(self, text, to_phonetic=True):
        """
        BIDIRECTIONAL CORRECTION LOGIC:
        Allows users to go back and forth between regular spelling and AI code.
        Saves user time and money by fixing AI mispronunciations.
        """
        words = text.lower().split()
        result = []

        if to_phonetic:
            for word in words:
                result.append(self.v5_library.get(word, word))
        else:
            reverse_lib = {v: k for k, v in self.v5_library.items()}
            for word in words:
                result.append(reverse_lib.get(word, word))

        return " ".join(result)

    def display_status(self):
        print(f"--- V5 Phonetic Engine Active ---")
        print(f"Version: {self.version}")
        print(f"Standard: {self.quality_standard}")
        print(f"Logic: Bidirectional Correction Enabled")
        print(f"Foundation: Philippians 3:13")
        print("-" * 33)

if __name__ == "__main__":
    engine = PhoneticEngineV5()
    engine.display_status()
    sample_text = "faith power forgiveness"
    print(f"Input: {sample_text}")
    print(f"V5 Output: {engine.translate(sample_text, to_phonetic=True)}")
