import time
import winsound
import keyboard
import pyautogui
import pyperclip

pyautogui.FAILSAFE = True

print("=" * 60)
print("  AUTO-TYPER SAE (CON CUENTA REGRESIVA Y PITIDOS)")
print("=" * 60)
print("Instrucciones de uso:")
print("1. En Sheets: seleccioná las celdas y copiá (Ctrl + C).")
print("2. Presioná F9 (estando en Sheets o en tu compu local).")
print("3. Tenés 4 segundos para pasar al SAE remoto y hacer clic en Cantidad.")
print("4. Asegurate de tener Bloq Mayús ENCENDIDO.")
print("=" * 60)
print("Listo y esperando F9...\n")


def disparar():
  contenido = pyperclip.paste().strip()
  if not contenido:
    print("[AVISO] El portapapeles está vacío. Copiá primero en Sheets.")
    winsound.Beep(500, 300)
    return

  lineas = contenido.splitlines()
  total = len([l for l in lineas if l.strip()])

  print(">> F9 detectado. Pasate a SAE y hacé clic en 'Cantidad'...")

  # Cuenta regresiva de 3 segundos con pitidos de aviso
  for i in range(3, 0, -1):
    winsound.Beep(1000, 150)  # Pitido corto de alerta
    print(f"Comenzando en {i}...")
    time.sleep(1)

  winsound.Beep(1800, 350)  # Pitido agudo de arranque
  print(f">> Escribiendo {total} partidas en SAE...")

  for i, linea in enumerate(lineas, start=1):
    if not linea.strip():
      continue

    columnas = linea.split("\t") if "\t" in linea else linea.split(",")

    if len(columnas) >= 2:
      cantidad = columnas[0].strip()
      clave = columnas[1].strip().lower()

      # 1. Escribir cantidad
      pyautogui.write(cantidad, interval=0.02)
      time.sleep(0.08)
      pyautogui.press("tab")
      time.sleep(0.12)

      # 2. Escribir clave
      pyautogui.write(clave, interval=0.03)
      time.sleep(0.1)

      # 3. Enter para saltar a la siguiente fila
      pyautogui.press("enter")
      time.sleep(0.35)

      print(f"[{i}/{total}] {cantidad} -> {clave.upper()}")

  print("\n¡Listo! Partidas ingresadas al 100%. Esperando siguiente F9...\n")


keyboard.add_hotkey("f9", disparar)
keyboard.wait()