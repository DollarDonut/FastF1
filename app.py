import fastf1
import fastf1.plotting

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2025, 'Dutch Grand Prix', 'R')
session.load(telemetry=False, laps=True, weather=True)

pickDriver = session.get_driver('VER') 
print(f"Pronto {pickDriver['FirstName']}?")


for drv in session.drivers: 
    driver = session.get_driver(drv)
    print(drv, driver['FullName'])