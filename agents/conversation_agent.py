
def maybe_log_conversation(intent_data, user_id, result):
    print(f"[Conversation Log] User: {user_id}, Intent: {intent_data.get('intent')}, Outcome: {result.get('status', result.get('error', 'unknown'))}")
