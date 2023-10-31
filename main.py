from pathlib import Path
from transformers import pipeline
import click
import librosa

@click.command(context_settings={'show_default': True})
@click.argument('files', nargs=-1)
def speech_to_text(files):
  for argument in files:
    for path in Path.cwd().glob(argument):
      # "WhisperFeatureExtractor was trained using a sampling rate of 16000"
      speech, sampling_rate = librosa.load(path, sr=16000)

      pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-medium",
        chunk_length_s=30,
        return_timestamps=True,
        max_new_tokens=4096,
        device='cpu',
        # task: transcribe is set to disable automatic translation
        generate_kwargs = {"task":"transcribe"} # optional: "language":"<|fr|>"
      )
      transcription = pipe(speech, batch_size=16)

      print("%s: %s" % (path.relative_to(Path.cwd()), transcription))

if __name__ == '__main__':
  speech_to_text()
