# TCHWD-DIR · Prototipo v0.1

Ampliación visual de la supervisión TCHWD, basada en «Dirección: centro de mando de IA.png». No sustituye el registro Programados ni el ZIP TCHWD-WIP-005_v0.1_aislado.zip. Este último no se ha inspeccionado ni integrado.

## Alcance

Panel de Dirección, cola Programados, búsqueda, filtro por estado, expedientes y revisión de ejemplo. AI Factory, Telemetría, Costes y Memoria tienen una pantalla informativa sin integración. Todos los IDs DEMO y estados son simulados. Las revisiones se pierden al recargar; no autorizan acciones. No hay autenticación, persistencia, backend ni conexión al registro real. WIP se calcula de los datos de ejemplo; no implementa bloqueo transaccional.

## Uso local

Node.js y npm. Ejecutar `npm ci`, después `npm run dev`. `npm run build` genera los archivos en dist/client y el empaquetado de la plantilla. No se ha publicado.

## Continuidad

ID provisional: TCHWD-DIR-UI-001. Responsable funcional: Dirección / Delegado LD-DEV. Prioridad propuesta: media. Estado: prototipo aislado para revisión. Alta en registro central: pendiente de conciliación; no se ha modificado Programados. No se ha comprobado el cupo global real.

Se conserva la estética oscura, jerarquía, barra lateral y estructura del centro de mando. Se adapta el contenido a toda TCHWD, se cuentan tareas en WIP y se reemplazan afirmaciones ficticias de seguridad, operatividad y gasto por estados no verificados. No crea un registro paralelo.

## Límites de verificación

Compilación y flujo principal comprobados en navegador de escritorio. CSS responsive incluido; vista móvil no verificada en un dispositivo o viewport móvil. Las fuentes Inter se cargan de Google Fonts con alternativa Arial. No se ha auditado SEC-001 ni seguridad de producción.
