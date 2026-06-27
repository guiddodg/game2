---
tipo: sistema
proyecto: Game2
status: bajo-desarrollo
tags: [granja, produccion, hay-day-style, economia-core]
updated: 2026-06-17
related: ["[[Taberna]]", "[[Herrería]]", "[[Economía]]", "[[Domesticación]]"]
---

# Granja (Hay Day-Style)

**Centro de producción.** Sistema de cultivos, animales y máquinas de procesamiento. Base de toda la economía del juego.

---

## Estructura & Layout del Terreno

### Ubicación General
- **Centro del mapa** — tu base principal
- **Terreno grande y expandible** (compras expansión en los bordes)
- **Conectada por caminos** a Taberna y Herrería (distancia variable)

### Layout Visual (Homestead Style)

```
        [EXPLORACIÓN - BIOMAS]
   ┌──────────────────────────────┐
   │                              │
   │  [CULTIVOS 1] [CULTIVOS 2]   │
   │                              │
   │ [MÁQUINAS] [ALMACÉN]         │
   │                              │
   │      [🏠 CASA]               │
   │                              │
   │ [ANIMALES]   [CARRETA]       │
   │                              │
   └──────────────────────────────┘
   
   [Expandible: norte, sur, este, oeste]
```

### Distribución de Áreas

**Centro: La Casa**
- Punto de spawn/respawn
- Centro visual del compound
- Punto de referencia

**Zona de Cultivos (Norte)**
- Parcelitas individuales (cada = 1 cultivo)
- Expandibles hacia afuera
- Agrupadas para eficiencia visual

**Zona de Animales (Sur)**
- Establos, gallineros, rediles, chiqueros
- Espacios separados por tipo de animal
- Acceso fácil a comida desde cultivos

**Zona de Máquinas (Este/Oeste)**
- Molino, quesería, prensa, panadería
- Se multiplican según necesidad
- Cerca de almacén (input/output fácil)

**Almacén (Lateral)**
- Inventario central de granja
- Accesible desde máquinas y carreta

**Carreta (Salida)**
- Estacionamiento
- Punto de carga/descarga
- Conexión a Taberna/Herrería

---

## Mecánica Core

### Flujo de Producción

```
Cultivos (plantas) ──→ Cosechas ──→ Venta/Procesa
                                        ↓
                                   Máquinas
                                        ↓
                                   Producto final
                                        ↓
                                   Taberna o Venta
```

**Animales (producen automáticamente con timer)**

```
Establo ──→ Alimentas ──→ Producen recurso (timer) ──→ Recolectas ──→ Taberna/Venta
```

---

## 1. CULTIVOS (Hay Day-Style)

### Mecánica
- **Plantas semillas** → esperas **timer** → cosechas
- Cada cultivo ocupa **1 slot de terreno**
- Diferentes cultivos = diferentes tiempos + rendimientos
- Cosechas se guardan en **almacén** (inventario de granja)

### Lista de Cultivos (Fase 1)

| Cultivo | Tiempo | Producción | Venta Bruta | Uso |
|---------|--------|------------|-------------|-----|
| **Trigo** | 2 min | 1 trigo | 10 monedas | Pan (Taberna), harina (máquina) |
| **Zanahoria** | 3 min | 1 zanahoria | 12 monedas | Comida animal (vaca), Taberna |
| **Maíz** | 3 min | 1 maíz | 12 monedas | Comida animal (gallina, caballo) |
| **Patata** | 4 min | 1 patata | 15 monedas | Comida animal (cerdo), Taberna |
| **Tomate** | 5 min | 1 tomate | 18 monedas | Salsa (máquina), Taberna |
| **Fresa** | 6 min | 1 fresa | 20 monedas | Mermelada (máquina), postre |

**Notas:**
- Tiempos ajustables según balance
- Cultivos se desbloquean conforme avanzas (fase 2+)
- Algunos cultivos requieren "comida especial" después de X cosechas

---

## 2. ANIMALES (Automáticos con Timer)

### Mecánica
- **Tienes establo/corral** → animal está adentro
- Produces recurso **automáticamente cada X minutos**
- Requieren **comida diaria** (si no les das, dejan de producir)
- Cada animal = 1 slot de espacio (mejoras aumentan slots)

