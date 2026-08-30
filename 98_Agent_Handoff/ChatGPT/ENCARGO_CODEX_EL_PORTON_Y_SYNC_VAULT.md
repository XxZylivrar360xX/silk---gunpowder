# Encargo para Codex — Corrección local de `El portón` + sincronización del vault

**Proyecto:** *Seda y Pólvora*  
**Repositorio:** `XxZylivrar360xX/silk---gunpowder`  
**Branch obligatoria:** `develop`  
**Tipo:** continuidad local + sincronización documental  
**Alcance:** `15_El_Porton.md` y referencias documentales directamente afectadas.  
**NO rediseñar H10. NO tocar otros capítulos de prosa salvo metadata si fuera estrictamente necesario. NO commit. NO push.**

---

# 0. Objetivo

Cerrar los dos bugs locales que aún quedan en `El portón` después de la nueva causalidad:

1. inconsistencia entre **sala de espera** y **ambulancia**;
2. carta de Chiara redactada como si ella sólo se hubiera enterado de lo de Héctor, cuando fue quien lo encontró.

Después, sincronizar las referencias del vault que quedaron desfasadas por la renumeración y por el ajuste final de `La regla del teléfono`.

No hay que reescribir la arquitectura.

---

# 1. Archivo principal

Localizar en `develop`:

`11_Books/Book_01_Seda_y_Polvora/Part_01_El_Encuentro_Y_La_Nada/15_El_Porton.md`

Leerlo completo antes de editar.

La causalidad nueva ya funciona y debe preservarse:

`camping con Marisol -> teléfono apagado -> Héctor cae -> Chiara llama emergencias -> intenta localizar a Cole -> Walt tampoco sabe el punto exacto -> Nadir/Danny retenidos -> taller tampoco puede alcanzarlo -> carta como último canal físico -> Cole regresa y recibe todo de golpe`

---

# 2. BUG 1 — sala de espera vs ambulancia

La narración establece que Chiara empieza a llamar a Cole:

> desde la sala de espera, después de que Héctor queda en manos del hospital.

Más tarde, hablando con Cole, dice que lo llamó:

> desde la ambulancia.

Eso es contradicción directa.

## Corrección

Conservar como verdad la versión dramatizada:

> **Chiara empieza a llamar a Cole desde la sala de espera.**

Ajustar el diálogo posterior para que coincida.

No hace falta explicar más.

La lógica debe quedar:

- durante el traslado ella se concentra en Héctor;
- cuando ya no puede hacer nada con las manos, empieza a buscar a Cole.

---

# 3. BUG 2 — contenido de la carta

La carta actual usa una formulación equivalente a:

> `me enteré de lo de Héctor`

Pero Chiara:

- encontró a Héctor en el suelo;
- llamó a emergencias;
- acompañó el proceso hasta el hospital;
- intentó localizar a Cole.

Por tanto, esa frase pertenece a la causalidad vieja.

## Corrección

Reformular únicamente la carta para que refleje que **ella fue quien lo encontró**.

Dirección sugerida:

> `Cole — encontré a Héctor ayer junto al portón de su casa. Está estable en Santa Aurelia...`

No es obligatorio usar exactamente esa redacción.

### Regla

La carta debe seguir siendo:

- sobria;
- sin dramatización;
- sin `llámame`;
- sin urgencia artificial;
- un último canal físico porque sabe que eventualmente Cole cruzará esa puerta.

No convertirla en una confesión ni en una escena romántica.

---

# 4. NO TOCAR en `El portón`

Conservar:

- apertura con Cole orillado y las llamadas entrando;
- mensaje de Walt;
- Nadir y Danny retenidos;
- Chiara encontrando a Héctor;
- llamadas directas a Cole;
- llamada a Walt;
- intento con Nadir/Danny;
- paso por el taller;
- carta bajo la puerta;
- Cole regresando primero a casa;
- taza del camping;
- visita al Monarch;
- furia sin objetivo;
- cierre `—Llévame con él.`

No introducir:

- culpa moral explícita por el camping;
- discusión sobre Marisol;
- nueva pelea con Chiara;
- nueva información criminal.

---

# 5. Sincronización de la ficha de Marisol

Revisar:

`02_Characters/Marisol_Grayson.md`

Hay referencias desfasadas.

## A. Numeración

Actualizar todas las etiquetas humanas que todavía digan:

> Capítulo 13 — La regla del teléfono

a:

> **Capítulo 14 — La regla del teléfono**

Los enlaces ya pueden apuntar al archivo correcto; corregir también el texto visible.

## B. Regla del teléfono desactualizada

La ficha todavía conserva una versión previa donde Cole protesta nombrando a Héctor:

> `está mayor, si pasa algo...`

Eso ya NO ocurre en la prosa vigente.

La versión actual es:

- Cole protesta porque el taller no puede quedarse sin él dos días;
- Marisol responde que Walt sabe encargarse;
- la regla existe para que Cole esté presente allí.

Actualizar la ficha para reflejar la versión final.

No conservar como canon una línea eliminada.

---

# 6. Conteo de capítulos

La Parte I actual tiene **19 capítulos**.

Revisar documentos vivos que todavía digan `18 capítulos escritos`.

Se detectó al menos ese desfase en:

- `11_Books/Book_01_Seda_y_Polvora/00_Book_Map.md`

`CURRENT_BRIEF.md` ya registra 19 en el estado conocido; verificar antes de tocar.

### Regla

No hacer reemplazo global ciego.

Corregir sólo referencias que hablen del número actual de capítulos escritos.

---

# 7. Auditoría rápida

Buscar referencias a:

- `Capítulo 13 — La regla del teléfono`
- `Cap. 13 — La regla del teléfono`
- `18 capítulos`
- `Héctor está mayor`
- `si pasa algo`
- `desde la ambulancia`
- `me enteré de lo de Héctor`

Clasificar hallazgos:

1. prosa activa a corregir;
2. documentación viva a corregir;
3. handoff histórico que debe conservarse como registro.

No reescribir handoffs históricos sólo porque contienen una versión antigua.

---

# 8. Estado esperado

Después de esta tarea:

- `15_El_Porton.md` debe quedar **candidato a TRIADO**;
- la causalidad H10 queda cerrada;
- `Marisol_Grayson.md` debe reflejar la versión vigente del Cap. 14;
- el vault debe reportar correctamente 19 capítulos donde corresponda.

No marcar nada como CERRADO.

---

# 9. Entrega

Mostrar:

1. diff de `15_El_Porton.md`;
2. diff de `02_Characters/Marisol_Grayson.md`;
3. lista de otros archivos documentales tocados;
4. `git diff --stat`;
5. cualquier referencia vieja que hayas decidido conservar por ser histórica.

**NO commit.**  
**NO push.**
