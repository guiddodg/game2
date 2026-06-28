---
tipo: sistema
proyecto: Game2
status: bajo-desarrollo
tags: [taberna, cocina, dinamico, ale-tale-style]
updated: 2026-06-18
related: ["[[Granja]]", "[[Herrería]]", "[[Economía]]"]
---

# Taberna (Ale & Tale-Style)

**Centro de servicio activo en tiempo real.** Cocina dinámica, gestión de clientes, limpieza, preparación de ingredientes. Contrasta con la Granja (Hay Day-style, calmado).

---

## Desbloqueo

### Cómo obtienes la Taberna

1. En la **Granja**, el "viejo tabernero" llega periódicamente pidiendo materia prima
2. Cumples sus pedidos → **Reputación sube**
3. Al alcanzar **reputación máxima** → Se jubila en el pueblo
4. **Te ofrece vender la Taberna + su carreta original**
   - Precio: **1,000 monedas** (costo significativo)
   - Pago único
5. **Si compras:** Hereda sus clientes (NPCs que iban a su taberna ahora van a la tuya)

---

## Estructura Física

### Ubicación
- **Zona de Comercio** — separada de Granja
- Accesible por carreta (viaje desde Granja)
- Expandible (más mesas, más cocina)

### Áreas de la Taberna

#### 1. Comedor
- **Mesas para clientes** (inicialmente 2-4, expandible)
- Clientes se sientan automáticamente
- Pueden emborracharse (riesgo de pelea)

#### 2. Cocina
- **Estaciones de cocción:**
  - Horno (pasteles, pan, carnes horneadas)
  - Caldero (sopas, guisos, bebidas calientes)
  - Parrilla (carnes a la parrilla)
  - Mesa de preparación (cortar ingredientes, mezclas frías)

#### 3. Barra de Bebidas
- **Barriles de fermentación** (cerveza, hidromiel, vino)
- **Tarros limpios** para servir
- Puntos de acceso para servir rápido

#### 4. Fregadero & Lavado
- Donde lavas platos y vajilla sucia
- Capacidad limitada de platos limpios

#### 5. Despensa & Almacén
- Guarda ingredientes de la Granja
- Almacenamiento limitado (require expansión)

---

## Bucle Principal: Cocina & Servicio

### Flujo de Pedido (Tiempo Real)

1. **Cliente se sienta** → orden aparece en interfaz
2. **Procesa ingredientes** (si es necesario: cortar, hervir)
3. **Selecciona estación de cocción** (horno, caldero, parrilla)
4. **Tiempo de cocción** (cada receta tiene timer específico)
   - Retirar **ANTES** = crudo (cliente rechaza)
   - Retirar **DESPUÉS** = quemado (ingredientes perdidos)
   - Retirar **A TIEMPO** = éxito (cliente satisfecho)
5. **Sirve el plato** → cliente come
6. **Recibe pago + propina** (o nada si está sucio/frío)
7. **Recoge platos sucios** → llevar al fregadero

### Barra de Paciencia

- Cada cliente tiene **barra de espera visible**
- Si espera demasiado → **se marchará sin pagar** (y molesto)
- Servicio rápido + taberna limpia → **propinas generosas**

---

## Procesamiento de Ingredientes

### Tipo 1: Ingredientes Brutos (de Granja)
- Trigo, carne, verduras, frutas, etc.
- Llegan en inventario desde Granja

### Tipo 2: Procesamiento Necesario
Algunos ingredientes requieren **preparación previa:**

| Ingrediente | Acción | Tiempo | Resultado |
|-------------|--------|--------|-----------|
| Trigo | Moler en mesa | 1 min | Harina |
| Carne | Cortar en tabla | 1 min | Carne picada |
| Cebolla | Picar en tabla | 1 min | Cebolla picada |
| Papa | Pelar en tabla | 1 min | Papa lista |
| Hierbas | Moler en mortero | 1 min | Hierbas molidas |

**Mecánica:** Si necesitas "carne picada" y solo tienes "carne cruda", debes procesarla en la mesa de preparación primero.

---

## Gestión de Bebidas (Fermentación)

### Sistema de Barriles

**Las bebidas NO se compran, se fermentan:**

