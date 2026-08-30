# Piloto editorial 01–10

- **Fecha:** 2026-08-29.
- **Estado:** `audit_only`.
- **Corpus:** capítulos 01–10 de `Part_01_El_Encuentro_Y_La_Nada`, fijados explícitamente en `tools/editorial/pilot_01_10.json`.

## Por qué capítulos 1–10

El bloque contiene la entrada de Cole y Chiara, el primer favor, la formación de la costumbre, H3, H9 y el atentado de H12. Ofrece diálogo, acción, negociación, recuerdos, cambios de cadencia y metadata real suficientes para calibrar V1 sin abrir todavía el resto de Parte I.

El manifiesto explícito evita incorporar por accidente archivos renumerados o capítulos 11–19.

## Qué mide

- frases vigiladas y n-gramas;
- construcciones negativas configurables;
- palabras, párrafos y oraciones aproximadas;
- concentración de párrafos cortos;
- intervención y proporción aproximada de diálogo;
- frecuencias léxicas, adverbios en `-mente` y gestos;
- metadata, títulos, comentarios internos y residuos editoriales;
- outliers simples mediante IQR en una segunda pasada.

## Qué no mide

- calidad literaria;
- verdad de canon o continuidad profunda;
- atribución confiable de hablante;
- fingerprint de voz de Cole o Chiara;
- sintaxis o semántica lingüística avanzada;
- probabilidad de autoría por IA;
- capítulos 11–19;
- necesidad de reescritura.

No hay autofix, prompts de reescritura, APIs ni modelos.

## Criterio de éxito

No buscamos muchas alertas. Buscamos precisión.

De las aproximadamente treinta alertas de mayor prioridad, idealmente al menos dos tercios deben ser puntos que un editor humano considere razonable revisar. Esto no es un test automático: lo calibran ChatGPT y el autor después de leer [[tools/editorial/reports/PILOT_01_10/PILOT_01_10_GLOBAL]].

Hasta esa calibración no se autoriza Fase 2 ni una skill de Claude.

## Calibración V1.1

V1 se conserva sin sobrescritura en [[tools/editorial/reports/PILOT_01_10/PILOT_01_10_GLOBAL]]. La calibración V1.1 reduce falsos positivos sin tocar prosa: estima habla aparte de incisos, impide que un parlamento largo aislado llegue a HIGH, clasifica clusters cortos como diálogo/narración/mezcla, separa residuos editoriales de alta y baja confianza, evita cadenas negativas entre hablantes, colapsa n-gramas contenidos y fusiona ventanas gestuales solapadas.

La nueva prioridad alta exige señal de confianza alta, combinación de señales o concentración excepcional. El monólogo de Héctor en *El corral* permanece como HIGH por `LONG_DIALOGUE_CLUSTER`, no por dos longitudes aisladas. La similaridad entre pasajes de capítulos distintos se incorpora como señal léxica experimental, con máximo MEDIUM.

Resultados y comparación: [[tools/editorial/reports/PILOT_01_10_V1_1/PILOT_01_10_V1_1_GLOBAL]] · [[tools/editorial/reports/PILOT_01_10_V1_1/V1_VS_V1_1]]. La revisión de ChatGPT y el autor sigue siendo obligatoria antes de Fase 2.
