---
tipo: arquitectura
proyecto: Game2
status: borrador
tags: [unity, arquitectura, tech-stack]
updated: 2026-06-20
related: ["[[Granja]]", "[[Taberna]]", "[[Herrería]]", "[[Combate]]"]
---

# Arquitectura Técnica — Game2 (Unity)

**Estructura de código, sistemas, persistencia y comunicación para Early Access.**

---

## 1. Stack Técnico

### Motor & Plataforma
- **Unity 2022 LTS** (o 6.0 si disponible)
- **C#** (GameObjects tradicionales, NO ECS)
- **Blender** — modelado 3D + animaciones/rigging

### Librerías Core
- **Newtonsoft.Json** — serialización (SQLite)
- **DOTween** — animaciones UI
- **InputSystem** — controles (recomendado)

### Persistencia
- **SQLite** — guardar economía, reputación, inventario, progreso
- **JSON** — config, datos estáticos (recetas, enemigos)

### UI
- **uGUI** (built-in) — interfaces principales
- **TextMesh Pro** — textos

---

## 2. Estructura de Carpetas

```
Assets/
├── Scenes/
│   ├── MainMenu.unity
│   ├── Farm.unity
│   ├── Tavern.unity
│   ├── Smithy.unity
│   └── Combat.unity
│
├── Scripts/
│   ├── Core/
│   │   ├── GameManager.cs (orquestador global)
│   │   ├── EventSystem.cs (comunicación)
│   │   ├── DataManager.cs (SQLite, guardar/cargar)
│   │   └── TimeManager.cs (día/noche, timers globales)
│   │
│   ├── Managers/
│   │   ├── FarmManager.cs (cultivos, animales, máquinas)
│   │   ├── TavernManager.cs (cocina, clientes, limpieza)
│   │   ├── SmithyManager.cs (forja, cadena suministro, vitrinas)
│   │   ├── CombatManager.cs (orquestador: decisiones combate)
│   │   ├── CharacterSystem.cs (estado universal: damage, heal, buffs, status)
│   │   ├── RewardManager.cs (drops, XP, dinero: quests, achievements, enemies)
│   │   ├── NPCManager.cs (comportamiento, negociación)
│   │   ├── InventoryManager.cs (almacén, carreta, jugador)
│   │   ├── EconomyManager.cs (dinero, precios dinámicos, reputación)
│   │   ├── InputManager.cs (mapea WASD + mouse + E proximidad)
│   │   ├── PlayerController.cs (movimiento 3ª persona, interacción)
│   │   ├── CameraManager.cs (cámara tipo Valheim, sigue player)
│   │   ├── PlayerLevelingSystem.cs (+1 punto/level, progresión)
│   │   ├── SkillTreeManager.cs (desbloquea skills por nivel)
│   │   ├── InteractionSystem.cs (E proximidad, lógica general)
│   │   ├── RespawnSystem.cs (respawn Granja, perder items)
│   │   ├── AnimationManager.cs (sincroniza anims con daño/skills)
│   │   ├── SceneTransitionManager.cs (cambio escenas: Granja, Taberna, etc)
│   │   └── SoundManager.cs (música, SFX, audio combate)
│   │
│   ├── Systems/
│   │   ├── Farm/
│   │   │   ├── CropController.cs
│   │   │   ├── AnimalController.cs
│   │   │   ├── MachineController.cs
│   │   │   └── OrderBoard.cs
│   │   │
│   │   ├── Tavern/
│   │   │   ├── KitchenController.cs
│   │   │   ├── CustomerController.cs
│   │   │   ├── RecipeSystem.cs
│   │   │   └── CleaningSystem.cs
│   │   │
│   │   ├── Smithy/
│   │   │   ├── MiningController.cs
│   │   │   ├── SmeltingController.cs
│   │   │   ├── ForgingController.cs
│   │   │   ├── DisplayCaseController.cs
│   │   │   └── ResearchTree.cs
│   │   │
│   │   ├── Combat/
│   │   │   ├── PlayerController.cs
│   │   │   ├── EnemySpawner.cs
│   │   │   ├── WaveManager.cs
│   │   │   ├── ClassSkillSystem.cs
│   │   │   └── LootDropSystem.cs
│   │   │
│   │   └── NPCs/
│   │       ├── NPCController.cs (base)
│   │       ├── NPCBehavior.cs (IA simple)
│   │       ├── NPCNegotiation.cs (diálogos venta)
│   │       └── ReputationSystem.cs
│   │
│   ├── UI/
│   │   ├── UIManager.cs (orquestador)
│   │   ├── HUD.cs (barras, dinero, día/noche)
│   │   ├── InventoryUI.cs
│   │   ├── MenuUI.cs
│   │   ├── CombatHUD.cs
│   │   └── DialogueUI.cs (negociación NPC)
│   │
│   ├── Entities/
│   │   ├── Item.cs (estructura base)
│   │   ├── Recipe.cs (recetas)
│   │   ├── NPC.cs (datos NPC)
│   │   └── Enemy.cs (datos enemigo)
│   │
│   └── Utilities/
│       ├── TimerPool.cs (pool de timers)
│       ├── ObjectPool.cs (enemigos, NPCs)
│       ├── SaveData.cs (modelo SQLite)
│       └── Constants.cs (valores globales)
│
├── Prefabs/
│   ├── Enemies/
│   ├── NPCs/
│   ├── Items/
│   └── UI/
│
├── Resources/
│   ├── Data/
│   │   ├── Crops.json
│   │   ├── Animals.json
│   │   ├── Recipes.json
│   │   ├── Enemies.json
│   │   └── NPCTypes.json
│   │
│   └── Localization/
│       └── ES.json
│
├── Models/ (Blender exports)
│   ├── Characters/
│   ├── Buildings/
│   ├── Items/
│   └── Enemies/
│
└── Audio/
    ├── SFX/
    └── Music/
```

