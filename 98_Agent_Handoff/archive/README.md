# Archivo de relevo

Historial de consulta, no instrucciones vigentes. Las copias conservan decisiones, diálogos, estados, contradicciones y rutas tal como estaban al corte; su conservación no revalida información superada.

## Corte del 2026-09-21

Copias íntegras, verificadas por SHA-256 antes de compactar:

- [[98_Agent_Handoff/archive/log_hasta_2026-09-21|Bitácora original]].
- [[98_Agent_Handoff/archive/2026-09-21_CURRENT_BRIEF|Brief acumulado original]].
- [[98_Agent_Handoff/archive/2026-09-21_PENDING|Pendientes originales, incluidos cierres y reservas]].
- [[98_Agent_Handoff/archive/2026-09-21_DECISIONS|Decisiones originales]].

Estas copias son inmutables. No corregir sus nombres, enlaces históricos ni canon superado por nuevas decisiones. Para estado actual, usar [[98_Agent_Handoff/CURRENT_BRIEF]], [[98_Agent_Handoff/PENDING]] y [[98_Agent_Handoff/BACKLOG]].

## Búsqueda por demanda

Desde la raíz del vault:

```powershell
rg -n -i "Palermo" 98_Agent_Handoff/sessions 98_Agent_Handoff/archive
rg -n "^##" 98_Agent_Handoff/archive/log_hasta_2026-09-21.md
```

Primero localizar coincidencias; después abrir sólo el tramo pertinente. No leer el archivo histórico completo por defecto. Las referencias antiguas a secciones de log/brief/pending/decisions se buscan en las copias correspondientes.

## Nuevos registros

Una nota por sesión en `98_Agent_Handoff/sessions/`. [[log]] enlaza las 30 más recientes; trasladar enlaces anteriores a índices `AAAA-MM_sesiones.md` en esta carpeta, enlazados aquí. Al rotar DECISIONS, archivar íntegramente las entradas retiradas y enlazar su archivo aquí. No mantener copias paralelas actualizables del mismo registro.

Markdown sigue siendo la fuente; una futura base de búsqueda deberá poder reconstruirse desde estos documentos.

## Actualización concurrente preservada

Durante la compactación otra sesión agregó el Cap. 40. También se conservaron íntegros [[98_Agent_Handoff/archive/2026-09-21_CURRENT_BRIEF_cap40]] y [[98_Agent_Handoff/archive/2026-09-21_PENDING_cap40]]. El relevo compacto incorpora ese avance y la discrepancia Tommaso/Alessio.

- Bitácora al terminar esa sesión: [[98_Agent_Handoff/archive/log_hasta_2026-09-21_cap40]]. Conserva también el registro completo del Cap. 40.
