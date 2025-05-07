import sys
import os 

os.system("cls" if os.name == "nt" else "clear")
print(f"Número de caracteres: {len(' '.join(sys.argv[1:]))}")
input("Pressione Enter para fechar...")
sys.exit(0)