---

## 3. Sistemas Principales & Responsabilidades

### 3.1 GameManager (Orquestador Global)

```
GameManager
├── Inicializa todos los managers
├── Maneja transiciones de escena
├── Coordina saves/loads
└── Controla día/noche (30 min día, 15 min noche)
```

**Responsabilidades:**
- Startup del juego
- Control de tiempo global
- Persistencia (GameData)
- Cambio de escenas

---

### 3.2 TimeManager (Simulación de Tiempo)

```
TimeManager (Singleton)
├── timeScale = 1.0 (configurable)
├── currentHour (0-24)
├── currentDay
├── eventDayChanged
├── eventNightStarted
└── eventTimeUpdated
```

**Sistema de tiempo:**
- 30 min real = 1 día game
- 15 min real = 1 noche
- Timers en el juego usan **Time.deltaTime** (respetan timeScale)

---

### 3.3 DataManager (Persistencia + SQLite)

```
DataManager
├── SaveGame(playerData: SaveData)
├── LoadGame() → SaveData
├── InitializeDatabase()
└── UpdateNPCReputation(npcID, delta)
```

**Base de datos SQLite:**

```
Tables:
├── PlayerData (dinero, experiencia, clase, nivel)
├── InventoryItems (itemID, cantidad, ubicación)
├── FarmState (cultivos, animales, máquinas progreso)
├── TavernState (nivel, recetas, clientes)
├── SmithyState (research, herreros, items)
├── NPCReputation (npcID → reputación, último encuentro)
├── Orders (pedidos activos, plazo, estado)
└── WorldState (bioma desbloqueado, bosses vencidos, eventos)
```

---

### 3.4 EventSystem (Comunicación Inter-Sistemas)

**Patrón:** Eventos genéricos con formato + acción + datos (desacoplado)

```csharp
public enum EventFormat {
    Success,    // Acción completada OK
    Fail,       // Acción falló (sin ser crítico)
    Error,      // Error crítico
    Question    // Requiere decisión/confirmación
}

public class GameEvent {
    public EventFormat format;           // Cómo presentar
    public string action;                // QUÉ pasó (crop_harvested, order_completed, etc)
    public Dictionary<string, object> data;  // Datos específicos
    public EventPriority priority;       // Low, Normal, High, Critical
    public DateTime timestamp;
    public string source;                // Qué manager emitió
}

public enum EventPriority {
    Low,       // Toast simple
    Normal,    // Toast normal
    High,      // Popup modal
    Critical   // Modal grande + sonido
}
```

**Patrón Central:**
```
EventSystem.OnEvent (event: GameEvent)
├── NotificationService → interpreta formato + priority
├── LoggerService → registra crudo (auditoría)
├── UIManager → actualiza según acción
├── Otros listeners → reaccionan según acción
```

---

**Ejemplo flujo completo:**

```
1. FarmManager: "Cosechado trigo"
   → EventSystem.OnEvent?.Invoke(new GameEvent {
       format: Success,
       action: "crop_harvested",
       data: { cropType: "trigo", quantity: 5 },
       priority: Normal,
       source: "FarmManager"
     })

2. InventoryManager escucha
   → if (action == "crop_harvested") { AddItem(...) }
   → Suma +5 trigo exitosamente
   → Emite su propio evento:
     → EventSystem.OnEvent?.Invoke(new GameEvent {
         format: Success,
         action: "inventory_updated",
         data: { itemType: "trigo", quantity: 5 },
         priority: Normal
       })

3. NotificationService escucha (ambos eventos)
   → if (format == Success && priority == Normal) {
       ShowToast($"✓ +5 trigo", Color.green, 2f);
     }

4. LoggerService escucha
   → LogToDatabase(gameEvent)  // Registra tal cual

5. UIManager escucha
   → if (action == "crop_harvested" || "inventory_updated") {
       UpdateFarmUI();
     }
```

**Ventajas:**
- **Desacoplado:** Formatos genéricos, datos específicos
- **Escalable:** Nuevo evento = nuevos datos, mismo formato
- **Flexible:** Cada listener decide cómo actuar
- **Auditable:** Todo se registra crudo en logs

---

### 3.5 Managers Específicos

#### FarmManager
```
FarmManager
├── cropSlots: Crop[] (10-25 slots expandibles)
├── animalSlots: Animal[] (con timers producción)
├── machineSlots: Machine[] (timers de procesamiento)
├── orderBoard: List<Order>
│
├── PlantCrop(cropType) → timer inicia
├── HarvestCrop(slotID) → evento CropHarvested
├── FeedAnimal(animalID, food) → verifica comida
├── ProcessInMachine(itemID, machineID) → timer
├── ReceiveOrder(order) → tablón actualiza
└── CompleteOrder(orderID) → dinero + reputación
```

---

