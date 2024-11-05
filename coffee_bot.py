from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os

# Initialize your Slack app
app = App(token="xoxb-your-bot-token")

# Create a simple button
@app.event("app_mention")
def show_coffee_button(event, say):
    # Show button when the bot is mentioned
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "Who wants coffee? :coffee:"}
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Coffee!"},
                        "action_id": "coffee_button_click"
                    }
                ]
            }
        ],
        text="Coffee anyone? :coffee:"
    )

# Handle button click
@app.action("coffee_button_click")
def handle_button_click(ack, body, client):
    ack()  # Acknowledge the button click
    # Send alert to a specific channel
    channel_id = "#coffee"  # Replace with your channel ID or name
    user = body["user"]["name"]
    client.chat_postMessage(channel=channel_id, text=f"☕ {user} wants coffee!")

if __name__ == "__main__":
    handler = SocketModeHandler(app, "xapp-your-socket-mode-token")
    handler.start()
