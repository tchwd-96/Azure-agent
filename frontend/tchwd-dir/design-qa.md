# Revisión visual · TCHWD-DIR v0.1

- Fuente visual: /workspace/scratch/260364c95f54/upload/Dirección: centro de mando de IA.png (1487 × 1058).
- Captura de implementación: /workspace/scratch/tchwd-dir-preview.jpg (1363 × 936; viewport CSS 1363 × 936; densidad 1).
- Estado: Dirección, escritorio, datos de ejemplo, sin expediente abierto.
- Comparación conjunta: /workspace/scratch/260364c95f54/comparison.jpg.
- Comparación focal de cabecera, capacidad y tabla: /workspace/scratch/260364c95f54/comparison-detail.jpg.
- Normalización: vistas escaladas proporcionalmente para inspección conjunta. No son capturas con viewport idéntico: la referencia es una imagen fija. La comparación evalúa la adaptación autorizada a TCHWD, no una copia píxel a píxel de AI Factory.

## Superficies evaluadas

- Tipografía: Inter con alternativa Arial; jerarquía y densidad de interfaz conservadas. Mayor lectura de filas con 12 px y auxiliares de 11 px; no hay colisiones visibles en escritorio.
- Espaciado: barra lateral, cabecera, cuatro resúmenes, tabla y tres regiones inferiores conservadas. El aviso de demostración y la mayor legibilidad añaden desplazamiento vertical. Controles persistentes visibles; no hay desbordamiento horizontal del documento en escritorio (scrollWidth 1363 / innerWidth 1363).
- Color: base azul muy oscuro, superficies navy, estados turquesa/ámbar y botón ámbar coherentes con referencia.
- Imágenes e iconos: no hay imágenes fotográficas en la pantalla seleccionada. Phosphor proporciona iconos de biblioteca. El globo suministrado y el catálogo son referencias de otras superficies; no se han usado como fondos del centro de mando.
- Contenido: adaptación intencional a supervisión global, con roles funcionales y datos DEMO. Se han eliminado afirmaciones de operatividad, conformidad, presupuestos y métricas no verificadas. La gráfica de modelos se sustituye por fuentes y trazabilidad, según el alcance general autorizado.

## Pruebas y correcciones

- Navegación a Programados: muestra 6 tareas de ejemplo.
- Filtro Bloqueada: muestra únicamente Memoria local / DEMO-03.
- Expediente: muestra responsable, prioridad, próxima acción y ausencia de evidencias reales.
- Revisión simulada: devuelve aviso explícito de que no autoriza ni ejecuta acciones.
- Búsqueda: se detectó combinación involuntaria con el filtro anterior. Se corrigió restableciendo Todas al buscar; nueva prueba Sous devuelve solo Sous Pilot.
- Revisión de lectura: texto de tabla ampliado a 12 px y auxiliares a 11 px. Captura posterior guardada y comparada.
- Seguridad: botón Ver alcance muestra la validación técnica pendiente, sin afirmar cumplimiento.
- Secciones inferiores inspeccionadas mediante captura adicional en navegador; sin recortes internos ni solapamientos.
- Consola: errores de extensión chrome-extension:// sobre envío de metadatos; no se observaron errores del código de aplicación en los mensajes revisados.
- Compilación: correcta.

## Diferencias aceptadas y límites

Esta entrega adapta una referencia de AI Factory a TCHWD-DIR; conserva el lenguaje visual y modifica contenido y densidad para el objetivo aprobado. La altura del documento es 1260 px a 1363 px de ancho; requiere desplazamiento vertical normal.

La adaptación móvil está implementada en CSS pero no ha sido validada en viewport móvil: queda como comprobación pendiente antes de aprobar uso móvil. Las pantallas secundarias informativas no equivalen a módulos conectados. No se verifica integración, autenticación, persistencia, aplicación transaccional WIP ni SEC-001.

## Resultado del alcance de escritorio

No se identifican defectos P0/P1/P2 pendientes en el flujo principal de escritorio dentro de la adaptación aprobada. La reproducción exacta del mock no es el objetivo de esta ampliación. La verificación móvil queda fuera de este resultado.

final result: passed
