from pathlib import Path
import subprocess, sys
BASE=Path(__file__).resolve().parent
files=["01_syed_offers_goals.py","02_jordan_clean_sheets.py","03_ujjwol_speed_goals.py","04_saugat_own_goals.py"]
for f in files:
    print("\n"+"="*70)
    subprocess.run([sys.executable,str(BASE/f)],check=True)
