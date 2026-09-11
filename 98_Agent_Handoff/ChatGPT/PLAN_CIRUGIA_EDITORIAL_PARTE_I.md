# PLAN DE CIRUGÍA EDITORIAL — PARTE I  
## Seda y Pólvora

**Repositorio:** `XxZylivrar360xX/silk---gunpowder`  
**Branch operativa:** `develop`  
**Alcance:** capítulos actuales 01–29 del Libro I  
**Modo de trabajo:** ejecución por bloques. **NO intentar resolver este documento completo en un solo turno ni en un solo commit.**

---

# 0. PROPÓSITO DEL ENCARGO

Este documento no pide una reescritura general de la novela.

Pide ejecutar una **cirugía estructural controlada** sobre los capítulos ya existentes para:

- reducir redundancias;
- concentrar funciones narrativas;
- fusionar capítulos cuando dos recipientes pertenecen al mismo movimiento dramático;
- migrar beats útiles antes de eliminar recipientes débiles;
- preservar voz, canon, intimidad, ritmo y causalidad;
- aumentar la cantidad de transformación narrativa por capítulo;
- hacer que romance, poder, territorio y peligro se afecten mutuamente con mayor frecuencia.

El objetivo NO es alcanzar un número determinado de palabras.

El objetivo es que cada capítulo tenga una razón clara para existir.

---

# 1. REGLA ABSOLUTA DE EJECUCIÓN

## NO EJECUTAR TODO ESTE PLAN DE UNA SOLA VEZ

Claude debe trabajar en **operaciones separadas**.

Después de cada operación:

1. revisar diff;
2. resumir qué cambió;
3. enumerar qué material se movió;
4. enumerar qué material se eliminó;
5. identificar cualquier duda o desviación respecto a este documento;
6. detenerse.

No continuar automáticamente con la siguiente cirugía.

Cada bloque debe poder revisarse y revertirse independientemente.

---

# 2. ORDEN DE LECTURA OBLIGATORIO ANTES DE TOCAR PROSA

Antes de cualquier modificación:

1. `AGENTS.md`
2. `CLAUDE.md`
3. `12_Craft_Policies/editorial/DO_NOT_TOUCH.md`
4. `12_Craft_Policies/editorial/EDITORIAL_POLICY.md`
5. `12_Craft_Policies/Redaccion_De_Capitulos.md`
6. reglas de voz de personajes involucrados;
7. archivos de revelaciones/hitos correspondientes;
8. capítulos específicos que van a intervenirse;
9. capítulo inmediatamente anterior y posterior al bloque afectado.

Para la relación Cole–Chiara consultar además, según necesidad:

- `06_Relationships/Cole_y_Chiara.md`
- `06_Relationships/Hitos.md`
- `06_Relationships/Momentos_de_Fractura.md`

Cuando haya conflicto entre una inferencia del agente y canon explícito del autor, gana el canon.

---

# 3. FUENTE OPERATIVA

Trabajar exclusivamente sobre:

`develop`

No usar `main` como referencia de continuidad.

No reconstruir el libro desde copias antiguas de `99_Reference`.

Los archivos dentro de `99_Reference/catchup-*` son material histórico de referencia, no fuente operativa cuando `develop` contiene una versión más nueva.

---

# 4. IMPORTANTE — CAPÍTULO 26 ACTUAL

La versión vigente de:

`26_Libros_Abiertos.md`

es considerablemente más desarrollada que versiones anteriores.

Debe tratarse como:

> **PROTEGER ESTRUCTURALMENTE / MICROEDITAR ÚNICAMENTE**

No fusionar.

No mover.

No canibalizar.

No reducir su función.

No eliminar revelaciones nuevas.

El capítulo actual ejecuta H15 completo y contiene, entre otras piezas:

- compra/juego del Lancia;
- jacuzzi;
- Il Consorzio nombrado;
- situación de Corrado desde el conocimiento de Chiara;
- Marta;
- Ruth;
- pasado militar de Cole;
- Nadir;
- cicatriz;
- niños;
- prisión;
- pregunta pendiente del golf;
- Michael;
- deseo de Chiara de hablar con Corrado;
- siembra Dario/Cole.

