# Forced Alignment using Montreal Forced Aligner (MFA)
This project demonstrates a complete forced alignment pipeline using the Montreal Forced Aligner (MFA).
Forced alignment automatically matches speech audio with its phonetic transcription, identifying when each word and phoneme begins and ends in the audio signal.

## Project Structure

```
mfa_project/
├─ corpus/                      # Contains .wav and .txt (transcripts are normalized and overwritten)
│   ├─ F2BJRLP1.wav
│   ├─ F2BJRLP1.txt
│   └─ ...
├─ outputs/
│   ├─ aligned/                 # Output folder containing alignments
│   │   ├─ F2BJRLP1.TextGrid
│   │   ├─ F2BJRLP2.TextGrid
│   │   ├─ alignment_analysis.csv
│   │   └─ ...
├─ scripts/
│   ├─ normalize_transcripts.py # Script to normalize text transcripts
├─ models/                      # Models and resources used by MFA
│   ├─ acoustic/
│   │   └─ english_us_arpa.zip
│   ├─ dictionary/
│   │   └─ english_us_arpa.dict
│   ├─ g2p/
│   │   └─ english_us_g2p.zip
│   └─ cache.json
└─ README.md
```

## Environment Setup

1. Using Conda Base Environment
   ```bash
   conda activate base
   ```
2. Install MFA
   ``` bash
   conda install -c conda-forge montreal-forced-aligner
   ```

## Preparing Data
   1. Organize Corpus
      * Ensure that the dataset folder follows the following structure
      ```
      corpus/
      ├─ F2BJRLP1.wav
      ├─ F2BJRLP1.txt
      ├─ F2BJRLP2.wav
      ├─ F2BJRLP2.txt
      └─ ...
      ```
      * Each .txt file should contain the exact transcript for its corresponding .wav file

   2. Normalize transcripts
      * Since the dictionary uses lowercase words, all transcripts must be made lowercase. Additionally, white spaces and punctuation are also removed.
        ``` bash
         python scripts/normalize_transcripts.py corpus/
        ```
      * This overwrites each .txt file with a lowercase, cleaned version compatible with MFA
