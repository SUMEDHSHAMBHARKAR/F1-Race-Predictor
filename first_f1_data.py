import fastf1

session = fastf1.get_session(2025, "Monaco" , "Q")

session.load()

# print(session)
# print(session.results.columns)
# print(session.laps.columns)
# print(session.weather_data.columns)

print(session.laps.pick_drivers("NOR"))