Función dramática actual:

> **Ambos eligen entregarse verdades que antes utilizaban para sobrevivir, justo antes de que las verdades que todavía retienen empiecen a cobrarles factura.**

La relación C26 → C27 → C28 → C29 debe preservarse cuidadosamente.

---

# 5. PRINCIPIO EDITORIAL CENTRAL

La revisión debe mejorar esta progresión:

> encuentro → elección → costumbre → colisión → hogar → conocimiento → defecto → presión → poder → elección consciente → intimidad → poder compartido → capital → verdad → factura

No convertir Parte I simplemente en una historia romántica más rápida.

No acelerar artificialmente el slow burn.

No eliminar escenas civiles sólo porque no contienen crimen.

La novela necesita seda y pólvora.

El objetivo es que progresivamente:

> **cada acto de intimidad pueda producir consecuencias materiales y cada movimiento de poder pueda producir consecuencias íntimas.**

---

# 6. CLASIFICACIÓN DE OPERACIONES

Cada fragmento revisado debe recibir una de estas cuatro etiquetas internas:

## CONSERVAR

El beat sigue siendo necesario en esa posición.

Puede recibir microedición, pero no debe perder su función.

---

## MOVER

El beat es necesario, pero funciona mejor dentro de otro capítulo.

Moverlo antes de eliminar el recipiente original.

---

## FUSIONAR

Dos beats ejecutan esencialmente la misma función.

Crear un único beat que conserve:

- información nueva;
- transformación;
- voz;
- consecuencia.

No sumar dos escenas completas una detrás de otra y llamarlo merge.

---

## CORTAR

Sólo permitido cuando:

- otro beat ya cumple mejor la misma función;
- no se pierde información futura;
- no se pierde canon;
- no se rompe causalidad;
- no se rompe ritmo emocional;
- no se elimina una pieza protegida.

Ante duda:

> NO CORTAR.

---

# 7. CRITERIO FUNDAMENTAL: ESTADO ANTES → ESTADO DESPUÉS

Para cada capítulo intervenido Claude debe identificar:

**Estado antes:** qué es cierto al entrar.

**Estado después:** qué ya no puede volver a ser igual al salir.

Si ambos estados son prácticamente idénticos, investigar:

- poda;
- merge;
- migración;
- canibalización.

Si existe un cambio irreversible claro, preservar la columna vertebral del capítulo.

---

# 8. FASES DE EJECUCIÓN

---

# BLOQUE 0 — PREPARACIÓN Y CONGELAMIENTO

## Objetivo

Preparar la cirugía sin alterar prosa todavía.

## Acciones

- confirmar branch `develop`;
- registrar HEAD actual;
- inspeccionar `git status`;
- no tocar archivos con cambios locales no relacionados;
- generar una lista de capítulos 01–29 con tamaño aproximado;
- confirmar que C26 vigente es la versión nueva;
- no renumerar nada;
- no regenerar EPUB.

## Entregable

Reporte corto:

```md
## Estado previo a cirugía

Branch:
HEAD:
Working tree:
Capítulos detectados:
Archivos protegidos:
Riesgos:
```

Después detenerse.

---

# BLOQUE 1 — APERTURA: C01–C03

## Tipo

**PODA + MIGRACIÓN**

No merge.

## Objetivo

Mantener tres capítulos diferenciados, pero reducir carga de instalación.

### C01 debe seguir siendo:
Cole.

### C02 debe seguir siendo:
Chiara.

### C03 debe seguir siendo:
San Aurelio empezando a conectar sus mundos.

## Buscar específicamente

Material que:

- demuestra por segunda o tercera vez que Cole es competente;
- explica una capacidad que luego vemos ejecutada;
- presenta demasiado pronto información que puede revelarse cuando tenga consecuencia;
- presenta secundarios antes de que tengan función;
- explica el pasado en bloques cuando después existe una escena mejor para hacerlo;
- repite que Chiara lee habitaciones/personas;
- repite que ambos tienen pasado pesado.

## NO eliminar

- identidad de La Almendra;
- carta de Walt;
- Nadir;
- Héctor;
- Almendra Towing;
- Peugeot;
- Monarch;
- llegada de Chiara;
- Dario;
- Tommaso;
- encuentro Cole–Chiara;
- cualquier semilla con payoff futuro.

