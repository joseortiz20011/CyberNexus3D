# INFORME TÉCNICO DE DESARROLLO DE VIDEOJUEGO
## CYBER NEXUS 3D: OMEGA ASCENT

---

### **PORTADA FORMATO UNIVERSITARIO**

* **INSTITUCIÓN**: Instituto Tecnológico de Excelencia Educativa (ITEE)
* **CARRERA**: Informática orientada en la programación
* **ASIGNATURA**: Programación de IA
* **DESARROLLADOR**: **José Ortiz (12vo PRG)**
* **DOCENTE**: Ing. Miklos Szabo
* **FECHA DE ENTREGA**: 16 de Septiembre de 2026
* **CIUDAD**: San Pedro Sula, Cortés, Honduras

---

## 1. ENLACES DEL PROYECTO (GITHUB Y YOUTUBE)

| Recurso | Descripción / Estado | Enlace URL |
| :--- | :--- | :--- |
| **Repositorio GitHub** | Código fuente completo, historial de commits y assets | `https://github.com/joseortiz20011/CyberNexus3D` |
| **Video Demostración (YouTube)** | Gameplay guiado, explicación del sonido y mecánicas de niveles | `https://youtu.be/bYw_tB775yw` |
| **Página Web en Vivo (GitHub Pages)** | Juego ejecutable desplegado en navegador web | `https://joseortiz20011.github.io/CyberNexus3D` |

---

## 2. TECNOLOGÍAS UTILIZADAS Y PLATAFORMA

Para este proyecto, mi objetivo principal fue construir un juego completo, vistoso y adictivo en un **único archivo ejecutable autónomo (`index.html`)**, capaz de ejecutarse de forma inmediata en cualquier navegador web moderno sin necesidad de instalar dependencias, configurar servidores locales ni descargar archivos multimedia externos.

* **Plataforma Objetivo**: Navegadores Web para PC y Escritorio (Google Chrome, Microsoft Edge, Mozilla Firefox, Brave y Safari).
* **HTML5 Canvas 2D / 3D proyectado**: Utilicé el elemento Canvas para renderizar todos los gráficos en tiempo real a 60 FPS. En lugar de utilizar motores externos pesados, implementé matemática de proyección 3D propia sobre el contexto 2D. Esto me permitió renderizar la nave espacial, los asteroides tridimensionales, los disparos de plasma y los jefes finales con sombras, rotación en 3 ejes (*Pitch, Yaw, Roll*) y perspectiva en profundidad.
* **JavaScript Vainilla (ES6+)**: Toda la lógica del juego, el motor de físicas, la detección de colisiones por distancia vectorial, la gestión de estados (Menú Principal, Selección de Niveles, Tienda Cyber, Gameplay y Game Over) y el spawner de enemigos fueron programados desde cero en JavaScript sin librerías externas.
* **Web Audio API de JavaScript**: Para evitar la dependencia de archivos `.mp3` o `.wav` externos, programé un sintetizador procedimental por código utilizando osciladores y nodos de ganancia en tiempo real. Esto me permitió crear 3 pistas de música totalmente distintas (Menú Principal, Partida y Tienda Cyber), además de sintetizar los efectos de sonido para disparos, explosiones, impactos y compras.
* **CSS3 Vanilla & Google Fonts**: Diseñé la interfaz gráfica del menú, la tienda y la barra de estado superior con un estilo Cyberpunk moderno, utilizando tipografías de Google Fonts (Orbitron y Rajdhani), efectos de brillo neón (*glow*) y animaciones fluidas.

---

## 3. RETOS TÉCNICOS RESUELTOS

Durante el proceso de desarrollo me enfrenté a varios desafíos complejos de programación y diseño que requerían soluciones creativas:

1. **Simulación 3D en un Canvas 2D sin librerías externas**:
   El reto principal fue lograr que los objetos se sintieran verdaderamente tridimensionales dentro de una pantalla plana. Lo resolví implementando ecuaciones de proyección perspectiva basándome en la distancia focal (FOV) y la profundidad en el eje Z:
   $$X' = X \cdot \frac{\text{FOV}}{\text{FOV} + Z + 300}, \quad Y' = Y \cdot \frac{\text{FOV}}{\text{FOV} + Z + 300}$$
   Esto me permitió calcular las coordenadas bidimensionales de cada vértice de la nave y los asteroides en tiempo real al aplicar rotaciones vectoriales en tres ejes.

