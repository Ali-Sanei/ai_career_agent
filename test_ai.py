from app.ai.ai_service import AIService

ai = AIService()

answer = ai.chat(
    "You are a helpful assistant.",
    "Say only: AI Career Agent is ready."
)

print(answer)