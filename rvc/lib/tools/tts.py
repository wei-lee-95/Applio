import sys
import asyncio
import edge_tts
import os
# from google.cloud import texttospeech


async def main():
    # Parse command line arguments
    tts_file = str(sys.argv[1])
    text = str(sys.argv[2])
    voice = str(sys.argv[3])
    rate = int(sys.argv[4])
    output_file = str(sys.argv[5])

    rates = f"+{rate}%" if rate >= 0 else f"{rate}%"
    if tts_file and os.path.exists(tts_file):
        text = ""
        try:
            with open(tts_file, "r", encoding="utf-8") as file:
                text = file.read()
        except UnicodeDecodeError:
            with open(tts_file, "r") as file:
                text = file.read()
    await edge_tts.Communicate(text, voice, rate=rates, volume="+50%").save(output_file)
    #print(f"TTS with {voice} completed. Output TTS file: '{output_file}'")


    # """
    # 使用方式：
    # python google_tts.py "Hello, world!" "zh-TW" "Wavenet-A" 1.0 0.0 "output.mp3"
    # 參數分別為：
    # 1. 要轉語音的文字
    # 2. 語言代碼（例如 zh-TW、en-US）
    # 3. 聲音名稱（可在官方語音列表查詢）
    # 4. 語速（rate，0.25~4.0，1.0為正常速度）
    # 5. 音高（pitch，-20~20，0.0為原始音高）
    # 6. 輸出檔案名稱
    # """
# import os
# from google.cloud import texttospeech
# from google.oauth2 import service_account

# def synthesize_text(
#     tts_text: str,
#     tts_language_code: str = "cmn-TW",
#     tts_voice: str = "cmn-TW-Standard-B",
#     tts_rate: float = 1.0,
#     pitch: float = 0.0,
#     output_tts_path: str = "Outputs/Voice/tts_output.mp3",
#     credentials_path: str = "/Users/v/Desktop/my-ai-companion/TTS API Configuration.json"
# ):
#     """
#     將文字轉成語音並輸出檔案
#     """

#     # 讀取服務帳戶 JSON
#     credentials = service_account.Credentials.from_service_account_file(credentials_path)
#     client = texttospeech.TextToSpeechClient(credentials=credentials)

#     # 確保輸出資料夾存在
#     os.makedirs(os.path.dirname(output_tts_path), exist_ok=True)

#     # 設定文字、語音、音訊格式
#     synthesis_input = texttospeech.SynthesisInput(text=tts_text)
#     voice = texttospeech.VoiceSelectionParams(language_code=tts_language_code, name=tts_voice)
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3,  # MP3 或 LINEAR16 (wav)
#         speaking_rate=tts_rate,
#         pitch=pitch
#     )

#     # 產生語音
#     response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

#     # 寫入檔案
#     with open(output_tts_path, "wb") as out:
#         out.write(response.audio_content)

#     print(f"語音生成完成！檔案：{output_tts_path}")
#     return output_tts_path

# 測試用
if __name__ == "__main__":
    asyncio.run(main())
    #synthesize_text("這是測試語音。")


