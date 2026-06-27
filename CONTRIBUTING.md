# 🔧 Workflow — Game2

Guía para colaboradores.

---

## 📋 Ramas

- **`master`** — No tocar (producción futura)
- **`develop`** — Rama principal de desarrollo
- **`feature/XX-descripcion`** — Ramas de features

---

## 🚀 Workflow (Git Flow)

### 1. Tomar una tarea

- Ve a [ROADMAP.md](./ROADMAP.md)
- Encuentra una tarea `Not started`
- Actualiza el ROADMAP:
  ```
  - [ ] Tarea X
    - Status: In progress
    - Assignee: @tuNombre
  ```

### 2. Crear rama feature

```bash
# Desde develop
git checkout develop
git pull origin develop

# Crear rama
git checkout -b feature/XX-nombre-descriptivo

# Ejemplo:
# git checkout -b feature/01-gamemanager
# git checkout -b feature/09-personaje-base
```

**Nomenclatura:**
- `feature/01-gamemanager`
- `feature/09-personaje-base-blender`
- `feature/15-combat-system`

### 3. Hacer commits

```bash
git add .
git commit -m "Mensaje claro y específico"

# Ejemplos:
# "Implement GameManager singleton with scene persistence"
# "Add TimeManager with day/night cycle callback system"
# "Import Personaje Base rig from Blender with animations"
```

**Reglas de commits:**
- Específicos (no "Update files")
- Imperativo ("Add X", "Fix Y", no "Added X")
- Referenciar issue si aplica: `#15 Fix CharacterSystem state`

### 4. Crear PR contra develop

```bash
git push origin feature/XX-nombre
# GitHub sugiere crear PR automáticamente
```

En GitHub:
- Title: `Feature/XX: Descripción clara`
- Body: Link a issue, qué cambió, testing notes
- Base: `develop`
- Head: `feature/XX-nombre`

### 5. Actualizar ROADMAP

En el PR o antes de mergear, actualiza ROADMAP.md:

```
- [x] Tarea X
  - Status: Done
  - Assignee: @tuNombre
  - PR: #123
```

### 6. Mergear

Code review + approval → Squash & merge a develop

---

## 📦 Estructura de Repo

```
game2/
├── ROADMAP.md              ← Tracking vivo
├── CONTRIBUTING.md         ← Este archivo
├── Assets/
│   ├── Scripts/
│   ├── Scenes/
│   ├── Prefabs/
│   ├── Models/
│   ├── Audio/
│   └── Resources/
├── Documentación/          ← .md files (GDD, Arquitectura, etc.)
└── .gitignore
```

---

## 🎯 Checklist antes de PR

- [ ] Commits claros y específicos
- [ ] ROADMAP.md actualizado (Status: Review)
- [ ] Tests pasan (si hay)
- [ ] Sin conflictos con develop
- [ ] Documentación actualizada si corresponde

---

## 💬 Comunicación

- **Issues en GitHub** — qué hacer
- **ROADMAP.md** — quién lo hace, en qué estado
- **PRs** — cómo se hizo y por qué

---

## 🔗 Referencias

- Documentación: [GDD + Arquitectura](./Documentación/)
- Tracking: [ROADMAP.md](./ROADMAP.md)
- Repo: https://github.com/guiddodg/game2
