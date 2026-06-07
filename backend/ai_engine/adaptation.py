import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GENAI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def adapt_trip_itinerary(trip_data, current_day, situtation):
    prompt = f"""
    You are an expert travel planner.

    Original Trip:
    {trip_data}

    Current Day;
    {current_day}

    Situation:
    {situtation}

    Modify ONLY the affected day's plan.

    Return ONLY valid JSON in this format:
    {{
        "updated_day": "day_{current_day}",
        "activities": [
            "activity 1",
            "activity 2",
            "activity 3"
        ],
        "reason": "short explanation"
    }}
    """

    response = model.generate_content(prompt)
    return response.text