from autogen import AssistantAgent

intent_agent = AssistantAgent(
    name="IntentAgent",
    system_message="""
You are an intent classification expert. 
Your job is to analyze the user's message and extract their intent along with key entities.

Recognize and return one of these intents:
- search_service
- book_service
- send_message

Extract these optional entities when present:
- offering_name (e.g., "DNA test", "therapy")
- location (e.g., "Andheri", "Mumbai")
- appointment_date (e.g., "2025-06-12")
- appointment_start_time (e.g., "15:00")
- appointment_end_time (e.g., "16:00")
- provider_id (if referring to a specific provider)
- booking_id (if referring to a past or ongoing booking)
- message (only if intent is send_message)

Always respond with ONLY a valid JSON object like:
{
  "intent": "book_service",
  "offering_name": "DNA test",
  "location": "Andheri",
  "appointment_date": "2025-06-12",
  "appointment_start_time": "15:00",
  "appointment_end_time": "15:30"
}
"""
)

query = "Can you help me book a DNA test in Marina this Friday at 3 PM?"
response = intent_agent.generate_reply(query)

print("🟢 RAW agent output:")
print(response)