#### TavernManager
```
TavernManager
├── kitchenStations: Station[] (horno, caldero, parrilla)
├── fermentationBarrels: Barrel[] (cerveza, hidromiel, vino)
├── currentCustomers: Customer[]
├── tables: Table[]
│
├── CustomerArrives(npcType) → espera, pide comida
├── CookDish(recipeID, stationID) → timer
├── ServeCustomer(customerID, dishID)
├── Customer.PatienceBar → decrece cada frame
├── CleanTaberna() → mejora limpieza
└── HireNPC(npcType, salario) → automático
```

---

#### SmithyManager
```
SmithyManager
├── mineLevels: Dictionary<mineType, yield>
├── smelters: Smelter[]
├── forges: Forge[]
├── displayCases: DisplayCase[]
├── researchTree: ResearchNode[]
├── employees: Employee[]
│
├── ExtractOre(mineType) → minero automático
├── SmeltOre(oreType, smelterID) → timer
├── ForgeMetal(metalID, forgeID, recipeID) → timer
├── PlaceInDisplayCase(itemID, caseID)
├── NegotiateWithCustomer(customerID, priceProposed)
├── ResearchTech(techID) → costo + timer
└── HireEmployee(role, salario)
```

---

#### CombatManager (Orquestador de Combate)
```
CombatManager (Decisiones de combate)
├── playerController: PlayerCombatController
├── enemyAI: EnemyAI[]
├── currentEnemies: List<string> (characterIDs)
├── waveController: WaveController
├── skillDatabase: SkillDatabase
│
├── StartCombat(biome, difficulty)
├── SpawnWave(waveNumber) → crea enemies en CharacterSystem
├── PlayerUseSkill(skillID, targetID)
│   └─ Consulta SkillDatabase
│   └─ Aplica via CharacterSystem
├── EnemyUseSkill(enemyID, skillID)
│   └─ IA decide skill
│   └─ Aplica via CharacterSystem
├── PlayerDies() → respawn Granja, items dropped
└── BossDefeated(bossID) → unlock siguiente bioma
```

**NO calcula damage/heal/buffs.** Solo orquesta.

---

#### CharacterSystem (Estado Universal de Characters)

```
CharacterSystem
├── characters: Dictionary<string, Character>
│   ├── "player_1" → Character (player)
│   ├── "enemy_goblin_001" → Character (enemy)
│   └── "boss_lobo_ancestral" → Character (boss)
│
├── ApplyDamage(charID, amount)
│   └─ Calcula defense, emite evento, checkea muerte
├── ApplyHeal(charID, amount)
│   └─ Suma health, emite evento
├── ApplyBuff(charID, buffID, duration)
│   └─ Suma buff con timer, recalcula stats
├── ApplyStatusEffect(charID, effectType, duration)
│   └─ Aplica estado (envenenado, congelado, etc)
├── EquipItem(charID, itemID)
│   └─ Recalcula stats
├── RecalculateStats(charID)
│   └─ Suma equipment + buffs → stats finales
└── UpdateAllCharacters(deltaTime)
    └─ Reduce timers de buffs/status
```

**Flujo Ejemplo: Player ataca enemigo**

```
1. CombatManager: "Player usa Slash nivel 3"
   → SkillDatabase.GetSkill("Slash", 3)
      ← { damage: 20, debuff: null }

2. CombatManager: Calcula daño final
   → if Random() < critChance → damage *= 1.5
   → Resultado: 20 damage (o 30 si crítico)

3. CombatManager: Aplica
   → CharacterSystem.ApplyDamage("enemy_goblin_001", 20)

4. CharacterSystem ejecuta:
   → Character enemy = GetCharacter("enemy_goblin_001")
   → netDamage = 20 - enemy.defense = 20 - 2 = 18
   → enemy.health -= 18
   → Emite evento:
     → EventSystem.OnEvent?.Invoke(new GameEvent {
         format: Fail,
         action: "character_took_damage",
         data: {
           characterID: "enemy_goblin_001",
           damage: 18,
           health: 32
         }
       })
   → Si health <= 0: KillCharacter()

5. Listeners reaccionan:
   → UIManager: actualiza enemy health bar
   → NotificationService: muestra "-18 HP"
   → LoggerService: registra ataque
```

---

**Flujo Ejemplo: Enemy usa Poison debuff**

```
1. CombatManager: EnemyAI decide usar Poison
   → SkillDatabase.GetSkill("Poison", 1)
      ← { statusEffect: "poisoned", duration: 5, damagePerTick: 2 }

2. CombatManager: Aplica
   → CharacterSystem.ApplyStatusEffect("player_1", "poisoned", 5f)

3. CharacterSystem:
   → Character player = GetCharacter("player_1")
   → player.statusDurations["poisoned"] = 5f
   → Emite evento:
     → EventSystem.OnEvent?.Invoke(new GameEvent {
         format: Fail,
         action: "status_effect_applied",
         data: {
           characterID: "player_1",
           effect: "poisoned",
           duration: 5
         }
       })

4. Cada frame, CharacterSystem.UpdateAllCharacters():
   → if player has "poisoned" status:
     → damagePerTick -= deltaTime
     → if (damagePerTick <= 0):
         → CharacterSystem.ApplyDamage("player_1", 2)
         → damagePerTick = 1.0f (next tick)
```

---

**Flujo Ejemplo: Player usa Heal + Buff**

