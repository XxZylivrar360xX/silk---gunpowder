# 2026-10-10 - Codex -> Claude - Guía de consulta para 11_Books

## Objetivo
Hacer localizable el contexto de desarrollo de cada libro sin duplicar canon ni crear otra capa de estado.

## Fuentes
- `11_Books/README.md`
- `98_Agent_Handoff/AGENT_ROLES.md`
- `98_Agent_Handoff/START_HERE.md`
- Referencia: `99_Reference/archivos_externos/README-vault-erp-remoto` y `99_Reference/archivos_externos/cerebroerpGonza-contexto-y-migracion`.

## Resultado
Se añadió a `11_Books/README.md` una tabla de rutas por tipo de tarea: relevo, arco, escena/capítulo, cronología, relación/hito, auditoría y fronteras entre libros. Se aclara que los mapas orientan y que las fuentes especializadas conservan la autoridad; también se propone admitir solo síntesis que eviten una búsqueda repetida.

Tras la instrucción del autor de que Codex tome el relevo de este frente, se auditó el uso de carpetas en `11_Books`. Los directorios de partes del Libro I contienen manuscrito y `00_Front_Matter` alimenta la salida editorial. El Libro II tiene borradores en Partes I y II; Parte III está vacía como placeholder previsto en el mapa. Los Libros III–VII no tienen carpetas de partes porque sus desgloses aún no están aprobados. No se borraron carpetas.

Se corrigió `Book_02_Sombras_De_Poder/00_Book_Map.md`: estaba desfasado al declarar el libro “sin prosa” y describir como vacías las carpetas que contienen borradores. Ahora registra *Hogar* y *Ya Llegó*, distingue el estado de cada uno y aclara que solo la Parte III carece de capítulos.

También se ajustó la regla inicial de `11_Books/README.md`: cada libro requiere mapa; las carpetas de partes siguen el orden de lectura y se crean conforme se aprueba el desglose. Esto refleja que los Libros III–VII aún no tienen desgloses de partes aprobados.

## Verificación
`git diff --check` pasó; `INDEX.md` ya enlaza el README. No se alteraron canon, timelines ni estructura física de carpetas.

## Pendiente
Si se desea reducir también los placeholders locales vacíos, decidir si la carpeta prevista de Parte III del Libro II se crea bajo demanda. Se conservó porque el mapa operativo la referencia y su arco está definido.
