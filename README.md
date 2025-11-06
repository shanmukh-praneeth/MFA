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

## Installation

1. Prerequisites