## Método

Antes de cortar una pieza preguntar:

> ¿El lector necesita saber esto antes de C04?

Si no:

- considerar MOVER;
- o eliminar sólo si otra escena posterior ya lo demuestra mejor.

## Final del bloque

Entregar:

- palabras aproximadas antes/después;
- lista de migraciones;
- lista de cortes;
- escenas protegidas;
- riesgos detectados.

Detenerse.

---

# BLOQUE 2 — C05 + C06

## Tipo

**MERGE RECOMENDADO**

### Archivos

- `05_La_Casa_No_Quiere_Ruido.md`
- `06_Una_Amiga.md`

## Transformación buscada

**Antes:**

> Cole y Chiara se relacionan porque circunstancias externas los juntan.

**Después:**

> Deciden pasar tiempo juntos porque quieren.

## Beats a proteger

De C05:

- entrada progresiva de Chiara al territorio de Cole;
- reciprocidad práctica;
- cualquier beat que demuestre que ya no es una extraña funcional.

De C06:

- Rocco;
- no-cita;
- tiempo voluntario juntos;
- cuidado sin verbalización;
- Cole esperando a verla entrar.

## Arquitectura deseada

Idealmente:

> obligación / circunstancia  
> → comodidad  
> → elección personal  
> → primera no-cita  
> → gesto final de cuidado.

## Prohibiciones

- no acelerar atracción;
- no convertir la escena en cita romántica consciente;
- no añadir confesiones;
- no eliminar Rocco;
- no volver demasiado evidente que ambos ya están enamorados.

## Archivo resultante

No renumerar todavía.

Claude puede proponer nombre de recipiente, pero no ejecutar renumeración global.

## Final

Mostrar diff conceptual y detenerse.

---

# BLOQUE 3 — C07 / C09

## Tipo

**PODA + CANIBALIZACIÓN CONDICIONAL**

### Archivos

- `07_Ambos.md`
- `09_La_Carrera_De_Mascaras.md`

## C07 debe preservar

- nacimiento de costumbre;
- lenguaje privado;
- comodidad mutua;
- transición hacia un “nosotros” funcional.

## C09 debe preservar

- Il Gelsomino;
- juego;
- carrera / máscaras;
- recuerdo compartido sin utilidad práctica;
- objeto que permanece;
- deseo de repetir una pésima idea.

## Problema actual

Ambos capítulos pueden reiterar:

- ya se entienden;
- les gusta pasar tiempo juntos;
- ya existe rutina;
- pueden bajar la guardia.

## Objetivo

No destruir la fase juguetona.

Pero reducir confirmaciones redundantes.

C09 puede perder autonomía **sólo si todos sus beats únicos reciben un hogar claramente mejor**.

No eliminar el archivo antes de completar la migración.

## Transformación buscada

> Ya disfrutan juntos  
> → ya construyeron lenguaje privado, juego y recuerdos que no sirven para sobrevivir.

## Final

Claude debe recomendar:

- `MANTENER C09`;
- `REDUCIR C09`;
- o `CANIBALIZAR C09`.

No borrar automáticamente.

Detenerse para decisión del autor.

---

# BLOQUE 4 — C11 + C16

## Tipo

**REESTRUCTURACIÓN / ABSORCIÓN PARCIAL**

### Archivos

- `11_El_Loft_Del_Soltero.md`
- `16_El_Porton.md`

## Idea estructural

C11 muestra:

> Cole y Chiara empiezan a construir inadvertidamente un hogar.

C16 aporta:

> Nadir observa el costo y desplazamiento producido por ese cambio.

## Objetivo

Convertir ambas funciones en una unidad más compleja:

> **Toda casa nueva ocupa espacio que antes pertenecía a otra cosa.**

## Proteger de C11

- elección/búsqueda/construcción del loft;
- objetos de Chiara;
- decisiones de espacio;
- sensación de hogar involuntario;
- cambios que Cole todavía no nombra.

## Proteger de C16

