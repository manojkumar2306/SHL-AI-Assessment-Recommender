from app.chatbot.intent_detector import IntentDetector
from app.chatbot.clarification import clarification_question
from app.conversation.conversation_manager import ConversationManager
from app.recommender.recommender import Recommender
from app.llm.gemini_client import generate_response


class SHLChatbot:

    def __init__(self):
        self.intent = IntentDetector()
        self.manager = ConversationManager()
        self.recommender = Recommender()

    def chat(self, messages):

        intent = self.intent.detect(messages)

        # -------------------------
        # Out-of-scope detection
        # -------------------------

        last_message = messages[-1]["content"].lower()

        blocked_topics = [
            "weather",
            "movie",
            "football",
            "cricket",
            "bitcoin",
            "stock",
            "recipe",
            "hotel",
            "flight",
            "politics"
        ]

        if any(word in last_message for word in blocked_topics):
            return {
                "reply": "I can only help with SHL assessments and assessment recommendations.",
                "recommendations": [],
                "end_of_conversation": True
            }

        # -------------------------
        # Compare Intent
        # -------------------------

        if intent == "compare":

            prompt = f"""
Compare the SHL assessments mentioned by the user.

Conversation:

{messages}

Compare them based on:

- Purpose
- Skills measured
- Best use case
- Recommended candidates
"""

            answer = generate_response(prompt)

            return {
                "reply": answer,
                "recommendations": [],
                "end_of_conversation": True
            }

        # -------------------------
        # Recommendation Flow
        # -------------------------

        requirements = self.manager.extract_requirements(messages)

        missing = self.manager.missing_information(requirements)

        if missing:

            return {
                "reply": clarification_question(missing),
                "recommendations": [],
                "end_of_conversation": False
            }

        recommendations = self.recommender.recommend(requirements)

        if not recommendations:

            return {
                "reply": "I couldn't find suitable SHL assessments. Please provide more details.",
                "recommendations": [],
                "end_of_conversation": False
            }

        assessment_list = "\n".join([
            f"- {a['name']}"
            for a in recommendations
        ])

        prompt = f"""
You are an SHL Assessment Recommendation Assistant.

User Requirements:

{requirements}

Recommended SHL Assessments:

{assessment_list}

Explain briefly why each assessment fits.

Use bullet points.

Do NOT invent assessments.

Mention only the assessments provided.
"""

        explanation = generate_response(prompt)

        response = []

        for item in recommendations:

            response.append({
                "name": item["name"],
                "url": item["link"],
                "duration": item["duration"],
                "remote": item["remote"],
                "adaptive": item["adaptive"]
            })

        return {
            "reply": explanation,
            "recommendations": response,
            "end_of_conversation": True
        }