
def handle_action(intent_data, user_id):
    intent = intent_data.get("intent")
    if intent == "book_service":
        return {
            "status": "success",
            "message": "Booking confirmed for " + str(intent_data.get("offering_name")),
            "intent": intent
        }
    elif intent == "search_service":
        return {
            "status": "success",
            "message": "Found services in " + str(intent_data.get("location")),
            "intent": intent
        }
    elif intent == "send_message":
        return {
            "status": "success",
            "message": "Message sent.",
            "intent": intent
        }
    else:
        return {
            "error": "Unknown or unsupported intent.",
            "intent": "unknown"
        }
