# Encargo a Codex: poner al día las referencias viejas a capítulos del Libro I

Fecha: 2026-11-01. Encarga: Claude Code, a pedido del autor («solventemos las viejas referencias de una vez»). Contrato de rol: [[98_Agent_Handoff/AGENT_ROLES]] (Codex). Al terminar, Claude verifica.

Antecedente: [[98_Agent_Handoff/sessions/2026-11-01_codex_para_claude_renumeracion_56]] (tu reporte, §Referencias conservadas). Numeración vigente: la **del 2026-11-01** (56 caps.), tabla en [[11_Books/Book_01_Mascaras_De_Cristal/00_Book_Map]].

**Autorización explícita del autor** para este encargo: se pueden tocar `06_Relationships/Hitos.md`, `00_Biblia/` y las fichas (`02_Characters/`, `03_Factions/`, `05_Locations/`), **sólo** en las referencias a número de capítulo del Libro I. Ni una palabra más de esos archivos.

## Fase 0: tabla de equivalencias de todas las épocas

Antes de sustituir nada, reconstruye la correspondencia **archivo ↔ número de capítulo** en cada numeración que tuvo el Libro I. Fuentes: `git log -p` de `00_Book_Map.md` y de los encabezados de los capítulos, y las sesiones de renumeración en `98_Agent_Handoff/sessions/` (2026-10-22, 2026-10-23, 2026-10-28, 2026-10-29 y la tuya del 2026-11-01). Épocas mínimas:

| Época | Desde | Regla general |
|---|---|---|
| Prefijo | hasta 2026-10-21 | En general, «Cap. N» = archivo N (comprobar las excepciones con letras: 05a/05b/05c, 08b, 12b, 24b–d, 33b, 50b) |
| 56 (corrida) | 2026-10-22 | |
| 57 | 2026-10-23 | separación de 08b |
| 58 | 2026-10-28 | robo del Monarch, 22a–22b, sustituye a *Causalidad* |
| 59 / 60 | 2026-10-29 | 12b *Por su cuenta*; 24d separado de 24c |
| **2026-11-01** | 2026-11-01 | vigente |

Se guarda como documento permanente en `01_Timeline/09_Equivalencias_Numeracion_Libro_I.md`: una fila por archivo (también los retirados) y una columna por época. Enlázalo desde la nota de numeración del Book_Map y desde [[01_Timeline/00_README]]. Si una época no se puede reconstruir con certeza, márcala así en la tabla y **no la uses para sustituir**.

## Alcance

**Sí se actualiza** todo documento vivo que cite capítulos del Libro I:
- las dos tablas de tu reporte (prioridad y «otros documentos de dominio»), salvo los archivos de relevo de abajo;
- `06_Relationships/` (Hitos, Kal_y_Chiara, Momentos_de_Fractura);
- `00_Biblia/` (incluido `00_Trilogy_Structure.md`);
- fichas de `02_Characters/`, `03_Factions/`, `05_Locations/` y `04_Concepts/`;
- `07_Ideas/`, `12_Craft_Policies/` (voz, reglas, políticas; **no** el ledger `revelations/`), `BACKLOG.md`;
- planes y diseños del Libro II y de los demás libros, en sus cruces al Libro I;
- planes del Libro I (`00_Plan_*`, `00_Propuesta_Titulos`), incluido el **cuerpo** de los seis documentos a los que sólo les pusiste la nota de equivalencia. En esos seis, la nota pasa a decir que el cuerpo ya está en la numeración del 2026-11-01.

**No se toca:**
- prosa de capítulos y comentarios iniciales de los capítulos (bitácora interna: ya llevan «Renumerado 2026-11-01: antes Cap. N»);
- histórico: `98_Agent_Handoff/sessions/`, `archive/`, `ChatGPT/`, `encargos/`, `99_Reference/`, `97_Supersedido/`, `Escenas_Eliminadas/`, los dictámenes fechados de `13_Auditorias/`, `12_Craft_Policies/revelations/`, `log.md`;
- relevo: `CLAUDE.md`, `AGENTS.md`, `CURRENT_BRIEF.md`, `PENDING.md`, `DECISIONS.md` (los ajusta Claude);
- números de capítulo **de otros libros**. En los documentos del Libro II en adelante, sólo se cambia lo que el contexto ata explícitamente al I («del I», «Libro I», *Máscaras*, un archivo `Book_01`, un título del I).

## Cómo se decide cada referencia

1. **Si trae archivo** («archivo 28», `28_La_Correa`, «(arch. 40)»): el archivo manda; número nuevo por la tabla vigente.
2. **Si trae título** del I: el título manda.
3. **Si sólo trae número:** época = la fecha de la nota o la sección donde aparece (o la del documento), con la tabla de la Fase 0. Confirma por contenido: el suceso citado tiene que estar en ese capítulo (su encabezado «Función» o el Book_Map). **Si época y contenido no coinciden, o no hay fecha, no se toca y va a la lista de dudas.**
4. **Formato de salida:** `Cap. N (archivo X)`, con el número de la numeración del 2026-11-01. Si el archivo ya estaba al lado, sólo cambia el número. Rangos: `Caps. 49–56 (archivos 44–50b)`.
5. **Capítulos que ya no existen:**
   - antiguo 6 → `Cap. 5 (coda; antes 05b)`;
   - antiguo 28 → `Cap. 25 *Bajo juramento* (archivo 24; fusión con el antiguo 28)`;
   - antiguos 14, 16 y 23 → `*El farol* / *Por su cuenta* / *Lo que nadie estaba mirando* (escena eliminada, archivo 11 / 12b / 19)`;
   - *Causalidad* y cualquier capítulo de épocas viejas que ya no exista → no se toca y va a dudas.
6. **No se toca:** lo que se marque como histórico en el propio texto («numeración de entonces», «antes Cap.», texto tachado `~~`, «(numeración de 60)»), las citas `archivo:línea` y los números de hito (H1, H13…).
7. Nada de desplazamientos globales ni de `sed` ciegos: cada sustitución sale de las reglas 1–3.

## Comprobaciones

- Los enlaces `[[...]]` siguen resolviendo (no cambian nombres de archivo).
- Muestreo propio: 20 sustituciones al azar, revisadas contra el encabezado del capítulo de destino.
- `git diff --check` limpio en los archivos tocados.
- Sin EPUB, PDF ni audio; sin commit ni push.

## Reporte

`98_Agent_Handoff/sessions/AAAA-MM-DD_codex_para_claude_referencias_viejas.md` (fecha real), con:

1. archivos tocados y número de sustituciones por archivo;
2. **registro completo** en `98_Agent_Handoff/sessions/AAAA-MM-DD_codex_referencias_viejas_registro.csv`: archivo · línea · antes · después · regla usada (archivo / título / época+contenido) · época inferida;
3. **lista de dudas** (archivo, línea, cita, por qué no se tocó) para que las decidan Claude y el autor;
4. el resultado de las comprobaciones.
