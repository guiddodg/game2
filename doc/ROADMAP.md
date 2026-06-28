# 🗺️ ROADMAP — Game2

Tracking vivo de tareas por semana. Actualizar cuando tomes/completes una tarea.

**Formato:**
```
- [ ] Tarea específica
  - Status: Not started | In progress | Blocked | Review | Done
  - Assignee: @user o -
  - PR: #PR_NUMBER o -
  - Notes: detalles relevantes
```

---

## 📅 SEMANA 1: Setup Unity + Core Systems

**Target:** GameManager, TimeManager, DataManager, EventSystem, folder structure.

### Tareas

- [ ] Crear proyecto Unity 2022 LTS
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Folder structure según Arquitectura.md

- [ ] Estructura de carpetas Assets/
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Scripts, Scenes, Prefabs, Resources, Models, Audio

- [ ] GameManager (Singleton)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Gestor central, no destruye entre escenas

- [ ] TimeManager (Day/Night cycle)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: 30min día, 15min noche, callback a listeners

- [ ] DataManager (SQLite)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Persistencia, auto-save cada 5min

- [ ] EventSystem + GameEvent struct
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Formato: Success/Fail/Error/Question + action + data

- [ ] InputManager (WASD + Mouse)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: InputSystem, devuelve dirección normalizada

- [ ] PlayerController (placeholder)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Mueve personaje, usa InputManager, espera animaciones

- [ ] CameraManager (3ª persona)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Sigue al personaje, collision con ambiente

- [ ] Importar Personaje Base (Blender)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: BLOCKER: Requiere rig humanoid + idle/walk/run/jump

---

## 📅 SEMANA 2-3: Granja MVP

**Target:** FarmManager, cultivos con timers, animales, máquinas, básicos.

### Tareas

- [ ] FarmManager (orquestador)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Gestiona cultivos, animales, máquinas

- [ ] CropController (timers)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Crecimiento basado en TimeManager, harvesteable

- [ ] AnimalController (producción)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Produce recursos, necesita alimentación

- [ ] MachineController (procesamiento)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Molino, Quesería, etc. Transforma items

- [ ] InventoryManager (integración)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Básico, almacena items, vinculado a UI

- [ ] UI Granja (placeholder)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Mostrar cultivos, animales, máquinas, inventory

- [ ] Testing economía
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Verificar progresión dinero (100-200 día 1 → 300-500 día 10)

---

## 📅 SEMANA 4-5: Combate Básico

**Target:** CharacterSystem, CombatManager, RewardManager, enemigos básicos, oleadas.

### Tareas

- [ ] CharacterSystem (estado universal)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Health, mana, stamina, buffs, debuffs. Usado por player + enemies

- [ ] CombatManager (orquestador)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Ejecuta acciones, aplica damage, chequea muerte

- [ ] RewardManager (drops + XP)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Centralizado: drops, XP, dinero, quests, achievements

- [ ] PlayerController (combate)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Recibe input → ejecuta skill/ataque via CombatManager

- [ ] SkillTreeManager (abilities)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: +1 punto por level, desbloquea skills según progresión

- [ ] EnemySpawner (básico)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Una ola simple, sin oleadas complejas aún

- [ ] Enemigos Bioma 1 (modelo + IA)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Requiere modelos Blender + animaciones

- [ ] Testing combate loop
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Atacar → recibir damage → muerte → respawn

---

## 📅 SEMANA 6: Integración & Pulido

**Target:** Todos los sistemas integrados, balance, EA ready.

### Tareas

- [ ] TavernManager integración
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Clientes, recetas, paga al jugador

- [ ] SmithyManager integración
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Forja, cadena suministro, venta de equipamiento

- [ ] NPCManager (arquetipos + negociación)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: 4 tipos, precios dinámicos, reputación

- [ ] Balance económico general
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Verificar que 100-2500 monedas/día sea viable

- [ ] UI Final (parchment medieval pixel art)
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Reemplazar placeholders con assets finales

- [ ] Testing End-to-End
  - Status: Not started
  - Assignee: -
  - PR: -
  - Notes: Semana completa: granja → combate → recompensas → progresión

---

## 📅 POST-EA: Historia + Quests (Semana 7+)

**Target:** Narrativa, cinemáticas, quests complejas.

*(Estos quedan para después del MVP, no son críticos para EA inicial)*

---

## 🎯 Estado Global

**Completado:** 0/63 features
**En Progreso:** 0/63 features
**Bloqueado:** 10 (requieren Personaje Base Blender)
**Not Started:** 53/63 features

**Blocker Crítico:**
- ⏳ Personaje Base (Blender): rig humanoid + idle/walk/run/jump

---

## 📝 Cómo Actualizar

1. **Cuando tomes una tarea:**
   ```
   - [ ] Tarea X
     - Status: In progress
     - Assignee: @tuNombre
     - PR: -
   ```

2. **Cuando crees un PR:**
   ```
   - [ ] Tarea X
     - Status: Review
     - Assignee: @tuNombre
     - PR: #123
   ```

3. **Cuando se mergea:**
   ```
   - [x] Tarea X
     - Status: Done
     - Assignee: @tuNombre
     - PR: #123
   ```

---

## 🔗 Referencias

- GDD: [[Visión]], [[Granja]], [[Taberna]], [[Herrería]], [[Combate]]
- Arquitectura: [[Arquitectura]]
- Backlog: [[Epics_Blender]]
- Repo: https://github.com/guiddodg/game2
