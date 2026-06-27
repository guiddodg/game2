---
tipo: sistema
proyecto: Game2
status: borrador
tags: [npcs, gameplay, economia]
updated: 2026-06-20
related: ["[[Granja]]", "[[Taberna]]", "[[Herrería]]", "[[Economía]]"]
---

# NPCs — Arquetipos Funcionales

**4 tipos de NPCs reutilizables.** Sin historias complejas, enfoque en mecánica de juego.

---

## 1. ALDEANO (Campesino/Local)

### Perfil
- **Rol:** Comprador de productos cotidianos
- **Personalidad:** Neutral, sin prisa, justo
- **Apariciones:** Tablón de pedidos (Granja), Taberna

### Comportamiento
- **Frecuencia:** Cada 2-3 horas (cada cierto tiempo in-game)
- **Qué compra:** Productos básicos (cultivos brutos, carnes, bebidas simples)
- **Negociación:** Propone precio base (-5%), acepta hasta base (+5%)
- **Compra típica:** 5-15 unidades

### Tabla de Precios

| Producto | Precio Base | Rango Negociación | Ejemplo |
|----------|------------|------------------|---------|
| Trigo bruto | 10 | 9-10 | "¿Me los dejas en 9?" |
| Huevo | 15 | 14-16 | Acepta 14-16 |
| Leche | 25 | 23-26 | Rígido en rango |
| Pan (procesado) | 40 | 38-42 | Valora procesamiento |

### Reputación
- Cada compra exitosa: +1 reputación
- Si rechazas 2 veces seguidas: -2 reputación (menos compras)

---

## 2. AVENTURERO (Explorador/Cazador)

### Perfil
- **Rol:** Comprador de equipo, paga bien
- **Personalidad:** Impaciente, exigente, buen pagador
- **Apariciones:** Herrería (vitrinas), Tablón pedidos (equipo especial)

### Comportamiento
- **Frecuencia:** Cada 4-5 horas (menos que Aldeano)
- **Qué compra:** Armas, armaduras, equipo de viaje
- **Negociación:** Propone -10-15%, negocia activamente (puede aceptar +10%)
- **Compra típica:** 1-3 items de valor alto

### Tabla de Precios

| Producto | Precio Base | Rango Negociación | Notas |
|----------|------------|------------------|-------|
| Espada Hierro | 80 | 70-90 | "¿Cuál es tu mejor precio?" |
| Armadura Cuero | 100 | 85-110 | Negocia bastante |
| Espada Acero | 150 | 130-170 | Calidad = precio |
| Armadura Mithril | 250 | 220-280 | Items raros, poco regateo |

### Reputación
- Compra exitosa: +2 reputación (valora variedad)
- Si ofreces items raros: +3 reputación
- Cada rechazo: -2 reputación

---

## 3. MILITAR/NOBLE (Contratista)

### Perfil
- **Rol:** Contratos grandes, tiempo limitado, dinero alto
- **Personalidad:** Directo, exigente, sin paciencia
- **Apariciones:** Tablón pedidos (solo), Herrería (encargos)

### Comportamiento
- **Frecuencia:** Cada 8-10 horas (raro)
- **Qué compra:** Equipo en cantidad, armas de guerra, suministros
- **Negociación:** Precio FIJO, no negocia (tomas o dejas)
- **Compra típica:** 10-50 unidades, plazo 3-7 días in-game

### Tabla de Precios

| Pedido | Cantidad | Precio Unitario | Plazo | Total |
|--------|----------|-----------------|-------|-------|
| "Espadas para ejército" | 20 | 150 | 3 días | 3000 |
| "Armaduras del rey" | 10 | 250 | 5 días | 2500 |
| "Herramientas militares" | 50 | 30 | 2 días | 1500 |

### Reputación & Consecuencias
- Cumples a tiempo: +5 reputación (futuras misiones mejores)
- Incumples plazo: -10 reputación (rechaza contratos futuros temporalmente)
- Calidad baja: cancelan, -5 reputación

---

## 4. MERCADER (Comerciante)

### Perfil
- **Rol:** Compra en volumen, márgenes bajos, frecuente
- **Personalidad:** Cálculador, siempre busca ganancia
- **Apariciones:** Tablón pedidos (granja), Taberna (provisiones)

### Comportamiento
- **Frecuencia:** Cada 1-2 horas (muy frecuente)
- **Qué compra:** Cualquier cosa que venda en bulk (productos procesados, bebidas)
- **Negociación:** Propone -20%, pero compra mucho (volumen = compensación)
- **Compra típica:** 20-50 unidades por ciclo

### Tabla de Precios

| Producto | Precio Base | Precio Mercader | Volumen Típico |
|----------|------------|-----------------|-----------------|
| Harina (procesada) | 20 | 16 (-20%) | 30 unidades |
| Queso | 50 | 40 (-20%) | 20 unidades |
| Cerveza | 25 | 20 (-20%) | 40 unidades |
| Pan | 40 | 32 (-20%) | 25 unidades |

### Reputación
- Cada compra: +1 reputación (valora consistencia)
- Si cumples 5 ciclos seguidos: desbloques descuentos en compra (Mercader vende items raros)
- Nunca pide plazo fijo (transacción inmediata)

---

## Sistema de Negociación (Unificado)

### Flujo
1. NPC ve item en vitrina O coloca pedido en tablón
2. **Propone precio** (base menos su % típico)
3. **Tú aceptas/rechazas**
   - Aceptar → venta inmediata
   - Rechazar → NPC se va (oportunidad perdida)
4. **Reputación afecta futuros precios** (más reputación = mejor disposición)

### Factores que Afectan Precio Final
- **Reputación con NPC:** Más reputación = NPC más flexible (+5-10%)
- **Calidad del item:** Items raros/maestría = precio más alto
- **Demanda actual:** Guerra (armas +20%), Paz (herramientas +20%)

---

## Repetición & Instancias

- Cada tipo puede **generar múltiples instancias** (10 Aldeanos distintos)
- NPCs se **repiten en ciclos** (mismo Aldeano vuelve cada 2-3 horas)
- **Nombres generados** (Rogelio, María, Diego, etc.) para variedad sin overhead

---

## Integración con Sistemas

| Sistema | Tipo de NPC | Acción |
|---------|-----------|--------|
| **Granja (Tablón)** | Aldeano, Mercader, Militar | Piden productos, ofrecen dinero + reputación |
| **Taberna (Clientes)** | Aldeano, Aventurero | Comen, beben, pagan + propina |
| **Taberna (Empleados)** | Aldeano | Pueden ser contratados (salarios) |
| **Herrería (Vitrinas)** | Aventurero, Militar | Ven equipo, negocian precios |
| **Herrería (Empleados)** | Aldeano | Pueden trabajar (herreros novatos) |

---

## Tabla de Referencia Rápida

| Arquetipo | Frecuencia | Negociación | Reputación Impact | Mejor Para |
|-----------|-----------|------------|------------------|-----------|
| **Aldeano** | Muy frecuente | Rígida (-5% a +5%) | +1 por compra | Ingresos constantes |
| **Aventurero** | Frecuente | Flexible (-15% a +10%) | +2 por compra | Dinero en picos |
| **Militar** | Raro | Ninguna (fija) | +5/-10 crítico | Contratos grandes |
| **Mercader** | Ultra frecuente | Agresiva (-20%) | +1 volumen | Venta masiva |

---

## Próximos Pasos

- [ ] Generar tabla de nombres por tipo (para instancias)
- [ ] Definir patrones visuales (ropa/apariencia por tipo)
- [ ] Integrar con sistemas de reputación por NPC
- [ ] Balancear precios base según economía general
