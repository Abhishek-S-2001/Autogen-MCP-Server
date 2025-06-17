
from flask import Flask, request, jsonify
from agents.intent_agent import detect_intent
from agents.action_agent import handle_action
from agents.response_agent import format_response
from agents.conversation_agent import maybe_log_conversation
import sys
import datetime
import json

app = Flask(__name__)

def log_conversation_step(title, data):
    print(f"\n🟢 [{datetime.datetime.now()}] {title}", file=sys.stderr)
    print(json.dumps(data, indent=2, ensure_ascii=False), file=sys.stderr)

@app.route("/ask-agent", methods=["POST"])
def ask_agent():
    try:
        data = request.get_json()
        user_query = data.get("query")
        user_id = data.get("user_id")

        log_conversation_step("User Message", {
            "user_id": user_id,
            "query": user_query
        })

        intent_data = detect_intent(user_query)
        log_conversation_step("Intent Detected", intent_data)

        try:
            action_result = handle_action(intent_data, user_id)
        except Exception as e:
            action_result = {"error": str(e), "intent": intent_data.get("intent", "unknown")}
        log_conversation_step("Action Agent Response", action_result)

        try:
            response_text = format_response({
                **action_result,
                "intent": intent_data.get("intent", "unknown")
            })
        except Exception as e:
            response_text = f"❌ Response Error: {str(e)}"
        log_conversation_step("Final Agent Reply", {
            "response": response_text
        })

        try:
            maybe_log_conversation(intent_data, user_id, action_result)
        except Exception as e:
            print("⚠️ Conversation Log Error:", str(e), file=sys.stderr)

        return jsonify({
            "response": response_text,
            "intent": intent_data.get("intent"),
            "raw_data": action_result
        })

    except Exception as ex:
        print("🟥 Endpoint Error:", str(ex), file=sys.stderr)
        return jsonify({
            "error": str(ex),
            "hint": "Check terminal logs for full trace."
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
