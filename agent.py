from tools import get_weather


class LlmAgent:
  def handle(self, user, message):
    print(f"디버깅 중...{user}  {message}")
    if "날씨" in message:
      weather = get_weather("서울")
      return f"[LLM]{user}님, 서울의 날씨는 '{weather}' 입니다."

    # 아주 단순한 LLM 흉내
    return f"[LLM]{user}님, '{message}' 잘 받았습니다."
