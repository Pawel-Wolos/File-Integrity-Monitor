import time 

target_file = "wazny_plik.txt"

print("=== ID: FILE INTEGRITY MONITOR (FIM) ===")
print(f"[*] Inicjalizacja ochrony... Monitorowany plik: {target_file}")

with open(target_file, "r", encoding="UTF-8") as file:
     trusted_content = file.read()

print("[+] Baza zaufana utworzona pomyślnie. Status: BEZPIECZNY.\n")

while True:
     
     time.sleep(3)
     with open(target_file, "r", encoding = "UTF-8") as file:
          current_content = file.read()
     
     if current_content != trusted_content:
        print("[🚨] ALERT: SYSTEM INTEGRITY VIOLATION DETECTED!")
        
        print(f"[-] Oczekiwano: {trusted_content.strip()}")
        print(f"[+] Wykryto:    {current_content.strip()}")

        print("[!] Rekomendacja SOC: Zweryfikuj uprawnienia i zablokuj konto użytkownika.")
        print("-" * 50)

        trusted_content = current_content