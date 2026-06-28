#!/bin/bash
epics=(
  "NPCs|4 arquetipos (Aldeano, Aventurero, Militar, Mercader)|Alta"
  "Enemigos|3 biomas + bosses|Alta"
  "Edificios|Granja, Taberna, Herrería, Tienda, Casas NPCs, Plaza|Alta"
  "Environment|Árboles, vegetación, terreno, rocas, detalles|Alta"
  "Objetos|Items, props, máquinas, interactuables|Alta"
  "Animaciones|Movimiento, combate, interacciones, IA|Alta"
  "Animales|Granja + mascotas|Alta"
)

for epic in "${epics[@]}"; do
  IFS='|' read -r name desc prio <<< "$epic"
  gh issue create --title "Epic: $name" --body "$desc

Prioridad: $prio (Semana 1-4)" 2>&1 | grep -o "issues/[0-9]*"
done
