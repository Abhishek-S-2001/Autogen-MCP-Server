
def format_response(data):
    if "error" in data:
        return f"❌ Error: {data['error']}"
    if data["intent"] == "book_service":
        return f"✅ {data['message']}"
    if data["intent"] == "search_service":
        return f"🔍 {data['message']}"
    if data["intent"] == "send_message":
        return f"📩 {data['message']}"
    return "⚠️ Unhandled intent."
