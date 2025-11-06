# Forced Alignment using Montreal Forced Aligner (MFA)
This project demonstrates a complete forced alignment pipeline using the Montreal Forced Aligner (MFA).
Forced alignment automatically matches speech audio with its phonetic transcription, identifying when each word and phoneme begins and ends in the audio signal.

## Project Structure

```
mfa/
├─ corpus/                      # Contains .wav and .txt (transcripts are normalized and overwritten)
│   ├─ F2BJRLP1.wav
│   ├─ F2BJRLP1.txt
│   └─ ...
├─ models/                      # Models and resources used by MFA
│   ├─ acoustic/
│   │   └─ english_us_arpa.zip
│   ├─ dictionary/
│   │   └─ english_us_arpa.dict
│   └─ cache.json
├─ outputs/
│   ├─ aligned/                 # Output folder containing alignments and alignment_analysis.csv
│   │   ├─ F2BJRLP1.TextGrid
│   │   ├─ F2BJRLP2.TextGrid
│   │   ├─ alignment_analysis.csv
│   │   └─ ...
├─ scripts/
│   ├─ normalize_transcripts.py # Script to normalize text transcripts
├─ transcripts/           # Consists of all transcripts files provided
├─ wav/                   # Consists of all audio files provided
├─ MFA_Assignment.pdf     # Report consisting of model/dictionary brief, alignment analysis and alignment visualization using Praat
└─ README.md
```

## Environment Setup

1. Using Conda Base Environment
   ```bash
   conda activate base
   ```
2. Install MFA
   ``` bash
   conda create -n aligner -c conda-forge montreal-forced-aligner
   ```
3. Shift to the aligner environment
   ``` bash
   conda activate aligner
   ```
4. Download the Acoustic model
   ```bash
   mfa model download acoustic english_us_arpa
   ```
5. Download the pronunciation dictionary
   ``` bash
   mfa model download dictionary english_us_arpa
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
      * The following bash command can be used to create a corpus folder with an MFA-required structure
      ``` bash
      mkdir -p corpus
      ```
      ```bash
      for f in wav/*.wav; do
         b=$(basename "$f" .wav);
         cp "$f" "corpus/${b}.wav";
         cp "transcripts/${b}.txt" "corpus/${b}.txt";
      done
      ```
      * Each .txt file should contain the exact transcript for its corresponding .wav file

   2. Normalize transcripts
      * Since the dictionary uses lowercase words, all transcripts must be made lowercase. Additionally, white spaces and punctuation are also removed.
        ``` bash
         python scripts/normalize_transcripts.py corpus/
        ```
      * This overwrites each .txt file with a lowercase, cleaned version compatible with MFA

## Running Forced Alignment
   ``` bash
   mfa align corpus english_us_arpa english_us_arpa outputs/aligned
   ```
   
