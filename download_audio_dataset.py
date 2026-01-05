# 1. Create the directory to store the dataset sample
!mkdir -p librispeech_sample

# 2. Download the 'dev-clean' subset of LibriSpeech
!wget -q https://www.openslr.org/resources/12/dev-clean.tar.gz -O dev-clean.tar.gz

# 3. Extract only the audio files (.flac) into the new directory
!tar -xzf dev-clean.tar.gz --directory librispeech_sample --wildcards "*.flac"

# 4. Verify the extraction by listing the first few .flac files
!find librispeech_sample -name "*.flac" | head
