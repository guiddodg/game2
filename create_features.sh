#!/bin/bash

# Epic 1: Personajes
for feature in "Base" "Skin Tanque" "Skin Support" "Skin Pícaro" "Skin Mago" "Skin Guerrero" "Skin Invocador"; do
  gh issue create --title "Feature: $feature (Personajes)" --body "Epic parent: #1

## Subtasks
- [ ] Modelado
- [ ] Texturizado
- [ ] Rigging
- [ ] Setup Blender" 2>&1 | grep -o "issues/[0-9]*" | head -1
done
