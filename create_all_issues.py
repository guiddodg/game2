#!/usr/bin/env python3
import subprocess
import re

epics = {
    2: {
        "name": "NPCs",
        "features": ["Aldeano", "Aventurero", "Militar", "Mercader"]
    },
    3: {
        "name": "Enemigos",
        "features": [
            "Bioma 1 (Bosque) - Enemigos",
            "Bioma 1 (Bosque) - Boss (Lobo Ancestral)",
            "Bioma 2 (Montaña) - Enemigos",
            "Bioma 2 (Montaña) - Boss (Gólem)",
            "Bioma 3 (Pantano) - Enemigos",
            "Bioma 3 (Pantano) - Boss (Brujo)"
        ]
    },
    4: {
        "name": "Edificios",
        "features": ["Granja", "Taberna", "Herrería", "Tienda", "Casas NPCs", "Plaza"]
    },
    5: {
        "name": "Environment",
        "features": ["Árboles", "Vegetación", "Terreno", "Rocas y piedras", "Detalles"]
    },
    6: {
        "name": "Objetos",
        "features": ["Items", "Props", "Máquinas", "Interactuables"]
    },
    7: {
        "name": "Animaciones",
        "features": [
            "Movimiento", "Combate", "Interacciones Granja",
            "Interacciones Taberna", "Interacciones Herrería",
            "NPCs", "Enemigos"
        ]
    },
    8: {
        "name": "Animales",
        "features": ["Animales Granja", "Mascotas", "Comportamiento IA"]
    }
}

for epic_num, epic_data in epics.items():
    print(f"\n[Epic #{epic_num}] {epic_data['name']}")
    for feature in epic_data["features"]:
        cmd = [
            "gh", "issue", "create",
            "--title", f"Feature: {feature} ({epic_data['name']})",
            "--body", f"Epic parent: #{epic_num}\n\n## Subtasks\n- [ ] Modelado\n- [ ] Texturizado\n- [ ] Rigging\n- [ ] Setup"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, cwd="C:\\Users\\guido\\game2")
        match = re.search(r'issues/(\d+)', result.stdout)
        if match:
            issue_num = match.group(1)
            print(f"  ✓ Feature: {feature} (#{issue_num})")
        else:
            print(f"  ✗ Error: {feature}")