- perspectiva legítima de Nadir;
- percepción del cambio;
- costo comunitario;
- fricción real;
- afecto y derecho de Nadir a disentir.

## Prohibición crítica

Nadir NO debe convertirse en:

- celoso;
- posesivo;
- resentido por romance;
- obstáculo artificial;
- caricatura del amigo desplazado.

Su función es:

> poder amar a Cole y aun así decir que ciertas decisiones tienen consecuencias.

## Método

C11 puede absorber beats de C16.

No necesariamente todo C16.

Después evaluar si queda suficiente función independiente para que C16 exista.

## Final

Indicar:

- qué se movió;
- qué quedó;
- si C16 conserva razón independiente para existir.

Detenerse.

---

# BLOQUE 5 — C12–C14

## Tipo

**PODA + REORDENAMIENTO**

NO merge automático.

### Archivos

- `12_El_Farol.md`
- `13_Roma_Atrii.md`
- `14_Auster.md`

## Funciones que deben preservarse

### C12

> Chiara descubre al Cole anterior a ella mediante otras personas y su comunidad.

Proteger:

- Walt;
- Mabel;
- valor de testigos externos;
- pasado humano de Cole.

### C13

> Cole descubre la maquinaria propia de Chiara.

Proteger:

- Roma Atrii;
- red;
- inteligencia operativa;
- agencia propia de Chiara.

### C14

> La maquinaria de Chiara empieza a emplearse directamente a favor de Cole.

Proteger:

- investigación;
- cobertura;
- protección;
- integración de Cole dentro de “su gente”.

## Progresión buscada

> conocer  
> → descubrir capacidad  
> → usar esa capacidad por el otro.

## Riesgo

Los tres capítulos usan investigación/información.

Eso no significa que tengan la misma función.

Primero podar redundancia.

Después evaluar si alguno perdió autonomía.

## Final

Claude debe entregar recomendación estructural.

No fusionar salvo que la función de dos capítulos resulte realmente inseparable después de la poda.

Detenerse.

---

# BLOQUE 6 — C15

## Tipo

**PROTEGER / PODA INTERNA**

### Archivo

`15_La_Regla_Del_Telefono.md`

## Función

Capítulo de tesis temática.

## Elementos protegidos

- Marisol;
- campamento;
- intento de desconexión;
- ausencia de Cole durante la crisis de Héctor;
- hospital;
- Héctor y Chiara;
- Héctor y Cole;
- línea:

> “No es tuyo decidir de qué la cuidas. Es de ella.”

Esa línea es estructural.

## Objetivo

Reducir repeticiones de:

- Cole cuida a todo el mundo;
- Cole no sabe desconectarse;
- Marisol lo conoce muy bien;

sin adelgazar tanto el campamento que el contraste con el hospital deje de funcionar.

## Final

Microedición únicamente.

Detenerse.

---

# BLOQUE 7 — C17

## Tipo

**AUDITORÍA DE PAYOFF**

### Archivo

`17_El_Sobre_Rojo.md`

## Pregunta

¿Qué hilo exacto abre?

¿Dónde cobra consecuencia?

¿La amenaza modifica conducta, información o estructura suficientemente pronto?

## Decisión posible

- CONSERVAR;
- REDUCIR;
- MIGRAR;
- o integrar su detonante a otro capítulo.

## Prohibición

No cortar una amenaza sólo porque no explota inmediatamente.

Primero revisar roadmap, revelaciones y payoffs futuros.

## Final

Entregar diagnóstico.

No modificar estructuralmente sin certeza.

Detenerse.

---

# BLOQUE 8 — C18 + C20

## Tipo

**MERGE RECOMENDADO**

### Archivos

- `18_Cuentas_Claras.md`
- `20_Tierra_Buena.md`

## Idea central

Ambos capítulos son parte del mismo fenómeno:

> Cole deja de tener únicamente gente y negocios y empieza a necesitar reglas, infraestructura y territorio.

## Proteger de C18

- consecuencia de decisiones de la red;
- negociación;
- necesidad de reglas;
- autoridad;
- “avísenme aunque vaya a decir que no” o equivalente funcional;
- transición de amistad a gobernanza.

## Proteger de C20

