import os
from google.cloud import texttospeech
from google.oauth2 import service_account

def synthesize_text(
    tts_text: str,
    tts_language_code: str = "cmn-TW",
    tts_voice: str = "cmn-TW-Standard-B",
    tts_rate: float = 1.0,
    pitch: float = 0.0,
    output_tts_path: str = "/content/tts_output.mp3",
    credentials_path: str = None
):
    """
    將文字轉成語音並輸出檔案
    """
    if credentials_path is None:
        raise ValueError("請提供 Google TTS JSON 憑證路徑")

    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    # 確保輸出資料夾存在
    os.makedirs(os.path.dirname(output_tts_path), exist_ok=True)

    # 設定文字、語音、音訊格式
    synthesis_input = texttospeech.SynthesisInput(text=tts_text)
    voice = texttospeech.VoiceSelectionParams(language_code=tts_language_code, name=tts_voice)
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=tts_rate,
        pitch=pitch
    )

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_tts_path, "wb") as out:
        out.write(response.audio_content)

    print(f"語音生成完成！檔案：{output_tts_path}")
    return output_tts_path

if __name__ == "__main__":
    synthesize_text("這是測試語音。")
