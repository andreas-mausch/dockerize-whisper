```bash
docker build -t speech-to-text .
docker run -it --rm --network none -v $PWD/speech-test.mp3:/home/python/speech-test.mp3 speech-to-text "speech-test.mp3"
```

Example: https://nlpcloud.com/de/how-to-install-and-deploy-whisper-the-best-open-source-alternative-to-google-speech-to-text.html

Benchmarks: https://www.tomshardware.com/news/whisper-audio-transcription-gpus-benchmarked