### Lista de Animales (Fase 1)

| Animal | Ubicación | Produce | Timer | Comida | Venta |
|--------|-----------|---------|-------|--------|-------|
| **Gallina** | Gallinero | 1 huevo | 4 min | Maíz x1 | 15 monedas |
| **Oveja** | Redil | 1 lana | 5 min | Pasto (free) | 18 monedas |
| **Vaca** | Establo | 1 leche | 6 min | Zanahoria x1 | 25 monedas |
| **Cerdo** | Chiquero | 1 carne* | 7 min | Patata x2 | 30 monedas |
| **Caballo** | Cuadra | Transporte | — | Maíz x2 | N/A (tracción) |

*Nota: Carne también da cuero (drop automático)

### Comida Animal
- Los animales comen **de tu inventario**
- Si no les alimentas: dejan de producir (alert visual)
- Comida: Cultivos específicos (maíz, zanahoria, pasto)
- **Pasto:** Crece naturalmente en terreno (free resource)

---

## 3. MÁQUINAS DE PROCESAMIENTO

### Mecánica
- **Colocas máquina** en granja (1 slot cada una)
- Pones ingredientes + esperas **timer** → obtienes producto final
- Producto final sale a almacén
- Mientras procesa, máquina está "ocupada" (no puedes usar)

### Máquinas (Fase 1)

| Máquina | Input | Output | Timer | Costo | Ganancia |
|---------|-------|--------|-------|-------|----------|
| **Molino** | 1 Trigo (10) | 1 Harina (20) | 2 min | **200 monedas** | +10 monedas |
| **Quesería** | 1 Leche (25) | 1 Queso (50) | 3 min | **250 monedas** | +25 monedas |
| **Prensa** | 1 Tomate (18) | 1 Salsa (35) | 2.5 min | **220 monedas** | +17 monedas |
| **Panadería** | 1 Harina (20) | 1 Pan (40) | 2 min | **250 monedas** | +20 monedas |

### Cadenas de Procesamiento (Ejemplo)

**Trigo → Harina → Pan:**
- Cultiva Trigo (2 min) = 10 monedas bruto
- Molino: Trigo→Harina (2 min) = 20 monedas
- Panadería: Harina→Pan (2 min) = 40 monedas
- **Total:** 6 minutos, +30 monedas netos (vs 10 venta directa)
- **ROI máquinas:** 500 monedas inversión / 30 por ciclo = ~17 ciclos = 102 minutos

**Leche → Queso:**
- Vaca produce Leche (6 min) = 25 monedas bruto
- Quesería: Leche→Queso (3 min) = 50 monedas
- **Total:** 9 minutos, +25 monedas netos (vs 25 venta directa) = DUPLICA ganancia

**Notas:**
- Máquinas se desbloquean en Fase 2 (Día ~15, cuando tengas ~500 monedas)
- Cada máquina ocupa 1 slot (require expansión)
- Multiple máquinas del mismo tipo = paralelizar producción (faster cycles)

---

## 4. ALMACÉN & INVENTARIO

### Almacén de Granja
- **Guardas productos cosechados** (sin límite inicial, expandible después)
- Productos listos para:
  - Vender a NPCs (tablón de pedidos)
  - Llevar a Taberna (carreta)
  - Procesar (máquinas)
  - Vender a viajeros (future)

### Gestión
- Interfaz clara: ves qué tienes, cuánto
- Puedes "mover" items entre almacén/máquinas/carreta

---

## 5. TABLÓN DE PEDIDOS

### Funciona así:
- NPCs vienen cada X tiempo pidiendo productos específicos
- Ejemplo: "Necesito 5 harina para mañana" → ofrecen precio
- Tú cumples: cargas carreta, viajas, entregas, ganas dinero + reputación

### Integración con producción:
- Ver pedido → "necesito 5 harina"
- Sabes que harina = Molino + Trigo
- Plantas trigo → cosechas → procesas en molino → tienes harina → cumples pedido

**Esta es la "dirección" que da gameplay a la granja.**

---

## 6. TRANSPORTE & CARRETAS

### Carretas
- **Pequeña:** 5 slots, 1 caballo, velocidad normal
- **Mediana:** 15 slots, 2 caballos, velocidad +20%
- **Grande:** 30 slots, 4 caballos, velocidad +40%

