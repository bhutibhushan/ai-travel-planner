import google.generativeai as genai
import os
from .fallback import fallback_itinerary

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_trip_itinerary(destination, days, budget, preferences):
    prompt = f"""
    You are a professional travel planner.

    Create a {days}-day travel itinerary for {destination}.
    Budget level: {budget}.
    Preferences: {", ".join(preferences)}.

    Respond ONLY in valid JSON with this structure:
    {{
      "overview": "string",
      "daily_plan": {{
        "day_1": ["activity", "activity"],
        "day_2": ["activity", "activity"]
      }},
      "estimated_budget": "string",
      "travel_tips": ["tip", "tip"]
    }}
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        return fallback_itinerary(
            destination,
            days,
            budget,
            preferences
        )