- compra de terreno;
- Harper;
- infraestructura productiva;
- conexión con Il Gelsomino;
- expansión real.

## Transformación

**Antes:**

> Cole tiene personas y operaciones dispersas.

**Después:**

> Cole empieza a tener sistema y territorio.

## Prohibición crítica

No hacer que Cole declare:

> “voy a fundar El Patio”.

El Patio debe emerger.

No ser una startup criminal consciente.

## Final

Mostrar nueva arquitectura.

Detenerse.

---

# BLOQUE 9 — C19

## Tipo

**PROTEGER / MICROEDITAR**

### Archivo

`19_El_Dia_Nublado.md`

## Función

Bisagra moral.

Chiara ofrece una salida.

Cole conoce suficiente peligro.

Cole decide quedarse.

## Regla

No reducir el espacio emocional necesario.

Podar únicamente:

- explicaciones posteriores a gestos que ya funcionan;
- reiteraciones de lo que ya dijo el diálogo.

## Estado

**Antes:** Cole todavía puede decir que no sabía.

**Después:** sabe suficiente y elige quedarse.

Detenerse.

---

# BLOQUE 10 — C21

## Tipo

**PROTEGER**

### Archivo

`21_El_Mirador.md`

## Proteger

- bolera;
- juego;
- drift;
- mirador;
- Dale y Ruth;
- penthouse;
- música;
- baile;
- beso;
- intimidad.

Es payoff de un slow burn largo.

No fusionar.

No apresurar.

No convertir en montaje.

Sólo microedición si existe redundancia obvia.

Detenerse.

---

# BLOQUE 11 — C22 + C23

## Tipo

**MERGE FUERTE**

### Archivos

- `22_La_Promesa.md`
- `23_Sin_Rastro.md`

## Concepto estructural

Ésta debe ser una miniatura del funcionamiento completo de Seda y Pólvora:

> **Una promesa íntima produce una consecuencia criminal.**

## Proteger de C22

- llamada nocturna;
- Marisol;
- reacción inmediata de Cole;
- Chiara entendiendo qué significa “llámame”;
- promesa.

## Proteger de C23

- “Tengo un problema. Necesito que sea tuyo” o función equivalente;
- solución rápida;
- activación de la red;
- desaparición del problema;
- Dario detectando la anomalía / variación.

## Arquitectura

> alguien de Cole necesita ayuda  
> → Chiara presencia cómo responde  
> → tiempo suficiente  
> → Chiara usa esa misma promesa  
> → Cole mueve la ciudad  
> → Dario ve la huella.

## Riesgo

No eliminar todo espacio temporal entre ambos hechos.

La promesa debe existir antes de cobrarse.

## Transformación

**Antes:** “puedes llamarme” es intimidad.

**Después:** esa intimidad ya produce poder observable.

## Final

Detenerse.

---

# BLOQUE 12 — C24 + C25

## Tipo

**MERGE A PRUEBA**

### Archivos

- `24_La_Letra_Pequena.md`
- `25_Bajo_Juramento.md`

## Función conjunta posible

> vulnerabilidad contractual  
> → estrategia  
> → tribunal  
> → propiedad formal.

## Proteger

- problema Villani;
- Garrett;
- Rivers;
- conflicto legal;
- juicio;
- resolución;
- participación formal de Cole.

## Riesgo

No crear un capítulo saturado de exposición jurídica.

## Método

Primero crear una maqueta estructural.

No eliminar archivos originales hasta verificar que el merge fluye.

## Transformación

**Antes:** Cole sabe operar alrededor del capital.

**Después:** Cole posee capital formalmente.

## Si el capítulo resultante se vuelve demasiado pesado

Mantener dos capítulos.

No forzar el merge sólo porque aparece en este plan.

## Final

Presentar resultado y recomendación.

Detenerse.

---

# BLOQUE 13 — C26

## Tipo

**CONGELADO ESTRUCTURALMENTE**

### Archivo

`26_Libros_Abiertos.md`

No fusionar.

No mover.

No reordenar.

Sólo detectar:

- repetición léxica;
- sobreexplicación obvia;
- pequeño eco innecesario.

No ejecutar cortes importantes sin autorización expresa.

Función:

