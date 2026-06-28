---
tipo: moc
proyecto: Game2
status: borrador
tags: [home, game-design]
updated: 2026-06-18
last_working_session: 2026-06-18
related: []
---

# 🎮 Game2 — Visión & Diseño

**Estado:** Fase de **design iterativo**. Todo es refinable antes de codear.

## 🏃 Última sesión (2026-06-20)

**ARQUITECTURA TÉCNICA 100% COMPLETA + SETUP KRITA MCP.**

**Gameplay Confirmado:**
- 3ª persona tipo Valheim (WASD + mouse)
- E proximidad para interacción + aim mouse para skills
- Skill tree: +1 punto/level, desbloquea abilities según progresión
- Respawn en Granja al morir, pierden items equipados

**Decisiones Arquitectónicas Clave:**
- **CharacterSystem:** Estado universal (player + enemigos) damage/heal/buffs
- **RewardManager:** Centralizado (drops + XP + dinero para enemies, quests, achievements)
- **Event-Driven:** GameEvent (formato + acción + datos) → desacoplado
- **SOLID:** Single Responsibility, Loose Coupling, bajo riesgo regresión
- **Managers nuevos:** InputManager, PlayerController, CameraManager, PlayerLevelingSystem, SkillTreeManager, InteractionSystem, RespawnSystem, AnimationManager, SceneTransitionManager, SoundManager

**Tech Stack + Tools:**
- Unity 2022 LTS (GameObjects, NO ECS)
- C# + SQLite + Newtonsoft.Json + DOTween + InputSystem
- Blender para modelado/rigging/animaciones
- **Krita + MCP Bridge** para UI 2D (configurado y listo)

**Próximo:** Setup Unity + Core systems (Week 1), luego Granja MVP (Week 2-3).

**GDD + Arquitectura + Tool Setup: 100% COMPLETO.** Listo para **prototipado.**

Granja + Taberna + Herrería defensora en un mundo donde la noche trae transformaciones monstruosas.

---

## 🎯 Secciones

### Diseño & Visión
- [[Visión]] — pitch, pilares, objetivos.
- [[Backlog]] — checklist de items completados.
- [[Historia]] — narrativa (Actos 1, 2, 3).
- [[Epics_Blender]] — 10 Epics, 62 Features, estructura Blender.

### Sistemas (Confirmados)
- [[Granja]] — cultivos, animales, pedidos, transporte.
- [[Taberna]] — comidas, clientes, limpieza, recetas.
- [[Herrería]] — forja, cadena suministro, vitrinas, I+D.
- [[Combate]] — 6 clases, oleadas, biomas, loot.
- [[Domesticación]] — mascotas, XP, usos.
- [[NPCs]] — 4 arquetipos, negociación, reputación.
- [[Economía]] — precios, dinero, transacciones.

### Técnica
- [[Arquitectura]] — Stack, Managers, persistencia, communication.

---

## 📌 Próximo Paso: PROTOTIPADO ITERATIVO

**GDD + Arquitectura Técnica: 100% DOCUMENTADO. Listo para codear.**

### Fase 1: Setup & Core (Semana 1)
1. Crear proyecto Unity 2022 LTS
2. Estructura de carpetas según arquitectura
3. Implementar Core systems (GameManager, TimeManager, DataManager)
4. Implementar EventSystem + GameEvent struct
5. Blender: setup para modelado + rigging

### Fase 2: Granja MVP (Semana 2-3)
1. FarmManager + CropController (cultivos con timers)
2. AnimalController (animales producción)
3. MachineController (máquinas procesamiento)
4. InventoryManager integración básica
5. Testing: economía (dinero/timers correctos)

### Fase 3: Combate Básico (Semana 4-5)
1. CharacterSystem (stats, damage, health)
2. CombatManager (orquestador)
3. RewardManager (drops, XP)
4. PlayerController (controles básicos)
5. EnemySpawner (una ola simple)

### Fase 4: Integración & Pulido (Semana 6)
1. Taberna integrada
2. Herrería integrada
3. NPCManager integrado
4. Balance económico general
5. EA Ready

### Filosofía de Desarrollo
- **Iterate, don't perfect** — MVP rápido, refine después
- **Test early** — RewardManager, CharacterSystem tests desde día 1
- **Data-driven** — cambios en JSON, no en código
- **Loose coupling** — si algo está acoplado, refactor inmediatamente