```
1. CombatManager: "Player usa Heal Spell nivel 2"
   → SkillDatabase.GetSkill("HealSpell", 2)
      ← { heal: 25, buff: "regeneration", buffDuration: 10 }

2. CombatManager: Aplica múltiples acciones
   → CharacterSystem.ApplyHeal("player_1", 25)
   → CharacterSystem.ApplyBuff("player_1", "regeneration", 10f)

3. CharacterSystem (ambos):
   → ApplyHeal: player.health += 25, emite evento
   → ApplyBuff: agrega buff con timer, recalcula stats
   → Emite 2 eventos (heal + buff)

4. Listeners reaccionan:
   → NotificationService: "+25 HP" + "Buff regeneration"
   → UIManager: actualiza health bar + visual buff icon
```

---

#### NPCManager
```
NPCManager
├── npcInstances: Dictionary<npcID, NPC>
├── npcBehavior: NPCBehavior[] (máquina estados)
├── reputationMap: Dictionary<npcID, int>
│
├── SpawnNPC(npcType, location) → instancia NPC
├── UpdateNPCBehavior(npcID, deltaTime)
├── NegotiatePrice(npcID, itemID, proposedPrice)
├── SaveReputation(npcID, delta)
└── GetNPCPrice(npcID, itemID) → calcula con reputación
```

---

#### InventoryManager
```
InventoryManager
├── farmInventory: Dictionary<itemID, int>
├── playerInventory: Dictionary<itemID, int>
├── cartSlots: int (5-30 según carreta)
│
├── AddItem(itemID, quantity, location)
├── RemoveItem(itemID, quantity, location)
├── MoveItem(itemID, fromLocation, toLocation)
├── GetInventory(location) → Dictionary
└── CanCarry(itemID, quantity) → bool
```

---

#### EconomyManager
```
EconomyManager
├── playerMoney: int
├── priceBaseMap: Dictionary<itemID, float>
├── demandModifiers: Dictionary<itemID, float> (guerra/paz)
├── reputationMultiplier: float
│
├── AddMoney(amount, reason)
├── SubtractMoney(amount, reason)
├── CalculatePrice(itemID, npcType) → float
├── ApplyDemandFluctuation(itemID, modifier)
├── GetNPCPrice(itemID, npcID) → incluye reputación
└── LogTransaction(type, amount, reason)
```

#### RewardManager (Sistema Centralizado de Recompensas)

```
RewardManager (Una fuente de verdad para TODAS las recompensas)
├── rewardDatabase: Dictionary<string, RewardDefinition>
│   ├── Rewards de enemigos (drops + XP + dinero)
│   ├── Rewards de quests
│   ├── Rewards de achievements
│   ├── Rewards de tareas diarias
│   └── Rewards de eventos
│
├── RollReward(rewardID, playerLevel?) → RewardDefinition
│   ├─ Busca en DB
│   ├─ Calcula RNG (drops con %)
│   ├─ Calcula escalado (XP basado en level)
│   └─ Retorna reward final
│
└── AwardReward(rewardID, playerID)
    ├─ Busca reward
    ├─ InventoryManager.AddItems()
    ├─ PlayerXP.AddXP()
    ├─ EconomyManager.AddMoney()
    ├─ NPCManager.AddReputation() (si aplica)
    └─ Emite evento único: "reward_awarded"
```

**Ventajas Arquitectónicas:**

```
Single Responsibility:
  RewardManager SOLO maneja lógica de recompensas
  (No mezcla: combate, inventario, XP, etc.)

Open/Closed Principle:
  Abierto a extensión: agregar nuevo reward type
  Cerrado a modificación: no toca otros sistemas

Testing Aislado:
  RewardManager.Tests → prueba SOLO esta lógica
  Si cambio drop rates, solo reviso 1 test file
  Riesgo de regresión: BAJO

Mantenimiento:
  Cambiar drop rates → editar solo RewardManager + JSON
  No toco CombatManager, EnemySpawner, etc.
  Bajo riesgo de romper código no relacionado
```

---

**Flujo Completo: Enemy muere → Rewards**

```
1. CombatManager: "Goblin nivel 30 muere"
   → CharacterSystem.KillCharacter("enemy_goblin_001")

2. CombatManager: Pide recompensas
   → RewardManager.RollReward("enemy_goblin_lvl_30", playerLevel: 25)

3. RewardManager calcula:
   → Busca en DB: "enemy_goblin_lvl_30"
   → Roll loot:
     └─ Random(100) = 67 < 50? NO (leather)
     └─ Random(100) = 28 < 30? SÍ → iron_ore
     └─ Random(100) = 12 < 15? SÍ → sword_iron
     └─ Random(100) = 98 < 5? NO (crystal)
   → Calcula XP:
     └─ Base: 100 (goblin)
     └─ Multiplicador: 30 * 10 = 300
     └─ Total: 100 * 300 = 30,000 XP
   → Calcula dinero: 500 monedas
   → Retorna: { items: [...], xp: 30000, money: 500 }

4. RewardManager: Otorga recompensas
   → InventoryManager.AddItems([iron_ore, sword_iron])
   → PlayerXP.AddXP(30000)
   → EconomyManager.AddMoney(500)

5. RewardManager: Emite evento único
   → EventSystem.OnEvent?.Invoke(new GameEvent {
       format: Success,
       action: "reward_awarded",
       data: {
         rewardID: "enemy_goblin_lvl_30",
         items: [iron_ore, sword_iron],
         xp: 30000,
         money: 500
       },
       priority: High
     })

6. Listeners reaccionan:
   → UIManager: muestra popup "30,000 XP + items + 500 monedas"
   → NotificationService: toast "+30,000 XP"
   → LoggerService: registra en DB
```

