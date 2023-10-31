# AI: speech-to-text

This is a dockerized CLI tool for speech-to-text.
It takes an audio file and prints the recognized text on the stdout.

It is designed for offline usage.

See also [my AI list on github.com](https://github.com/stars/andreas-mausch/lists/ai).

# Build and run

```bash
docker build -t speech-to-text .
docker run -it --rm --network none -v $PWD/speech-test.mp3:/home/python/speech-test.mp3 speech-to-text "speech-test.mp3"
```

# Links

Example: https://nlpcloud.com/de/how-to-install-and-deploy-whisper-the-best-open-source-alternative-to-google-speech-to-text.html

Benchmarks: https://www.tomshardware.com/news/whisper-audio-transcription-gpus-benchmarked