| Bebida | Ingredientes | Tiempo Fermentación | Rendimiento |
|--------|--------------|-------------------|-------------|
| **Cerveza** | Agua + Lúpulo + Malta | 20 min (idle) | 5 tarros |
| **Hidromiel** | Agua + Miel + Levadura | 25 min (idle) | 5 tarros |
| **Vino** | Agua + Uva + Levadura | 30 min (idle) | 5 tarros |

**Mecánica:**
1. Llenas barril con ingredientes
2. Esperas tiempo de fermentación (ocurre en background)
3. Barril está listo → puedes servir
4. Sirves en tarros limpios
5. Si tarro sucio → cliente rechaza

### Tarros Limpios

- Capacidad limitada de tarros limpios
- Si se agotan → **no puedes servir bebidas**
- Los tarros sucios deben lavarse en el fregadero

---

## Limpieza & Mantenimiento

### Mecánica Activa

**Taberna sucia = clientes infelices = menos dinero**

### Tareas de Limpieza

| Tarea | Acción | Impacto |
|-------|--------|--------|
| **Barrer pisos** | Caminar y recoger basura visible | Mejora limpieza general |
| **Recoger platos sucios** | Ir a mesas, tomar platos | Libera espacio, evita desastre |
| **Lavar vajilla** | Llevar platos al fregadero | Restaura platos limpios |

### Efectos de Suciedad

- **Taberna muy sucia:** -30% dinero de clientes
- **Taberna medianamente sucia:** -15% dinero
- **Taberna limpia:** +0% (normal)
- **Taberna impecable:** +10% propinas

---

## Recetas & Comidas

### Sistema de Recetas

**Todas las comidas requieren ingredientes específicos + tiempo de cocción:**

| Comida | Ingredientes | Estación | Tiempo | Venta Bruta | Ganancia |
|--------|-------------|----------|--------|------------|----------|
| **Pan** | Harina | Horno | 3 min | 30 monedas | +20 |
| **Sopa Vegetal** | Verduras variadas + agua | Caldero | 4 min | 35 monedas | +25 |
| **Estofado** | Carne picada + papa + cebolla | Caldero | 5 min | 50 monedas | +35 |
| **Carne Asada** | Carne + sal | Parrilla | 4 min | 45 monedas | +30 |
| **Pastel de Frutas** | Harina + fruta + azúcar | Horno | 5 min | 40 monedas | +25 |
| **Cerveza** | (fermentación) | Barril | 20 min idle | 25 monedas | +15 |

### Desbloqueo de Recetas

**Escalonado por reputación con NPCs de Granja:**
- **Reputación 50%:** Receta básica
- **Reputación 100%:** Receta especial/avanzada

---

## Interacción con Clientes

### Tipos de Clientes

**Humanoides normales (agricultores, viajeros, aventureros):**
- Piden comida/bebida específica
- Barra de paciencia normal
- Propinas si están felices

**Clientes Ebrios (noche, consumo de alcohol):**
- Barra de paciencia más corta
- Mayor riesgo de pelea si se enojan
- Pueden romper cosas (mobiliario dañado)

### Combate en Taberna

**Ocasionalmente un cliente se emborracha y comienza pelea:**
- Aparece aviso (cliente rojo/enojado)
- Tomas arma blanda (palo, botella vacía)
- Luchas cuerpo a cuerpo en la taberna
- Si lo derrotas: lo expulsas
- Si pierde el jugador: cliente se va, daño al mobiliario, otros clientes se asustan (-dinero)

### Barra de Paciencia

Cada cliente tiene barra visible:
- Se vacía con el tiempo (espera)
- Se llena si: sirves rápido, taberna limpia, comida buena
- Cuando llega a 0: se va sin pagar, habla mal de ti (reputación -5)

---

## Progresión: Niveles de Taberna

### Cómo Suben Niveles

- Cada cliente satisfecho = +1 XP de taberna
- Cada 100 XP = +1 nivel

### Qué Desbloquea Cada Nivel

| Nivel | Desbloquea | Efecto |
|-------|-----------|--------|
| 1 | Recetas básicas | Pan, sopa, cerveza |
| 2 | +1 mesa (3 total) | Más clientes simultáneamente |
| 3 | Nuevas recetas | Estofado, carne asada |
| 4 | Mejora de horno | -1 min tiempo de cocción |
| 5 | +1 mesa (4 total) | Aún más clientes |
| 6 | Recetas especiales | Pasteles, platos complejos |
| 7 | Fermentación rápida | -5 min tiempo barriles |
| 8 | +1 mesa (5 total) | Máximo inicial |