---

**Tabla de Recompensas Unificada (JSON Config)**

```json
{
  "rewards": {
    "enemy_goblin_lvl_21": {
      "type": "enemy",
      "baseXP": 5000,
      "baseMoney": 300,
      "items": [
        { "itemID": "leather", "dropRate": 50 },
        { "itemID": "iron_ore", "dropRate": 30 },
        { "itemID": "sword_iron", "dropRate": 15 },
        { "itemID": "crystal_common", "dropRate": 5 }
      ]
    },
    "enemy_goblin_lvl_30": {
      "type": "enemy",
      "baseXP": 9000,
      "baseMoney": 500,
      "items": [
        { "itemID": "iron_ore", "dropRate": 40 },
        { "itemID": "sword_steel", "dropRate": 25 },
        { "itemID": "crystal_uncommon", "dropRate": 10 }
      ]
    },
    "boss_lobo_ancestral": {
      "type": "boss",
      "baseXP": 50000,
      "baseMoney": 2000,
      "items": [
        { "itemID": "mithril_ore", "dropRate": 40 },
        { "itemID": "boss_sword", "dropRate": 20 },
        { "itemID": "crystal_rare", "dropRate": 8 },
        { "itemID": "scroll_skill_ancestral", "dropRate": 2 }
      ]
    },
    "quest_main_rescue_villager": {
      "type": "quest",
      "baseXP": 15000,
      "baseMoney": 1000,
      "items": [
        { "itemID": "sword_steel", "quantity": 1 }
      ],
      "reputation": [
        { "npcID": "aldeano_001", "delta": 10 }
      ]
    },
    "achievement_defeat_first_boss": {
      "type": "achievement",
      "baseXP": 25000,
      "badge": "dragon_slayer",
      "unlock": "skill_dragon_resistance"
    },
    "daily_task_collect_20_items": {
      "type": "daily",
      "baseXP": 500,
      "baseMoney": 100
    }
  }
}
```

---

**Casos de Uso Unificados**

```
RewardManager.AwardReward("enemy_goblin_lvl_30", playerID)
  → Mata un goblin

RewardManager.AwardReward("quest_main_rescue_villager", playerID)
  → Completa una quest

RewardManager.AwardReward("achievement_defeat_first_boss", playerID)
  → Desbloquea logro

RewardManager.AwardBatch([
  "daily_task_1",
  "daily_task_2",
  "daily_task_3"
], playerID)
  → Completa múltiples tareas diarias
```

**Mismo código. Diferentes rewards. Todo centralizado.**

---

## 3.6 Sistemas de Gameplay

### InputManager (Mapeo de Controles)

```csharp
InputManager
├── Mapeos de teclas:
│   ├── WASD → movimiento (PlayerController)
│   ├── Mouse → cámara (CameraManager)
│   ├── E → interacción cercana (InteractionSystem)
│   ├── 1-4 → skills de combate (CombatManager)
│   ├── I → inventario (UIManager)
│   ├── C → árbol de habilidades (SkillTreeManager)
│   └── ESC → pausa
│
└── GetInput(action) → Vector3/bool/etc
```

### PlayerController (Movimiento 3ª Persona)

```csharp
PlayerController (tipo Valheim)
├── position: Vector3 (en el mundo)
├── velocity: Vector3
├── rotación: Quaternion (sigue mouse)
├── Update():
│   ├─ InputManager.GetInput(WASD)
│   ├─ Aplica movimiento + gravedad
│   ├─ Anima (AnimationManager)
│   └─ CharacterSystem.ApplyMovement()
└── CheckInteractions() (E proximidad)
```

### CameraManager (Cámara tipo Valheim)

```csharp
CameraManager
├── Posición: relativa a player (offset)
├── Distancia: ~3-5 unidades atrás/arriba
├── Rotación: sigue cabeza del player
├── Zoom: mouse wheel
└── Obstructions check (roca entre cámara y player)
```

### PlayerLevelingSystem

```csharp
PlayerLevelingSystem
├── currentXP: int
├── currentLevel: int
├── skillPoints: int (se suma cada level up)
├── AddXP(amount)
│   ├─ currentXP += amount
│   ├─ if currentXP >= nextLevelXP:
│   │   ├─ Level Up
│   │   ├─ skillPoints += 1
│   │   ├─ Emite evento: "player_level_up"
│   │   └─ SkillTreeManager.UnlockNewSkills()
│   └─ Emite evento: "xp_gained"
```

### SkillTreeManager

```csharp
SkillTreeManager
├── skillTree: Dictionary<skillID, SkillNode>
│   ├── Cada nodo requiere X level para desbloquear
│   ├── Ejemplo: "FireStrike" requiere level 5
│   └── Gasto 1 skill point para desbloquear
├── UnlockSkill(skillID)
│   ├─ if player.level >= requirement:
│   │   ├─ Agrega skill a player.skills[]
│   │   ├─ skillPoints -= 1
│   │   └─ Emite evento: "skill_unlocked"
└── GetAvailableSkills() → solo skills desbloqueados
```

### InteractionSystem

```csharp
InteractionSystem
├── Detecta objetos cercanos (cast radio 2-3 unidades)
├── Si player presiona E → qué interactúa:
│   ├─ Cultivo → FarmManager.HarvestCrop()
│   ├─ Máquina → MachineController.Interact()
│   ├─ NPC → NPCManager.InitiateTrade()
│   ├─ Puerta → SceneTransitionManager.ChangeScene()
│   └─ Itemdrop → InventoryManager.PickUp()
└─ UI: muestra "E" si hay algo interactuable
```

