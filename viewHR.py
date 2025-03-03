import pandas as pd
import matplotlib.pyplot as plt

# Načtení dat ze souboru CSV
data = pd.read_csv("hr2.csv", parse_dates=["date"])

# Výběr dat pro určité časové rozpětí
start_date = "2025-01-01 00:00:00"
end_date = "2025-01-01 12:00:00"
data_filtered = data[(data["date"] >= start_date) & (data["date"] <= end_date)]

# Vykreslení grafu
plt.figure(figsize=(10, 5))
plt.plot(data_filtered["date"], data_filtered["heartrate"], marker="o", linestyle="-", color="b", label="Tepová frekvence")
plt.xlabel("Čas")
plt.ylabel("Tepová frekvence (BPM)")
plt.title(f"Vývoj tepové frekvence v čase ({start_date} - {end_date})")
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m %H:%M'))
plt.legend()
plt.grid()
plt.show()
