# 2026-10-03 — Migración delta: Alessio Lusardi y sermón final

## Objetivo

Registrar el estado real en `develop` del material de Alessio Lusardi trabajado en incubación y evitar una migración duplicada o contradictoria.

Esta nota no propone insertar prosa nueva. Su función es indicar a Claude Code qué material ya existe en canon, qué decisiones quedaron resueltas y qué asuntos siguen abiertos.

---

## Contexto mínimo

Durante la incubación se trabajó la última conversación entre Alessio Lusardi y Chiara Bellandi como un sermón patriarcal en italiano.

La intención era que Alessio no sonara como un monstruo explosivo, sino como un hombre socialmente impecable y profundamente convencido de que matrimonio, tradición, apellido y fe le conceden autoridad sobre Chiara.

El sermón debía cerrarle todas las salidas hasta convertir la situación en una decisión de supervivencia: **él o ella**.

Antes de preparar esta migración se contrastó el material con la rama `develop`.

---

## Canon del autor ya presente en `develop`

### Muerte de Alessio

La ficha `02_Characters/Alessio_Lusardi.md` ya fija explícitamente que:

- Chiara mata a Alessio de un disparo.
- La versión antigua donde lo apuñalaba quedó supersedida.
- El arma es la pistola personal y personalizada de Alessio.
- Alessio la guardaba en el cajón derecho de su escritorio de estilo victoriano.
- No es la Beretta .25 que Chiara lleva posteriormente.

Por tanto, el conflicto anterior **“apuñalamiento vs. disparo” ya está resuelto en canon** y no debe volver a abrirse salvo decisión expresa posterior del autor.

---

### Idioma del sermón

La última conversación ya está registrada en la ficha de Alessio con:

- narración en español;
- diálogos completamente en italiano.

Esto coincide con la corrección del autor durante la incubación.

---

### Frase final

La ficha ya conserva como canon:

> **“Questo è un mandato divino. Dio lo sa. E anch'io.”**

La función fijada en el repo es que Alessio utiliza deliberadamente la fe de Chiara contra ella.

También existe una regla de contraste:

- Alessio instrumentaliza su fe para someterla.
- Kal puede bromear con la fe de Chiara, pero nunca la utiliza contra ella y respeta que forma parte de quien ella eligió ser.

---

### Naturaleza de Alessio

`develop` ya registra que Alessio:

- era impecable en público;
- socialmente parecía un marido perfectamente aceptable;
- se colocaba detrás de Chiara con las manos en sus hombros, funcionando como presencia que la mantenía contenida;
- ejerció humillaciones;
- ejerció negaciones;
- ejerció violencia física;
- no debe producir una lectura de “Chiara asesina”, sino de una mujer que aguantó hasta llegar a una situación sin salida.

---

### Los tres apellidos

La ficha de Chiara ya contiene la arquitectura:

- **Ardizzone** — lo que heredó.
- **Lusardi** — lo que otros intentaron convertirla en.
- **Bellandi** — lo que eligió ser.

El sermón de Alessio utiliza precisamente esa lucha identitaria: intenta decretar que el matrimonio invalida la autonomía que Chiara asocia a Bellandi y Ardizzone.

---

### Uso dentro de Libro I

La ficha actual establece que la escena completa **no se muestra en Libro I**.

En cambio:

- la frase del “mandato divino” aparece como recuerdo;
- en el Capítulo 25 Chiara le cuenta a Kal, en sus propias palabras, lo ocurrido;
- menciona la pistola del cajón;
- menciona que Alessio sostenía que ella no podía irse;
- menciona la frase religiosa;
- menciona el disparo.

No debe reemplazarse ese mecanismo por una analepsis completa sin decisión expresa del autor.

---

### Versión oficial

La ficha conserva que después de la muerte alguien construyó la versión que protegió a Chiara:

- Alessio fue encontrado muerto en su residencia;
- Chiara quedó fuera de la escena;
- informes y personas sostuvieron una versión compatible;
- el caso quedó formalmente cerrado;
- Il Consorzio habría tenido razones para intervenir si se conocía la verdad.

Permanece pendiente quién construyó esa versión.

Leone Valenti conserva su reacción:

> **“Qué lamentable.”**

La narración nunca debe resolver si Valenti creyó realmente la versión oficial.

---

## DISEÑO — función dramática del sermón

Aunque la prosa completa ya está almacenada en la ficha, la función estructural que debe preservarse es:

1. Alessio empieza sereno y razonable.
2. Habla desde convicción, no desde rabia.
3. Trata la autonomía de Chiara como una anomalía que él tiene derecho a corregir.
4. Convierte el matrimonio en jerarquía.
5. Convierte el apellido Lusardi en posesión.
6. Convierte la obediencia en obligación moral.
7. Convierte la fe en legitimación de esa autoridad.
8. Niega explícitamente que Chiara pueda marcharse.
9. Su propia formulación debe cerrar la salida pacífica.
10. Chiara dispara como ruptura de una ecuación donde Alessio ha declarado que mientras él exista ella no puede ser libre.

La fuerza del momento depende de que Alessio **no comprenda que acaba de formular su propia sentencia**.

---

## DISEÑO — tono

No convertir a Alessio en:

- villano gritón;
- caricatura de mafioso;
- hombre histérico;
- fanático religioso plano.

Debe conservar una cualidad:

- paternal;
- condescendiente;
- educada;
- doméstica;
- casi litúrgica.

Lo intolerable es que él cree sinceramente que su posición es normal, correcta y legítima.

---

## Restricción de migración

**No migrar ni reescribir el monólogo como nueva prosa para un capítulo.**

La ficha actual ya contiene una versión completa. Bajo las reglas vigentes de ChatGPT:

- ChatGPT no escribe prosa final destinada directamente a capítulos;
- cualquier nueva exploración debe tratarse como propuesta;
- Claude Code decide cualquier integración o reconciliación en el repo.

Esta nota sólo conserva función, intención y estado de canon.

---

## PENDIENTE

- Quién construyó la versión oficial que salvó a Chiara.
- Peso exacto de la famiglia Lusardi dentro de Il Consorzio.
- Si queda algún Lusardi que dude de la versión oficial.
- En qué punto futuro, si alguno, se muestra la escena completa más allá del relato de Chiara en Cap. 25.
- Detalles concretos de la violencia previa de Alessio: siguen siendo material delicado y no deben inventarse sólo para justificar retroactivamente el disparo.

---

## Preguntas para el autor

1. ¿Quieres que la escena completa del sermón permanezca sólo como material de ficha/reserva, mientras Libro I conserva únicamente el recuerdo y el relato del Cap. 25?
2. ¿El siguiente trabajo sobre Alessio debe centrarse en la famiglia Lusardi y la persona que construyó la versión oficial, o prefieres dejar ese vacío abierto?
