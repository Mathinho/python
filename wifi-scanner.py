import subprocess, time, json

while True:
  f = open("wlan-namen.csv", "a")
  j = open("wlan-json.js", "a")
  results = subprocess.check_output(["netsh","wlan","show","network"])  #Abfrage WLAN-Netzwerke in Reichweite
  string_results = str(results)                             #Ergebnisse von Bytes in String umwandeln
  string_results = string_results.split(r"\r\n")            #Splitten nach \r\n
  string_results = string_results[4:]                       #SSIDs extrahieren
  ssids = []
  x = 0
  while x < len(string_results):
    if x % 5 == 0:
      ssids.append(string_results[x])
    x += 1
  ssids = str(ssids)

  f.write(ssids)                                            #SSIDs in Datei abspeichern
  f.close()
  json.dump(ssids, j)
  print(ssids)
  time.sleep(5)