> **Intimidad mediante la verdad.**

Estado después:

> ambos han probado que sí pueden abrirse voluntariamente.

Esto es esencial para que después quede claro que el ocultamiento de Cole no nace de incapacidad emocional sino de una elección:

> cree que él puede decidir qué verdad Chiara debe soportar.

Detenerse.

---

# BLOQUE 14 — C27–C29

## Tipo

**NO CIRUGÍA ESTRUCTURAL**

### Archivos

- `27_Me_Encuentro_Bien.md`
- `28_Riesgo_Pendiente.md`
- `29_La_Correa.md`

Estos capítulos ya muestran el tipo de causalidad que el resto de la revisión intenta alcanzar.

## Progresión

C27:

> Chiara comprende que Varek la considera una pieza utilizable.

C28:

> Halbrook deja de pertenecer al pasado y puede controlar el presente de Cole.

C29:

> las dos amenazas colisionan y Cole rompe estrategia.

## Regla

No merge.

No reordenar.

No cambiar POV estructural.

Sólo microedición posterior, después de toda la cirugía de Parte I.

---

# 9. FASE POSTOPERATORIA

NO iniciar hasta completar los bloques estructurales aprobados.

Después de la cirugía:

leer Parte I completa de corrido.

No capítulo por capítulo aislado.

Buscar:

- suturas visibles;
- personajes que aparecen sin preparación;
- referencias a capítulos eliminados;
- saltos temporales abruptos;
- emociones repetidas;
- objetos que aparecen antes de introducirse;
- información que quedó sin fuente;
- payoffs cuya preparación fue cortada;
- ritmo demasiado acelerado;
- ritmo todavía estancado;
- exceso de transición;
- ausencia prolongada de amenaza externa;
- pérdida de San Aurelio como presencia.

---

# 10. NO RENUMERAR HASTA EL FINAL

Durante toda esta cirugía usar numeración actual como identificadores históricos.

Ejemplo:

- C05+C06;
- C11←C16;
- C18+C20.

No hacer renumeración global mientras las decisiones sigan abiertas.

Sólo renumerar cuando:

- todos los merges estén aprobados;
- todos los recipientes supervivientes sean definitivos;
- se haya hecho una lectura postoperatoria.

Después actualizar:

- Book Map;
- Cadena de Eventos;
- Hitos;
- índices;
- enlaces internos;
- handoffs;
- cualquier referencia numérica afectada.

---

# 11. NO REGENERAR EPUB DURANTE LA CIRUGÍA

No reconstruir EPUB tras cada operación.

La regeneración sólo debe ocurrir cuando:

- el autor lo pida explícitamente;
- o quede cerrada una etapa completa de revisión.

---

# 12. COMMITS

Preferencia:

una operación quirúrgica por commit.

Ejemplos:

```text
edit(part1): trim opening chapters 01-03
edit(part1): merge chapters 05 and 06
edit(part1): compress routine arc 07-09
edit(part1): integrate Nadir perspective into loft arc
edit(part1): tighten investigation arc 12-14
edit(part1): merge governance and territory beats
edit(part1): merge promise and first payoff
edit(part1): test Villani legal arc merge
```

No mezclar en el mismo commit:

- C01–03;
- C05–06;
- C11–16;
- C18–20;

etc.

Cada cirugía debe poder revertirse por separado.

---

# 13. REPORTE OBLIGATORIO DESPUÉS DE CADA BLOQUE

Usar este formato:

```md
# REPORTE DE CIRUGÍA — BLOQUE X

## Archivos tocados

- ...

## Estado antes

...

## Estado después

...

## Beats conservados

- ...

## Beats movidos

- origen:
- destino:
- razón:

## Beats fusionados

- ...

## Material cortado

- ...
- razón narrativa:

## Canon protegido

- ...

## Riesgos o dudas

- ...

## Conteo aproximado

Antes:
Después:
Variación:

## Evaluación

- ¿Existe transformación clara?
- ¿Se perdió información futura?
- ¿Se aceleró demasiado la relación?
- ¿Se debilitó algún secundario?
- ¿Se debilitó San Aurelio?
- ¿Se rompió algún payoff?
- ¿El capítulo resultante tiene mejor razón para existir?

## Siguiente paso recomendado

...
```

