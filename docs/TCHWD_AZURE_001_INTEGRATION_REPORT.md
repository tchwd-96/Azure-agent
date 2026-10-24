# TCHWD-AZURE-001 · Informe de integración

**Fecha:** 24-10-2026
**Repositorio:** `tchwd-96/Azure-agent`
**Rama autorizada:** `feat/tchwd-azure-manager-bootstrap`
**Commit de integración:** `7c3facb` (`feat(frontend): import TCHWD-DIR v0.1 prototype`)
**Alcance:** incorporación del prototipo en `frontend/tchwd-dir/`, validación local y preparación de una recomendación. No se ha desplegado en Azure, fusionado ni abierto un pull request.

## Resultado

Se integraron los 15 archivos del prototipo en sus rutas originales bajo `frontend/tchwd-dir/`. El script auxiliar `importar-desde-repositorio.sh` incluido en el ZIP no se incorporó ni ejecutó: realiza `git add` y `git commit` automáticamente. La importación se hizo manualmente en la rama indicada.

El código de la interfaz, estilos, worker y pruebas se conserva sin cambios. Se actualizaron solo el manifiesto y el lockfile de npm como adaptación de seguridad: Vite pasó de 6.4.2 a 6.4.5 y `npm audit fix` actualizó nueve paquetes transitivos dentro de rangos compatibles. El `npm audit` posterior informa cero vulnerabilidades.

La interfaz sigue siendo una demostración. Sus datos son ficticios; no incorpora autenticación, persistencia, backend conectado ni acceso a Azure. Sus acciones de revisión no autorizan cambios reales.

## Archivos incorporados

| Ruta | Uso |
|---|---|
| `frontend/tchwd-dir/.npmrc` | Configuración de npm del prototipo |
| `frontend/tchwd-dir/.openai/hosting.json` | Configuración de empaquetado para Sites |
| `frontend/tchwd-dir/AGENTS.md` | Instrucciones locales del prototipo |
| `frontend/tchwd-dir/README.md` | Alcance, uso y límites de la demo |
| `frontend/tchwd-dir/design-qa.md` | Criterios de revisión visual |
| `frontend/tchwd-dir/index.html` | Entrada HTML de Vite |
| `frontend/tchwd-dir/package-lock.json` | Lockfile actualizado tras auditoría |
| `frontend/tchwd-dir/package.json` | Scripts y dependencias; Vite fijado en 6.4.5 |
| `frontend/tchwd-dir/scripts/prepare-sites-build.mjs` | Preparación del empaquetado de Sites |
| `frontend/tchwd-dir/src/App.jsx` | Interfaz React |
| `frontend/tchwd-dir/src/main.jsx` | Punto de entrada React |
| `frontend/tchwd-dir/src/styles.css` | Estilos del prototipo |
| `frontend/tchwd-dir/tests/sites-worker.test.mjs` | Pruebas del worker y artefactos Sites |
| `frontend/tchwd-dir/vite.config.mjs` | Configuración de compilación Vite |
| `frontend/tchwd-dir/worker/index.js` | Worker SPA de Sites |

Los artefactos generados (`node_modules/` y `dist/`) están ignorados por Git y no se publicaron.

## Verificaciones ejecutadas

