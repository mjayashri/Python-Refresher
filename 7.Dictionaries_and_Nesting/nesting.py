capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

cities_visited = [
    {
        "Country": "France",
        "cities_visited": ["Paris",
                           "Lillie",
                           "Dijon"
                           ],
        "total_visits":14
    }
]

print(cities_visited)
# Nesting Dictionaries
travel_log = {
    "France": {"cities_visited": [
        "Paris",
        "Lillie",
        "Dijon"
    ], "total_visits": 20}
}

print(travel_log["France"]["cities_visited"])
