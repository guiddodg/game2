---
tipo: epics
proyecto: Game2
status: planning
tags: [blender, epics, backlog]
updated: 2026-06-24
related: ["[[Backlog]]", "[[Arquitectura]]"]
---

# Epics Blender — Game2

Estructura de trabajo Blender: Epic → Feature → Subtask.

---

## PRIORIDAD ALTA (Semanas 1-4)

### 1. Epic: Personajes

Jugador + 6 clases.

**Features:**
- [ ] Base (rig genérico, estructura común)
- [ ] Skin Tanque
- [ ] Skin Support
- [ ] Skin Pícaro
- [ ] Skin Mago
- [ ] Skin Guerrero
- [ ] Skin Invocador

**Subtasks por Feature (Base):**
- Modelado mesh base
- Rigging (esqueleto, bones)
- Setup Blender (layers, naming)

---

### 2. Epic: NPCs

4 arquetipos, múltiples instancias por tipo.

**Features:**
- [ ] Aldeano (hombre + mujer)
- [ ] Aventurero (hombre + mujer)
- [ ] Militar (hombre + mujer)
- [ ] Mercader (hombre + mujer)

**Subtasks por Feature (Aldeano):**
- Modelado base
- Texturizado
- Rigging
- Setup nombres generados

---

### 3. Epic: Enemigos

3 biomas, enemigos progresivos + bosses.

**Features:**
- [ ] Bioma 1 (Bosque) - Enemigos
- [ ] Bioma 1 (Bosque) - Boss (Lobo Ancestral)
- [ ] Bioma 2 (Montaña) - Enemigos
- [ ] Bioma 2 (Montaña) - Boss (Gólem)
- [ ] Bioma 3 (Pantano) - Enemigos
- [ ] Bioma 3 (Pantano) - Boss (Brujo)

**Subtasks por Feature (Bioma 1 Enemigos):**
- Modelado (3-4 tipos)
- Texturizado
- Rigging
- Setup behavior básico

---

### 4. Epic: Edificios

Centro del pueblo + estructuras jugador.

**Features:**
- [ ] Granja (casa jugador + estructuras)
- [ ] Taberna
- [ ] Herrería
- [ ] Tienda
- [ ] Casas NPCs
- [ ] Plaza (pozo, tablón)

**Subtasks por Feature (Granja):**
- Modelado casa principal
- Modelado estructuras (gallinero, corral, almacén)
- Texturizado
- Props (puertas, ventanas, detalles)

---

### 5. Epic: Environment

Flora, terreno, decoración.

**Features:**
- [ ] Árboles (varios tipos)
- [ ] Vegetación (arbustos, plantas, flores)
- [ ] Terreno (caminos, prados, agua)
- [ ] Rocas y piedras
- [ ] Detalles (vallas, postes, decoración)

**Subtasks por Feature (Árboles):**
- Modelado (3-4 variantes)
- Texturizado
- LODs (simplificadas)
- Props accesorios

---

### 6. Epic: Objetos

Items, máquinas, props interactuables.

**Features:**
- [ ] Items (armas, armaduras, herramientas)
- [ ] Props (barriles, cajas, muebles)
- [ ] Máquinas (molino, quesería, forja, alambique)
- [ ] Interactuables (puertas, cofres, camas)

**Subtasks por Feature (Máquinas):**
- Modelado (molino, quesería, forja, alambique)
- Texturizado
- Detalles funcionales
- Piezas móviles (si aplica)

---

### 7. Epic: Animaciones

Movimiento, combate, interacciones, IA.

**Features:**
- [ ] Movimiento (idle, walk, run, jump)
- [ ] Combate (ataque básico, skills, muerte)
- [ ] Interacciones Granja (usar máquina, recoger, sembrar)
- [ ] Interacciones Taberna (comer, beber, servir)
- [ ] Interacciones Herrería (forjar, templar, vender)
- [ ] NPCs (hablar, esperar, reaccionar)
- [ ] Enemigos (patrulla, ataque, muerte)

**Subtasks por Feature (Movimiento):**
- Idle
- Walk
- Run
- Jump
- Landing

---

### 8. Epic: Animales

Granja + mascotas.

**Features:**
- [ ] Animales Granja (Gallina, Cerdo, Vaca, Caballo)
- [ ] Mascotas (tipos según taming)
- [ ] Comportamiento IA (movimiento, feeding, producción)

**Subtasks por Feature (Animales Granja):**
- Modelado (Gallina, Cerdo, Vaca, Caballo)
- Texturizado
- Rigging
- Animaciones básicas

---

## PRIORIDAD BAJA (Semanas 5-6)

### 9. Epic: Historia

Narrativa, cinemáticas, arcos NPCs.

**Features:**
- [ ] Acto 1 (Descubrimiento maldición)
- [ ] Acto 2 (Búsqueda mineral purificador)
- [ ] Acto 3 (Expansión/final)
- [ ] Cinemáticas (intro, transiciones)
- [ ] NPCs principales (arcos narrativos)

**Subtasks por Feature (Acto 1):**
- Guión/narrativa
- Personajes cinemática
- Escenas key
- Diálogos

---

### 10. Epic: Quests

Objetivos jugables, rewards, progresión.

**Features:**
- [ ] Quests Granja (siembra, cosecha, producción)
- [ ] Quests Taberna (recetas, clientes, limpieza)
- [ ] Quests Herrería (forja, upgrades, ventas)
- [ ] Quests Combate (biomas, bosses, oleadas)
- [ ] Quests Domesticación (taming, leveling)
- [ ] Quests Economía (ventas, reputación)

**Subtasks por Feature (Quests Granja):**
- Definir objetivos específicos
- Rewards (XP, dinero, items)
- Progresión/desbloques
- Aceptación/entrega mecánica

---

## 📊 Estado

- **Total Epics:** 10
- **Total Features:** 62
- **Priority Alta:** 8 Epics
- **Priority Baja:** 2 Epics

**Próximo:** Crear tareas en sistema tracking.
