import os
from botbuilder.core import TurnContext, ActivityHandler
from openai import AzureOpenAI

class MyBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_text = turn_context.activity.text or ""

        try:
            client = AzureOpenAI(
                api_key=os.environ["AZURE_OPENAI_API_KEY"],
                api_version=os.environ["AZURE_OPENAI_API_VERSION"],
                azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            )

            response = client.chat.completions.create(
                model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful Azure AI student project chatbot. Answer clearly and briefly."
                    },
                    {
                        "role": "user",
                        "content": user_text
                    }
                ],
                max_tokens=300,
                temperature=0.7,
            )

            reply = response.choices[0].message.content.strip()
            await turn_context.send_activity(reply)

        except Exception as e:
            await turn_context.send_activity(f"Sorry, I hit an error: {str(e)}")