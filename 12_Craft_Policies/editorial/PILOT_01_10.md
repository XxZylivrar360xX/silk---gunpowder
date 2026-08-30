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

