import os
import time
import pyaudio
import wave
from google.cloud import texttospeech
from config import mp3_path, CREDENTIALS_PATH

# Set Google Cloud credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH
os.chdir(mp3_path)

def TTS(text, output_file_name):

    client = texttospeech.TextToSpeechClient()

    # 텍스트 입력
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # 음성 설정 (언어 = 한국어, 성별 = 중립)
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # 텍스트를 WAV 파일로 변환
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16  # WAV 포맷 사용
    )

    # 텍스트 음성 변환 수행
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # 파일 저장
    with open(output_file_name, "wb") as out:
        out.write(response.audio_content)
        print(f'실행 파일: "{output_file_name}"')

    # 파일 재생
    play_wav(output_file_name)

def play_wav(file_name):
    # .wav 파일을 열고 재생
    wf = wave.open(file_name, 'rb')

    # pyaudio 설정
    p = pyaudio.PyAudio()

    # 오디오 스트림 설정
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # 오디오 데이터를 읽어 스트리밍으로 재생
    chunk = 1024
    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    # 스트림 종료
    stream.stop_stream()
    stream.close()
    p.terminate()

# Example usage:
if __name__ == "__main__":
    start = time.time()
    TTS("복정역으로 안내할까요?", "asdeddwqer.wav")
    end = time.time()
    print(f"실행 시간: {end-start}초")
    pass