### RespawnSystem

```csharp
RespawnSystem
├── OnCharacterDeath(playerID):
│   ├─ Guarda posición de muerte
│   ├─ Emite eventos (items dropped en suelo)
│   ├─ Player respawns en Granja (spawn point)
│   ├─ Pierde items equipados (caen en suelo)
│   ├─ Mantiene dinero + XP
│   └─ Emite evento: "player_respawned"
```

### AnimationManager

```csharp
AnimationManager
├── Anima al player según estado:
│   ├─ Idle (parado)
│   ├─ Walking (WASD)
│   ├─ Attacking (skill usado)
│   ├─ TakingDamage (hit feedback)
│   ├─ Dead
│   └─ Interacting (E en objeto)
├── Sincroniza con CharacterSystem:
│   ├─ Si player.health baja → "TakingDamage" anim
│   ├─ Si player usa skill → skill anim
│   └─ Hit feedback visual (knockback, shake)
```

### SceneTransitionManager

```csharp
SceneTransitionManager
├── Cambios de escena:
│   ├─ Granja ↔ Taberna (carreta)
│   ├─ Granja ↔ Herrería (carreta)
│   ├─ Granja → Combate (noche/oleada)
│   └─ Combate → Granja (muerte/victoria)
├── OnTransition(targetScene):
│   ├─ DataManager.SaveGame() (guardar estado)
│   ├─ Load targetScene
│   ├─ Restaura player state (posición, inventario, etc)
│   └─ Emite evento: "scene_changed"
```

---

## 3.5 Servicios que Consumen EventSystem

### NotificationService (Interpreta Formato)

```csharp
public class NotificationService : MonoBehaviour {
    void Start() {
        EventSystem.OnEvent += HandleGameEvent;
    }

    void HandleGameEvent(GameEvent evt) {
        // Solo interpreta formato, ignora acción específica
        switch (evt.format) {
            case EventFormat.Success:
                ShowToast("✓ " + GetActionLabel(evt.action), Color.green, 2f);
                break;
            case EventFormat.Fail:
                ShowToast("✗ " + GetActionLabel(evt.action), Color.yellow, 2f);
                break;
            case EventFormat.Error:
                ShowPopupModal("❌ Error: " + GetActionLabel(evt.action));
                break;
            case EventFormat.Question:
                ShowModalWithConfirm("¿" + GetActionLabel(evt.action) + "?");
                break;
        }
    }

    string GetActionLabel(string action) {
        // Convierte "crop_harvested" → "Cosechado"
        return action switch {
            "crop_harvested" => $"+{data["quantity"]} {data["cropType"]}",
            "order_completed" => "Orden completada",
            "reputation_changed" => $"Reputación {data["delta"]}",
            _ => action
        };
    }
}
```

### LoggerService (Registra Todo)

```csharp
public class LoggerService : MonoBehaviour {
    void Start() {
        EventSystem.OnEvent += LogGameEvent;
    }

    void LogGameEvent(GameEvent evt) {
        // Registra crudo en SQLite (auditoría completa)
        string json = JsonConvert.SerializeObject(evt);
        
        database.LogEvent(new EventLogEntry {
            timestamp = evt.timestamp,
            format = evt.format.ToString(),
            action = evt.action,
            source = evt.source,
            dataJson = json,
            priority = evt.priority.ToString()
        });
    }
}
```

### UIManager (Actualiza según Acción)

```csharp
public class UIManager : MonoBehaviour {
    void Start() {
        EventSystem.OnEvent += HandleGameEvent;
    }

    void HandleGameEvent(GameEvent evt) {
        // Ignora formato, reacciona por acción
        switch (evt.action) {
            case "crop_harvested":
                UpdateFarmUI((string)evt.data["cropType"]);
                break;
            case "inventory_updated":
                RefreshInventoryPanel();
                break;
            case "money_changed":
                UpdateMoneyDisplay((int)evt.data["delta"]);
                break;
        }
    }
}
```

---

## Tabla de Acciones Comunes

| Action | Format | Priority | Datos | Quién emite |
|--------|--------|----------|-------|------------|
| `crop_harvested` | Success | Normal | cropType, quantity | FarmManager |
| `animal_produced` | Success | Low | animalType, quantity | FarmManager |
| `inventory_full` | Error | High | reason | InventoryManager |
| `customer_arrived` | Success | Normal | npcType, npcID | TavernManager |
| `customer_left_unhappy` | Fail | Normal | npcID, lostReputation | TavernManager |
| `order_completed` | Success | High | orderID, reward | NPCManager |
| `order_failed_timeout` | Error | High | orderID | NPCManager |
| `item_crafted` | Success | Normal | itemID, quality | SmithyManager |
| `enemy_died` | Success | Low | enemyType, loot | CombatManager |
| `boss_defeated` | Success | Critical | bossName, biomeUnlocked | CombatManager |
| `reputation_changed` | Success/Fail | Normal | npcID, delta, reason | NPCManager |
| `money_changed` | Success/Fail | Low | delta, reason | EconomyManager |

---

## 4. Flujo de Datos (Ejemplo: Venta a NPC)

