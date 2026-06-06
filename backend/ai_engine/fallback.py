def fallback_itinerary(destination,days,budget,prefrences):
    daily_plan={}

    for day in range (1,days+1):
        daily_plan[f"day_{day}"]=[
            f"Explore popular attractions in {destination}",
            "Try local cuisine at a recommended restaurant",
            "Evening walk and relaxation"
        ]
    return {
    "overview": f"A {days}-day trip to {destination} planned with a {budget} budget.",
    "daily_plan": daily_plan,
    "estimated_budget": "Estimated locally based on budget preference",
    "travel_tips": [
        "Book tickets in advance",
        "Wear comfortable shoes",
        "Stay hydrated"
    ]
}