# TCHWD-AZURE-001 · Guía Azure Cloud Shell

**Estado:** Desarrollo y validación remota; NO despliegue automatizado. **Responsable:** ld-dev.
**Seguridad:** SEC-001. **Presupuesto declarado:** hasta 175 EUR de bono Azure, 0 EUR de fondos propios.

## Ruta probada: repositorio GitHub

```bash
git clone --branch feat/tchwd-azure-manager-bootstrap --single-branch https://github.com/tchwd-96/Azure-agent.git
cd Azure-agent
bash scripts/cloud-shell-setup.sh
python3 cloud/tchwd_cloud_runner.py qa --approve-local
```

Revisar `frontend/tchwd-dir/package-lock.json` antes de aprobar QA: `npm ci` descarga paquetes externos. Si Cloud Shell es efímero, clonación, dependencias y resultados pueden perderse al cerrar la sesión.

Los resultados están en `.tchwd-run/events.jsonl` (ignorarlo en Git). Copiar fuera de la sesión solo si se revisan secretos y datos sensibles.

## Supervisión de Google Antigravity

Antigravity no está integrado automáticamente: el archivo de evidencias es una interfaz **documental**, no una conexión API. Un agente autorizado puede revisar salida/commits y emitir recomendaciones, pero este programa no se las atribuye ni ejecuta decisiones remotas por su cuenta.

## Distinguir Cloud Shell de hosting 24/7

Cloud Shell no garantiza procesos persistentes ni dispone necesariamente de almacenamiento montado. Para ejecución ininterrumpida se requiere infraestructura separada y estimación previa de costes. No ejecutar `nohup` esperando persistencia permanente.

## Antes de publicar TCHWD-DIR

Verificar funcionamiento, acceso, seguridad, copia de seguridad y plan de reversión del App Service existente `tchwd-org`, mantener demo separada de datos reales y revisar cobertura del bono. No contiene orden de `az webapp deploy`, `az group create`, `git push` ni cambios a Programados.

## Control

1. Comprobación local: `python3 cloud/tchwd_cloud_runner.py inspect`.
2. QA tras revisión: `python3 cloud/tchwd_cloud_runner.py qa --approve-local`.
3. Evidencias: `cat .tchwd-run/events.jsonl`.
4. Entregar informe a Dirección. La capacidad global WIP-005 continúa sin confirmar.