```
1. FarmManager: Planta & cosecha trigo
   → EventSystem.OnEvent?.Invoke(new GameEvent {
       format: Success,
       action: "crop_harvested",
       data: { cropType: "trigo", quantity: 5 },
       priority: Normal
     })

2. InventoryManager escucha
   → Suma +5 trigo al almacén
   → Emite su propio evento:
     → EventSystem.OnEvent?.Invoke(new GameEvent {
         format: Success,
         action: "inventory_updated",
         data: { itemType: "trigo", quantity: 5 }
       })

3. NotificationService escucha (ambos)
   → format == Success → ShowToast("✓ +5 trigo")

4. LoggerService escucha
   → Registra ambos eventos en DB

5. Jugador: Procesa en Molino
   → MachineController: timer activo
   → Al terminar:
     → EventSystem.OnEvent?.Invoke(new GameEvent {
         format: Success,
         action: "item_processed",
         data: { input: "trigo", output: "harina", quantity: 5 }
       })
   → InventoryManager: -5 trigo, +5 harina

6. NPCManager: Aldeano llega pidiendo harina
   → EventSystem.OnEvent?.Invoke(new GameEvent {
       format: Question,
       action: "npc_negotiation_started",
       data: { npcID: "aldeano_001", itemType: "harina", quantity: 5 },
       priority: High
     })
   → NotificationService: Muestra modal de negociación

7. Negociación:
   → EconomyManager.CalculatePrice("harina", "aldeano_001")
   → Base: 20 × 5 = 100
   → Reputación +5 → +5% = 105
   → Aldeano propone 95

8. Jugador acepta:
   → EventSystem.OnEvent?.Invoke(new GameEvent {
       format: Success,
       action: "order_completed",
       data: { 
         npcID: "aldeano_001", 
         itemType: "harina",
         quantity: 5,
         price: 95 
       },
       priority: High
     })

9. Múltiples listeners reaccionan:
   → InventoryManager: -5 harina
   → EconomyManager: +95 monedas
   → NPCManager: Reputación aldeano +1
   → NotificationService: ShowToast("✓ Orden completada +95 monedas")
   → LoggerService: Registra todo
   → UIManager: Actualiza dinero, inventario
   → DataManager: Guarda progreso
```

---

## 5. Comunicación Entre Sistemas

### Patrón Event-Driven (Desacoplado)

```
Manager A (Productor)
    │
    └─ EventSystem.OnEvent?.Invoke(new GameEvent {
         format: Success,
         action: "crop_harvested",
         data: { ... }
       })
       
       ├─→ Manager B escucha
       │   └─ Suma items si action == "crop_harvested"
       │
       ├─→ NotificationService escucha
       │   └─ Muestra toast (format == Success)
       │
       ├─→ LoggerService escucha
       │   └─ Registra evento en DB
       │
       └─→ UIManager escucha
           └─ Actualiza UI según action
```

**Ventajas:**
- **Desacoplado:** Productores no saben de listeners
- **Escalable:** Agregar nuevo listener = solo suscribirse
- **Flexible:** Formatos genéricos, acciones específicas
- **Auditable:** Todo se registra crudo

**NO usamos:**
- Direct coupling (Manager A llamando a Manager B)
- Singletons acoplados (Manager.Instance.DoThing())

**Sí usamos:**
- Subscripción a eventos genéricos (formato + acción)
- Listeners interpretan según su necesidad
- Single responsibility

---

## 6. UI Architecture

### UIManager (Canvas principal)

```
Canvas (World Space)
├── HUD/
│   ├── MoneyDisplay
│   ├── TimeDisplay (día/noche, hora)
│   ├── SelectedItemDisplay
│   └── ActionButtons
│
├── Modals/
│   ├── InventoryUI (modal sobre pantalla)
│   ├── DialogueUI (negociación NPC)
│   ├── CombatHUD (oleadas, vida)
│   ├── MenuPausa
│   └── SettingsUI
│
└── Popups/
    ├── NotificationUI (ganancia dinero, evento)
    ├── ConfirmationUI (¿vender items?)
    └── ErrorUI (no hay espacio, etc.)
```

**Pattern:** 
- UIManager mantiene referencia a todos los UI controllers
- Evento → UIManager actualiza UI relevante
- UI → Evento de acción (ej: btnSell → venta)

---

## 7. Entity Management

### NPCs (Instancias)

```
NPC (clase base)
├── npcID: string (aldeano_001)
├── npcType: string (aldeano, aventurero, militar)
├── position: Vector3
├── behavior: StateMachine (idle, shopping, leaving)
├── currentOrder: Order (qué quiere comprar)
└── reputation: int (relación con jugador)
```

**Ciclo de vida NPC:**
1. Spawn (aparece en tablón/taberna)
2. Behavior (busca items, compra, come)
3. Satisfecho/Insatisfecho → reputación ±
4. Despawn (se va)

---

### Enemigos (Pool)

```
Enemy (clase)
├── enemyID: int (pool index)
├── type: string (goblin, orco, jefe)
├── health: int
├── damage: int
├── lootTable: LootDrop[]
└── state: StateMachine (patrol, chase, attack, dead)
```

**Pool de objetos:**
- Reutilizar instancias de enemigos
- +20 enemigos simultáneamente = 20 instancias máx
- Reciclar cuando mueren

---

### Items (Data)

```
Item (ScriptableObject)
├── itemID: string (trigo_001)
├── itemType: enum (crop, animal, cooked, weapon)
├── basePrice: int
├── icon: Sprite
├── stackable: bool
└── properties: Dictionary<string, object>
```

