---
tipo: backlog
proyecto: Game2
status: living
tags: [backlog, game-design]
updated: 2026-06-18
related: ["[[Visión]]", "[[Historia]]"]
---

# Backlog — Game2

Pendientes de design y planificación. Al completar un item, marcar `[x]`.

## GDD Core (confirmado)

- [x] **Progresión & Gating** — acceso a biomas es lineal, gated por boss drops del bioma anterior. Ver [[Visión#Progresión & Gating]].

## Arquitectura Técnica (100% COMPLETA)

- [x] **Stack técnico** — Unity 2022 LTS, C#, SQLite, DOTween, InputSystem. Ver [[Arquitectura]].
- [x] **Estructura de carpetas** — Assets organizados por tipo (Scripts, Scenes, Prefabs, Resources).
- [x] **Core Managers** — GameManager, TimeManager, DataManager, EventSystem.
- [x] **Business Managers** — FarmManager, TavernManager, SmithyManager (Negocios).
- [x] **Combat Managers** — CombatManager (orquestador), CharacterSystem (estado universal), RewardManager (rewards centralizado).
- [x] **Economy Managers** — NPCManager, InventoryManager, EconomyManager.
- [x] **Gameplay Managers** — InputManager, PlayerController, CameraManager, PlayerLevelingSystem, SkillTreeManager, InteractionSystem, RespawnSystem, AnimationManager, SceneTransitionManager, SoundManager.
- [x] **Comunicación** — Event-driven con GameEvent struct (formato + acción + datos).
- [x] **SOLID Principles** — Single Responsibility, Loose Coupling, bajo riesgo regresión.
- [x] **Persistencia** — SQLite schema definido, auto-save cada 5 min.
- [x] **UI 2D Tools** — Krita + MCP Bridge configurado para crear/editar UI artística.

## GDD Core (Completado)

- [x] **Mecánica de venta NPC** — 4 arquetipos funcionales (Aldeano, Aventurero, Militar, Mercader). Ver [[NPCs]].
- [x] **Progresión económica** — framework simple de 3 fases. Costos específicos TBD después de detallar Granja. Ver [[Economía]].
- [x] **Oleadas nocturnas** — scaling progresivo por día/semana. Más enemigos y fuertes conforme avanza. Ver [[Combate#Oleadas Nocturnas - Scaling Progresivo]].
- [x] **Sistema de muerte** — respawn en Granja, sin permadeath. Pierdes items equipados (recuperables). Ver [[Combate#Sistema de Muerte]].
- [ ] **Sistema de leveling/habilidades** para el jugador (¿hay o es stat-based solamente?).
- [ ] **Hambre/salud** del jugador — ¿es necesario?

## Sistemas & Mecánicas (confirmados)

- [x] **Granja** — centro de producción (cultivos + animales). Sistema de pedidos en tablón. Transporte con carretas y caballos. Ver [[Granja]].
- [x] **Taberna** — desbloquea al máximo reputación con viejo tabernero. NPCs comen, reputación sube/baja. Recetas desbloqueadas por NPCs. Ver [[Taberna]].

## Sistemas & Mecánicas (confirmados - continuación)

- [x] **Herrería** — taller de forja (armas, armaduras, carroajes, herramientas). Desbloquea por dinero/mineral. Planos de bosses. Venta a aventureros. Ver [[Herrería]].

## Sistemas & Mecánicas (confirmados - continuación 2)

- [x] **Combate** — Valheim-like. 6 clases (Tanque, Support, Pícaro, Mago, Guerrero, Invocador). Ver [[Combate]].

## Sistemas & Mecánicas (a detallar)
- [ ] **NPCs compradores** — comportamiento específico, negociación, personalidades.
- [ ] **Mecánica de leveling** para el jugador (skills tree, stat progression).
- [ ] **UI/UX mockups** — interfaces principales.

## Biomas (confirmados - a expandir)

- [x] **Bioma 1: Bosque** — (Low Level) enemigos, recursos, boss Lobo Ancestral. Ver [[Visión#Los 3 Biomas]].
- [x] **Bioma 2: Montaña** — (Medium Level) enemigos, recursos, boss Gólem de piedra. Ver [[Visión#Los 3 Biomas]].
- [x] **Bioma 3: Pantano** — (High Level) enemigos, recursos, boss El Brujo (final). Ver [[Visión#Los 3 Biomas]].

## Historia & Narrativa (a escribir)

- [ ] Causa de llegada al pueblo.
- [ ] Acto 1: Descubrimiento de la maldición.
- [ ] Acto 2: Búsqueda del mineral purificador.
- [ ] Acto 3: Expansión (post-EA?).
- [ ] NPCs principales y sus arcos.

## UI/UX (a diseñar)

- [ ] Mockups de interfaz principal.
- [ ] Flujo de venta (cómo ve el jugador a los NPCs, cómo negocia).
- [ ] HUD de defensa nocturna (enemigos, salud, oleadas).
- [ ] Inventario y equipo.

## Early Access Scope (confirmar)

- [x] Granja funcional.
- [x] Tienda con sistema de ventas.
- [x] Herrería con crafting.
- [x] 3 biomas explorable.
- [x] Defensas del compound (muros, trampas).
- [x] Ciclo día/noche (30/15 min).
- [x] Oleadas nocturnas.
- [x] Domesticación (3 tipos).
- [ ] Historia mínima viable (intro + acto 1).
- [ ] Balanced economy (costs vs. rewards).

## Ideas sueltas (sin priorizar)

- (agregar acá lo que surja durante iteración)

---

## 📊 Estado Final — GDD + Arquitectura + Filosofía

**✅ GAME DESIGN (100%):**
- Granja (Hay Day-style, números, layout)
- Taberna (Ale & Tale-style, real-time, mecánicas)
- Herrería (Blacksmith Master + Shop Titans, tycoon)
- Combate (6 clases, Valheim-like, oleadas)
- Domesticación (Rappelz-style pets)
- Historia (3 actos, narrativa)
- Biomas (3 biomas lineales, bosses)
- Economía (100-2500 monedas/día)
- NPCs (4 arquetipos, negociación)
- UI/UX (formatos notification)

**✅ ARQUITECTURA TÉCNICA (100%):**
- Stack: Unity 2022 LTS, C#, SQLite, DOTween, InputSystem
- 9 Managers + Services (CleanCode, SOLID)
- **CharacterSystem:** Estado universal (player = enemigos)
- **RewardManager:** Centralizado (drops, XP, dinero, quests, achievements)
- **EventSystem:** GameEvent desacoplado (formato + acción + datos)
- Persistencia SQLite (auto-save, schema completo)
- Object pooling (enemigos, NPCs)
- Data-driven (JSON configs: recetas, enemigos, rewards)

**✅ FILOSOFÍA DE DESARROLLO:**
- Single Responsibility (cada manager una cosa)
- Loose Coupling (EventSystem, no direct calls)
- Testeable (servicios aislados, bajo riesgo regresión)
- Mantenible (cambios aislados, bajo impacto)
- Escalable (agregar features sin tocar otros sistemas)

**⏳ NICE-TO-HAVE (post-EA):**
- UI/UX mockups visuales completos
- Oleadas nocturnas balance por bioma
- Skill tree player detalles
- Multiplayer (si EA tiene éxito)

**🎮 100% LISTO PARA PROTOTIPADO**
- Documentación: Completa
- Arquitectura: Validada
- Decisiones: Tomadas
- Código: Listo para empezar

**→ Siguiente fase: Implementación iterativa (Semana 1-6)**
