---
tipo: sistema
proyecto: Game2
status: bajo-desarrollo
tags: [herrería, fabricación, blacksmith-master-style, shop-titans-style]
updated: 2026-06-18
related: ["[[Granja]]", "[[Taberna]]", "[[Economía]]", "[[Historia]]"]
---

# Herrería (Blacksmith Master + Shop Titans)

**Taller de fabricación estratégico con tienda de venta.** Combina cadena de suministro (Blacksmith Master) con sistema de clientes (Shop Titans). Enfoque Tycoon/Factory Management isométrico.

---

## Desbloqueo

### Cómo obtienes la Herrería

1. **Encuentras el mineral purificador** explorando los biomas (drop de bosses)
2. O **acumulas X dinero** de la Granja/Taberna
3. Construyes/compras la Herrería en la zona de comercio
   - Costo: **2,000 monedas** (más caro que Taberna)
   - O: Obtener mineral purificador (narrativo para historia)
4. **Herreros llegan** a trabajar/pueden ser contratados
5. Comienza operación de fabricación

### Timing

- **Desbloqueo:** Después de expandir Granja + comprar Taberna (~Semana 4-5 de gameplay)
- Requiere acumulación significativa de dinero (~2000+ monedas)

---

## Estructura Física (Isométrica Tycoon-Style)

### Ubicación
- **Zona de Comercio** — junto a Taberna
- Espacio grande (múltiples pisos para expansión)
- Expandible verticalmente (más pisos = más producción)

### Distribución de Áreas

#### Planta Baja: Minería & Fundición
- **Minas conectadas** (acceso a minerales de biomas)
- **Mineros extraen mena** (trabajo automático, requiere pago)
- **Hornos de fundición** (hierro, cobre, mithril)
- **Bariles de almacenamiento** (lingotes esperando procesamiento)

#### Piso 1: Forja & Procesamiento
- **Yunques** (forjado de armas/armaduras)
- **Hornos de fuego** (mantienen metal caliente)
- **Mesas de trabajo** (procesamiento inicial)
- **Barriles de templado** (enfriamiento agua/aceite)

#### Piso 2: Acabado & Ensamblaje
- **Mesas de afilado** (filo de espadas)
- **Mesas de ensamblaje** (empuñaduras, correas)
- **Área de joyas/precisión** (para items de lujo)
- **Almacén de productos finales**

#### Planta Baja/Piso 1: Tienda
- **Vitrinas de exposición** (muestran equipamiento)
- **Mostrador de negociación** (interacción con clientes)
- **Área de transacción** (donde compran)

---

## Parte 1: Factory Management (Blacksmith Master-Style)

### Cadena de Suministro

```
Minería → Transporte → Fundición → Almacén Lingotes
                                        ↓
                                    Forjado
                                        ↓
                                    Templado
                                        ↓
                                    Acabado
                                        ↓
                                 Almacén Final
```

### 1. Minería & Extracción

**Sistemas:**
- **Mineros contratados** trabajan automáticamente en minas
- Extraen mena bruta (hierro, cobre, estaño, mithril)
- Transporte: llevadores transportan mena al taller
- Costo: Salario mineros (30-50 monedas/día cada uno)

**Rendimiento (por minero/día):**
- Hierro: ~20 unidades
- Cobre: ~15 unidades
- Estaño: ~10 unidades (raro)
- Mithril: ~5 unidades (muy raro, del Pantano)

### 2. Fundición

**Mecánica:**
- Mena bruta entra a horno
- Requiere **combustible** (carbón de leña, obtiene de Granja)
- Tiempo de fusión: 3-5 min según mena
- Output: Lingote puro (1 mena = 1 lingote)

**Gestión:**
- Hornos limitados (expandible)
- Combustible es cuello de botella (must optimize)
- Lingotes calientes deben ir rápido a forja (se enfrían = ineficientes)

**Almacenamiento:**
- Barriles almacenan lingotes
- Capacidad limitada (require expansión)
- Lingotes fríos pierden valor (-10% venta)

### 3. Forjado

**Estaciones:**
- **Yunques** (forjan forma básica)
- **Hornos de fuego** (mantienen metal caliente)
- **Mesas de trabajo** (iniciar proceso)

**Proceso:**
1. Lingote caliente va a yunque
2. Herrero golpea (automático, depende skill)
3. Tiempo: 3-5 min según arma
4. Sale forma bruta (espada bruta, armadura bruta, etc.)

**Especialización de Herreros:**
- **Novato:** Pueden hacer herramientas básicas, clavos, herraduras
- **Experimentado:** Armas simples, armaduras normales
- **Maestro:** Armas de guerra, armaduras de elite, items especiales

### 4. Templado & Acabado