**Instancias en inventario:**
```
InventorySlot
├── itemID: string (referencia al Item)
├── quantity: int
└── quality: enum (normal, good, masterwork)
```

---

## 8. Timers & Coroutines

### TimerPool (custom simple)

```
TimerPool
├── activeTimers: List<Timer>
├── pooledTimers: Stack<Timer> (reutilizar)
│
├── StartTimer(duration, onComplete)
├── StopTimer(timerID)
├── UpdateAllTimers(deltaTime) → se llama en Update()
└── ReleaseTimer(timerID) → retorna a pool
```

**Por qué custom:**
- Los timers deben respetar `TimeManager.timeScale`
- Mejor control que Coroutines
- Más eficiente (reutilización)

**Uso:**
```
// Cultivo crece en 2 min
timerPool.StartTimer(120f, () => {
    CropReady(cropID);
});

// En Update:
timerPool.UpdateAllTimers(Time.deltaTime);
```

---

## 9. Persistencia (SQLite)

### SaveData (estructura)

```
SaveData
├── playerData
│   ├── money: int
│   ├── class: string
│   ├── level: int
│   └── position: Vector3
│
├── farmData
│   ├── cropStates: CropState[]
│   ├── animalStates: AnimalState[]
│   └── machineStates: MachineState[]
│
├── tavernData
│   ├── level: int
│   ├── unlockedRecipes: string[]
│   └── employees: Employee[]
│
├── smithyData
│   ├── researchProgress: ResearchState[]
│   ├── employees: Employee[]
│   └── displayItems: ItemState[]
│
├── inventories
│   ├── farm: Dictionary<itemID, int>
│   ├── player: Dictionary<itemID, int>
│   └── cart: Dictionary<itemID, int>
│
├── npcReputation
│   └── Dictionary<npcID, int>
│
└── worldState
    ├── day: int
    ├── time: float
    ├── unlockedBiomes: string[]
    └── defeatedBosses: string[]
```

**Frequency:**
- Auto-save cada 5 min (configurable)
- Save antes de cambiar escena
- Save en eventos críticos (orden completada, jefe vencido)

---

## 10. Diagrama de Flujo (Ciclo Principal)

```
GameLoop:
┌─────────────────────────────┐
│  1. Update (cada frame)     │
│  ├─ TimeManager.UpdateTime()│
│  ├─ Managers.Update()       │
│  ├─ EventSystem.Process()   │
│  └─ UIManager.UpdateUI()    │
│                             │
│  2. Si EventoCrítico        │
│  ├─ DataManager.SaveGame()  │
│  └─ EventSystem.Fire()      │
│                             │
│  3. Rendering               │
│  └─ Canvas + Sprites render │
└─────────────────────────────┘
```

---

## 11. Flujo de Escenas

```
MainMenu
    ↓
GameManager.LoadGame() → 
    ├─ DataManager.Load()
    ├─ TimeManager.Initialize()
    ├─ Managers.Initialize()
    └─ Load Farm Scene
        ↓
Farm Scene (Granja abierta)
    ├─ Interactúa con cultivos
    ├─ Accede a Taberna (carreta)
    ├─ Accede a Herrería (carreta)
    ├─ Noche → Oleada nocturna (Combat Scene)
    │   └─ Win: Vuelve a Farm
    │   └─ Lose: Respawn en Farm
    └─ Save automático cada evento

Save Game / Quit
    └─ DataManager.SaveGame()
```

---

## 12. Dependencies (qué necesita qué)

```
GameManager
├── TimeManager (necesita)
├── DataManager (necesita)
└── Todos los Managers (inicia)

FarmManager
├── TimeManager (para timers)
├── InventoryManager (para items)
├── EconomyManager (para dinero)
├── EventSystem (para eventos)
└── DataManager (para persistencia)

CombatManager
├── TimeManager (para timers de ataque)
├── NPCManager (para drops)
└── EconomyManager (para recompensas)

UIManager
├── Todos los managers (escucha eventos)
└── EventSystem (se suscribe)

NPCManager
├── InventoryManager (verifica items)
├── EconomyManager (calcula precios)
├── ReputationSystem (track reputación)
└── EventSystem (comunica compras)
```

---

## 13. Próximos Pasos (Implementación)

- [ ] Crear base de datos SQLite schema
- [ ] Implementar Core/ (GameManager, TimeManager, DataManager, EventSystem)
- [ ] Implementar cada Manager (FarmManager, TavernManager, etc.)
- [ ] Implementar UI (UIManager + modales)
- [ ] Crear prefabs de entidades (NPCs, enemigos, items)
- [ ] Integración Blender (importar modelos, animaciones)
- [ ] Testing y balance (ajustar timers, dinero, dificultad)

---

## Notas Importantes

1. **Single Responsibility:** Cada Manager hace UNA cosa bien
2. **Loose Coupling:** Managers no se llaman directamente, usan EventSystem
3. **Data-Driven:** Configuración en JSON + SQLite, no hardcodeada
4. **Escalabilidad:** Fácil agregar nuevos sistemas sin tocar los existentes
5. **Performance:** Object pooling, timers custom, updates optimizados

---

## Relacionado

- [[Granja]] — FarmManager
- [[Taberna]] — TavernManager
- [[Herrería]] — SmithyManager
- [[Combate]] — CombatManager
- [[NPCs]] — NPCManager + ReputationSystem