| Comprobación | Resultado observado |
|---|---|
| Repositorio y rama | Repositorio público verificado; rama autorizada existente y clonada. Sin cambios en `main`. |
| Instrucciones | Leídos `AGENTS.md`, `README.md` y `docs/TCHWD_DIR_IMPORT.md` de la rama. |
| ZIP | Rutas del prototipo comprobadas; 15 archivos extraídos a `frontend/tchwd-dir/`. |
| Secretos | Búsqueda de patrones conocidos de claves, tokens y claves privadas en archivos importados: sin coincidencias. No había `gitleaks` ni `trufflehog` disponible; esto no equivale a una auditoría formal de secretos. |
| Dependencias | 115 paquetes resueltos en lockfile; todos tienen integridad registrada y URLs npm; no se encontraron dependencias Git. `npm ci`: correcto, 66 paquetes añadidos. |
| Build | `npm run build`: correcto con Vite 6.4.5; generó `dist/client/index.html` (JS 255.87 kB, 75.44 kB gzip; CSS 12.63 kB, 3.40 kB gzip), además de los archivos de empaquetado de Sites. |
| Pruebas del prototipo | `npm run test:sites`: 4 pasaron, 0 fallaron. |
| Auditoría npm inicial | 6 avisos corregibles: 5 altos y 1 moderado, incluidos Vite y dependencias transitivas. |
| Auditoría npm final | `npm audit`: 0 vulnerabilidades (0 informativas, bajas, moderadas, altas o críticas). |
| Prueba backend existente | Instaladas temporalmente las dependencias declaradas en `backend/requirements.txt`; `python -m pytest -q`: 1 pasó. El uso inicial del ejecutable `pytest -q` no añadió la raíz al import path y falló la colección; el comando equivalente como módulo funcionó. |
| Diferencias de formato | `git diff --cached --check`: sin errores. |

Durante las órdenes npm apareció el aviso del entorno `Unknown env config "http-proxy"`; no impidió instalación, compilación, pruebas ni auditoría.

## Adaptación y compatibilidad con Azure App Service F1 Linux

La configuración incluida usa Vite y un worker de Sites. El worker espera un entorno con `env.ASSETS`; App Service no proporciona ese contrato. Por ello, **el prototipo no es desplegable tal cual en App Service**. La carpeta `dist/client` contiene una SPA estática; una vista previa necesitará un servidor compatible que entregue esos archivos y aplique fallback de rutas a `index.html`, además de un comando de inicio para Linux. El FastAPI existente solo tiene `/health` y todavía no sirve el frontend.

Compatibilidad estimada del frontend compilado: **alta tras una adaptación pequeña de hosting**, siempre que el plan F1 esté disponible para la suscripción y región. El prototipo es pequeño y cliente, pero F1 es compartido, tiene 60 minutos de CPU diarios, 1 GB de memoria y 1 GB de almacenamiento en la tarifa oficial consultada. Microsoft destina el plan gratuito a pruebas y aprendizaje, sin SLA, y no lo soporta para cargas de producción. La disponibilidad de la SKU debe comprobarse en la suscripción antes de planificar una prueba.

Referencias oficiales consultadas el 24-10-2026:

- [Precios de App Service para Linux](https://azure.microsoft.com/en-us/pricing/details/app-service/linux/)
- [Planes de hospedaje de Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans)

## Riesgos y límites

- Los datos y estados que se muestran son DEMO y no reflejan Programados ni el WIP real.
- No hay control de acceso, autorización de acciones, persistencia ni API de Azure.
- La hoja de estilos carga Inter desde Google Fonts; el estilo tipográfico depende de conectividad externa y tiene alternativa Arial.
- El servidor Vite de desarrollo configura `host: 0.0.0.0`; no se debe exponer públicamente como servidor de producción.
- No se verificó visualmente un viewport móvil en este entorno. El documento de QA incluye CSS responsive, pero eso no prueba la experiencia móvil.
- El resultado no acredita compatibilidad de despliegue hasta añadir y probar un adaptador de hosting para App Service.
- No se verificaron cuotas ni disponibilidad de recursos en una suscripción Azure. No se usaron credenciales Azure ni se hicieron llamadas a Azure.
- No se generaron cargos de Azure ni se cambiaron recursos de producción.

## Próxima acción propuesta

Solicitar aprobación de Dirección para preparar en la misma rama un adaptador local de hosting para App Service Linux, servir el build de `dist/client` con fallback SPA y añadir pruebas de rutas y health check. Después, presentar instrucciones y un cálculo de costes actual antes de pedir autorización separada para crear o desplegar una vista previa en Azure. El despliegue sigue pendiente de aprobación expresa.