**Templado:**
- Pieza caliente va a barril (agua/aceite)
- Tiempo: 2 min
- Mejora durabilidad/filo

**Acabado:**
- Afilado (si es arma)
- Ensamblaje (espada = lámina + empuñadura)
- Pulido/decorado (items de lujo)
- Tiempo: 2-4 min según complejidad

### 5. Almacén Final

- Guarda productos terminados
- Listos para venta o espera de clientes
- Capacidad limitada (require expansión)

---

## Parte 2: Shop Management (Shop Titans-Style)

### Sistema de Clientes

#### Cómo Llegan Clientes

- **Aventureros/exploradores** entran al taller
- Ven vitrinas con equipamiento disponible
- Piden arma/armadura específica (si la tienes)
- Si no la tienes, pueden esperar encargo

#### Vitrinas de Exposición

**Mecánica:**
- Colocas productos en vitrinas (hasta 8-10 items)
- Clientes ven y deciden si compran
- Diferentes vitrinas por categoría (armas, armaduras, herramientas)

#### Negociación (Shop Titans-Style)

1. **Cliente ve item** en vitrina
2. **Propone precio** (a veces menos de lo que cuesta)
3. **Tú aceptas/rechazas**
4. Si aceptas → venta completa
5. Si rechazas → cliente se va (oportunidad perdida)

**Factores que afectan negociación:**
- Reputación de herrería (más reputación = mejor precio)
- Calidad del item (items de maestro = más precio)
- Demanda actual (guerra = armas caras, paz = herramientas caras)

---

## Recetas & Productos

### Sistema de Recetas

**Cada item requiere ingredientes específicos + tiempo:**

| Item | Ingredientes | Estación | Tiempo | Venta Bruta |
|------|-------------|----------|--------|------------|
| **Clavos** | Hierro x1 | Yunque | 2 min | 10 monedas |
| **Herramienta Básica** | Hierro x2 | Yunque+Acabado | 4 min | 30 monedas |
| **Espada Hierro** | Hierro x3 | Yunque+Templado+Acabado | 7 min | 80 monedas |
| **Armadura Cuero** | Cuero x3 + Hierro x1 | Ensamblaje | 6 min | 100 monedas |
| **Espada Acero** | Acero x3 + Filo x1 | Yunque+Templado+Afilado | 8 min | 150 monedas |
| **Armadura Mithril** | Mithril x2 + Acero x1 | Yunque+Templado+Acabado | 10 min | 250 monedas |

### Desbloqueo de Recetas

**Por I+D (Investigación & Desarrollo):**
- Inviertes dinero en investigación
- Desbloqueas nuevas aleaciones (bronce, acero, mithril)
- Desbloqueas nuevos items (armas de guerra, armaduras de elite)

**Por Reputación con NPCs:**
- NPCs comparten "secretos de forja"
- Al alcanzar reputación máxima: +1 receta especial

---

## Investigación & Desarrollo (I+D)

### Árbol de Tecnología

| Investigación | Costo | Desbloquea | Efecto |
|---------------|-------|-----------|--------|
| **Fundición Mejorada** | 300 monedas | +5% lingotes/horno | Más eficiente |
| **Forja de Acero** | 500 monedas | Receta acero | Acero = 50% durabilidad |
| **Templado Profesional** | 400 monedas | Templado rápido | -1 min templado |
| **Aleación Mithril** | 800 monedas | Receta mithril | Mejor item raro |
| **Martillo Automático** | 600 monedas | Forja 50% automática | -50% tiempo forja |
| **Fuelles Hidráulicos** | 700 monedas | Fundición automática | Hornos 50% automático |

### Automatización

A medida que investigas, algunas tareas se automatizan:
- Forja manual → Martillo automático (50% automático)
- Fundición manual → Fuelles (50% automático)
- Eventualmente, fábrica casi completamente automatizada

---

## Gestión de Pedidos & Economía

### Tipos de Clientes

#### Clientes Locales (Tablón)
- Aldeanos piden herramientas cotidianas
- Pagan regular, menos urgencia
- Ejemplo: "Necesito una azada" (30 monedas)

#### Contratos Militares (Tablón)
- Rey/Señor pide armas/armaduras en cantidad
- Pagan MUCHO mejor (pero tiempo estricto)
- Ejemplo: "20 espadas para el ejército" (150 monedas cada una, plazo 3 días)

#### Aventureros (Directos)
- Llegan al taller, ven vitrinas
- Negocian precio
- Sin plazo fijo, depende de si tienes stock

### Fluctuación de Mercado

**Demanda varía según eventos:**
- **Rumores de guerra:** Armas +50% precio, herramientas -20%
- **Época de cosecha:** Herramientas +30%, armas -10%
- **Festival:** Items decorativos +20%
- **Paz total:** Todo precio normal