### Uso
- Cargas producto en carreta
- Viajas a Taberna o Herrería
- Descargas
- Caballos entrenados = más rápido

### Riesgo Nocturno
- Si viajas de noche = enemigos pueden atacar
- Pierdes cargamento si no te defiendes bien

---

## 7. PROGRESIÓN DE GRANJA & EXPANSIONES

### Expansiones de Terreno

| Expansión | Slots Totales | Costo | Cuándo (estimado) | Qué permite |
|-----------|---------------|-------|-------------------|-------------|
| Inicial | 10 | 0 monedas | Día 1 | Empezar |
| +1 | +5 (15 total) | 150 monedas | Día 3-5 | Más cultivos |
| +2 | +5 (20 total) | 250 monedas | Día 10-12 | Primer máquina |
| +3 | +5 (25 total) | 350 monedas | Día 20+ | Múltiples máquinas |

### Fase 1: Inicial (Días 1-14)
- **Slots:** 10-15 (inicial + 1ª expansión)
- **Cultivos:** Trigo, Zanahoria, Maíz (básicos)
- **Animales:** Gallina, Vaca (máx 2-3)
- **Máquinas:** NINGUNA
- **Venta:** Productos brutos a NPCs (pedidos simples)
- **Dinero acumulado:** ~100-200 monedas/día
- **Meta:** Aprender mecánica, acumular $ para máquinas

### Fase 2: Expansión (Días 15-35)
- **Slots:** 20-25 (expansiones 1-2 compradas)
- **Cultivos:** Todos desbloqueados (Patata, Tomate, Fresa)
- **Animales:** 3-4 tipos simultáneamente (gallina, vaca, oveja, cerdo)
- **Máquinas:** Primeras 1-2 (Molino, Quesería)
- **Venta:** Mix productos brutos + procesados
- **Dinero acumulado:** ~300-500 monedas/día
- **Meta:** Optimizar cadenas, recuperar inversión máquinas

### Fase 3: Optimización (Días 36+)
- **Slots:** 25+ (múltiples expansiones)
- **Cultivos:** Todos, rotación constante
- **Animales:** Todos tipos, production completa
- **Máquinas:** 3-4 simultáneamente (paralelizar)
- **Venta:** Productos complejos (Pan, Queso, Salsa, etc.)
- **Dinero acumulado:** ~800-1500 monedas/día
- **Meta:** Eficiencia máxima, financiar otros negocios (Taberna, Herrería)

---

## 8. ECONOMÍA EMERGENTE

### Costos Estimados (TBD - ajustar según balance)

**Desbloqueos:**
- Expansión Granja (cada +5 slots): 150-300 monedas
- Molino: 200 monedas
- Quesería: 250 monedas
- Etc.

**Ingresos (por producto final):**
- Trigo bruto: 10 monedas
- Harina (procesado): 20 monedas (2x ganancia)
- Leche bruta: 35 monedas
- Queso (procesado): 60 monedas (1.7x ganancia)

**La progresión económica emerge:**
- Más máquinas = más procesamiento = más ganancia
- Pero requiere inversión inicial
- Incentiva especializarse en cadenas productivas

---

## 9. Flujo de Un Día (Ejemplo)

```
MAÑANA:
- Despiertas en Granja
- Recolectas huevos de gallina (lista)
- Alimentas vaca (zanahoria)
- Ves tablón: "NPC X necesita 10 harina para hoy"

ACCIÓN:
- Plantas 5 trigo en terreno disponible
- Esperas 2 min (crecen)
- Cosechas trigo
- Pones en molino (convierte trigo → harina, 2 min)
- Esperas

TARDE:
- Recolectas harina del molino
- Cargas carreta pequeña (10 harina)
- Viajan a ver NPC X
- Entregas → +100 monedas, reputación sube

NOCHE:
- Vuelves a Granja
- Oleada nocturna ataca compound
- Defiendes

CICLO REPITE...
```

---

## 10. Relacionado

- [[Taberna]] — recibe productos procesados
- [[Herrería]] — vende carretas/herramientas
- [[Domesticación]] — animales se obtienen explorando
- [[Economía]] — balance de costos emerge de aquí
