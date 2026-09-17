# 🎮 CYBER NEXUS 3D: OMEGA ASCENT

[![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas%202D%2F3D-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
[![Web Audio API](https://img.shields.io/badge/Audio-Web%20Audio%20API-blue.svg)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/Status-100%25%20Functional-brightgreen.svg)]()

> **Videojuego 2D/3D Arcade Espacial/Cyberpunk autónomo de nivel competitivo universitario.**
> Diseñado en un único archivo ejecutable (`index.html`) con física de proyectiles, renderizado 3D proyectado, sintetizador de audio procedimental por código y menú de selección de niveles (2 Mundos de 5 Niveles cada uno).

---

## 🌟 Descripción General y Lore

**CYBER NEXUS 3D: OMEGA ASCENT** coloca al jugador en el papel del **Comandante Kai Vane**, piloto del caza de vanguardia 3D *Plasma-Aegis*. En el año 2188, la superinteligencia artificial **OMEGA-9** ha tomado el control de la Estación Espacial Orbital (Sector Alfa) y está perforando las profundidades del Núcleo Cuántico (Sector Omega).

### 🚀 Características de Primer Lugar:
- **10 Niveles Progresivos en 2 Mundos Distintos**:
  - *Mundo 1: Sector Alfa (Estación Espacial, Niveles 1–5)*: Drones asesinos, Crawlers, trampas de ácido y el jefe centinela **MECHA-HYDRA 5000** (Nivel 1-5).
  - *Mundo 2: Sector Omega (Núcleo Cuántico, Niveles 6–10)*: Bioma biomecánico, campos de asteroides 3D, portales de fase, láseres intermitentes y el Gran Jefe Final **OMEGA-9 OVERLORD** (Nivel 2-5 / Nivel 10).
- **Menú de Selección de Niveles**: Permite seleccionar libremente cualquiera de los 10 sectores en los 2 mundos.
- **Game Juice y Efectos Visuales 3D**:
  - **Motor 3D Proyectado**: Renderizado en perspectiva tridimensional $(X, Y, Z)$ para la nave del jugador y asteroides con inclinación dinámica (*Pitch, Yaw, Roll*).
  - **Screen Shake Engine**: Sacudida reactiva de pantalla en explosiones e impactos EMP.
  - **Sistema de Partículas**: Estelas de motor, chispas de plasma y fragmentación de asteroides.
- **Armas Especiales & Modificadores**:
  - **Destructor Beam (Láser continuo)**: Rayo de energía masiva que arrasa con enemigos.
  - **Bomba EMP Masiva**: Destrucción total de proyectiles y daño masivo.
  - **Modo BERSERK (Combo $\ge 4x$)**: Aura de fuego rojo, doble cadencia de tiro y disparos multiplicados.
  - **Bullet Time (Slo-Mo)**: Ralentiza el tiempo a 0.35x para esquivar ráfagas mortales con `SHIFT`.
- **Sintetizador Web Audio API Procedural**: Música Synthwave en tiempo real y efectos SFX sintetizados matemáticamente por código.

---

## 🌐 Publicación en GitHub Pages (Guía Paso a Paso)

Para publicar el juego usando tu repositorio oficial de GitHub:

1. Crea o usa el repositorio público en GitHub: `https://github.com/joseortiz20011/CyberNexus3D`
2. Inicializa git y sube tus archivos:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: CYBER NEXUS 3D"
   git branch -M main
   git remote add origin https://github.com/joseortiz20011/CyberNexus3D.git
   git push -u origin main
   ```
3. En GitHub, ve a **Settings** ➔ **Pages**.
4. En la sección **Source**, selecciona `Deploy from a branch`, elige la rama `main` / `/ (root)` y haz clic en **Save**.
5. Tu juego estará disponible públicamente en la URL:
   `https://joseortiz20011.github.io/CyberNexus3D/`

---

## ⌨️ Guía de Controles

| Acción | Control Teclado / Mouse |
| :--- | :--- |
| **Mover Nave 3D** | `W`, `A`, `S`, `D` o Flechas Direccionales |
| **Apuntar** | Movimiento del Mouse |
| **Disparo de Plasma / Láser** | Mantener Clic Izquierdo del Mouse |
| **Bomba EMP Masiva** | `Barra Espaciadora` o Clic Derecho |
| **Tiempo Lento (Bullet Time)** | Mantener `SHIFT` (Consume barra Slo-Mo) |
| **Pausar Misión** | `ESC` o Tecla `P` |

---

## 📄 Licencia

Hecho por José Ortiz 12vo PRG.
Dios los bendiga
