# Encargo para Claude Code — integración de incubadora Libro 4

Trabaja sobre la rama `develop` del repositorio `silk---gunpowder`.

Base de esta migración: `734d519433d9591cdb8c5c062391b300366ace0a`.

## Objetivo

Integrar al vault el material de `07_Ideas/Libro_04_Incubadora/` **sin convertir automáticamente brainstorming en canon**.

## Proceso obligatorio

1. Lee primero:
   - `07_Ideas/Arco_Elenna_Libro_04.md`
   - `07_Ideas/Tres_Hermanas_Epilogo.md`
   - `08_Scenes/Book_03/Tres_Hermanas_Material_Narrativo.md`
   - `02_Characters/Elenna_Mercer.md`
   - `02_Characters/Raymond_Keene.md`
   - `02_Characters/Elena_Vega.md`
   - `02_Characters/Nereo_Volpi.md`
   - `03_Factions/Departamento_de_Policia_de_San_Aurelio.md`
   - `03_Factions/El_Casino.md`
   - fichas actuales de Kal, Chiara, Riley, Marisol, Corrado, Nadir, Danny y Walt si existen.

2. Para cada idea de la incubadora, clasifica internamente:
   - `CANON YA EXISTENTE`
   - `CANON DEL AUTOR`
   - `DISEÑO FUERTE`
   - `SEMILLA`
   - `SUPERADO / DESCARTAR`

3. No alteres el epílogo de *Interregno* para adelantar la trama policial.

4. No cambies a Elenna de `Police Recruit` a oficial plena sin que la cronología lo justifique.

5. No muevas a Nicholas Voss a `02_Characters` hasta comprobar si su nombre/rol están suficientemente fijados por el autor. Si se crea ficha, marcar lo no aprobado como abierto.

6. Mantén la corrección: **The Monarch es legado de Chiara, no de Kal.**

7. Mantén la regla de familia:
   - Kal → “Elenna”.
   - Chiara → “Ragazza”.
   - Corrado → “Tesoro mio”.
   - Elenna → Corrado: “Nonno”.

8. No conviertas al antagonista en psicópata clínico genérico ni en copia directa de ninguna inspiración externa.

9. No conviertas a Volpi en asesino de Nora. Su función propuesta es corregir/administrar el encubrimiento posterior.

10. No uses a Kal/Chiara para resolver el caso. Sus apariciones deben funcionar como familia/hogar y legado, no como protagonistas operativos.

## Salida deseada

Haz una propuesta de integración en dos niveles:

### A. Actualizaciones de archivos existentes

Sugiere qué material debe incorporarse a:

- `07_Ideas/Arco_Elenna_Libro_04.md`
- fichas de personajes ya existentes;
- relaciones/lugares si corresponde.

### B. Nuevos archivos recomendados

Sólo crea archivos nuevos cuando un núcleo tenga suficiente identidad propia. Posibles destinos:

- ficha de Nicholas Voss;
- concepto del Caso Nora;
- concepto del antagonista;
- relaciones post-trilogía;
- escenas guía específicas.

## Protección de escenas

En `06_Escenas_Faro.md`, separar:

- líneas aportadas directamente por el autor;
- movimientos/función emocional aprobados;
- prosa generada durante brainstorming.

Las primeras dos categorías pueden preservarse como guía. La tercera debe permanecer provisional.

## Revisión antes de commit

Antes de modificar:

- verifica enlaces wiki existentes;
- busca contradicciones de edad/cronología;
- revisa nombres obsoletos;
- no dupliques conceptos ya documentados.

Después:

- muestra resumen de archivos modificados/creados;
- lista cualquier contradicción encontrada;
- lista decisiones que requieren al autor;
- ejecuta validaciones internas del vault si existen;
- haz **un solo commit coherente** de migración, sin tocar EPUB/manuscrito salvo que el autor lo pida.

Mensaje sugerido de commit:

`docs: migra incubadora post-trilogia de Elenna y Nicholas`
