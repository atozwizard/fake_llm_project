from agent import LlmAgent

print("메인에서 수정한 완전 다른 내용")
if __name__ == "__main__":
  agent = LlmAgent()
  reply = agent.handle("사용자", "안녕")
  print("응답:", reply)