Y detenerse.

---

# 14. PROHIBICIONES GENERALES

Claude NO debe:

- inventar escenas nuevas para “rellenar” merges salvo microcosturas;
- cambiar canon sin autorización;
- eliminar diálogos canon;
- reescribir completamente la voz del libro;
- suavizar moralmente a Cole;
- volver pasiva a Chiara;
- convertir a Nadir en celoso;
- hacer que Dario explique demasiado;
- adelantar revelaciones de Corrado;
- revelar el origen de Cole antes del momento correspondiente;
- nombrar a Anya antes de donde corresponda;
- explicar cada símbolo;
- eliminar silencios útiles;
- transformar toda ambigüedad en exposición;
- forzar todos los merges aquí propuestos;
- renumerar antes de cerrar cirugía;
- reconstruir EPUB;
- intentar todo este documento en un solo turno.

---

# 15. PRINCIPIOS DE VOZ

## Cole

Su afecto suele aparecer como:

- acción;
- resolución;
- objeto;
- protección;
- logística;
- presencia.

Evitar que verbalice demasiado pronto aquello que normalmente demuestra.

---

## Chiara

Su afecto suele aparecer como:

- elección;
- lectura precisa;
- presencia;
- decisión;
- abrir acceso;
- intervenir directamente.

No reducirla a “mujer preocupada por Cole”.

Debe seguir generando trama.

---

## Nadir

Debe poder decir:

> entiendo por qué lo hiciste y aun así estuvo mal.

Su función no es impedir la relación.

Es mostrar costo, historia y límites.

---

## Dario

No explica lo que piensa.

Declara decisiones.

---

# 16. OBJETIVO DE PODA

No existe cuota obligatoria.

La versión actual ronda aproximadamente las 90k palabras para los capítulos disponibles.

Un resultado de aproximadamente 78–84k puede ser razonable si surge naturalmente.

Pero:

- 86k con mucho mejor ritmo = éxito;
- 82k = posible éxito;
- 70k = revisar inmediatamente por posible mutilación.

La métrica principal no es:

> cuántas palabras salieron.

Es:

> **cuánta transformación narrativa existe por capítulo.**

---

# 17. CRITERIO DE ÉXITO FINAL DE PARTE I

Después de cirugía, Parte I debe sentirse aproximadamente así:

### Encuentro

Cole y Chiara existen primero como sistemas independientes.

### Elección

Eligen seguir viéndose.

### Costumbre

Construyen lenguaje privado.

### Colisión

El peligro demuestra que sus mundos no pueden mantenerse separados.

### Hogar

Empiezan a ocupar espacio mutuo.

### Conocimiento

Descubren las redes y pasados del otro.

### Defecto

Se formula que proteger no da derecho a decidir.

### Presión

El mundo externo vuelve a recordar que existen consecuencias.

### Poder

Cole empieza a necesitar gobierno y territorio.

### Elección consciente

Cole sabe suficiente y decide quedarse.

### Intimidad

Cruzan la última frontera de “sólo amigos”.

### Poder compartido

Una promesa íntima empieza a tener consecuencias criminales.

### Capital

Cole adquiere estructura legal real.

### Verdad

Ambos abren voluntariamente páginas muy profundas.

### Factura

Inmediatamente después, cada uno vuelve a decidir qué verdad cree que puede soportar el otro.

---

# 18. PRIMERA INSTRUCCIÓN PARA CLAUDE CODE

Cuando recibas este documento:

**NO empieces todavía a editar capítulos.**

Primero:

1. lee los documentos obligatorios;
2. confirma branch `develop`;
3. revisa el estado del working tree;
4. inspecciona C01–C03;
5. entrega el reporte del BLOQUE 0;
6. propone tu interpretación exacta del BLOQUE 1;
7. detente.

No ejecutes BLOQUE 1 hasta tener confirmación.

---

# FIN DEL ENCARGO

La prioridad de esta revisión es preservar lo que la novela ya descubrió que es.

La cirugía no busca convertirla en otra novela.

Busca quitar distancia entre sus mejores causas y sus mejores consecuencias.