**Estrategia:** Anticipar tendencias = mayor ganancia

---

## Optimización Espacial

### Logística & Eficiencia

**El layout del taller afecta productividad:**
- Distancia mena → horno → yunque → templado → acabado
- Trabajadores pierden tiempo caminando si taller está mal diseñado
- Lingotes se enfrían si tienen que viajar lejos

### Ejemplos de Optimización

**Mal diseño:**
```
Horno (arriba)
       ↓ (largo viaje)
   Yunque (abajo)
       ↓ (largo viaje)
  Templado (medio)
```
= Ineficiencia, lingotes fríos, +tiempo

**Buen diseño:**
```
Horno → Yunque → Templado → Acabado
(secuencia lineal)
```
= Flujo óptimo, lingotes calientes, -tiempo

### Expansión Vertical

Conforme crece, desbloqueas nuevos pisos:
- **Piso 1:** Separar fundición (piso 0) de forja (piso 1)
- **Piso 2:** Acabado delicado lejos del ruido
- **Cada piso:** Especialización, eficiencia

---

## Contratación de Personal

### Roles

| Rol | Salario | Función |
|-----|---------|---------|
| **Minero** | 40 monedas/día | Extrae mena (automático) |
| **Fundidor** | 50 monedas/día | Funde mena en lingotes (automático) |
| **Herrero Novato** | 60 monedas/día | Forja básica (azadas, clavos) |
| **Herrero Exp** | 100 monedas/día | Forja armas/armaduras simples |
| **Maestro Armero** | 150 monedas/día | Forja items de elite |
| **Transportista** | 30 monedas/día | Lleva materiales entre estaciones |

### Especialización

Los herreros ganan **experiencia en cada item:**
- Hacen 100 espadas → aprenden espadas (más rápido, mejor calidad)
- Hacen 50 armaduras → expertos en armaduras

**Maestros pueden:**
- Hacer items de mayor calidad (+10% venta)
- Más rápido (-20% tiempo)
- Crear items especiales (únicos, legendarios)

---

## Progresión de Herrería

### Fase 1: Inicial (Días 1-14 post-desbloqueo)
- 1-2 hornos de fundición
- 2-3 yunques
- 2-3 herreros novatos
- Producción manual (sin automatización)
- Items básicos (herramientas, espadas simples)
- Ingresos: ~100-200 monedas/día

### Fase 2: Expansión (Días 15-35)
- +1 piso desbloqueo
- 4-6 hornos + yunques
- +maestros contratados
- Primeras investigaciones (acero, etc.)
- Items intermedios
- Ingresos: ~300-500 monedas/día

### Fase 3: Optimización (Días 36+)
- Múltiples pisos especializados
- Automatización (martillos, fuelles)
- Maestros expertos
- Items raros/legendarios
- Economía de mercado optimizada
- Ingresos: ~1000-2000 monedas/día

---

## Economía de Herrería

### Costos Fijos
- **Salarios:** 200-800 monedas/día (según staff)
- **Investigación:** 300-800 monedas (puntuales)
- **Mejoras:** 500-1000 monedas (expansiones)

### Ingresos

**Venta promedio por item: 30-250 monedas**
- Item básico (clavo): 10 monedas
- Herramienta: 30-80 monedas
- Arma simple: 80-120 monedas
- Arma de guerra: 150-250 monedas
- Item raro: 200-400 monedas

### Ganancia Neta

- **Fase 1:** ~200-400 monedas/día (margen: 50%)
- **Fase 2:** ~600-1000 monedas/día (margen: 60%)
- **Fase 3:** ~1500-2500 monedas/día (margen: 70%)

---

## Flujo de Un Día (Ejemplo)

```
MAÑANA:
- Mineros extraen mena (automático)
- Fundidores funden en lingotes
- Maestro herrero asigna tareas

MEDIODIA:
- Yunques procesan lingotes → espadas brutas
- Templado en barriles
- Aventurero llega: ve espada hierro en vitrina
- Negocia: pide 60 monedas (tú pides 80)
- Aceptas 70 monedas → venta

TARDE:
- Acabado: afilado, empuñaduras
- Nuevo item listo: espada acero
- Investigación completada: +1 receta

NOCHE:
- Cierra taller
- Ganancias: ~300 monedas
- Planifica mañana (qué producir)

CICLO REPITE...
```

---

## Relacionado

- [[Granja]] — produce combustible (carbón de leña)
- [[Taberna]] — clientes pueden pedir equipamiento
- [[Combate]] — equipamiento mejora con items raro
- [[Historia]] — mineral purificador desbloquea Herrería