---

## Decoración & Mejoras

### Decoración Afecta Satisfacción

- Cuadros, plantas, mesas bonitas = +5% satisfacción cliente
- Taberna fea/vacía = -5% satisfacción

### Mejoras de Estación

| Mejora | Costo | Efecto |
|--------|-------|--------|
| Horno Mejorado | 300 monedas | -1 min tiempo cocción |
| Caldero Grande | 350 monedas | +1 barril simultáneo |
| Parrilla Profesional | 320 monedas | -1 min tiempo cocción |
| Fregadero Rápido | 250 monedas | Lavar más rápido |
| Mesa Lujosa | 150 monedas | +10% propinas |

---

## Contratación de NPCs

### Sistema de Empleados

**Puedes contratar NPCs para delegar tareas:**

| NPC | Tarea | Salario | Efecto |
|-----|-------|---------|--------|
| **Limpiador** | Barre, recoge platos | 50 monedas/día | Automático: taberna limpia |
| **Lavandero** | Lava vajilla | 40 monedas/día | Automático: platos siempre limpios |
| **Preparador** | Procesa ingredientes | 60 monedas/día | Automático: ingredientes listos |
| **Barman** | Gestiona bebidas/barril | 70 monedas/día | Automático: bebidas listas, tarros limpios |
| **Mozo de Mesón** | Toma pedidos, sirve | 80 monedas/día | Automático: clientes atendidos sin tu intervención |

### Cómo Contratar

- Hablas con NPCs en el pueblo
- Negocias salario
- Firmas contrato
- NPC llega a trabajar al día siguiente
- Salario se descuenta diario de ganancias

### Ventaja de Contratar

**Ejemplo:** Si contratas Limpiador + Lavandero:
- Taberna siempre limpia (no pierdes dinero por suciedad)
- Gastos: 50 + 40 = 90 monedas/día
- Ganancia neta: tu tiempo libre para otras tareas, taberna optimizada

---

## Flujo de Un Día (Ejemplo)

```
MAÑANA:
- Revisas barriles de fermentación (cerveza lista)
- Verificas inventario de ingredientes de Granja
- Abre taberna

MEDIODIA:
- Cliente llega: pide Sopa Vegetal
- Tienes ingredientes: verduras, agua
- Pones en caldero (4 min timer)
- Mientras esperas: barres, recoges platos sucios
- Sopa lista: sirves
- Cliente come, paga 35 monedas + 5 propina (limpieza)

TARDE:
- Más clientes llegan: panes, carnes asadas
- Gestiones horno/parrilla en paralelo
- Algunos beben cerveza del barril
- Un cliente bebe de más → intenta pelea → lo sacas

NOCHE:
- Cierra taberna
- Lava toda la vajilla
- Actualiza barriles para fermentación
- Ganancias del día: ~300-400 monedas

CICLO REPITE...
```

---

## Economía de Taberna

### Ingresos

**Venta promedio por cliente: 30-50 monedas**
- Comida: 30-50 monedas bruto
- Bebida: 20-30 monedas bruto
- Propina: 5-10 monedas (si satisfecho)

**Clientes/día: ~10-15 (escalable)**
- Fase 1: 8-10 clientes/día
- Fase 2: 10-15 clientes/día
- Fase 3: 15-20 clientes/día

### Gastos

- **Salarios NPCs:** 0-400 monedas/día (según cuántos contrates)
- **Ingredientes:** Llegan de Granja (no costo)
- **Mejoras:** Puntuales (300-350 monedas)

### Ganancia Neta

- **Día 1-5:** ~200-300 monedas/día (sin NPCs, gestión manual)
- **Día 10-20:** ~400-600 monedas/día (con 1-2 NPCs)
- **Día 30+:** ~800-1200 monedas/día (full staff, optimizado)

---

## Relacionado

- [[Granja]] — produce ingredientes
- [[Herrería]] — vende mejoras/decoración
- [[Economía]] — balance total del juego
