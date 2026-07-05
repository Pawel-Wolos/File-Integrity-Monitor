# File Integrity Monitor (FIM) - Monitor Integralności Plików

Prosty program w języku Python służący do monitorowania integralności systemów i plików w czasie rzeczywistym. Narzędzie automatycznie wykrywa nieautoryzowane modyfikacje w wybranym pliku konfiguracyjnym lub systemowym, symulując działanie podstawowych systemów bezpieczeństwa (SIEM/FIM) wykorzystywanych w centrach operacji bezpieczeństwa (SOC).

## 🚀 Jak to działa?
1. **Inicjalizacja**: Program przy uruchomieniu wczytuje zawartość wskazanego pliku (`wazny_plik.txt`) i zapamiętuje ją jako zaufany stan bazowy (wzorzec).
2. **Monitorowanie w tle**: Działając w nieskończonej pętli, skrypt co 3 sekundy sprawdza aktualny stan pliku. Użycie funkcji optymalizacyjnej pozwala na zerowe obciążenie procesora.
3. **Detekcja i Alert**: W przypadku wykrycia jakiejkolwiek zmiany (dopisanie lub usunięcie znaków przez intruza), program natychmiast generuje alert bezpieczeństwa w konsoli i automatycznie aktualizuje zaufany wzorzec do nowego stanu.

## 🛠️ Funkcje projektu
* **Detekcja w czasie rzeczywistym**: Natychmiastowe wykrywanie modyfikacji plików.
* **Optymalizacja wydajności**: Zastosowanie kontrolowanych pauz chroni system przed przeciążeniem CPU.
* **Logika SOC**: Architektura programu odzwierciedla mechanizmy powiadomień stosowane w profesjonalnych systemach Cybersec.

## 💻 Wykorzystane technologie
* Python 3
* Biblioteka standardowa (`time`, `os`)