2. **Creación de un Sintetizador de Música Tri-pista con Web Audio API**:
   Sintetizar música envolvente mediante código fue un reto exigente. Tuve que definir estructuras de secuencias de notas y tempos en arreglos de JavaScript. Para evitar la monotonía y hacer la experiencia atractiva, programé tres melodías totalmente distintas (Menú relajante, Partida estilo synthwave rápido y Tienda cyber-lounge) y ajusté el volumen global para que la música se escuchara potente y clara.

3. **Limpieza de Pantalla y Control del Spawner entre Niveles**:
   En las primeras pruebas, al avanzar de nivel los enemigos del nivel anterior quedaban flotando en pantalla, creando un desorden visual que impedía jugar normalmente. Resolví este problema rediseñando el ciclo de vida del juego e implementando la función `resetLevelState()`, la cual limpia de forma estricta los arreglos de proyectiles, partículas y oleadas antes de inicializar el nuevo sector.

4. **Diseño Visual "Super Animaciones" sin Saturar el Rendimiento**:
   Para cumplir la exigencia de gráficos avanzados sin provocar caídas de frames ni saturación en pantalla, creé un sistema de partículas graduadas con tiempos de vida de desvanecimiento suave (*alpha fade-out*), rastros de luz neón y sombras proyectadas. Esto mantiene la pantalla limpia y permite jugar de forma fluida.

5. **Sistema de 2 Mundos, 10 Niveles y Menú de Selección**:
   Para darle una estructura académica y comercial al juego, dividí la campaña en dos mundos temáticos (Mundo 1: Estación Espacial con el Jefe MECHA-HYDRA 5000 en el Nivel 5; y Mundo 2: Núcleo Cuántico con el Gran Jefe Final OMEGA-9 OVERLORD en el Nivel 10). Implementé un Menú de Selección de Niveles interactivo para que el jugador sepa siempre en qué mundo y nivel se encuentra.

---

## 4. LECCIONES APRENDIDAS

El desarrollo de este proyecto me dejó valiosas lecciones tanto técnicas como de disciplina de trabajo:

* **El valor del "Game Juice" y la experiencia de usuario**: Aprendí que un buen videojuego no depende solo de que el código funcione, sino de los pequeños detalles visuales y auditivos: el sonido de los impactos, la vibración suave, los colores neón y el balance del volumen cambian por completo la sensación de juego.
* **Uso efectivo de la Inteligencia Artificial como copiloto**: Trabajar junto a la IA me enseñó a formular preguntas precisas, iterar sobre la marcha y resolver problemas de lógica de forma rápida. La IA no sustituye el criterio del programador, sino que multiplica su productividad y capacidad de aprendizaje.
* **Matemática y geometría aplicada a la programación**: Comprendí cómo conceptos matemáticos de proyección, trigonometría y álgebra de vectores se aplican de forma práctica e inmediata para crear movimiento y profundidad en pantalla.
* **Organización y arquitectura de código autónomo**: Mantener más de 1,500 líneas de código limpias y funcionales dentro de un único archivo `index.html` me obligó a ser riguroso con la modularidad de las funciones y el manejo de estados.

---

## 5. CONCLUSIONES

1. El proyecto *CyberNexus 3D* demuestra que es posible desarrollar videojuegos modernos, llamativos e interactivos con tecnologías web estándar (HTML5, JavaScript y Web Audio API) en un único archivo autónomo, alcanzando un nivel de calidad cercano a motores comerciales.
2. La asistencia de herramientas de Inteligencia Artificial fue clave para resolver retos de sintaxis, sintetizar el audio procedimental y optimizar el rendimiento, demostrando que **usar la IA es lo mejor** cuando se utiliza de manera responsable para potenciar el aprendizaje académico.
3. El juego cumple al 100% con los requerimientos asignados, ofreciendo 10 niveles, 2 mundos temáticos, 2 jefes finales, tienda de mejoras, menú de niveles y 3 pistas de música dinámicas.
4. Trabajo realizado con dedicación por **José Ortiz (12vo PRG)**. ¡Dios los bendiga!
