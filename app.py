import fastf1

session = fastf1.get_session(2023, 'Australian Grand Prix', 'Q')
session.load(telemetry=False, laps=True, weather=True)

pia = session.get_driver('PIA') 
print(f"Pronto {pia['FirstName']}?")
