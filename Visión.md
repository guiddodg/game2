---
tipo: vision
proyecto: Game2
status: borrador
tags: [vision, game-design]
updated: 2026-06-16
related: ["[[Backlog]]", "[[Historia]]"]
---

# Visión — Game2

> 🎮 Diseño inicial. Refinar iterativamente con el usuario antes de codear.

## Pitch

**Granja + Tienda + Herrería defensora en un mundo donde la noche trae transformaciones monstruosas.**

Un simulador de negocios tipo Valheim donde construyes un pequeño imperio económico: comienza con una granja, expandes a una tienda, luego una armería. De día, NPCs compran tus productos. De noche, los habitantes del pueblo se transforman en bestias hostiles y atacan tu compound. Defiéndete, explora biomas para conseguir minerales y planos, domestica animales, y eventualmente descubre la maldición que causa todo.

**Inspiraciones:** Valheim (exploración, construcción, defensa) + Shop Titans (sistema de ventas) + Stardew Valley (progresión de negocios).

## Pilares

1. **Economía orgánica** — los productos fluyen naturalmente: Granja → Tienda/Herrería → Ventas a NPCs. El jugador decide qué vender.
2. **Defensa nocturna** — ciclo día/noche (30 min día, 15 min noche). Oleadas de enemigos atacan. El jugador es libre pero hay consecuencias.
3. **Exploración rewarding** — tres biomas con enemigos únicos, minerales, planos de crafting, animales domesticables.
4. **Combate acción directa** — similar a Valheim. Muros, trampas, animales aliados, armas/armadura.
5. **Progresión natural** — Granja → Tienda → Herrería. Cada edificio desbloquea nuevas ventas/recetas.

## Progresión & Gating

**Acceso a biomas:** Lineal, sin posibilidad de saltear etapas.

- **Cada bioma requiere:** Derrotar el boss del bioma anterior.
- **Boss dropea:** Item/fragmento especial que desbloquea acceso al siguiente bioma (llave, mineral purificador, etc.) o fragmentos para craftear herramienta de acceso en la armería.
- **No se puede saltear:** No hay alternate route. Boss 1 → Bioma 2. Boss 2 → Bioma 3.
- **Efecto:** Progresión clara y obligatoria. El jugador siempre sabe qué hacer (derrotar boss actual para avanzar).

## Los 3 Biomas (Early Access)

### 1. Bosque (Época Primaria)
- **Dificultad:** Low Level
- **Estética:** Natural, bosque denso
- **Enemigos:** Lobos, esqueletos menores, espíritus débiles
- **Recursos:** Madera, cuero, huesos básicos
- **Boss:** Lobo Ancestral
- **Drop:** Abre acceso a Montaña
- **Animales domesticables:** Lobos, venados

### 2. Montaña (Época de Construcción/Minería)
- **Dificultad:** Medium Level
- **Estética:** Rocosa, minerales, ruinas de construcción antigua
- **Enemigos:** Trasgos, espíritus de piedra, enanos corrompidos
- **Recursos:** Minerales (hierro, cobre), cristales
- **Boss:** Gólem de piedra
- **Drop:** Abre acceso a Pantano
- **Animales domesticables:** Cabras, aves grandes

### 3. Pantano (Época de Corrupción)
- **Dificultad:** High Level
- **Estética:** Oscuro, corrupto, agua estancada
- **Enemigos:** Muertos vivientes, criaturas acuáticas, chamanes oscuros
- **Recursos:** Hierbas raras, cristales oscuros, veneno
- **Boss Final:** El Brujo (antagonista principal)
- **Animales domesticables:** Cocodrilos (combate), anfibios (viaje acuático)

## A confirmar / refinar

- ¿Permadeath o respawns ilimitados?
- ¿Sistema de hambre/salud para el jugador o simplemente HP?
- ¿NPCs tienen nombres/personalidades individuales?
- ¿Qué causa que el jugador caiga al pueblo? (narrativa de intro)
- Detalles de **progresión de dificultad** (oleadas nocturnas aumentan con el tiempo)
- Detalles de **economía** (cómo defines precios, negociación con NPCs)
