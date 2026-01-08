import json

# --- THIS IS YOUR V5.1 GOLDEN APPLE GLOSSARY ---
glossary_data = {
    # --- UNIVERSAL POWER PACK ---
    "faith": "fay-ay-thhh [airy]",
    "power": "POW-errr [grit]",
    "hallelujah": "hal-lay-LOO-yah [soaring]",
    "forgiveness": "fuh-GIV-nessss [long sustain]",
    "anointed": "uh-NOYN-ted [reverb]",
    "mercy": "MUR-see [soft]",
    "victory": "VIC-tuh-ree [punchy]",
    "freedom": "FREE-dum [open]",
    "glory": "GLOR-ee-ay [sustained]",
    
    # --- LATANKAL (LATIN/TROPICAL) ---
    "corazon": "ko-rah-SOHN [vibrant]",
    "ritmo": "REET-moh [percussive]",
    "baile": "BYE-lay [smooth]",
    "fuego": "FWAY-go [sharp]",
    "musica": "MOO-see-kah [staccato]",
    "bailando": "by-LAHN-doh [swing]",

    # --- THE "BACK" LOGIC ---
    "fuh-GIV-nessss [long sustain]": "forgiveness",
    "fay-ay-thhh [airy]": "faith",
    "hal-lay-LOO-yah [soaring]": "hallelujah",
    "ko-rah-SOHN [vibrant]": "corazon",
    "uh-NOYN-ted [reverb]": "anointed"
}

# --- THIS IS YOUR ENGINE LOGIC ---
def golden_apple_engine():
    print("--- Golden Apple V5.1 Engine Active ---")
    print("Test the 'Back Logic' by typing the phonetic spelling!")
    
    while True:
        user_input = input("\nUser Input: ").strip() # Removed .lower() to keep your bracket tags [airy] safe
        
        if user_input.lower() == 'q':
            print("Shutting down... Straining forward (Phil 3:13)")
            break
        
        if user_input in glossary_data:
            result = glossary_data[user_input]
            print(f"Engine Output: {result}")
        else:
            # Check lowercase just in case for standard words
            if user_input.lower() in glossary_data:
                print(f"Engine Output: {glossary_data[user_input.lower()]}")
            else:
                print("Result: Word not in V5.1 Starter Pack yet.")

# Run the test
golden_apple_engine()
